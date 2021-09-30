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
    bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve

init: 
    $ timer_range = 0
    $ timer_jump = 0
    define e = "elodie"

label menu2:
    $ time = 5.0
    $ timer_range = 5.0
    $ timer_jump = 'menu2_v2'
    show screen countdown
    menu:
        "Choice 1 fast":
            hide screen countdown
            e "you chose choice 1 fast"
            jump menu2_end
        "choice 2 fast":
            hide screen countdown
            e "you chose choice 2 fast"
            jump menu2_end
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
