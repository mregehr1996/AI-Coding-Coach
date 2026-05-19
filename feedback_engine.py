"""
Feedback engine module.

This file gives improvement feedback on code.
"""


class FeedbackEngine:
    """Gives code improvement suggestions."""

    def __init__(self, ai_client):
        self.ai_client = ai_client

    def give_feedback(self, code):
        """Give feedback on code quality."""
        prompt = f"""
You are a professional but beginner-friendly code reviewer.

Review this code.

Use this format:
1. What is good about the code
2. What can be improved
3. Cleaner version if needed
4. One next skill the programmer should practice

Code:
{code}
"""
        return self.ai_client.ask(prompt)
