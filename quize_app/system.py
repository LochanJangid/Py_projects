import json
import random 

from ask_q_and_ans import *

def user_score(questions_count):
    with open('questions.json', encoding='utf-8') as f:
        questions = json.load(f)
        length = len(questions)
        appeared_questions = []
        correct_answers = 0
        i = 0
        while i < questions_count:
            random_question = random.randint(0, length-1)
            if random_question in appeared_questions:
                continue
            ask_question(questions[random_question], i)
            # Store in appeared questions
            appeared_questions.append(random_question)
            if ask_answer(questions[random_question]):
                correct_answers += 1
            i += 1

    return correct_answers