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
#screen countdownInWarehouse:
   # timer 0.01 repeat True action If(time>0, true=SetVariable('time', time-0.01),false=[Hide('countdown'), Jump(timer_jump_warehouse)])
   # bar value time range timer_range_chase xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve

init: 
    $ timer_range_chase = 0 #length of time to chase in first part of qte
    $ timer_jump = 'timer_jump_default_label';
    $ timer_jump_warehouse = 'timer_jump_warehouse_default_label'
    $ timer_range_warehouse = 0; #length of time to chase in 2nd part of qte
    $ visited_right_deadend = False;
    $ visited_left_deadend = False;
    

##every decision is a label menu##

#active chase, qte fast"
label begin_chase_room:
    python:
        currently_playing = renpy.music.get_playing(channel=u'music')
        if currently_playing == None or currently_playing != audio.mazebgm:
            renpy.music.play(audio.mazebgm, u'music', loop=True, fadein=5.0)
        renpy.music.set_volume(0.3, delay=0, channel =u'music')
    if visited_right_deadend:
        "I somehow ended up outside the same room I started in."
    $ time = 5.0
    $ timer_range_chase = 5.0
    $ timer_jump = 'timerout'
    show screen countdown
    menu:
        "{color=#eb142c}Do nothing{/color}":
            hide screen countdown
            "{i}If I stay still maybe it will leave me alone.{/i}"
            "I felt a chill down my shoulder blades."
            "{i}What was that?{/i}"
            mc "A-"
            jump death
        "{color=#c81126}Go left{/color}":
            hide screen countdown
            #sfx#
            play sound runningLight volume 1.0
            #sfx#
            "I turned left and sped down the hall, shining my flashlight ahead for visibility."
            jump room_02
        "{color=#c81126}Go right{/color}":
            hide screen countdown
            #sfx#
            play sound runningLight volume 1.0
            #sfx#
            "I swiftly made a right and ran down the dimly lit hallway."
            $ visited_right_deadend = True
            jump begin_chase_room
            
label room_02:
    hide screen countdown
    "I came upon another room."
    "After a quick glance around the room, I found no good hiding spots."
    #sfx#
    play sound runningLight
    #sfx#
    "I heard a soft whisper from behind me and I bolted out of the room and decided to..."
    $ time = 5.0
    $ timer_range_chase = 5.0
    $ timer_jump = 'timerout'
    show screen countdown
    menu: 
        "{color=#c81126}Go left{/color}":
            hide screen countdown
            #sfx#
            play sound runningLight volume 1.0
            #sfx#
            "I took another left and continued running forward."
            "{i}I can hear the whispers right behind me. I need to get out of here befo-{/i}"
            jump death

        "{color=#c81126}Head straight{/color}":
            hide screen countdown
            #sfx#
            play sound runningLoud volume 1.0
            #sfx#
            "I dashed down the hallway."
            jump room_03
            
        "{color=#c81126}Go down stair{/color}":
            hide screen countdown
            #sfx#
            play sound runningLight volume 1.0
            #sfx#
            "I turned right and shine the lights down the hallway. I notice the staircase."
            "{i}This looks like it may leads to a way out.{\i}"
            jump warehouse

label room_03:
    hide screen countdown
    "I see a room up ahead and did a quick peek into the room looking for any good hiding spots."
    "{i}Another room with no decent hiding spots, huh.{\i}"
    "All of the sudden, my flashlight started flickering uncontrollably. I heard the familiar whispers creeping closer to me and I..."
    $ time = 5.0
    $ timer_range_chase = 5.0
    $ timer_jump = 'timerout'
    show screen countdown
    menu: 
        "{color=#c81126}Go left{/color}":
            hide screen countdown
            #sfx#
            play sound runningLight volume 1.0
            #sfx#
            "I take a sharp left and continued sprinting down the hall."
            $ visited_left_deadend = True
            jump begin_chase_room
            
        "{color=#c81126}Go right{/color}":
            hide screen countdown
            #sfx#
            play sound runningLight volume 1.0
            #sfx#
            "I decided to go right."
            jump warehouse

#choices are lowercase bc mc is panicking, qte slower#
label warehouse:
    "My flashlight flickered before completely turning off."
    "I couldn't do anything except run blindly straight ahead."
    #sfx#
    play sound runningLight
    #sfx#
    "After a few minutes of running in the dark, I ended up in a half-lit room."
label ghost_at_exit_mc_hiding:
    hide screen countdown
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
        "{color=#c81126}hide{/color}":
            hide screen countdown
            "I kept quiet and hid behind the table."
            jump ghost_explore_another_part_of_room
        "{color=#c81126}distract{/color}":
            hide screen countdown
            "{i}Maybe I can distract it with this glass bottle.{\i}"
            jump ghost_gets_close_mc_while_walking_to_distract
        "{color=#c81126}run{/color}":
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
    "I can hear the distant whispers and objects hitting the floor."
    "{i}It must be over there...what should I do now?{/i}"
    $ time = 7.0
    $ timer_range_chase = 7.0
    $ timer_jump = 'timerout'
    show screen countdown
    menu:
        "{color=#c81126}hide{/color}":
            hide screen countdown
            "I chose to continue hiding behind the table."
            jump ghost_explore_very_close_to_mc
        "{color=#c81126}distract{/color}":
            hide screen countdown
            "I threw the glass bottle I found near my feet to the opposite corner of the room."
            jump ghost_investigates_distraction
        "{color=#c81126}run{/color}":
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
        "{color=#c81126}hide{/color}":
            hide screen countdown
            "I clamped both of my hands over my mouth, inched closer to the couch and hid myself."
            "I can hear faint whispering coming closer to me."
            "I dug my fingers into my cheeks to prevent myself from making even a single breath."
            jump ghost_investigates_distraction
        "{color=#c81126}distract{/color}":
            "{i}It seems like it's working but...I feel like it is closer to me than ever before.{/i}"
            "{i}I can try throwing my flashligh-{/i}"
            "I felt an icy chill breathe on my neck and my vision blackened."
            hide screen countdown
            jump death
        "{color=#c81126}run{/color}":
            hide screen countdown
            "I crawled to the other side of the couch and peeked out. Glancing around, I see a wide opened door close by."
            "{i}Could that be the exit? Should I risk it?{/i}"
            "I decided to risk it."
            "Sucking in a deep breath, I leaped out from behind the couch and ran straight for the exit."
            #sfx#
            play sound runningLoud volume 1.0
            #sfx#
            "However in the middle of my dash, my foot snagged a loose floorboard and I fell right in front of the door."
            "I could feel the whispers coming closer. I have to hurry. Ignoring the throbbing pain in my head, I quickly pushed myself up from the ground."
            jump mc_gets_injured

label ghost_explore_very_close_to_mc:
    hide screen countdown
    "I held my breath, trying to make myself as small as possible. I could feel the ghost approaching. It's near by."
    "{i}What should I do now?{/i}"
    $ time = 7.0
    $ timer_range_chase = 7.0
    $ timer_jump = 'timerout'
    show screen countdown
    menu: 
        "{color=#c81126}hide{/color}":
            hide screen countdown
            "{i}I figured I should play it safe and continued to hide behind the table.{/i}"
            "{i}As long as I stay quiet, it shouldn't be able to notice me.{/i}"
            "{i}My teammates will notice me missing and look for me so I should stay put here.{/i}"
            "I leaned toward the table and stayed quiet for a few minutes. But I felt that same chill run down my back."
            "I leap away from the table but all I heard was the whispers ringing louder and louder in my ears before I blacked out."
            jump death
        "{color=#c81126}run{/color}":
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
        "{color=#c81126}hide{/color}":
            hide screen countdown
            "{i}It's better to play it safe. I don't know how long the distraction will last so I shouldn't do anything drastic.{/i}"
            "I continued to hide behind the couch and kept very still."
            jump ghost_explore_very_close_to_mc
        "{color=#c81126}run{/color}":
            hide screen countdown
            "{i}It's distracted now, I should make a break for it.{/i}"
            #sfx#
            play sound runningLoud volume 1.0
            #sfx#
            "I crept closer to the open doorway and then bolted for the door."
            jump exit_warehouse

label mc_gets_injured:
    "I rushed through the doorway and slammed the door shut behind me."
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
    "I barely had time to make a choice before I felt a sudden chill behind me."
    mc "N-no, I should have decided sooner..!"
    jump death
label death:
    python:
        renpy.music.stop(channel=u'music',fadeout=2.0)
    hide screen countdown
    "{b}You have been killed by the ghost.{/b}"
    jump restart
label restart:
    python:
        renpy.music.stop(channel=u'music',fadeout=2.0)
    menu: 
        "{color=#c81126}Try again.{/color}":
            jump begin_chase_room
label exit_warehouse:
    #music#
    python:
        renpy.music.stop(channel=u'music',fadeout=2.0)
    #music#
    play music mainbgm fadein 5.0 fadeout 2.5
    "I pushed past the doorway and closed the door behind me. Suddenly I felt so exhausted."
    #sfx#
    play sound doorSlamClick volume 1.0
    #sfx#
    "{i}It seems like I've made to the backyard.{/i}"
    "I backed away from the door behind me and slumped down onto the ground before calling my teammates through the walkie-talkie."
    return
label exit_injured:
    #music#
    python:
        renpy.music.stop(channel=u'music',fadeout=2.0)
    #music#
    play music mainbgm fadein 5.0 fadeout 2.5
    mc "At least I got out alive..."
    "I touched the bump on my forehead again and blenched."
    mc "There's probably an icepack back at the truck."
    return
label exit_wo_friends:
    #music#
    python:
        renpy.music.stop(channel=u'music',fadeout=2.0)
    #music#
    play music mainbgm fadein 5.0 fadeout 2.5

    "I made it through the doorway and slammed the door before running away as fast as I could."
    #sfx#
    play sound doorSlam volume 1.0
    #sfx#
    "{i}Looks like haa.. Aa.. Haa.. I.. Haa.. Made it to the backyard.{/i}"
    "After a few moments of catching my breath, I clicked the walkie-talkie button to call my teammates."
    mc "Hello? Hey I'm in the backyard, where is everyo-"
    "I was cut off by a loud screech followed muffled screams and static."
    play sound radioStatic volume 1.0
    mc "H-hey where are you g-guys??"
    "The static noise quickly muffled out any voices and screams before going silent."
    mc "...No..N-no.."
    stop sound 
    return
