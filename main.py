#Batoul Khoulani
# 11/18/2026
# Honors Computer Science 1301 - project2: Games and puzzles
## This program creates 3 games scramble, hangman/guess the word, and an extra game (custom scramble)

# import the random module
import random

#This is a dictionary for the scrambled game word list. It creates a hint system with the word being the key and the word description being the value
#that will be given to the user as a hint
scrambled_words = {
  "right": "Opposite of wrong",
  "Yellow": "The color of a banana",
  "Telescope": "Used to look at the sky",
  "Mystery": "What is unexplained",
  "Whisper": "Speaking quietly",
  "Castle": "Where a king might live",
  "Parachute": "Protects skydivers",
}
#This is a dictionary for the guess the word game word list. It creates a hint system with the word being the key and the word description being the value
#that will be given to the user as a hint
guess_words = {
  "Pizza": "Italians' favorite dish",
  "Guitar": "A string instrument",
  "Dinosaur": "Extinct animal",
  "Treasure": "What pirates look for",
  "Rhythm": "The beat of a song",
  "Extraordinary": "What is not ordinary",
  "Queue": "Line of people",
  
}

# This is a helper function that asks the user a yes or no question
#It keeps asking the user till a y or n is passed
# @param is the message shown to the player when the function play() is called
# @return True if the player answered y and False if the player answered n
def play(message = "Play again (Y/N)?"):
    while True:
        # Takes the answer of the user and return it to a lower case letter if it is upper case
        answer = input(message).strip().lower()
        if answer == "y":
            return True
        if answer == "n":
            return False
        print("Type (Y or N)")

#This is function is a Word Scramble game
# The function goes through a list of words randomly
#It scramble the word and gives the user 3 attempts to unscramble the Word
#The game ends when the user completes all the words or run out of attempts
#The game gives the user a hint when typing "bonus" which cost 1 attempts
#The game can stop after any word and display the score
#This function has no paramters and does not return anything
def scramble():
  while True:
    print("Scramble Words")
    print("Type 'bonus' for a clue; if a clue is used, attempts drop by 1")
    words = ["right", "Yellow", "Telescope", "Mystery", "Whisper", "Castle", "Parachute"]
    score = 0
    #Randomize the order of the words
    random.shuffle(words)
    # Loops through each word in the list words
    for word in words:
      scrambled = word
      while scrambled == word:
          #Scramble the word can return the same word so
          #it keep scrambling untill the word is different
        scrambled = "".join(random.sample(word, len(word)))

      print(f"Scrambled word: {scrambled}")
      attempts = 3
      solved = False
      while attempts > 0 and not solved:
        print(f"You have {attempts} remaining")
        #Ask the user to make an attempt
        guess = input("unscrambled: ").strip().lower()

        #Reject non-letters guesses
        if not guess.isalpha():
          print("Invalid input. Enter letters only")
          continue
  
        #Checks if the user ask for a bonus
        if guess == "bonus":
            #Decrease the attempts by 1 if the guess is 'bonus'
          attempts = attempts - 1
          #provide a hint from the values in the dictionary scrambled_words
          print("Clue:", scrambled_words[word])
          #Display the attempts remaining after the hint
          print(f"Attempts remaining: {attempts}")
          continue

        #Checks if the guess matches the correct word
        #The word is converted into lower case letters
        if guess == word.lower():
          print("Correct!!!")
          #Increases the score by 1
          score = score + 1
          solved = True
        else:
          print("Wroooong!!!")
          # decrease the attempts by 1
          attempts = attempts - 1

      #If the user fails the word and score are displayed
      if not solved:
        print(f"incorrect the word is {word}")
        print(f"Your score is {score} points")

      
      #If the remaining attempts are 0 the game ends
      if attempts == 0:
        print("Out of attempts! :(")
        break
    #Display the score
      print(f"Your current score is {score} points")
      #End the game if the word is not the last word and the user decided to stop playing
      if word != words[-1] and not play("keep playing (Y/N)?"):
        print(f"You scored {score} points")
        return

    #Print the score and end the game if the user decide to stop
    print(f"You scored {score} points")
    if not play():
      break
      
# This is a helper function that picks a random word for the game guess the word
# @return the randomly chosen word from the list
def word_guess():
  ws = ["Pizza", "Guitar", "Dinosaur", "Treasure", "Rhythm", "Extraordinary", "Queue"]
  return random.choice(ws)

#This is a helper function that returns a secret hidden word
#The function show the guessed letter and  "_" for the hidden letters
# @param w is secret word
# @param guessed_letters is the letters the player has guessed
# @return a string of the current status of the word with the guessed and non guessed letters
def letters(w, guessed_letters):
  visible = ""
  #loops through the letters in the word
  for i in w:
    #Check if the guessed letter is in the word and display it
    #convert the user input to lower case letter
    if i.lower() in guessed_letters:
      visible = visible + i
    # If the letter has not been guessed it 
    #shows an underscore
    else:
      visible = visible + "_"
  return visible
 
 
# Function plays a hangman/guess the word game
#where the game picks a random word and the player has to guess 
# one letter at a time. the player is given 4 attempts, guessing a wrong letter cost 1 attempt.
#The game also give the player a hint by typing "bonus" which cost 1 attempt.
#The game ends when the word is guessed or the player run out of attempts
#The player is then asked to continue playing or quite
#The function has no parameters and does not return any value
def guessing():
  while True:
    print("Guess the Word")
    print("Type 'bonus' for a clue; if a clue is used, attempts drop by 1")
    #call the function word_guess and store it in secret
    secret = word_guess()
    #look for the clue in the dictionary guess_words
    clue = guess_words[secret]
    #Create a set for the guessed letters
    guessed_letters = set()
    score = 0
    attempts = 4
    #display the secret word with "_" in the place of each letter
    print("Guess the word:", letters(secret, guessed_letters))

    
    while attempts > 0:
      #ask the user to make a guess and convert it to lower case letter  
      entry = input("Guess a letter: ").strip().lower()
      #If the user entry is "bonus" the game provid hint from the 
      # dictionary guess_words and decrease attempts by 1
      if entry == "bonus":
        attempts = attempts - 1
        print("Clue:", clue)
        print(f"Attempts left: {attempts}")
        continue

      #If the user provided non letter or more than one letter
      #the game ask the user to provide a valid input
      if len(entry) != 1 or not entry.isalpha():
        print("Invalid entry try again")
        continue
      #If the letter is already guessed the game
      #ask the user to make another guess
      if entry in guessed_letters:
        print("Already guessed try again")
        continue
      #The guessed letter is added to the entries of the user  
      guessed_letters.add(entry)
      #If the user guessed a letter that is not in the word
      #the attempts drop by 1
      if entry not in secret.lower():
        attempts = attempts - 1
        print(f"The letter '{entry}' is not in the word")
        print(f"you have {attempts} remaining")

      mystery_word = letters(secret, guessed_letters)
      print("secret word:", mystery_word)
      #If the user guessed the word and no "_" remain
      #The score increase by 1, the score and word are displayed, and the game ends
      if "_" not in mystery_word:
        score = score + 1
        print(f"Great you guessed the word :) your score is {score} points, the correct word is {secret}")
        break
    #If the user has 0 attempts remaining the game ends
    #and the secret word is displayed
    if attempts == 0:
      print(f"You ran out of attempts :( the correct word is {secret}")
    #Ask the user to continue playing or quit
    #If the answer is n the game ends
    if not play("Play again? (y/n): "):
      break
    
#This function exit the game
# @return True stop the main menu loop
def exit_game():
  print("Thanks for playing! Goodbye :)")
  return True

#This function is the bonus feature. it is a custom
#Scramble game which ask the user to provide words that will be stored in a set
#The program pick a random word and scramble
#It gives the user 3 attempts to unscramble It
#The score is shown after each word and at the end of the round and the 
#player can choose to play again with the Same
#words or quit
#This game has no parameters and does not return any value
def custom_scramble():
    print("Custom Scramble")
    print("Enter your own word to create a custom scramble game. Once you are done press enter to stop")
    #Create an empty set
    customized = set()

    while True:
        #Ask the user to enter words
        #Convert the words to lower case letter
        word = input("Enter a word: ").strip().lower()
        #If the word has no letters and 
        #there are no words in the set
        #The user is asked to enter a word
        if word == "":
            if len(customized) == 0:
                print("Please enter a word")
                continue
            break
        #If the provided word has non letters, is shorter than 3 letters,
        #or the word has the same letter it ask the user to enter a word
        #consistent of at least 3 unique letters
        if not word.isalpha() or len(word) < 3 or len(set(word)) < 2:
            print("Enter at least 3 unique letters")
            continue
        #If the provided word already exist in the set the user
        #is asked to provid another word
        if word in customized:
            print("This word already exists, please enter a new word")
            continue
        #The word is added to the set customized
        customized.add(word)

    while True:
        #The set customized is turned into a list
        #Called words_list because a set has no posistions
        #which make it impossible to use the function random on a set
        words_list = list(customized)
        score = 0
        #This loops through the list words_list
        #and keep picking words unit every word is used once
        while len(words_list) > 0:
            #pick random word from the list
            word = random.choice(words_list)
            #Remove the word so it is only used once
            words_list.remove(word)
            #Scramble the word randomly and repeat
            #If the result matches the original word
            scrambled = word
            while scrambled == word:
                scrambled = "".join(random.sample(word, len(word)))
            print(f"Unscramble: {scrambled}")

            attempts = 3
            solved = False

            while attempts > 0 and solved == False:
                #Ask the user to make a guess and convert the
                #guessed word to a lower case letters word
                guess = input("Make a guess: ").strip().lower()
                #If the guess is non-letter the user
                #is asked to try again
                if not guess.isalpha():
                    print("Invalid input. Enter letters only")
                    continue
                #If the guess is correct the score 
                #increase and the condition solved is met
                if guess == word:
                    print("Correct!!")
                    score = score + 1
                    solved = True
                #If the guess is incorrect the attempts decrease
                else:
                    attempts = attempts - 1
                    print("Wroooong!!")
                #If the attempts reach 0 the game ends
                if attempts == 0:
                    print(f"You have 0 attempts remaining :(")
                    break
            #If the user fails the word is printed
            #and the code moves to the next one
            if not solved:
                print(f"The word is: {word}")
            #The score is shown when the game ends
            print(f"Your score is {score} points")
        #The final score is displayed and the game ask the player to 
        #continue or quit
        print(f"Your final score is {score} points")
        if not play("Play again (Y/N)? "):
            break
            
#The dictionary store the main menu options.
#Each key is what users should type, and the value is a pair
#of the available options and the function that runs when 
#the option is chosen
menu = {
  "1": ("Scramble Words", scramble),
  "2": ("Guess the Word", guessing),
  "3": ("My Bonus Feature", custom_scramble),
  "4": ("Exit", exit_game)
  
}

#This functions displays the main menu by looping through the menu dictionary
#This function does not have any parameters
#and does not return any values
def display_menu():
  print("===Main Menu===")
  for key, (name, _) in menu.items():
    print(f"{key}. {name}")

#This function runs the program
#it displays the menu, ask the user to make a choice,
#runs the chosen game. The menu is displayed again after each game.
#Loop stops when the user choose exit.
#Invalid choices show a message and display the menu again
#This function has no parameters and does not return
#any values
def main():
  while True:
    #Calls the displa_menu function to show the menu
    display_menu()
    #Ask the user to make a choice
    choice = input("Make a choice: ").strip().lower()

    #If the choice is in the menu function run the game
    if choice in menu:
      name, game = menu[choice]
      if game():
        break

    else:
      print("Invalid choice, make another choice: ")
      
#Start the program
main()


  