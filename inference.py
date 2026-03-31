from tasks import task_easy, task_medium, task_hard


def run_baseline():
    print("\n" + "="*60)
    print(" CLOUD KITCHEN ENVIRONMENT - BASELINE EVALUATION")
    print("="*60)

    print("\nRunning tasks...\n")

    easy = task_easy()
    print(f"[Easy Task   ] Score: {easy:.2f}  -> Basic scheduling with sufficient resources")

    medium = task_medium()
    print(f"[Medium Task ] Score: {medium:.2f}  -> Tighter deadlines, limited resources")

    hard = task_hard()
    print(f"[Hard Task   ] Score: {hard:.2f}  -> High pressure, extra orders, strict constraints")

    avg = (easy + medium + hard) / 3

    print("\n" + "-"*60)
    print(" SUMMARY")
    print("-"*60)

    print(f"Easy   : {easy:.2f}")
    print(f"Medium : {medium:.2f}")
    print(f"Hard   : {hard:.2f}")
    print(f"\nAverage Score: {avg:.2f}")

    print("\n" + "-"*60)
    print(" INTERPRETATION")
    print("-"*60)

    print("Higher score = better performance")
    print("Lower score = more challenging environment")

    print("\nThis shows how the agent performs under increasing difficulty levels.")
    print("The environment introduces real-world constraints like deadlines,")
    print("limited cooking slots, and reward trade-offs.")

    print("="*60)
    print("\n" + "="*60)
    print("Author: Monu Mandal | Cloud Kitchen RL Environment")


if __name__ == "__main__":
    run_baseline()