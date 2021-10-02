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
define audio.mainbgm = "./music/Ringin_eaR_ost_ver.wav"
define audio.enteringHouse = "./music/Ringin_eaR.wav"
define audio.setupbgm = "./music/Ghost_techies.wav"
#########

##SFX##
define audio.glassShatter = "./sfx/glass_shatter10.wav"
define audio.doorSlam = "./sfx/door_slam.wav"
define audio.doorSlamClick = "./sfx/door_slam_click.wav"
define audio.heavyBreathFast = "./sfx/heavy_breathing_fast.wav"
define audio.heavyBreathSlow = "./sfx/heavy_breathing_slow.wav"
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
define audio.radioStatic = "./sfx/radio_static.wav"
#######

##Image Character Sprites##
image bp sad = "./images/bp_rock_d.png"

image ghost mad = "./images/ghost_mad.png"
image ghost neutral = "./images/ghost_neutral.png"

image elodie neutral = "./images/elodie_neutral.png"
image elodie happy = "./images/elodie_happy.png"
image elodie scared = "./images/elodie_scared.png"
image elodie smug = "./images/elodie_smug.png"
image vance neutral = "./images/vance_neutral.png"
image vance scared = "./images/vance_scared.png"
image vance happy = "./images/vance_happy.png"

image ilse happy = "./images/ilse_happy.png"
image ilse mad = "./images/ilse_mad.png"
image ilse neutral = "./images/ilse_neutral.png"
image ilse scared = "./images/ilse_scared.png"

image mc happy = "./images/mc_happy.png"
image mc neutral = "./images/mc_neutral.png"
image mc scared = "./images/mc_scared.png"

##Image Backgrounds##
image bg dorm night = "./images/A01-3_HomeBase_DormRoom_Night.png"
image bg dorm day = "./images/A01-3_HomeBase_DormRoom_daytime.png"
image bg dorm evening = "./images/A01-3_HomeBase_DormRoom_Evening.png"
image bg bathroom day = "./images/Bath_house_test_daytime_v3.png"
image bg bathroom dusk = "./images/Bath_house_text_dusk_v2.png"
image bg bathroom night = "./images/Bath_house_text_night1_v2.png"
image bg bathroomGhostOrb night = "./images/Bath_house_text_night2_v2.png"

###########################

##custome x coord for sprites##

###############################

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
    scene bg dorm night with fade

    python:
        mcname = renpy.input("Your name?", length=32)
        mcname = mcname.strip()
        if not mcname: 
            mcname = "Emm Cee"
    mc "The name is [mc]."
    
    if DEBUG_start_menu_testing:
        call DEBUG_start_menu

    jump ch01

    return

label ch01:
    scene car_ride

    "\"Your destination is on the right.\""

    "While the monotone voice of the GPS barely catches my attention, the car rolling into a slow stop"
    "makes me look up and out the van's wide window."

    "Squinting through the darkness of night, I can make out an average sized townhouse."

    "The client had said it wasn't an old or decrepit house, and yet looking at it now,
    "I can see chipped paint and a boarded up window. Sure it's not old, but it's definitely damaged."

    "The client, a rather skittish lawyer, insisted on our services. Supposedly, they're having trouble"
    "transferring the property's ownership to new hands."
    
    "The new owner-to-be finds the house eerie and disturbing, so uncomfortable they might refuse to inherit it."

    "Both the lawyer and the owner-to-be believe these uncomfortable feelings originate from a" 
    "supernatural source."

    "There were unknown messes littering the ground, furniture moved to positions"
    "they weren't supposed to be in, appliances broken when they were working the 
    "last time they were touched."

    "Both attributed these mysteries to the presence of a ghost."

    "That's where we come in."

    "I'm a member of a team of ghost hunters, hired to eliminate threats from the afterlife."

    "It's not the most dignified occupation, but I applied hoping to satisfy my need for"
    "adventure."

    "As the newest member of the team, I can only hope that I meet everyone's expectations."

    "After all, this is a team of professionals I'm joining."

    jump ch02

label ch02:
    scene truck

    "\"Out!\""

    "As per our team leader's orders, I scramble out of the van. They're already standing"
    "outside, waiting, signature hat secured on their head." 

    show ilse neutral at left
    ""
    show ilse neutral at right with easeinleft 
    show mc neutral at left
    mc "Yes, boss!" 
    hide mc neutral at left
    "Boss" "No need to call me boss. Just Ilse is fine."
    "That's the boss for you; reliable and friendly. They know everything there is to" 
    "know about ghost hunting. I'm sure I'll learn a lot from watching them."
    il "I'm opening the trunk. Get your things."
    "My things? Uh..."
    
    "While Ilse grabs the Ghyson Vac-Pack and secures it onto their back, "
    "I look at the heaping pile of objects nearly spilling out of the open trunk."
    hide ilse neutral at right
    "Not only are all the ghost hunting gadgets dumped in this pile, "
    "but a good portion of it is made of snacks."
    
    "I have no doubt that the snacks were packed by Elodie."
    
    "Speaking of, Elodie finally slinks out of the car."
    show elodie neutral at left
    el "What am I supposed to bring again?"
    hide elodie neutral at left
    "Even as she asks, she doesn't look up from her phone screen."
    show ilse neutral at left
    il "Here. You can watch over the EMF meter this time."
    hide ilse neutral at left
    show elodie neutral at left
    el "Right. The enterprise media functions."
    hide elodie neutral at left
    "The what now?"
    show mc neutral at left
    mc "Do you mean the-"
    hide mc neutral at left
    show elodie happy at left 
    el "Sorry, sorry. I was watching a video. I meant the Ecto-Mode Finder!"
    hide elodie happy at left
    show mc neutral at left
    mc "Huh? I thought it was the electromag-"
    hide mc neutral at left
    show elodie neutral at right with easeinleft
    el "Eggs, muffins, frittata!"
    "Elodie rushes past me to the pile of everything and grabs her snacks, "
    "stuffing whatever fits into her pockets."
    "She must've had food on her mind."

    el "This job is cutting into my dinner time, you know?"

    el "Let's get in, clean the place, prove nothing spooky's up, and get out."
    hide elodie neutral at right
    show mc neutral at left

    mc "Huh? Is it likely for it to end up being nothing? The client seemed pretty scared of going back"
    "to the house."

    mc "It doesn't look like the usual haunted house, but there must be "
    "something paranormal going on if we were called in, right?"

    hide mc neutral at left 
    show ilse neutral at left
    
    il "It's possible. There are false alarms once in a while."
    
    il "But whether there is or isn't a ghost, we'll still at least check thoroughly like we were hired to."
    
    show ilse happy at left
    
    il "However, I do believe there's something. The signs the client reported are pretty convincing."
   
    show ilse neutral at right with easeoutright
    
    "As expected of the boss! Their confidence is a steady presence that bolsters my own courage."
    
    hide ilse at right
    
    "I quickly find my heavy-duty flashlight and video camera. Luckily, neither were damaged during the drive." 

    "With the video cam, I'll be able to record my first job for prosperity!"

    "And maybe if I'm lucky, I can get a glimpse of the ghost!"

    "In my excitement, I nearly miss that only three of our four member team are present."
    show mc neutral at left
    mc "Where's Vance?"

    "\"Shh, not so loud!\"" # vance

    "I look around."
    
    $ looking_for_vance_left = False
    $ looking_for_vance_right = False

    label looking_for_vance_section:
        menu:
            "Look left" if not looking_for_vance_left:
                $ looking_for_vance_left = True
                "I looked over to my left. Nothing."
                jump looking_for_vance_section
            "Look right" if not looking_for_vance_right:
                $ looking_for_vance_right = True
                "I looked over to my right. Nothing."
                jump looking_for_vance_section
        
    "I peer around the car but I can't see the source of the voice."

    "... Wait, it can't be... can it?"

    "I look in the one place I haven't yet: back inside the car."

    "There he is, the last member of our team."
    
    hide mc neutral at left
    show vance neutral at left
    # Enter Vance

    "Vance is stiff, still sitting in his seat."

    va "If Ilse forgets about me, I won't need to go in."
    
    hide vance neutral at left
    show mc neutral at left
   
    mc "What, why not? Isn't this exciting?"
   
    hide mc neutral at left
    show vance neutral at left
    
    va "More like the complete opposite! What's fun about sacrificing ourselves to"
    "the demons inside that house?!"
    
    show vance neutral at right with easeoutright
    
    # Enter Ilse
    show ilse neutral at left
    
    il "There you are, Vance. It's time to go."
    
    va "No. Please, don't make me go in there."

    il "It'll be over soon."

    va "Nooooo!"

    # Exit Ilse, Vance
    hide vance neutral
    hide ilse neutral
    
    "Well, that's everyone."
    
label ch03:
    show ilse neutral at left
    show ilse neutral at right with easeinright
    il "Everyone ready?"
    hide ilse neutral at right
    show vance scared at left
    show vance scared at right with easeinleft
    va "No! Can I leave? Three is more than enough people."
    show elodie smug at left 
    el "Calm down, Vance. It's just an old house."
    show vance scared at right 
    va "Just?! Say that again when you're six feet under!" with vpunch

    menu:
        "Yes, boss!":
            show ilse neutral at right with easeinleft
            il "Alright. Looks like we're at a consensus. Let's begin."

            "Ilse turns the handle. Unlocked."

            "Ooh, things are already spooky."
            show elodie neutral at left with ease
            
            
            "Elodie follows the boss, dragging Vance along forcefully. I close in behind the group, dutifully filming everything."
        "Maybe Vance has a point.":
            
            el "Aw, not you, too! C'mon, it'll be a quick in and out job."
            show lance neutral at left with ease
            hide elodie neutral
            hide lance neutral
            show ilse neutral at right 
            il "This is your chance to get more experience. It's not as scary as Vance makes it out to be."
            hide ilse neutral 
            show mc neutral at left 
            mc "That's true… I suppose I should be brave about it."

            "They're right. I can't psych myself out before I've even started."
            hide mc neutral 
            "Ilse opens the front door, and as the others start filing in, I take a deep calming breath."
    
    "The open doorway looms over me menacingly, like it's trying to scare me away and dare me to enter at the same time."
    "A scuffed old doormat lies in front of it."

    "{i}Wel{/i}, it reads. The rest has faded away."
    show mc neutral at left 
    "Well. Then I'll come in."

    menu:
        "Wipe my feet on the mat before entering.":
            pass
        "Enter without wiping my feet on the mat":
            pass

    "The moment I step past the threshold, I feel an immediate chill wash over me and shiver. The others don't seem"
    "to be affected in the same way."
    
    show lance neutral at middle 
    "Well, except for Vance, but he was already shivering in fright before entering the house."
    "But he isn't any more frightened than before. Is this what it means to be a professional?"
    hide lance neutral at middle 
    "The entranceway is connected to the living room. The place isn't empty; there's still some furniture left"
    "over from the previous tenant."

    "A visible layer of dust coats everything, so thick our footsteps could probably kick clumps of it into the air."
    show elodie neutral at right with easeinleft
    "Elodie waves her EMF meter in a wide arc over her head. "
    "It creates a lagging streak of green across the screen of the camera."
    show elodie happy at right 
    el "This room's clear!"
    hide elodie happy 
    "What? Bull!" 

    "That should only check Elodie's immediate vicinity, not the whole room. Unless...?"

    "It's possible that the company's tech R&D team upgraded the EMF to cover a wider area, isn't it? 
    "That amazing tech just hasn't reached my newly employed hands."

    show lance scared at left 
    va "T-The lights...They're not working!" with vpunch 

    va "Have the ghosts already short circuited the electricity? I thought the client said the appliances worked!"
    
    show ilse shocked at middle with ease 
    il "Actually, the client said the appliances didn't work."
    
    va "But they're supposed to!"

    show elodie neutral at right with ease
    el "No worries. They probably just stopped the electricity service while no one's living here."
    el "That's how you save on bills."

    show ilse neutral 
    il "It's fine. We all have flashlights for a reason. Are we all done with this room?"
    
    "Everyone nods."
    
    il "Alright, gang. Let's split up."

    mc "I thought the first rule of horror movies was to not split up."

    va "I agree! How about we don't?"
    
    el "But that'll take more time. Didn't you want to get out of here fast? I know I do."

    il "We're professionals. We know what we're doing."

    il "Then again, it is your first job. How about this?"

    il "According to the floorplan that was given to us, there are three other rooms downstairs." 
    il "We'll split up and cover one room each on the ground floor."

    il "After that, we'll all go upstairs and divvy up the area again." 
    il  "That way, we can stick close. Ish."

    # TODO: Update the dialogue where you are one-and-one with another character
    menu:
        il "Where do you want to go?"

        "Kitchen with Ilse":
            pass

        "Bathroom with Vance":
            pass

        "Dining Room with Elodie":
            pass

label ch04:
    "Eventually, ew gather back into the living room."  
    #jump credits  
