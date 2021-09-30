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
    define mc = "elodie" #can change name

##every decision is a label menu##

label begin_chase_room:
    
    if visited_right_deadend:
        e "you arrived at where you've begin"
    $ time = 5.0
    $ timer_range_chase = 5.0
    $ timer_jump = 'death'
    show screen countdown
    menu:
        "{color=#f00}Do nothing{/color}":
            hide screen countdown
            e "you have been killed by the ghost"
            jump death
        "{color=#f00}Go left{/color}":
            hide screen countdown
            e "you turn left"
            jump room_02
        "{color=#f00}Go right{/color}":
            hide screen countdown
            e "you make a right turn"
            $ visited_right_deadend = True
            jump begin_chase_room
            
label room_02:
    hide screen countdown
    "Decision 2"
    $ time = 5.0
    $ timer_range_chase = 5.0
    $ timer_jump = 'death'
    show screen countdown
    menu: 
        "{color=#f00}Left{/color}":
            hide screen countdown
            e "you make a left turn"
            jump death

        "{color=#f00}Middle{/color}":
            hide screen countdown
            e "you go through the middle"
            jump room_03
            
        "{color=#f00}Right{/color}":
            hide screen countdown
            e "you make a right turn"
            jump warehouse

label room_03:
    hide screen countdown
    "Decision 3" 
    $ time = 5.0
    $ timer_range_chase = 5.0
    $ timer_jump = 'death'
    show screen countdown
    menu: 
        "{color=#f00}Left{/color}":
            hide screen countdown
            e "you make a left turn"
            $ visited_left_deadend = True
            jump begin_chase_room
            
        "{color=#f00}Right{/color}":
            hide screen countdown
            e "you make a right turn"
            jump warehouse


label warehouse:
    e "you ran to the warehouse"
    
label ghost_at_exit_mc_hiding:
    hide screen countdown
    "ghost_at_exit_mc_hiding"
    $ time = 7.0
    $ timer_range_chase = 7.0
    $ timer_jump= 'death'
    show screen countdown
    menu:
        "{color=#f00}hide{/color}":
            hide screen countdown
            jump ghost_explore_another_part_of_room
        "{color=#f00}distract{/color}":
            hide screen countdown
            jump ghost_gets_close_mc_while_walking_to_distract
        "{color=#f00}run{/color}":
            hide screen countdown
            jump exit_wo_friends

label ghost_explore_another_part_of_room:
    hide screen countdown
    "ghost_explore_another_part_of_room"
    $ time = 7.0
    $ timer_range_chase = 7.0
    $ timer_jump = 'death'
    show screen countdown
    menu:
        "{color=#f00}hide{/color}":
            hide screen countdown
            jump ghost_explore_very_close_to_mc
        "{color=#f00}distract{/color}":
            hide screen countdown
            jump ghost_investigates_distraction
        "{color=#f00}run{/color}":
            hide screen countdown
            jump death
label ghost_gets_close_mc_while_walking_to_distract:
    hide screen countdown
    "ghost_gets_close_mc_while_walking_to_distract"
    $ time = 7.0
    $ timer_range_chase = 7.0
    $ timer_jump = 'death'
    show screen countdown
    menu:
        "{color=#000}hide{/color}":
            hide screen countdown
            jump ghost_investigates_distraction
        "{color=#f00}distract{/color}":
            hide screen countdown
            jump death
        "{color=#f00}run{/color}":
            hide screen countdown
            jump mc_gets_injured

label ghost_explore_very_close_to_mc:
    hide screen countdown
    "ghost_explore_very_close_to_mc"
    $ time = 7.0
    $ timer_range_chase = 7.0
    $ timer_jump = 'death'
    show screen countdown
    menu: 
        "{color=#f00}hide{/color}":
            hide screen countdown
            jump death
        "{color=#f00}run{/color}":
            hide screen countdown
            python:
                chance_survival = (renpy.random.random()*99)+1
                if(chance_survival > 50):
                    renpy.jump('death')
                if(chance_survival <= 50):
                    renpy.jump('exit_warehouse')
                ##
label ghost_investigates_distraction:
    hide screen countdown
    "ghost_investigates_distraction"
    $ time = 7.0
    $ timer_range_chase = 7.0
    $ timer_jump = 'death'
    show screen countdown
    menu:
        "{color=#f00}hide{/color}":
            hide screen countdown
            jump ghost_explore_very_close_to_mc
        "{color=#f00}run{/color}":
            hide screen countdown
            jump exit_warehouse

label mc_gets_injured:
    "mc_gets_injured"
    # TODO: variable for being injured when exiting
    jump exit_warehouse

##endings
label death:
    e "you have died"
    jump restart
label restart:
    menu: 
        "{color=#f00}Try again.{/color}":
            jump begin_chase_room
label exit_warehouse:
    e "you have made it out alive"
    return
label exit_wo_friends:
    e "you made it out alive but your friends did not (poggers)"
    return


python: # TODO: delete this python section
    """
    label menu2_v2:
        $ time = 5.0
        $ timer_range = 5.0
        $ timer_jump = 'menu2_slow'
        show screen countdown
        menu:
            "choice 1 slow":
                hide screen countdown
                e "choice 1 slow"
                jump menu2_end
            "choice 2":
                hide screen countdown
                e "choice 2, slow"
                jump menu2_end
    label menu2_slow:
        e "you were really slow"
    label menu2_end:
        e "anyways"
        return
    """
