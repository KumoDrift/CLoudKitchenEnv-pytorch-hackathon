from env.models import Action, Assignment


def simple_agent(obs):
    assignments = []

    # get free slots
    free_slots = [s for s in obs.slots if s.order_id is None]

    # sort orders by earliest deadline
    sorted_orders = sorted(obs.orders, key=lambda o: o.deadline)

    # assign orders to free slots
    for slot, order in zip(free_slots, sorted_orders):
        assignments.append(
            Assignment(
                slot_id=slot.slot_id,
                order_id=order.id
            )
        )

    return Action(assignments=assignments)