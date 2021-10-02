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
    def request_input_for_hangman_answer():
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
    
    def randomly_select_hangman_answer(possible_answers):
        """
        Randomly selects an answer for hangman from a list of possible answers.

        Parameters:
            possible_answers (array of strings): array of possible answers

        Returns: the selected answer
        """
        return renpy.random.choice(possible_answers)

    def say_message_object(message):
        """
        Say a message object (uses the Message class)

        Parameters:
            message (Message): the message object containing the character and message
        """
        if (message != None):
            renpy.say(message.character, message.message)
    

# init python priority 5: place to setup variables
init 5 python:
    # set max number of tries
    max_tries = 6

    DEBUG_force_request_answer = False # For debugging, forcibly requests an answer
    possible_answers = [
        "leave my home",
        "get the heck out",
        "i will kill you",
        "you will die here",
        "death awaits you"
    ]

    # set messages to be told per used-up try (first item = first message shown at the start)
    # player lose feelings to body parts.
    messages_per_try = [
            None,
            Message("", "... That's strange, my leg fell asleep."),
            Message("", "Now my other leg fell asleep... What's going on?"),
            Message("", "I can no longer feel my left arm. This ghost is doing something to me..."),
            Message("", "My right arm is gone too..."),
            Message("", "I can't feel my chest anymore... I think I'm going to faint...")
        ]




"""
===== Screen Initialization Section =====
"""
screen hangman(message):
    style_prefix "black"
    frame:
        xalign 0.5
        ypos 0.45
        vbox:
            text "[message]"

style black_frame:
    background "#000000d9"

screen hangman_used(used_letters):
    style_prefix "black"
    frame:
        xalign 0.5
        ypos 0.60
        vbox:
            text "Letters Used: \"[used_letters]\""

style black_frame:
    background "#000000d9"




    
"""
===== Main Label for Hangman =====
"""
# Hangman starts here
label hangman:
    play music "<from 11 to 30>./music/Ringin_eaR.wav" fadein 4.0 volume 0.2 loop

    python:
        """
        1) Retrieve an answer
        """
        answer = ""
        if (DEBUG_force_request_answer):
            # DEBUG: Retrieves answer from standard input
            answer = request_input_for_hangman_answer()
        else:
            # This retrieves an answer from a list of possible answers
            answer = randomly_select_hangman_answer(possible_answers)


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
            renpy.show_screen("hangman_used", excluded_letters)

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
                guess = renpy.input("I have only [remaining_tries] tries left, h-huh?. I s-should pick a different letter.", "", length=1, allow="abcdefghijklmnopqrstuvwxyz", exclude=excluded_letters)


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
                renpy.say(None, "I-it's not the letter [guess] h-huh? M-man...what is this ghost trying to say..")
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
        renpy.hide_screen("hangman_used")
        if correct_answer_found:
            renpy.play(audio.correct, channel=u'sound')
            renpy.music.set_volume(0.5, delay=0, channel=u'sound')
            renpy.say(None, "I did it. I did it!! I guessed correct and was able to communicate with the ghost! \"[answer]\", huh!? Man..this ghost sounds aggressive." )
        else:
            renpy.play(audio.buzzWrong, channel=u'sound')
            # Possibly print the last message
            if message_index == current_tries and message_index < len(messages_per_try):
                say_message_object(messages_per_try[message_index])
                message_index += 1
            renpy.say(None, "I couldn't..do..it. My whole body hurts.. The last thing I saw was my teammates running toward me...")
            renpy.jump("restart_hangman")
    stop music fadeout 1.0
    return

label restart_hangman:
    menu: 
        "{color=#9b0617}Try again.{/color}":
            jump hangman