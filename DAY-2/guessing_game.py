correct_word = "maya"
guess_word = ""
guess_count = 0
guess_limit = 5
out_of_guesses = False

while guess_word != correct_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess_word = input("Enter your guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You LOSE!!!!!!!!")
else:
    print("You WIN!!!!!!!!")
