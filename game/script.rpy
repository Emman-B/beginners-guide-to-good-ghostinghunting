#Credits:
#https://lemmasoft.renai.us/forums/viewtopic.php?t=26544
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#mc input name
define mc = Character("[mcname]") # purple
define il = Character("Ilse") # beekeeper
define el = Character("Elodie") # blue
define va = Character("Vance") # red
##configure fonts ##
#name: Nova Slim
#text: Inconsolata
#maze: Inconsolata
#hangman: Lacquer
init python:
    DEBUG_start_menu_testing = False # Set to true to enable the debug menu at the start
    config.preload_fonts = ['NovaSlim-Regular.ttf','PoorStory-Regular.ttf','Lacquer-Regular.ttf','Inconsolata-Regular.ttf']
    
# The game starts here.

##MUSIC##
define audio.mazebgm = "./music/panik@theHouseonYYYYstreet.wav"
define audio.mainbgm = "./music/Ringin_eaR.wav"
define audio.setupbgm = "./music/Ghost_techies.wav"
#########

##SFX##
define audio.glassShatter = "./sfx/glass_shatter10.wav"
define audio.doorSlam = "./sfx/door_slam.wav"
define audio.doorSlamClick = "./sfx/door_slam_click.wav"
define audio.heavyBreath1 = "./sfx/heavy_breathing01.wav"
define audio.heavyBreath2 = "./sfx/heavy_breathing02.wav"
define audio.clothRustling = "./sfx/cloth_rustling.wav"
define audio.runningLight = "./sfx/footstep_running_light.wav"
define audio.runningLoud = "./sfx/footstep_running_loud.wav"
define audio.buzzWrong = "./sfx/buzz_wrong.wav"
define audio.tearing02 = "./sfx/tearing02.wav"
define audio.vaccum = "./sfx/vaccum.wav"
define audio.electronicAmbience = "./sfx/electronic_ambience.wav"
define audio.clickSingle = "./sfx/click_single.wav"
define audio.windClose = "./sfx/wind_med_speed_close.wav"
define audio.correct ="./sfx/correct.wav"
#######

label DEBUG_start_menu:
    menu:
        "You're in the debug menu! Choose where you want to be sent."

        "Ghost-chase scene":
            call begin_chase_room
        
        "Debug hangman game":
            call hangman

        "Exit debug menu":
            return

label start:
    "Hello there. What is your name?"
    python:
        mcname = renpy.input("I'm...", length=32)
        mcname = mcname.strip()
        if not mcname: 
            mcname = "Emm Cee"
    
    if DEBUG_start_menu_testing:
        call DEBUG_start_menu

    jump ch01

    return

label ch01:
    scene car_ride

    "\"Your destination is on the right.\""

    "While the monotone voice of the GPS barely catches my attention, the car rolling into a slow stop
    makes me look up and out the van's wide window."

    "Squinting through the darkness of night, I can make out an average sized townhouse."

    "The client had said it wasn’t an old or decrepit house, and yet looking at it now,
    I can see chipped paint and a boarded up window. Sure it’s not old, but it’s definitely damaged."

    "The client, a rather skittish lawyer, insisted on our services. Supposedly, they’re having trouble
    transferring the property’s ownership to new hands."
    
    "The new owner-to-be finds the house eerie and disturbing, so uncomfortable they might refuse to inherit it."

    "Both the lawyer and the owner-to-be believe these uncomfortable feelings originate from a
    supernatural source."

    "There were unknown messes littering the ground, furniture moved to positions
    they weren’t supposed to be in, appliances broken when they were working the last time they were
    touched."

    "Both attributed these mysteries to the presence of a ghost."

    "That’s where we come in."

    "I'm a member of a team of ghost hunters, hired to eliminate threats from the afterlife."

    "It's not the most dignified occupation, but I applied hoping to satisfy my need for
    adventure."

    "As the newest member of the team, I can only hope that I meet everyone's expectations."

    "After all, this is a team of professionals I'm joining."

    jump ch02

label ch02:
    scene truck

    "\"Out!\""

    "As per our team leader’s orders, I scramble out of the van. They’re already standing
    outside, waiting, signature hat secured on their head."

    mc "Yes, boss!"

    "Boss" "No need to call me boss. Just Ilse is fine."

    "That’s the boss for you; reliable and friendly. They know everything there is to
    know about ghost hunting. I’m sure I’ll learn a lot from watching them."

    il "I’m opening the trunk. Get your things."
