"""
Code explainer module.

This file explains code in beginner-friendly language.
"""


class CodeExplainer:
    """Explains code step by step."""

    def __init__(self, ai_client):
        self.ai_client = ai_client

    def explain(self, code):
        """Explain pasted code."""
        prompt = f"""
You are a patient coding tutor.

Explain this code for a beginner.

Use this format:
1. What the code is trying to do
2. Line-by-line explanation
3. Important programming concepts
4. One simple practice example

Code:
{code}
"""
        return self.ai_client.ask(prompt)
