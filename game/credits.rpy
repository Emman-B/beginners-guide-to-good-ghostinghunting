image credits_overlay = './gui/nvl.png'
image credits_bg = './gui/Background.jpg'
label credits:
    python:
        # Only prevent input if the player hasn't seen credits
        if not persistent.seen_credits:
            persistent.seen_credits = True      # set this to true
            set_allowed_input(False)            # block input
    play music ('./music/Ghost_techies.wav')
    $ credits_speed = 15 #scrolling speed in seconds

    # Background setting ===
    scene credits_bg #replace this with a fancy background
    #with dissolve
    show credits_overlay
    # ===
    show theend:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(0.5)
    hide theend
    show cred at Move((0.5, 5.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credits_speed)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(0.5)
    hide thanks
    stop music fadeout 1.0
    show logo with dissolve
    with Pause(0.5)
    
    # YOU MUST INCLUDE THIS BEFORE LEAVING THIS LABEL
    $ set_allowed_input(True)


    jump ending

init python:
    credits = ('Lead Programmer', 'Emmanuel'), ('Narrative Writer', 'Kaizena'), ('Level Designer, Programmer', 'Kendra'), ('Artist', 'Linda'), ('Programmer, Sound Designer', 'XQ'), ('Special Thanks to the following:', ''), ('Dark Room Background, Bathroom Background', 'by Nekomakino Dev'), ('House Backgrounds', ' by _hope_ow'), ('Interior Room Background', ' by annako')
    credits_s = "{size=80}Credits\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=40}" + c[0] + "\n"
        credits_s += "{size=60}" + c[1] + "\n"
        c1=c[0]
    credits_s += "\n{size=40}Engine\n{size=60}Ren'py\n7.4.8.1895" #Don't forget to set this to your Ren'py version


    # Function for allowing/preventing input
    def set_allowed_input(allowed):
        store._game_menu_screen = u'save_screen' if allowed else None
        store._dismiss_pause = allowed
        store._skipping = allowed
        store._rollback = allowed
    
init:
#    image cred = Text(credits_s, font="myfont.ttf", text_align=0.5) #use this if you want to use special fonts
    image cred = Text(credits_s, text_align=0.5)
    image theend = Text("{size=80}Fin", text_align=0.5)
    image thanks = Text("{size=80}Thanks for Playing!", text_align=0.5)


label ending:
    # This is just in case the previous call to allow input was removed
    $ set_allowed_input(True)
    # hide everything shown in credits
    hide theend
    hide cred
    hide thanks
    hide logo
    
    "..."
    ".........." 
    "To be continued...{w}..?"
    
    
    return 