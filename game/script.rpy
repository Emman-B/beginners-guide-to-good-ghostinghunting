#Credits:
#https://lemmasoft.renai.us/forums/viewtopic.php?t=26544
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
##configure fonts ##
#name: Nova Slim
#text: Inconsolata
#maze: Inconsolata
#hangman: Lacquer
init python:
    config.preload_fonts = ['NovaSlim-Regular.ttf','PoorStory-Regular.ttf','Lacquer-Regular.ttf','Inconsolata-Regular.ttf']
    #change fonts in gui.rpy#
    #style.default.font = "NovaSlim-Regular.ttf"
#define gui.text_font = "Inconsolata-Regular.ttf" #sets dialogue text to inconsolata
#style say_label font "PoorStory-Regular.ttf" #sets character font to nova slim
# The game starts here.

##MUSIC##
define audio.mazebgm = "./music/panik@theHouseonYYYYstreet.wav"
define audio.mainbgm = "./music/Ringin'eaR.wav"
define audio.setupbgm = "./music/Ghost techies.wav"
#########

##SFX##
define audio.glassShatter = "./sound_edited/glass_shatter10.wav"
define audio.doorSlam = "./sound_edited/door_slam.wav"
define audio.doorSlamClick = "./sound_edited/door_slam_click.wav"
define audio.heavyBreath1 = "./sound_edited/heavy_breathing01.wav"
define audio.heavyBreath2 = "./sound_edited/heavy_breathing02.wav"
define audio.clothRustling = "./sound_edited/cloth_rustling.wav"
define audio.runningLight = "./sound_edited/footstep_running_light.wav"
define audio.runningLoud = "./sound_edited/footstep_running_loud.wav"
define audio.radioStatic = "./sound_edited/radio_stathicc.wav"
#######
label start:

    scene debug_bg

    show debug_character

    menu:
        "You're in the debug menu! Choose where you want to be sent."

        "Ghost-chase scene":
            call begin_chase_room
        
        "Debug hangman game":
            call hangman

        "Exit game":
            return


    return
