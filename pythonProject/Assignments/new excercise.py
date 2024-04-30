import random

new_list=["apple","banana","carrot","spinach","grapes"]
user_choice=input("Enter the word")
def chances():
    chances=2
    return chances
def guess_word():
    computer_choice=random.choice(new_list)
    chances=2
    while chances > 0:
        if user_choice == computer_choice:
            break
        chances -= 1
    else:
        print(f"Sorry, you have run out of attempts. The correct word was {computer_choice}")
guess_word()



