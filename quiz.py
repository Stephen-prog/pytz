# Python quiz game

questions = ("How many elements are in the periodic table?: ",
             "Which animal lays the largest egg?: ",
             "What is the most abundant gas in Earth's atmosphere?: ",
             "How many bones are in the Human body?: ",
             "Which planet in the solar system is the hottest?: ")

options = (("A. 116", "B. 117", "C. 119", "D. 118"),
           ("A. Whale", "B. Ostrich", "C. Crocodile", "D. Elephant"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
           ("A. 209", "B. 208", "C. 207", "D. 206"),
           ("A. Mars", "B. Venus", "C. Mercury", "D. Earth"))

answers = ("D", "B", "A", "D", "C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter an option between A-D: ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"The correct answer is {answers[question_num]}.")
    question_num += 1

print("-----------------------")
print("        RESULTS        ")
print("-----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%.")