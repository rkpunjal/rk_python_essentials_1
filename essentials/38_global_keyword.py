
score = 100

def double_score():
    global score
    print("read in function : ", score )
    # you can read, but not assign
 #  score = score * 2 # UnboundLocalError: local variable 'score' referenced before assignment

    # access global variable
    score *= 2 # and change it

    # declare a global variable inside the function
    # it can be accessed outside the function
    global score_in_func
    score_in_func = 24


double_score()
print("score : ", score)  # changed from within the function
print("score_in_func : ", score_in_func) # global variable declared inside function accessed outside the function
