import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
KB_FILE = os.path.join(BASE_DIR, "knowledge_base.json")


def load_knowledge_base():
    with open(KB_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def search_knowledge_base(user_question):
    knowledge_base = load_knowledge_base()

    question = user_question.lower()

    for item in knowledge_base:
        text = (
            item["category"]
            + " "
            + item["problem"]
            + " "
            + " ".join(item["solution"])
        ).lower()

        if any(word in text for word in question.split()):
            return item

    return None