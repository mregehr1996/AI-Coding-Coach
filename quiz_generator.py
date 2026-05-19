"""
Quiz generator module.

This file creates programming practice quizzes.
"""


class QuizGenerator:
    """Generates coding quizzes."""

    def __init__(self, ai_client):
        self.ai_client = ai_client

    def generate_quiz(self, topic, difficulty):
        """Generate a quiz about a coding topic."""
        prompt = f"""
Create a {difficulty} level programming quiz about {topic}.

Use this format:
1. Five multiple-choice questions
2. Four answer choices per question
3. Answer key
4. Short explanation for each answer

Make it helpful for someone learning programming.
"""
        return self.ai_client.ask(prompt)
