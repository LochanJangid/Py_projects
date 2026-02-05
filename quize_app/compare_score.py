def comp_score(user_score):
    """Compare score and store score"""
    filepath = 'scores.txt'
    with open(filepath) as f:
        scores = f.readlines()
        total_scores = len(scores) # Must be stored at least one score because [ZeroDivisionError]
        # Scores that are less than current user score
        less_scores = 0
        for score in scores:
            if int(score) < user_score:
                less_scores += 1
            
        user_above_scores = less_scores * 100 / total_scores
        
    
    with open(filepath, 'a') as f:
        # Store score 
        f.write(f'{int(user_score)}\n')

    return user_above_scores