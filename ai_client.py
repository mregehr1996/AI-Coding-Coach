"""
AI client module.

This file connects the app to the Google Gemini API.
"""

import os
from dotenv import load_dotenv
from google import genai


class AIClient:
    """Handles communication with the Gemini API."""

    def __init__(self):
        load_dotenv()

        self.api_key = os.getenv("GEMINI_API_KEY")
        self.model = os.getenv("GEMINI_MODEL", "gemini-2.0-flash")

        if not self.api_key:
            raise ValueError(
                "Missing GEMINI_API_KEY. Create a .env file and add your API key."
            )

        self.client = genai.Client(api_key=self.api_key)

    def ask(self, prompt):
        """Send a prompt to Gemini and return the response text."""
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt
        )

        return response.text or "No response was generated."
