import time
# greeting the user
print("Welcome to python quiz!")
time.sleep(2)
print("I will shortly explain how the game works. To answer the question, just type the letter you choose.")
time.sleep(4)

# dictionary that will store all the questions
quiz_dict = {
    1 :  { 
        "text" : "What is the capital of Italy?: ",
        "answer_A" : "A) Rome",
        "answer_B" : "B) Paris",
        "answer_C" : "C) Berlin",
        "answer_D" : "D) Prague",
        "correct"  : "A"
    },
    2 :  { 
        "text" : "Which element is the most abundant in the Earth's atmosphere?: ",
        "answer_A" : "A) Oxygen",
        "answer_B" : "B) Nitrogen",
        "answer_C" : "C) Carbon Dioxide",
        "answer_D" : "D) Hydrogen",
        "correct" : "B"
    },
    3 :  { 
        "text" : "Who was the first President of the United States?: ",
        "answer_A" : "A) Abraham Lincoln",
        "answer_B" : "B) George Washington",
        "answer_C" : "C) Thomas Jefferson",
        "answer_D" : "D) John Adams",
        "correct" : "B"
    },
    4 :  { 
        "text" : "Who wrote the play Romeo and Juliet? : ",
        "answer_A" : "A) William Shakespear",
        "answer_B" : "B) Charles Dickens",
        "answer_C" : "C) Jane Austen",
        "answer_D" : "D) Mark Twain",
        "correct" : "A"
    },
    5 :  { 
        "text" : "What is the largest desert in the world by area?: ",
        "answer_A" : "A) Sahara",
        "answer_B" : "B) Gobi",
        "answer_C" : "C) Antartic Desert",
        "answer_D" : "D) Arabian Desert",
        "correct" : "C"
    }
}
# definition of the quiz function that will start the game, show the questions 
# and controll the user's answer
def quiz():
    try:
        score = 0 # 1 correct answer = 50 points, 1 wrong answer = 0 points
        for i in quiz_dict:
            # shows the question with the multiple answer to the user
            print(quiz_dict[i]["text"])
            time.sleep(2)
            print(quiz_dict[i]["answer_A"],quiz_dict[i]["answer_B"],quiz_dict[i]["answer_C"],quiz_dict[i]["answer_D"])
            user_answer = input("What is your answer?: ")
            # checks if the answer is correct
            if user_answer.lower() == quiz_dict[i]["correct"].lower():
                print(f"Congratulation! {user_answer} is the correct answer!")
                score += 50
            else:
                print(f"{user_answer} is not correct. Let's move on to the next question")
            i += 1
        print(f"Your final score is {score}! Thank you for playing! ")
    except :
        print("Your input is not valid")

quiz()