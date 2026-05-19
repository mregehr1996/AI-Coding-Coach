"""
AI Coding Coach

Run this file to start the app:

python main.py
"""

from ai_coding_coach.ai_client import AIClient
from ai_coding_coach.bug_checker import BugChecker
from ai_coding_coach.code_explainer import CodeExplainer
from ai_coding_coach.feedback_engine import FeedbackEngine
from ai_coding_coach.quiz_generator import QuizGenerator


def print_menu():
    """Display the main menu."""
    print("\n" + "=" * 50)
    print("AI Coding Coach")
    print("=" * 50)
    print("1. Explain code")
    print("2. Check code for bugs")
    print("3. Get feedback on code")
    print("4. Generate a practice quiz")
    print("5. Ask a general coding question")
    print("6. Exit")
    print("=" * 50)


def get_multiline_input(prompt):
    """
    Let the user paste multiple lines of code or text.
    Type DONE on its own line when finished.
    """
    print(f"\n{prompt}")
    print("Type DONE on its own line when finished.\n")

    lines = []

    while True:
        line = input()

        if line.strip().upper() == "DONE":
            break

        lines.append(line)

    return "\n".join(lines).strip()


def main():
    """Start the AI Coding Coach app."""
    try:
        ai_client = AIClient()
    except ValueError as error:
        print(f"Setup error: {error}")
        return

    code_explainer = CodeExplainer(ai_client)
    bug_checker = BugChecker(ai_client)
    feedback_engine = FeedbackEngine(ai_client)
    quiz_generator = QuizGenerator(ai_client)

    while True:
        print_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            code = get_multiline_input("Paste the code you want explained:")
            print("\nAI Response:\n")
            print(code_explainer.explain(code))

        elif choice == "2":
            code = get_multiline_input("Paste the code you want checked for bugs:")
            print("\nAI Response:\n")
            print(bug_checker.check_for_bugs(code))

        elif choice == "3":
            code = get_multiline_input("Paste the code you want feedback on:")
            print("\nAI Response:\n")
            print(feedback_engine.give_feedback(code))

        elif choice == "4":
            topic = input("\nWhat topic should the quiz be about? ")
            difficulty = input("Difficulty level beginner, intermediate, or advanced? ")
            print("\nAI Response:\n")
            print(quiz_generator.generate_quiz(topic, difficulty))

        elif choice == "5":
            question = get_multiline_input("Ask your coding question:")
            print("\nAI Response:\n")
            print(ai_client.ask(question))

        elif choice == "6":
            print("\nKeep building. You are getting better every rep.")
            break

        else:
            print("\nInvalid choice. Please choose a number from 1 to 6.")


if __name__ == "__main__":
    main()
