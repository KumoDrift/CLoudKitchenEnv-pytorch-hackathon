print("🔥 inference.py started")
import os
from openai import OpenAI
from tasks import task_easy, task_medium, task_hard


# -----------------------------
# ENV VARIABLES (REQUIRED)
# -----------------------------
API_BASE_URL = os.getenv("API_BASE_URL")
API_KEY = os.getenv("HF_TOKEN")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")


# -----------------------------
# INIT CLIENT (SAFE)
# -----------------------------
client = None
if API_BASE_URL and API_KEY:
    try:
        client = OpenAI(
            base_url=API_BASE_URL,
            api_key=API_KEY
        )
    except Exception:
        client = None


# -----------------------------
# OPTIONAL LLM INTERPRETATION
# -----------------------------
def interpret_results(easy, medium, hard, avg):
    if client is None:
        return "LLM interpretation skipped (no API configuration).Falling back to rule-based evaluation."

    try:
        prompt = f"""
Interpret these reinforcement learning environment results:

Easy: {easy:.2f}
Medium: {medium:.2f}
Hard: {hard:.2f}
Average: {avg:.2f}

Give a short, insightful summary.
"""

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100,
            temperature=0.3,
        )

        return response.choices[0].message.content.strip()

    except Exception:
        return "LLM interpretation unavailable due to API error. "


# -----------------------------
# MAIN EXECUTION
# -----------------------------
def main():
    print("🔥 inside main()")
    print("\n" + "="*60)
    print(" CLOUD KITCHEN ENVIRONMENT - BASELINE EVALUATION")
    print("="*60)

    print("\nRunning tasks...\n")

    easy = task_easy()
    print(f"[Easy Task   ] Score: {easy:.2f}")

    medium = task_medium()
    print(f"[Medium Task ] Score: {medium:.2f}")

    hard = task_hard()
    print(f"[Hard Task   ] Score: {hard:.2f}")

    avg = (easy + medium + hard) / 3

    print("\n" + "-"*60)
    print(" SUMMARY")
    print("-"*60)

    print(f"Easy   : {easy:.2f}")
    print(f"Medium : {medium:.2f}")
    print(f"Hard   : {hard:.2f}")
    print(f"Average: {avg:.2f}")

    print("\n" + "-"*60)
    print(" LLM INTERPRETATION")
    print("-"*60)

    interpretation = interpret_results(easy, medium, hard, avg)
    print(interpretation)

    print("\n" + "="*60)
    print("Author: Monu Mandal | Cloud Kitchen RL Environment")
    print("="*60)


if __name__ == "__main__":
    main()

    