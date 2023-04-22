import random

answer = "Hello World!"

#Convert the answer to list of characters
answer_chars = list(answer)

#Shuffle up the list and then convert it back to string
random.shuffle(answer_chars)
shuffled_answer = "".join(answer_chars)

#Keep looping until the 3 attempts are used
attempts = 3
while attempts > 0:

#Ask user to input their answer
    print("Please rearrange the letters to spell the correct word! : ")
    print(shuffled_answer)

#Get the user's answer
    user_answer = input("Your answer: ")

#Check if user is correct
    if user_answer == answer:
        print("Congrats! you spelled it correct!")
        break
    else:
        print("Sorry, that is incorrect. Try again...")
        attempts -= 1

#Display correct answer if out of attempts
if attempts == 0:
    print("Sorry, you are out of attempts.")
    print(f"The correct answer is {answer}")
