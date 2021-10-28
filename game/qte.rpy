"""
Code derived from: https://www.renpy.org/wiki/renpy/doc/cookbook/Timed_menus

This code handles quick-time events in the form of timed choices.
"""

transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide: 
        linear 0.5 alpha 0

screen countdown:
    timer 0.01 repeat True action If(time>0, true=SetVariable('time', time-0.01),false=[Hide('countdown'), Jump(timer_jump)])
    bar value time range timer_range_chase xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve


init: 
    $ timer_range_chase = 0 #length of time to chase in first part of qte
    $ timer_jump = 'timer_jump_default_label';
    $ timer_jump_warehouse = 'timer_jump_warehouse_default_label'
    $ timer_range_warehouse = 0; #length of time to chase in 2nd part of qte
    $ visited_right_return_to_start = False;
    $ visited_left_return_to_start = False;
    

##every decision is a label menu##

#active chase, qte fast"
label begin_chase_room:
    scene bg bedroom1 with dissolve 
    python:
        currently_playing = renpy.music.get_playing(channel=u'music')
        if currently_playing == None or currently_playing != audio.mazebgm:
            renpy.music.play(audio.mazebgm, u'music', loop=True, fadein=5.0)
        renpy.music.set_volume(0.3, delay=0, channel =u'music')
    if visited_right_return_to_start:
        scene bg bedroom1 with dissolve 
        "I somehow ended up outside the same room I started in."
    $ time = 5.0
    $ timer_range_chase = 5.0
    $ timer_jump = 'timerout'
    show screen countdown
    menu:
        "Do nothing":
            hide screen countdown
            "{i}If I stay still maybe it will leave me alone.{/i}"
            "I felt a chill down my shoulder blades."
            "{i}What was that?{/i}"
            mc "A-"
            jump death
        "Go left":
            hide screen countdown
            #sfx#
            play sound runningLight volume 1.0
            #sfx#
            scene bg hallway with dissolve 
            "I turned left and sped down the hall, shining my flashlight ahead for visibility."
            jump room_02
        "Go right" if not visited_right_return_to_start:
            hide screen countdown
            #sfx#
            play sound runningLight volume 1.0
            #sfx#
            scene bg hallway with dissolve
            "I swiftly made a right and ran down the dimly lit hallway."
            $ visited_right_return_to_start = True
            jump begin_chase_room
            
label room_02:
    hide screen countdown
    scene bg bedroom2 with dissolve 
    "I came upon another room."
    "After a quick glance around the room, I found no good hiding spots."
    #sfx#
    play sound runningLight
    #sfx#
    show ghost mad with dissolve:
        alpha 0.1
    "I heard a soft whisper from behind me and I bolted out of the room and decided to..."
    hide ghost mad 
    $ time = 5.0
    $ timer_range_chase = 5.0
    $ timer_jump = 'timerout'
    show screen countdown
    menu: 
        "Go left":
            hide screen countdown
            #sfx#
            play sound runningLight volume 1.0
            #sfx#
            scene bg hallway with dissolve 
            "I took another left and continued running forward."
            show ghost mad with dissolve:
                alpha 0.1
            "{i}I can hear the whispers right behind me. I need to get out of here befo-{/i}"
            jump death

        "Head straight":
            hide screen countdown
            #sfx#
            play sound runningLoud volume 1.0
            #sfx#
            scene bg hallway with dissolve
            "I dashed down the hallway."
            jump room_03
            
        "Go downstairs":
            hide screen countdown
            #sfx#
            play sound runningLight volume 1.0
            #sfx#
            scene bg hallway with dissolve 
            "I turned right and shine the lights down the hallway. I notice the staircase."
            "{i}This looks like it may leads to a way out.{\i}"
            jump warehouse

label room_03:
    hide screen countdown 
    "I see a room up ahead and did a quick peek into the room looking for any good hiding spots."
    "{i}Another room with no decent hiding spots, huh.{\i}"
    show ghost mad with dissolve:
        alpha 0.1
    "All of the sudden, my flashlight started flickering uncontrollably. I heard the familiar whispers creeping closer to me and I..."
    hide ghost mad 
    $ time = 5.0
    $ timer_range_chase = 5.0
    $ timer_jump = 'timerout'
    show screen countdown
    menu: 
        "Go left" if not visited_left_return_to_start:
            hide screen countdown
            #sfx#
            play sound runningLight volume 1.0
            #sfx#
            "I take a sharp left and continued sprinting down the hall."
            $ visited_left_return_to_start = True
            jump begin_chase_room
            
        "Go right":
            hide screen countdown
            #sfx#
            play sound runningLight volume 1.0
            #sfx#
            "I decided to go right."
            jump warehouse

#choices are lowercase bc mc is panicking, qte slower#
label warehouse:
    scene hallway with Dissolve(0.2)
    #pause .3
    scene black with Dissolve(0.2)
    #pause .25
    scene hallway with Dissolve(0.2)
    #pause .2
    scene black with Dissolve(0.2)
    #pause .2
    scene hallway with Dissolve(0.2)
    #pause .1
    scene black with Dissolve(0.2)

    "My flashlight flickered before completely turning off."
    "I couldn't do anything except run blindly straight ahead."
    #sfx#
    play sound runningLight
    #sfx#
    "After a few minutes of running in the dark, I ended up in a half-lit room."
label ghost_at_exit_mc_hiding:
    hide screen countdown
    scene bg diningRoom with Dissolve(1)
    "Looking around in the dimmed lights, I noticed a few broken furniture scattered throughout the room."
    "I snuck behind a fallen table closest to me and crouched down."
    "{i}What should I do now...{/i}"
    $ time = 7.0
    $ timer_range_chase = 7.0
    $ timer_jump= 'timerout'
    #music#
    python:
        renpy.music.set_volume(0.2, delay = 0, channel=u'music')
    #music#
    show screen countdown
    menu:
        "hide":
            hide screen countdown
            "I kept quiet and hid behind the table."
            jump ghost_explore_another_part_of_room
        "distract":
            hide screen countdown
            "{i}Maybe I can distract it with this glass bottle.{\i}"
            jump ghost_gets_close_mc_while_walking_to_distract
        "run":
            hide screen countdown
            "I peeked out from behind the table and noticed something resembling an exit at the other end of the room."
            "{i}Could that be the exit?{/i}"
            #sfx#
            play sound runningLoud volume 1.0
            #sfx#
            "I decided to risk it and dashed across the room."
            jump exit_wo_friends

label ghost_explore_another_part_of_room:
    hide screen countdown
    show ghost mad with dissolve: 
        alpha .1
    "I can hear the distant whispers and objects hitting the floor."
    hide ghost mad with dissolve 
    "{i}It must be over there...what should I do now?{/i}"
    $ time = 7.0
    $ timer_range_chase = 7.0
    $ timer_jump = 'timerout'
    show screen countdown
    menu:
        "hide":
            hide screen countdown
            "I chose to continue hiding behind the table."
            jump ghost_explore_very_close_to_mc
        "distract":
            hide screen countdown
            "I threw the glass bottle I found near my feet to the opposite corner of the room."
            jump ghost_investigates_distraction
        "run":
            hide screen countdown
            "I craned my neck around the leg of the table and noticed something looking like an exit on the other side of the room."
            "{i}If I can run fast enough and make it there, I can probably make it out.{/i}"
            "I made a mad dash for the exit."
            jump death
label ghost_gets_close_mc_while_walking_to_distract:
    hide screen countdown
    #sfx#
    play sound glassShatter volume 1.0
    #sfx#
    "The bottle hit the ground few feet away from me and made a huge shattering sound."
    "The shatter echoed through the room for a few seconds."
    "I ducked down behind a couch and thought about my choices. I..."
    $ time = 7.0
    $ timer_range_chase = 7.0
    $ timer_jump = 'timerout'
    show screen countdown
    menu:
        "hide":
            hide screen countdown
            "I clamped both of my hands over my mouth, inched closer to the couch and hid myself."
            show ghost mad with dissolve: 
                alpha 0.1 
            "I can hear faint whispering coming closer to me."
            hide ghost mad with dissolve 
            "I dug my fingers into my cheeks to prevent myself from making even a single breath."
            jump ghost_investigates_distraction
        "distract":
            show ghost mad at middle with dissolve:
                alpha .1 zoom 1.2
            "{i}It seems like it's working but...I feel like it is closer to me than ever before.{/i}"
            "{i}I can try throwing my flashligh-{/i}"
            "I felt an icy chill breathe on my neck and my vision blackened."
            scene black with dissolve 
            hide screen countdown
            jump death
        "run":
            hide screen countdown
            "I crawled to the other side of the couch and peeked out. Glancing around, I see a wide opened door close by."
            "{i}Could that be the exit? Should I risk it?{/i}"
            "I decided to risk it."
            "Sucking in a deep breath, I leaped out from behind the couch and ran straight for the exit."
            scene bg door with dissolve 
            #sfx#
            play sound runningLoud volume 1.0
            #sfx#
            "However in the middle of my dash, my foot snagged a loose floorboard and I fell right in front of the door."
            show ghost mad with dissolve:
                alpha 0.1
            "I could feel the whispers coming closer. I have to hurry. Ignoring the throbbing pain in my head, I quickly pushed myself up from the ground."
            hide ghost mad with dissolve 
            jump mc_gets_injured

label ghost_explore_very_close_to_mc:
    show ghost mad with dissolve:
        alpha 0.1 
    hide screen countdown
    "I held my breath, trying to make myself as small as possible. I could feel the ghost approaching. It's near by."
    hide ghost mad with dissolve 
    "{i}What should I do now?{/i}"
    $ time = 7.0
    $ timer_range_chase = 7.0
    $ timer_jump = 'timerout'
    show screen countdown
    menu: 
        "hide":
            hide screen countdown
            "{i}I figured I should play it safe and continued to hide behind the table.{/i}"
            "{i}As long as I stay quiet, it shouldn't be able to notice me.{/i}"
            "{i}My teammates will notice me missing and look for me so I should stay put here.{/i}"
            "I leaned toward the table and stayed quiet for a few minutes. But I felt that same chill run down my back."
            show ghost mad with dissolve:
                alpha 0.25
            "I leap away from the table but all I heard was the whispers ringing louder and louder in my ears before I blacked out."
            jump death
        "run":
            hide screen countdown
            "Cautiously, I peeked out from the side of the table and noticed a doorway at the end of the room."
            "{i}That might be the exit. If I can make it to that door, I can escape. I can do this.{/i}"
            #sfx#
            play sound runningLoud volume 1.0
            #sfx#
            "I braced myself, jumping from behind the table and raced for the door on the other side of the room."
            "{i}It's all or nothing now.{/i}"
            python: ##50/50 chance of survival
                chance_survival = (renpy.random.random()*99)+1
                if(chance_survival > 50):
                    renpy.jump('death')
                if(chance_survival <= 50):
                    renpy.jump('exit_warehouse')
                
label ghost_investigates_distraction:
    hide screen countdown
    "I heard the sound of glass crunching in the distance."
    "{i}It's not gonna stay distracted forever so I should..."
    $ time = 7.0
    $ timer_range_chase = 7.0
    $ timer_jump = 'timerout'
    show screen countdown
    menu:
        "hide":
            hide screen countdown
            "{i}It's better to play it safe. I don't know how long the distraction will last so I shouldn't do anything drastic.{/i}"
            "I continued to hide behind the couch and kept very still."
            jump ghost_explore_very_close_to_mc
        "run":
            hide screen countdown
            "{i}It's distracted now, I should make a break for it.{/i}"
            #sfx#
            play sound runningLoud volume 1.0
            #sfx#
            "I crept closer to the open doorway and then bolted for the door."
            jump exit_warehouse

label mc_gets_injured:
    #scene bg door with dissolve 
    #(prev choice already has this bg)
    "I rushed through the doorway and slammed the door shut behind me."
    scene bg outsideHouse with fade 
    #sfx#
    play sound doorSlam volume 1.0
    #sfx#
    "{i}I'm safe...{/i}"
    "I wiped the sweat off my forehead before wincing. The bump on my forehead throbbed painfully."
    "{i}Dang, must have got that from when I fell...tch{/i}"
    jump exit_injured

#endings#
label timerout:
    #music#
    python:
        renpy.music.stop(channel=u'music',fadeout=3.0)
    #music#
    hide screen countdown
    show ghost mad with dissolve:
        alpha 0.05
    "I barely had time to make a choice before I felt a sudden chill behind me."
    show mc scared at left 
    mc "N-no, I should have decided sooner..!"
    hide mc scared 
    jump death
label death:
    python:
        renpy.music.stop(channel=u'music')
        renpy.play(audio.buzzWrong, channel=u'sound')
    hide screen countdown
    show ghost mad at middle with dissolve:
        alpha .5 zoom 1.3
    "{b}You have been killed by the ghost.{/b}"
    hide ghost with dissolve 
    jump restart
label restart:
    python:
        renpy.music.stop(channel=u'music',fadeout=2.0)
    menu: 
        "Try again.":
            jump begin_chase_room
label exit_warehouse:
    #music#
    python:
        renpy.music.stop(channel=u'music',fadeout=2.0)
    #music#
    play music mainbgm fadein 5.0 fadeout 2.5
    scene bg door with fade 
    "I pushed past the doorway and closed the door behind me. Suddenly I felt so exhausted."
    #sfx#
    play sound doorSlamClick volume 1.0
    #sfx#
    "{i}It seems like I've made to the backyard.{/i}"
    "I backed away from the door behind me and slumped down onto the ground before calling my teammates through the walkie-talkie."
    scene bg outsideHouse with dissolve 
    show mc neutral at left 
    mc "Boss? I made it out."
    hide mc neutral with dissolve 
    va "{i}You’re alive! I thought for sure you were dead!{/i}"
    el "{i}What were you even running from?{/i}"
    il "{i}That’s good. What happened to the ghost?{/i}"
    show mc neutral at left 
    mc "It’s still inside. It left me alone after I got outside."
    hide mc neutral with dissolve 
    il "{i}Ah, I see it!{/i}"
    "I only hear static through the walkie-talkie as what I assume is the Ghyson Vac-Pack is turned on."
    "Oh, and Vance’s screaming. I also hear that in the background."
    "The team soon makes their way outside."
    show elodie neutral at left with moveinright
    show ilse neutral at middle with moveinright
    show vance neutral at right with moveinright
    show ilse neutral 
    il "Job well done, team."
    show elodie happy at left 
    show vance happy at right 
    hide elodie happy with dissolve 
    hide vance happy with dissolve 
    show ilse happy 
    il "And good job to you, as well, for making it out alive."
    show mc scared at left with dissolve 
    mc "Was that...something I should’ve been more worried about?"
    "Maybe I should reconsider this ghost hunting job..."
    hide mc scared 
    jump credits 
    #return

label exit_injured:
    #music#
    python:
        renpy.music.stop(channel=u'music',fadeout=2.0)
    #music#
    play music mainbgm fadein 5.0 fadeout 2.5
    scene bg outsideHouse with dissolve
    show vance neutral at left with moveinright
    show ilse neutral at middle with moveinright
    show elodie neutral at right with moveinright
    "The rest of the team return sooner than expected."
    hide ilse neutral 
    hide vance neutral 
    show mc scared at left with dissolve 
    mc "You’re back already?"
    el "It’s better we regroup and recuperate."
    hide elodie neutral 
    show vance scared at right with dissolve 
    va "You’re {i}hurt{/i}?!"
    show mc neutral 
    mc "Nothing that can’t be fixed with a little rest."
    mc "What about the ghost?"
    hide vance scared 
    show ilse neutral at right with dissolve 
    il "We can always come back. It’s not like the anyone will move in while the ghost is still here."
    mc "If you say so, boss."
    show ilse happy
    il "No need to be disappointed. That’s just the danger of this job."
    show mc happy at left 
    mc "I won’t let you down next time, boss."
    hide ilse neutral with dissolve 
    show mc neutral at left 
    mc "Surely, I can do better..." 
    hide mc neutral 
    jump credits 
    return
label exit_wo_friends:
    #music#
    python:
        renpy.music.stop(channel=u'music',fadeout=2.0)
    #music#
    play music mainbgm fadein 5.0 fadeout 2.5
    scene bg door with dissolve 
    "I made it through the doorway and slammed the door before running away as fast as I could."
    #sfx#
    play sound doorSlam volume 1.0
    #sfx#
    #show mc happy at left 
    scene bg outsideHouse with dissolve 
    "{i}Looks like haa.. Aa.. Haa.. I.. Haa.. Made it to the backyard.{/i}"
    hide mc scared at left 
    "After a few moments of catching my breath, I clicked the walkie-talkie button to call my teammates."
    show mc happy at left 
    mc "Hello? Hey I'm in the backyard, where is everyo-"
    hide mc happy 
    "I was cut off by a loud screech followed muffled screams and static."
    play sound radioStatic volume 1.0
    show mc scared at left 
    mc "H-hey where are you g-guys??" with vpunch 
    hide mc scared at left 
    "The static noise quickly muffled out any voices and screams before going silent."
    show mc scared at left 
    mc "...No..N-no.."
    hide mc scared 
    stop sound 
    jump credits 
    #return
