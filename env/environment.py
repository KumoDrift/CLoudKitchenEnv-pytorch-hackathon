from env.models import *
import random


class CloudKitchenEnv:
    def __init__(self):
        self.reset()

    def reset(self):
        self.current_time = 0
        
        random.seed(42)  # for reproducibility 
        # initial orders
        self.orders = [
           Order(id=1, name="pizza", cook_time=random.randint(4,7), deadline=10, value=200),
           Order(id=2, name="burger", cook_time=random.randint(2,5), deadline=6, value=100),
           Order(id=3, name="pasta", cook_time=random.randint(6,9), deadline=12, value=250),
        ]

        # active orders (currently cooking)
        self.active_orders = {}

        # cooking slots (1 stove) to make it more challenging for the agent 
        self.slots = [
            Slot(slot_id=1, order_id=None, remaining_time=0),
         
        ]

        return self.state()

    def state(self):
        return Observation(
            current_time=self.current_time,
            orders=self.orders,
            slots=self.slots
        )

    def step(self, action: Action):
        reward = 0.0

        # NEW: track events (for printing/debugging)
        info = {
            "events": []
        }

        # 1. Assign orders to free slots
        for assign in action.assignments:
            slot = next((s for s in self.slots if s.slot_id == assign.slot_id), None)

            if slot and slot.order_id is None:
                order = next((o for o in self.orders if o.id == assign.order_id), None)

                if order:
                    slot.order_id = order.id
                    slot.remaining_time = order.cook_time

                    # track active order
                    self.active_orders[order.id] = order

                    # remove from pending
                    self.orders.remove(order)

        # 2. Cooking progresses
        completed_orders = []

        for slot in self.slots:
            if slot.order_id is None:
                reward -= 1 # small penalty for idle slot to make our agent make good decisions
            if slot.order_id is not None:
                slot.remaining_time -= 1
                

                if slot.remaining_time == 0:
                    completed_orders.append(slot.order_id)

        # 3. Handle completed orders
        for order_id in completed_orders:

            order = self.active_orders[order_id]
            finish_time = self.current_time + 1  # more accurate

            # reward logic + event logging
            if finish_time <= order.deadline:
                reward += order.value
                info["events"].append(
                    f"Order {order_id} completed ON TIME (+{order.value})"
                )

            elif finish_time <= order.deadline + 3:
                late_reward = order.value * 0.5
                reward += late_reward
                info["events"].append(
                    f"Order {order_id} completed LATE (+{late_reward})"
                )

            else:
                penalty = order.value * 0.5
                reward -= penalty
                info["events"].append(
                    f"Order {order_id} TOO LATE (-{penalty})"
                )

            # free the slot
            for slot in self.slots:
                if slot.order_id == order_id:
                    slot.order_id = None
                    slot.remaining_time = 0

            # remove from active tracking
            del self.active_orders[order_id]

        # 4. Increase time
        self.current_time += 1

        # 5. Check if done
        done = False

        # max time limit
        if self.current_time >= 20:
            done = True

        # all orders completed
        if len(self.orders) == 0 and all(s.order_id is None for s in self.slots):
            done = True

        return self.state(), Reward(value=reward), done, info