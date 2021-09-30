"""
===== Initialization Section =====
"""
# init python priority 0: any declarations
init 0 python:
    # Classes
    class Message:
        def __init__(self, character, message):
            self.character = character
            self.message = message

    # Functions
    def request_hangman_answer():
        """
        Debug function requesting user input for hangman answers

        Returns: the answer from user input
        """
        answer = ""
        while len(answer) < 3:
            answer = renpy.input("What should be the answer to the hangman?", "hello world", allow="abcdefghijklmnopqrstuvwxyz ")
            if len(answer) < 3:
                renpy.say(None, "That's a bit short, can you come up with something else?")
        
        renpy.say(None, "Answer retrieved!")
        return answer

    def say_message_object(message):
        """
        Say a message object (uses the Message class)

        Parameters:
            message (Message): the message object containing the character and message
        """
        renpy.say(message.character, message.message)
    

# init python priority 5: place to setup variables
init 5 python:
    # set max number of tries
    max_tries = 3

    # set messages to be told per try (first item = first message shown at the start)
    messages_per_try = [
            Message("Bob", "Hello world!"),
            Message("Steve", "Oh no, you don't have many tries"),
            Message("Mike", "It's your last try!")
        ]




"""
===== Screen Initialization Section =====
"""
screen hangman(message):
    style_prefix "black"
    frame:
        xalign 0.5
        ypos 0.5
        vbox:
            text "[message]"

style black_frame:
    background "#000000d9"




    
"""
===== Main Label for Hangman =====
"""
# Hangman starts here
label hangman:
    python:
        """
        1) Retrieve an answer
        """
        answer = request_hangman_answer()


        """
        2) Create two arrays, one for the answer as a character array and another for 
        flagging known letters (letters that the player has found in the answer).

        Also, if the answer contains spaces, set the spaces to be "True" (i.e.,
        it is shown)
        """
        # convert answer into char array
        answer_array = list(answer)
        # create list of flags per character
        current = [False] * len(answer_array)

        # set spaces in answer to true
        for i in range(len(answer_array)):
            if answer[i] == " ":
                current[i] = True

        """
        3) Set up for the hangman loop. We maintain variables for: how many tries
        that the player has used, whether correct answer was found, and any
        letters to exclude from the user input (to prevent duplicate letters
        being shown).
        """
        # used for navigating hangman
        current_tries = 0
        correct_answer_found = False
        excluded_letters = ""
        message_index = 0 # deciding what message to show
        
        """
        4) Start the hangman loop. This loops while the player hasn't found
        the correct answer and while they still have enough tries.
        """
        while max_tries > current_tries and not correct_answer_found:
            """
            4.1) Show the player's current progress.
            """
            # print the current
            print_current = ""
            for i in range(len(answer_array)):
                if current[i]:
                    print_current += " " + answer_array[i] + " "
                else:
                    print_current += " _ "
            # renpy.say(None, print_current)
            renpy.show_screen("hangman", print_current)

            """
            4.15) Print a message (if able to)
            """
            if message_index == current_tries and message_index < len(messages_per_try):
                say_message_object(messages_per_try[message_index])
                message_index += 1


            """
            4.2) Print how many tries the player has and also request
            for their input for what letter to guess. When a valid guess
            is provided, add that letter to the string containing excluded
            letters.
            """
            # display number of tries and accept input
            remaining_tries = max_tries - current_tries
            guess = ""
            while len(guess) == 0:
                guess = renpy.input("You have [remaining_tries] tries left. Guess a letter.", "", length=1, allow="abcdefghijklmnopqrstuvwxyz", exclude=excluded_letters)


            # exclude the guessed letter
            excluded_letters += guess

            """
            4.4) Try to check if the player guessed a correct letter. If so,
            go through the array of letters to show (in this case, it's the
            list called "current") and mark the corresponding positions in the
            list to be true.

            If the guess is wrong, reduce the number of tries by 1.
            """
            # try to find letter in answer
            if guess in answer_array:
                # Success Case, update the current array
                for i in range(len(current)):
                    if answer_array[i] == guess:
                        current[i] = True
            else:
                # Failure case: decrement number of tries
                renpy.say(None, "The letter [guess] was not found")
                current_tries += 1
            
            """
            4.5) If the player guessed all of the letters (all of the flags are True),
            then mark the correct answer as being found
            """
            # Correct answer is found if all elements in current is True
            if current.count(True) == len(current):
                correct_answer_found = True

        """
        5) Show the correct answer to the screen (whether it is found or not).

        Then, tell the user what the answer is with a different message depending
        on whether they won or not.
        """
        renpy.show_screen("hangman", answer)
        if correct_answer_found:
            renpy.say(None, "Congratulations! You found the correct answer: \"[answer]\"")
        else:
            renpy.say(None, "Sorry, the correct answer was: \"[answer]\"")

    return