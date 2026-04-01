import os
import openai
import dotenv

dotenv.load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

class Brain:
    def __init__(self):
        self.memory = []

    def add_to_memory(self, message):
        self.memory.append(message)

    def get_memory(self):
        return self.memory
    
    def get_messages(self):
        return "\n".join(self.memory)

    def generate_response(self, prompt):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()