label credits:
    play music ('./music/Ghost_techies.wav')
    $ credits_speed = 15 #scrolling speed in seconds
    scene black #replace this with a fancy background
    with dissolve
    show theend:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(2)
    hide theend
    show cred at Move((0.5, 5.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credits_speed)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(2)
    hide thanks
    stop music fadeout 1.0
    show logo with dissolve
    with Pause(2)
    
    return

init python:
    credits = ('Lead Programmer', 'Emmanuel'), ('Narrative Writer', 'Kaizena'), ('Level Designer, Programmer', 'Kendra'), ('Artist', 'Linda'), ('Programmer, Sound Designer', 'XQ'), ('Special Thanks', 'Backgrounds '), (' Dark Room, Bathroom', 'by Nekomakino Dev'), ('House Backgrounds', ' by _hope_ow'), ('Interior Room', ' by annako')
    credits_s = "{size=80}Credits\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=40}" + c[0] + "\n"
        credits_s += "{size=60}" + c[1] + "\n"
        c1=c[0]
    credits_s += "\n{size=40}Engine\n{size=60}Ren'py\n7.4.8.1895" #Don't forget to set this to your Ren'py version
    
init:
#    image cred = Text(credits_s, font="myfont.ttf", text_align=0.5) #use this if you want to use special fonts
    image cred = Text(credits_s, text_align=0.5)
    image theend = Text("{size=80}Fin", text_align=0.5)
    image thanks = Text("{size=80}Thanks for Playing!", text_align=0.5)


label ending:
    
    #"..."
    #".........." 
    #".:. To be continued." 
    
    
    return 