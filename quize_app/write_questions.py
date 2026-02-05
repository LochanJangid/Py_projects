import json 


def write_new_question():
    """A model that writes new questions to question.json"""

    with open('questions.json', mode='r', encoding='utf-8') as f:
        questions = json.load(f)
        new_id = len(questions)

    # Take Inputs 
    new_question = input('Question: ')
    if  new_question.lower() == 'q': return

    option_a = input('Option A: ')
    if  option_a.lower() == 'q': return

    option_b = input('Option B: ')
    if  option_b.lower() == 'q': return

    option_c = input('Option C: ')
    if  option_c.lower() == 'q': return

    option_d = input('Option D: ')
    if  option_d.lower() == 'q': return
    # For take write answer
    while True:
        answer = input('Answer: ')
        if answer.lower() in ['a','b','c','d']:
            break
        print('Answer should be a / b / c / d')
        print('Try Again!')



    new_question = {"question_id": new_id,
                    "question": new_question,
                    "options": [option_a, option_b, option_c, option_d],
                    "answer": answer}

    questions.append(new_question)

    with open('questions.json', 'w', encoding='utf-8') as f:
        json.dump(questions, f)


yes_responses = ['y', 'yes', 'ya']
while True:
    print('Type \'q\' anytime for quit')
    write_new_question()
    response = input('Do you want to add more questions? ')
    if response.lower() not in yes_responses:
        'Ta Ta Bye Bye.'
        break
