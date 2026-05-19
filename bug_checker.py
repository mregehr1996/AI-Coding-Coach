"""
Bug checker module.

This file checks code for likely bugs and explains fixes.
"""


class BugChecker:
    """Checks code for errors and possible bugs."""

    def __init__(self, ai_client):
        self.ai_client = ai_client

    def check_for_bugs(self, code):
        """Review code for bugs."""
        prompt = f"""
You are a helpful debugging coach.

Check this code for bugs.

Use this format:
1. What errors or issues you see
2. Why each issue happens
3. Corrected code
4. How to avoid this mistake next time

Code:
{code}
"""
        return self.ai_client.ask(prompt)
