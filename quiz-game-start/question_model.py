from dataclasses import dataclass


@dataclass
class Question:
    text: str
    answer: str

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
