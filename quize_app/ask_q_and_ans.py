def ask_question(question, i):
    """A model that make interface of asking question."""
    print(' ', end=' ')
    print('-'*len(question['question']))
    print(f'  Q{i+1}: {question['question']}')
    print(' ', end=' ')
    print('-'*len(question['question']))

    for j in range(4):
        print(f"\t {chr(65+j)}) {question['options'][j]}")
    print()
    
def ask_answer(question):
    """Ask questions"""
    user_answer = input('\tYour answer: ')
    print()
    if user_answer == question['answer']:
        return True
    return False