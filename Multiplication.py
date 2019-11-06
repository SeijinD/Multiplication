import random

print("If you want to exit click q.")
print("If you want to reset number to practice again in different number click c.")

while True:
    breaker = False
    print("Type a number to practice?")
    wrongInput1 = True
    while wrongInput1:
        number = input()
        if number == "q": exit()
        try:
            int(number)
            wrongInput1 = False
        except:
            print("Print number or q")
            wrongInput1 = True 

    factors = list(range(10))
    random.shuffle(factors)

    for n in factors:
        if breaker:
            break
        wrong = True   
        while wrong:
            question = f"{n} x {number} = "
            wrongInput2 = True
            while wrongInput2:
                answer = input(question)
                if answer == "q": exit()
                if answer == "c": 
                    breaker = True
                    break          
                try:
                    int(answer)
                    wrongInput2 = False
                    if int(answer) == (n * int(number)):
                        print('Congratulation!')
                        wrong = False 
                    else:
                        print('Try Again!')
                except:
                    print("Print number or q or c")
                    wrongInput2 = True
            if breaker:
                break
