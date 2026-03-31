from env.environment import CloudKitchenEnv
from agent import simple_agent


# -----------------------------
# RUN ONE FULL EPISODE
# -----------------------------
def run_episode(env):
    obs = env.reset()  # initial observation with all orders and resources
    total_reward = 0

    done = False

    while not done:
        action = simple_agent(obs)
        obs, reward, done, _ = env.step(action)
        total_reward += reward.value

    return total_reward


# -----------------------------
# TASK 1: EASY
# -----------------------------
def task_easy():
    env = CloudKitchenEnv()
    env.reset()

    score = run_episode(env)

    max_possible = 550  # 200 + 100 + 250
    return max(0, min(score / max_possible, 1))


# -----------------------------
# TASK 2: MEDIUM
# -----------------------------
def task_medium():
    env = CloudKitchenEnv()
    env.reset()

    # tighter deadlines
    for order in env.orders:
        order.deadline -= 2

    score = run_episode(env)

    max_possible = 550

    return max(0, min(score / max_possible, 1))


# -----------------------------
# TASK 3: HARD
# -----------------------------
def task_hard():
    env = CloudKitchenEnv()
    env.reset()

    # much tighter deadlines
    for order in env.orders:
        order.deadline -= 3

    # add extra order
    env.orders.append(
        env.orders[0].model_copy(update={
            "id": 4,
            "cook_time": 6,
            "deadline": 8,
            "value": 180
        })
    )

    score = run_episode(env)

    max_possible = 730  # 550 + 180

    return max(0, min(score / max_possible, 1))


# -----------------------------
# RUN ALL TASKS
# -----------------------------
def run_all_tasks():
    print("\n--- TASK RESULTS ---")

    easy = task_easy()
    print(f"Easy Score   : {easy:.2f}")

    medium = task_medium()
    print(f"Medium Score : {medium:.2f}")

    hard = task_hard()
    print(f"Hard Score   : {hard:.2f}")


if __name__ == "__main__":
    run_all_tasks()