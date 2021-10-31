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
        "Somehow, I've ended up outside the same room I started in."
    $ time = 5.0
    $ timer_range_chase = 5.0
    $ timer_jump = 'timerout'
    show screen countdown
    menu:
        "Do nothing":
            hide screen countdown
            "If I stay still maybe it will leave me alone?"
            "I feel a chill roll down my shoulder blades."
            "{i}What was that?{/i}"
            mc "A-"
            jump death
        "Go left":
            hide screen countdown
            #sfx#
            play sound runningLight volume 1.0
            #sfx#
            scene bg hallway with dissolve 
            "I turn left and speed down the hall, shining my flashlight ahead for visibility."
            jump room_02
        "Go right" if not visited_right_return_to_start:
            hide screen countdown
            #sfx#
            play sound runningLight volume 1.0
            #sfx#
            scene bg hallway with dissolve
            "I swiftly make a right and run down the dimly lit hallway."
            $ visited_right_return_to_start = True
            jump begin_chase_room
            
label room_02:
    hide screen countdown
    scene bg bedroom2 with dissolve 
    "I come upon another room."
    "Glancing quickly around the room, I can't find any good hiding spots."
    #sfx#
    play sound runningLight
    #sfx#
    show ghost mad with dissolve:
        alpha 0.1
    "I hear a soft whisper come from behind me. I bolt out of the room and decide to..."
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
            "I take another left and continue running forward."
            show ghost mad with dissolve:
                alpha 0.1
            "I can hear the whispers right behind me. I need to get out of here befo-"
            jump death

        "Head straight":
            hide screen countdown
            #sfx#
            play sound runningLoud volume 1.0
            #sfx#
            scene bg hallway with dissolve
            "I dash down the hallway."
            jump room_03
            
        "Go downstairs":
            hide screen countdown
            #sfx#
            play sound runningLight volume 1.0
            #sfx#
            scene bg hallway with dissolve 
            "I turn right and shine my light down the hallway. In the corner of my eye, I catch sight of the staircase."
            "This could be it. I've got a feeling this is the path to my way out."
            jump warehouse

label room_03:
    hide screen countdown 
    "I see a room up ahead and quickly peek into the it, looking for hiding spots."
    "This room is a bust as well."
    show ghost mad with dissolve:
        alpha 0.1
    "All of a sudden, my flashlight starts flickering uncontrollably. That familiar ghostly whisper is creeping closer behind me, so I..."
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
            "I take a sharp left and continue sprinting down the hall."
            $ visited_left_return_to_start = True
            jump begin_chase_room
            
        "Go right":
            hide screen countdown
            #sfx#
            play sound runningLight volume 1.0
            #sfx#
            "I decide to go right."
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

    "My flashlight flickers slowly, dimmer than ever, before suddenly shutting off."
    "There's no more time to think. All I can do is blindly run straight ahead."
    #sfx#
    play sound runningLight
    #sfx#
    "After a couple minutes of running in the dark, I can see a faint light up ahead!"
    "I arrive in a half-lit room."
label ghost_at_exit_mc_hiding:
    hide screen countdown
    scene bg diningRoom with Dissolve(1)
    "Looking around in the dimmed lights, I notice a few pieces of furniture scattered throughout the room."
    "I crouch down behind a fallen table close by."
    "What should I do now...?"
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
            "I keep quiet and stay hidden behind the table."
            jump ghost_explore_another_part_of_room
        "distract":
            hide screen countdown
            "Maybe I can distract it by throwing this convenient glass bottle."
            jump ghost_gets_close_mc_while_walking_to_distract
        "run":
            hide screen countdown
            "Peeking out from behind the table, I notice something resembling an exit at the other end of the room."
            "Should I go for it? I'm stuck here otherwise. There's really no other choice."
            #sfx#
            play sound runningLoud volume 1.0
            #sfx#
            "I make a mad dash across the room."
            jump exit_wo_friends

label ghost_explore_another_part_of_room:
    hide screen countdown
    show ghost mad with dissolve: 
        alpha .1
    "Distantly, I can hear the ghost's odd noises. Thumping noises and crashing sounds follow it as objects hit the floor."
    hide ghost mad with dissolve 
    "The ghost... it's over there somewhere. What should I do?"
    $ time = 7.0
    $ timer_range_chase = 7.0
    $ timer_jump = 'timerout'
    show screen countdown
    menu:
        "hide":
            hide screen countdown
            "If I'm lucky, the ghost won't come this way. I continue hiding behind the table."
            jump ghost_explore_very_close_to_mc
        "distract":
            hide screen countdown
            "There's a stray glass bottle lying near my feet. I can distract it!"
            "Gripping the cold bottle neck tight, I throw it towards the opposite corner of the room with all my might."
            jump ghost_investigates_distraction
        "run":
            hide screen countdown
            "Craning my head around one of the table legs, I notice something looking like an exit on the other side of the room."
            "If I can run fast enough, I can probably make it out... I better be fast enough."
            "Taking a deep breath, I make a break for it."
            "I can make it! I'm so close to the exit, I can taste i-"
            jump death
label ghost_gets_close_mc_while_walking_to_distract:
    hide screen countdown
    #sfx#
    play sound glassShatter volume 1.0
    #sfx#
    "The bottle hits the ground a few feet away from me. The bottle shatters, the noise echoing throughout the room."
    "Crap. I thought my throwing arm was stronger than that."
    "Knowing I can't stay in the same spot, I duck behind a nearby couch and think about my available options. I..."
    $ time = 7.0
    $ timer_range_chase = 7.0
    $ timer_jump = 'timerout'
    show screen countdown
    menu:
        "hide":
            hide screen countdown
            "I clamp both my hands over my mouth and do my best to shrink down even smaller."
            show ghost mad with dissolve: 
                alpha 0.1 
            "The whispy noise I associate with the ghost moving approaches."
            hide ghost mad with dissolve 
            "I dig my nails into my cheeks, hoping to prevent any noise from escaping past my fingers."
            jump ghost_investigates_distraction
        "distract":
            show ghost mad at middle with dissolve:
                alpha .1 zoom 1.2
            "It... seems like it worked? But at the same time... Is it just me, or is the ghost even closer to me than before?"
            "I can always try making another distraction by throwing my flashli-"
            "All I feel is a chill fluttering on the back of my neck as my vision starts to blacken."
            scene black with dissolve 
            hide screen countdown
            jump death
        "run":
            hide screen countdown
            "I crawl to the far side of the couch and try to get a glimpse of the place. Glancing around, I see a door left wide open."
            "Surely, I can make it?"
            "I take off towards the door."
            scene bg door with dissolve 
            #sfx#
            play sound runningLoud volume 1.0
            #sfx#
            "However in my mad scramble, a loose floorboard catches my foot and I tumble to the ground right in front of the door."
            show ghost mad with dissolve:
                alpha 0.1
            "But I can't afford to lay about and whine; I can hear the ghost coming closer. Ignoring the throbbing pain in my head I got from tumble, I force myself to stand."
            hide ghost mad with dissolve 
            jump mc_gets_injured

label ghost_explore_very_close_to_mc:
    show ghost mad with dissolve:
        alpha 0.1 
    hide screen countdown
    "I hold my breath, trying to make myself as silent as possible. It's so close I can feel it moving."
    hide ghost mad with dissolve 
    "What now?"
    $ time = 7.0
    $ timer_range_chase = 7.0
    $ timer_jump = 'timerout'
    show screen countdown
    menu: 
        "hide":
            hide screen countdown
            "I play it safe and continue hiding behind the table."
            "As long as I stay quiet, it shouldn't be able to notice me... right?"
            "Sooner or later, my teammates will locate me if I stay put."
            "I relax against the table silently and wait. Only a few minutes pass when I feel a chill run down my back."
            show ghost mad with dissolve:
                alpha 0.25
            "It's found me! I leap away from the table, but it's too late."
            "All I hear is the ghost's ominous voice screeching at me louder and louder in my ears until I blacked out."
            jump death
        "run":
            hide screen countdown
            "Cautiously, I peek out from around the table and notice a doorway at the end of the room."
            "It's possible that could be the exit. If I can make it to that door, I can escape!"
            #sfx#
            play sound runningLoud volume 1.0
            #sfx#
            "I brace myself, jumping out from my hiding place and race for the door."
            "There's no going back now."
            python: ##50/50 chance of survival
                chance_survival = (renpy.random.random()*99)+1
                if(chance_survival > 50):
                    renpy.jump('death')
                if(chance_survival <= 50):
                    renpy.jump('exit_warehouse')
                
label ghost_investigates_distraction:
    hide screen countdown
    play sound glassShatter
    "I hear the sound of glass crunching in the distance."
    "It's not gonna stay distracted forever so I should..."
    $ time = 7.0
    $ timer_range_chase = 7.0
    $ timer_jump = 'timerout'
    show screen countdown
    menu:
        "hide":
            hide screen countdown
            "It's better to play it safe. I don't know how long the distraction will last so I shouldn't do anything drastic."
            "I continue hiding behind the couch and keep very still."
            jump ghost_explore_very_close_to_mc
        "run":
            hide screen countdown
            "It's distracted now. I should make a break for it."
            #sfx#
            play sound runningLoud volume 1.0
            #sfx#
            "I creep closer to the open doorway. When I see my chance, I bolt for the door."
            jump exit_warehouse

label mc_gets_injured:
    #scene bg door with dissolve 
    #(prev choice already has this bg)
    "Stumbling through the doorway, I slam the door shut behind me."
    scene bg outsideHouse with fade 
    #sfx#
    play sound doorSlam volume 1.0
    #sfx#
    "Finally, I'm safe..."
    "I wipe the sweat off my forehead and wince. There's a bump on my head where I hit my head when I fell."
    "Ow."
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
    "I spent too long making a decision, the ghost has already caught up to me!"
    show mc scared at left 
    mc "N-no, I should have decided sooner...!"
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
    "I push past the doorway and close the door behind me. I made it out!"
    "All at once, the adrenaline fades and all I feel is exhaustion."
    #sfx#
    play sound doorSlamClick volume 1.0
    #sfx#
    "When I finally look up, I see that I've made to the backyard."
    "I slump to the ground. Now that I have the time to rest, I pull out my walkie-talkie and call my teammates."
    scene bg outsideHouse with dissolve 
    show mc neutral at left 
    mc "Boss? I made it out."
    #music#
    python:
        renpy.music.stop(channel=u'music',fadeout=2.0)
    #music#
    play sound radioStatic volume 0.5
    stop sound
    hide mc neutral with dissolve 
    va "You’re alive! I thought for sure you were dead!"
    el "What were you even running from?"
    il "That’s good. What happened to the ghost?"
    show mc neutral at left 
    play music setupbgm
    mc "It’s still inside. It left me alone after I got outside."
    hide mc neutral with dissolve 
    il "Ah, I see it!"
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
    hide ilse happy
    jump credits 
    #return

label exit_injured:
    #music#
    python:
        renpy.music.stop(channel=u'music',fadeout=2.0)
    #music#
    play music mainbgm volume 0.9 fadein 5.0 fadeout 2.5
    scene bg outsideHouse with dissolve
    "I flinch when I touch the bump on my head again."
    show mc neutral at left 
    mc "The van. There must be an ice pack back at the van."
    "Slowly, I make my way around the house to the car. Slapping an ice pack against my head, I wait for the others to make it out."
    hide mc neutral at left
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
    #return
label exit_wo_friends:
    #music#
    python:
        renpy.music.stop(channel=u'music',fadeout=2.0)
    #music#
    play music mainbgm fadein 5.0 fadeout 2.5
    scene bg door with dissolve 
    "I make it through the doorway and slam the door shut behind me. I don't bother slowing down until I'm a good distance away from the exit."
    #sfx#
    play sound doorSlam volume 1.0
    #sfx#
    #show mc happy at left 
    scene bg outsideHouse with dissolve 
    "It takes me a few long moments to catch my breath, but when I finally look around, I see that I made it to the backyard."
    hide mc scared at left 
    "Now that I'm no longer running for my life, I have the time to pull out my walkie-talkie to contact my teammates."
    show mc happy at left 
    mc "Hello? I made it out to the backyard. Where is everyo-"
    hide mc happy 
    play sound radioStatic volume 1.0 fadeout 0.1
    "I'm cut off by a loud screech of static. The walkie-talkie drops to the ground when I let go, startled."
    "When the static noises finally fades, it's followed by muffled screaming."
    show mc scared at left 
    mc "H-Hey, what's going on? Are you all okay?" with vpunch 
    hide mc scared at left 
    "The screams are overtaken when the static noise starts once more."
    play sound buzzWrong
    "Then suddenly, it stops."
    show mc scared at left 
    mc "...No... N-no..."
    hide mc scared 
    stop sound 
    jump credits 
    #return
