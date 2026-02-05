from compare_score import comp_score
from system import user_score

print('\t\t\t\t***QUIZE_APP***\n')

questionCountInput = True
while questionCountInput:
    try: questions_count = int(input('-How many questions do you want to answer: '))
    except ValueError: print('Invalid input!')
    else: questionCountInput = False

correct_answers = user_score(questions_count)
score = correct_answers*100/questions_count

print(f'Result: {score:.2f}%')
print(f'You are more intelligest than {comp_score(score):.0f}% CEO\'s.')