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
        "death awaits you",
        "tresspassers will be persecuted"
    ]

    # set messages to be told per used-up try (first item = first message shown at the start)
    # player lose feelings to body parts.
    messages_per_try = [
            None,
            Message("", "... That's strange, I can't feel my leg! What's going on?"),
            Message("", "Now I've suddenly lost feeling in my other leg... I can't even walk like this. The ghost, it's doing something to me."),
            Message("", "I can no longer feel my left arm. I'm running out of limbs... I've got to find out what the ghost is saying!"),
            Message("", "My right arm...That's the last of my limbs. I can't move! At this rate..."),
            Message("", "I can hear my pulse slowing down in my chest. I think... this is my last chance to get it right before I pass out...")
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
    play music "<from 11 to 30>./music/Ringin_eaR.wav" fadein 4.0 volume 0.4 loop

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
                guess = renpy.input("Guess a letter:", "", length=1, allow="abcdefghijklmnopqrstuvwxyz", exclude=excluded_letters)


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
                renpy.say(None, "Looks like the letter [guess] isn't part of the message. Just what is it trying to say...?")
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
            renpy.say(None, "I did it! This must be the correct answer! The ghost is saying \"[answer]\" ...? That's... really aggressive." )
            renpy.hide_screen("hangman")
            renpy.jump("hangman_end")
        else:
            renpy.play(audio.buzzWrong, channel=u'sound')
            # Possibly print the last message
            if message_index == current_tries and message_index < len(messages_per_try):
                say_message_object(messages_per_try[message_index])
                message_index += 1
            renpy.say(None, "I've...failed. This is it. I can feel... the last of my focus fading... away. I'll... do better in my... next life...")
            renpy.jump("restart_hangman")
    stop music fadeout 1.0
    return

label restart_hangman:
    menu: 
        "{color=#9b0617}Try again.{/color}":
            jump hangman

label hangman_end: 
    hide ghost mad
    "My limbs feel heavy, but slowly, I regain feeling in them."
    "The ghost must have also inflicted this sensation onto my teammates."
    "I watch as everyone else also struggles to get up."
    show ilse shocked at right with easeinleft
    "With a surge of energy, Ilse stands in the blink of an eye, even with the heft of the Ghyson Vac-Pack weighing them down."
    "In a single swift motion, the Ghyson is switched on. The loud {i}‘vwwoooooom’{/i} of the vacuum overtakes all other noises in the room."
    hide ilse shocked 
    show ghost mad at middle with dissolve:
        alpha 0.25
        xzoom 1.0 yzoom 1.0
        linear 1.0 xzoom 1.20 yzoom .80
        linear 1.0 xzoom .80 yzoom 1.20
        linear 1.0 xzoom 1.0 yzoom 1.0
        repeat 1
    g "{i}OOooooOooouuuuUuAAHhh{/i}"
    hide ghost mad with dissolve 
    "The ghost’s shrieks are drowned out as it’s sucked into the Vac-Pack."
    "As expected of the boss, forever reliable!"
    show ilse happy at middle with dissolve 
    il "Good job, team."
    show vance neutral at right with moveinright
    va "Whew, what a relief now that it’s gone. My legs are still shaking..."
    show elodie scared at left with moveinleft
    el "Now that what’s gone? By the way, I think there’s a leaky gas pipe somewhere."
    el "The carbon monoxide poisoning really got us bad." 
    #show vance scared at offscreenleft with move 
    hide vance scared with dissolve 
    #show elodie scared at offscreenleft with move
    hide elodie scared with dissolve 
    show ilse neutral 
    il "That was good work you did back there."
    show ilse happy 
    il "Keep it up and before you know it, you’ll be the leader of your own ghost hunting team!"
    show ilse shocked 
    il "In fact, you’ll be the leader of this team starting tomorrow!"
    hide ilse shocked 
    show mc scared at left with dissolve 
    mc "Huh?"
    show ilse neutral at right with dissolve 
    il "This was my last job. I’m retiring."
    "B-But I was looking forward to learning from the boss!"
    show ilse happy 
    il "I’m sure you can make use of the team’s individual strengths."
    "What strengths?!"
    show ilse neutral 
    il "You’ve proven yourself capable of being a professional ghost hunter."
    show ilse neutral at offscreenright with move
    hide ilse neutral with dissolve 
    "This was only my first job. I’m still just a beginner!"
    "Boss, come baaaackkk!!!"
    show mc scared at offscreenright with move 
    hide mc scared 




