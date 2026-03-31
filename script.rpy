# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character ("Speed Dating Announcer")
define n = Character("Tall box")
define y = Character("[povname]")
define d = Character("Robo box")
define h = Character("Box head")

## POINTS
default long_con = 0

default robo_con = 0

default head_con = 0

default long_kill = 0
default robo_kill = 0
default head_kill= 0

default qo1 = 0
default qo2 = 0
default qo3 = 0
default qo4 = 0
default qw1 = 0
default qw2 = 0
default qw3 = 0
default qt1 = 0
default qt2 = 0
default qt3 = 0

default qo1_ = 0
default qo2_ = 0
default qo3_ = 0
default qw1_ = 0
default qw2_ = 0
default qw3_ = 0
default qt1_ = 0
default qt2_ = 0
default qt3_ = 0
# The game starts here.

label start:
    play music "(Loop) juanjo_sound - chimzle.WAV"
    scene bg speed

    $ povname = renpy.input("What is your name?", length=32)


    a "WELCOME everyone! I hope you're having a good evening and I hope your ready for some..."
    a "SPEED DATING..."

    menu:
        "Sounds fun":
            y "Dating is fun. Meeting new people is fun. Speed dating just makes sense!"
            jump Cont
        "Sounds sad ":
            y "What kind of sad life leads you here..."
            y "I may be the kind of loser that goes to speed dating, but i don't wanna meet the kind of losers who go to speed dating"
            y "Whatever, let's just do this"
            jump Cont


    label Cont:
        a "BEGIN DATING IN 3, 2, 1, GOOOO!"
    play sound "audio/new screech.mp3" volume 0.5
    show long top norm with moveinright
    n"..."

    y "{i}WHY IS THIS PERSON IN A BOX?{/i}"
    show long top norm right
    n "You go outside often?"
    show long top norm
    menu:
        "Yes":
            show long top norm side right
            n "Oh, cool, cool. I uhh, don't usually leave the house."
            show long top norm right right
            n "Very scary out here, with the sun and the people"
            show long top norm right
            n "One time a pigeon looked at me. I was terrified"
            show long top norm
            n "This is the most I've talked all night, my heart is racing"
            show long top norm shine
            n "MY HEART IS RACING!!!"
            jump Q1
        "No":
            show long top norm shine
            n "Really!? Me nither!"
            show long top norm side right
            n "I spend all day inside watching horror movies and drinking milkshakes, I make a bomb-ass milkshake"
            show long top norm
            n "I'm INCREDIBLY lactose intolerant but i just tank it"
            y "Real shit"
            jump Q1
        "Why are you in a box?":
            show long top norm left
            n "Feels more comfortable in the box, less people watching me"  
            y "Less people? Are you sure?"
            show long top norm right
            n "Oh definately! Cardboard is a very boring material?"
            show long top norm
            jump Q1

    label Q1:
        screen longone:


            textbutton "How long have you been crazy?" action If(qo1<1, Jump("now")):
                xalign 0.28
                yalign 0.70
            textbutton "What's your favourite dinosaur?" action If(qo2<1, Jump("god")):
                xalign 0.71
                yalign 0.70
            textbutton "What's your dream job?" action If(qo4<1, Jump("last")):
                xalign 0.71
                yalign 0.86
            button:
                align(0.27,0.86)

                vbox:
                    xysize(500,100)
                    textbutton "What qualities do you value" action If(qo3<1, Jump("here"))
                    textbutton "most in a relationship?" action If(qo3<1, Jump("here"))
                    #action Jump("here")
        show book menu1
        call screen longone

        $ renpy.pause ()   # will wait untill player click


        label now:
            hide screen longone
            hide book menu1
            $ long_con += 1
            $ qo1 += 1
            #y "How long have you been crazy?"
            show long top norm side left
            n "About a week"
            show long top norm up
            n "I just got a new lamp for my room and i thought: 'Why am i not a danger to myself and those around me?'"
            show long top norm
            n "Ha, I'm just joshing ya. I've been like this for a whiiiile!"
            while long_con < 2:
                jump Q1

            jump time

        label god:
            hide screen longone
            hide book menu1
            $ long_con += 1
            $ qo2 += 1
            #y "What's your favourite dinosaur?"
            show long top norm shine
            n "Definately Godzilla, that dude can ball"
            show long top norm side left
            n "I remember watching a Godzilla movie where they said all Godzillas are born preggers"
            show long top norm side right
            n "At first i was like 'What the hell' but the more i think about it the more I'm concerned I may be developing a weird...interest..."
            y "Have you considered thinking about it less?"
            show long top norm
            n "I'm looking into lobotomies"
            while long_con < 2:
                jump Q1

            jump time

        label here:
            hide screen longone
            hide book menu1
            $ long_con += 1
            $ qo3 += 1
            #y "What qualities do you value most in a relationship?"
            show long top norm
            n "I think I'm looking for support:"
            show long top norm side left
            n "I want to find someone who is emotionally intelligent; they understand when you need support but they're also willing to be vulnerable and accept support when they need it."
            show long top norm side right
            n  "We all need someone to lean on but that's a two way system"
            show long top norm
            n "'All give and no take' can be just as destructive as 'all take and no give'"
            while long_con < 2:
                jump Q1

            jump time

        label last:
            hide screen longone
            hide book menu1
            $ long_con += 1
            $ qo4 += 1
            #y "What's your dream job?"
            show long top norm down
            n "huh...I'm not super sure anymore..."
            show long top norm left left
            n "When i was a kid i wanted to be a painter. I never learned how to paint though... It never really occured to me that I had too"
            show long top norm down
            n "I was just a kid...I just kinda expected that if I loved it I could do it one day...Not the case..."
            show long top norm right right
            n "Nowadays I'd rather just be in bed... Just lie there until I'm gone..."
            while long_con < 2:
                jump Q1

            jump time

    label time:
        a "NEXT!!! "
        jump Cont2

    label Cont2:
        hide long top norm with moveoutleft
        play sound "audio/new screech.mp3" volume 0.5
        show robo norm wave left with moveinright
        d "WASSUP BABY"
        y "{i}MORE BOXES!?!?{/i}"
        show robo norm flex
        d "You got a whole lotta ass and I'm tryna take a shit!"
        play sound "audio/SCCU.mp3"
        y "huh?"
        show robo norm 

        d "Listen baby, I live by two words:"
        #d "セックスして、お金を稼ごう"
        show robo norm flex
        show japan behind top_text
        image top_text = ParameterizedText(xalign=0.2125, yalign=0.785)
        show top_text "{size=*1.33}{color=#cc0066}Robo box{/color}{/size}" onlayer overlay
        show japanese onlayer overlay
        pause
        play sound "audio/SCCCU.mp3"
        y "huh?"
        show robo norm wave right face left
        d "Don't speak no Japan-ish? It's alright baby, we all got flaws"
        jump Q2

        label Q2:
        show book menu1
        call screen japannn


        screen japannn:


            textbutton "What do you do for fun?" action If(qw1<1, Jump("roids")):
                xalign 0.275
                yalign 0.86
            textbutton "What's your guilty pleasure?" action If(qw2<1, Jump("guilt")):
                xalign 0.69
                yalign 0.70
            #textbutton "last" action If(qo3<1, Jump("last")):
                #xalign 0.71
                #yalign 0.86
            button:
                align(0.29,0.735)

                vbox:
                    xysize(500,100)
                    textbutton "What qualities do you value" action If(qw3<1, Jump("ass"))
                    textbutton "most in a relationship?" action If(qw3<1, Jump("ass"))
                    #action Jump("here")



        label roids:
            hide screen longone
            hide book menu1
            $ robo_con += 1
            $ qw1 += 1
            #y "What do you do for fun?"
            show robo norm flex right
            d "Steroids mostly"
            y "Oh, ok"
            while robo_con < 2:
                jump Q2
            
            jump Cont3

        label ass:
            hide screen longone
            hide book menu1
            $ robo_con += 1
            $ qw3 += 1
            #y "What qualities do you value most in a relationship?"
            show robo norm wave left
            d "Listen, I consider myself an ass samurai"
            show robo norm flex
            d "Everyday is my birthday and I'm here for the {b}CAKE{/b}"
            y "At least you know what you want?"
            show robo norm wave left face left
            d "Oh baby, BAAABY! it's not what i want, it's what i {b}neeed{/b}"
            show robo norm wave right face right
            d "I have the thirst of a thousand camels"
            y "Are camels particularly thirsty? ya know, with the hump and all..."
            show robo norm 
            d "FORGET ABOUT THE HUMP, I'm here for the {b}rump!{/b}"
            while robo_con < 2:
                jump Q2

            jump Cont3

        label guilt:
            hide screen longone
            hide book menu1
            $ robo_con += 1
            $ qw2 += 1
            #y "What's your guilty pleasure?"
            show robo norm
            d "Baby, the only thing I'm guilty of is liking you"
            show robo norm flex  left
            d "I don't do regrets! I don't feel guilt! When i make a mistake I admit it, I improve as a person and I move on!"
            show robo norm flex
            d "I live, I learn and I love; and I'm in the mood for some {i}looove{/i} baby"
            while robo_con < 2:
                jump Q2

            jump Cont3

        y "bad"





    label Cont3:
        a "NEXT!!! "
        hide robo norm with moveoutleft
        play sound "audio/new screech.mp3" volume 0.5
        show head norm with moveinright
        h "Beep beep"
        y "{i}LESS BOXES!!! This is good{/i}"
        show head norm wave right
        h "Hello, it is very nice to meet you. I am new to town and looking for fuuuun"
        show head norm left arm
        h "I am a very coolio person and I can operate a motorized vehicle {i}very fast{/i}"
        show head norm right arm
        h "I dislike pineapples on pizza and Adolf Hitler"
        show head norm  
        h "How cool are you {i}big dog?{/i}"
        menu:
            "I eat nails for breakfast (No milk)":
                show head norm tilt right
                h "..."
                h "I did not know people could do that..."
                y "It's just one of my many cool traits"
                show head norm tilt left
                h "Wow...You must be a specimen of extreme coolness"
                jump Q3
            "I play video games and Dnd":
                show head norm tilt right
                h "Oh no..."
                show head norm tilt left
                h "Daddy-O, I hope you're not playing League of Legends"
                menu:
                    "I promise I'm not evil!":
                        show head norm both arm
                        h "You're a cool cat, big dog"
                        jump Q3

                    "I'm kinda evil like that!":
                        show head norm
                        h "This is a deeply troubling outcome"
                        jump Q3
            "I'm not very cool":
                show head norm tilt right
                h "How unfortunate for you. Have you considered keeping it cool and hanging loose? Maybe chillaxing..."
                jump Q3



        label Q3:
        show book menu1
        call screen space


        screen space:


            textbutton "Do you have a hidden talents?" action If(qt1<1, Jump("hidden")):
                xalign 0.275
                yalign 0.86
            textbutton "Where did you move from?" action If(qt2<1, Jump("move")):
                xalign 0.69
                yalign 0.70
            textbutton "What's your favourite dinosaur?" action If(qt3<1, Jump("dino")):
                xalign 0.28
                yalign 0.70
            #button:
                #align(0.29,0.735)

                #vbox:
                    #xysize(500,100)
                    #textbutton "What qualities do you value" action Jump("ass")
                    #textbutton "most in a relationship?" action Jump("ass")
                    #action Jump("here")

    label hidden:
        hide screen longone
        hide book menu1
        $ head_con += 1
        $ qt1 += 1
        #y "Do you have a hidden talent?"
        show head norm up arm
        h "HIDDEN!? I-I am not hiding anything! I am just a cool person who visits abandoned barnyards -BUT THERE IS NOTHING THERE..."
        y "...You're hiding your face"
        show head norm both arm
        h "AH YES, MY COOL AND FASHIONABLE HEADWEAR! WHAT A WONDERFUL TOPIC OF CONVERSATION! LET US DISCUSS THAT! OR SOMETHING ELSE!"
        while head_con < 2:
            jump Q3

        jump Eliminate


    label dino:
        hide screen longone
        hide book menu1
        $ head_con += 1
        $ qt3 += 1
        #y "What's your favourite dinosaur?"
        show head norm tilt left
        h "Die-No-Saw? What is a die-no-saw?"
        y "A dinosaur!? You don't know what a dinosaur is!? Giant lizards, millions of years old..."
        show head norm tilt right
        h "..."
        h "Liz-Ard?"
        "You pull out your phone and show them pictures of dinosaurs"
        show head norm up arm
        h "...{i}Holy moly...that thing is...and they are millions of years old...we are all in danger...{/i}"
        y "No wait, that's not what I-"
        show head norm both arm
        h "DO THE AUTHORITIES KNOW ABOUT THIS!? WHO WILL PROTECT US!? HOW CAN YOU LIVE LIKE-"
        y "THEY ARE EXTINCT!" with vpunch
        show head norm
        h "...ahem, thankfully i maintained my {i}cool{/i}"
        while head_con < 2:
            jump Q3

        jump Eliminate

    label move:
        hide screen longone
        hide book menu1
        $ head_con += 1
        $ qt2 += 1
        #y "Where did you move from?"
        show head norm wave left
        h "My cool ass is from far away but what matters is the here and the now!"
        show head norm left arm
        h "When i arrived here, my first companion told me to 'Live fast and die hard'. He was a particularly cool specimen and thusly I belive he is to be trusted"
        show head norm both arm
        h "That is why I am here! {i}Speed{/i} Dating! So far this is enjoyable, I look forwards to getting hard and dying"
        #h "I always drempt of running away, somewhere far away where nobody knows me"
        while head_con < 2:
            jump Q3

        jump Eliminate

label Eliminate:
    a "NEXT!!!"
    hide head norm with moveoutleft
    a "{i}Phew!{/i} Speed dating sure goes fast!"
    a "Let's pick up the pace! Choose someone to eliminate and we'll start another round with your 2 favourites"
    #show long boxx at left with moveinright 
    #show robo boxx at center with moveinright 
    #show  head boxx at right with moveinright 
    hide long boxx at left
    hide robo boxx at center
    hide  head boxx at right
    call screen lim

    screen lim:
        

        imagebutton:
            xalign 0.5
            yalign 1.0
            idle "robo boxx"
            hover "robo boxxx"
            action Jump("killrobo")
        imagebutton:
            xalign 1.0
            yalign 1.0
            idle "head boxx"
            hover "head boxxx"
            action Jump("killhead")
        imagebutton:
            xalign 0
            yalign 1.0
            idle "long boxx"
            hover "long boxxx"
            action Jump("killlong")


label killrobo:
    $ robo_kill += 5
    show robo boxx at center
    pause 0.2
    hide robo boxx with moveoutbottom
    jump oops

label killlong:
    $ long_kill += 5
    show long boxx at left
    pause 0.2
    hide long boxx with moveoutbottom
    jump oops

label killhead:
    $ head_kill += 5
    show head boxx at right
    pause 0.2
    hide head boxx with moveoutbottom
    jump oops

label oops:
    a "BEGIN DATING IN 3, 2, 1, GOOOO!"
    while long_kill < 1:
        jump longconvo2   
    jump roboconvo2

label longconvo2:
    play sound "audio/new screech.mp3" volume 0.5
    show long top norm with moveinright
    n "Hi...again"
    show long top norm left left
    n "Thanks for not turning me into glue. I assume that's what they did to the other guy..."
    show long top norm left
    y "Glue? Like they do to horses?"
    show long top norm side right
    n "Yeah...It's just a guess but i've seen it happen before...sticky situation..."
    show long top norm
    n "Do you watch horror movies?"
    menu:
        "No, they scare me":

            show long top norm side left
            pause 0.5
            show long top norm side right
            pause 0.5
            show long top norm
            n "..."
            n "The scary movies scare you...I uhhh, I guess dude"
            show long top norm right right
            n "Isn't that the fun part, ya know, the {i}thrill{/i}"
            show long top right
            y "I guess it's not really a thrill for me, I just get scared, like 'I don't want to be here' scared, like 'don't turn off the lights yet' scared"
            show long top norm
            n "..."
            show long top side left
            n "That's kinda cute..."
            jump Q2_1
        "No, they're boring":
            show long top norm shine
            n "WHAT? How could you think that? Even the bad movies are funny, but boring..."
            y "Most of the time it's just unnessisary slow action to build tention to some fake out jump scare, plus all the repetative cliches!"
            show long top norm down
            n "Why did I bother leaving the house..."
            jump Q2_1
        "Yes, they're scary":
            show long top norm left
            n "{i}Yeees hehehe!{/i} It gives me such a rush, it's like a rollercoster in my bedroom"
            show long top norm right
            n "It's also so cool to just lock in on something so {i}intense. hehehe{/i}"
            jump Q2_1
        "Yes, they're funny":
            show long top norm up
            n "You gotta watch some of the classics! That's real shit-yourself scary {i}hehehe{/i}"
            jump Q2_1








    label Q2_1:
        show book menu1
        call screen life


        screen life:


            textbutton "Do you have a hidden talents?" action If(qt1_<1, Jump("cith")):
                xalign 0.275
                yalign 0.70
            #textbutton "" action If(qt2_<1, Jump("cry")):
                #xalign 0.28
                #yalign 0.70
            textbutton "What do you do for work?" action If(qt2_<1, Jump("employ")):
                xalign 0.28
                yalign 0.86
            button:
                align(0.73,0.735)

                vbox:
                    xysize(600,100)
                    textbutton "If you could have any superpower," action If(qt3_<1, Jump("cry"))
                    textbutton "what would it be?" action If(qt3_<1, Jump("cry"))
                    #action Jump("here")


    label cith:
        hide screen longone
        hide book menu1
        $ long_con += 1
        $ qt1_ += 1
        #y "Do you have a hidden talent?"
        show long top norm side right
        n "I've got like hella roaches in my room and I think that I'm learning to talk to them"
        y "Oh, right...roaches...what uhhh, what do you talk to them about?"
        show long top norm left left
        n "I guess I don't really talk to them as much as I control them. Basic stuff right now, summoning them and sending them around my room..."
        show long top norm  right right
        n "Soon I think they might be able to fetch things for me. It's alot of responsibility! I'm concerned the power may corrupt me..."
        y "I'm glad I'm learning this now and not later"
        while long_con < 4:
            jump Q2_1

        jump robocheck

    label employ:
        hide screen longone
        hide book menu1
        $ long_con += 1
        $ qt2_ += 1
        #y "What do you do for work?"
        show long top norm side left
        n "Not much, I've got a part time job as a cashier but I take as few hours as possible..."
        show long top norm
        n "Since I basically live off of instant noods and milkshakes I don't need alot of money"
        show long top norm right right
        n "And I buy most of it from the convenience store I work at so it gives me more time to hangout in my room"
        y "I'm becoming increasingly worried for you"
        show long top norm
        n "Please do not form an opinion of me"
        while long_con < 4:
            jump Q2_1

        jump robocheck


    label cry:
        hide screen longone
        hide book menu1
        $ long_con += 1
        $ qt3_ += 1
        #y "If you could have any superpower, what would it be?"
        show long top norm shine
        n "X-RAY VISION..."
        show long top norm side left
        pause 0.2
        show long top norm
        pause 0.2
        show long top norm side left
        y "...{i}haha{/i}...kinda sounds...ya know..."
        show long top norm side right
        n "I don't wanna talk about this anymore..."
        while long_con < 4:
            jump Q2_1
        jump robocheck

label robocheck:
    while robo_kill < 1:
        jump roboconvo2
    a "NEXT!!! "
    jump headconvo2

label roboconvo2:
    hide long top norm with moveoutleft
    play sound "audio/new screech.mp3" volume 0.5
    show robo norm flex left with moveinright
    d "I missed you baby! Dem bunz looking {i}TIGHT!!!{/i} You been doing squats?"
    menu:
        "...Yeah sure, I've been doing tons of squats":
            show robo norm flex
            d "{i}Without me?...{/i}"
        "I've been sitting here the whole time...":
            show robo norm flex
            d "Sitting there and looking pretty, baby I {i}looove{/i} how you do that!"
        "My eyes are up here buddy":
            show robo norm flex
            d "And what beutiful eyes they are...{i}rrrragh{/i}"
    d "Listen baby, If I could get out of these damn boxes I'd carry you right into the sunset!"
    show robo norm
    jump Poop



    label Poop:
        show book menu1
        call screen overn


        screen overn:


            textbutton "Are you stuck in those boxes?" action If(qw1_<1, Jump("stuck")):
                xalign 0.275
                yalign 0.70
            #textbutton "" action If(qt2_<1, Jump("cry")):
                #xalign 0.28
                #yalign 0.70
            textbutton "Do you have any hidden talents?" action If(qw2_<1, Jump("built")):
                xalign 0.28
                yalign 0.86
            button:
                align(0.73,0.735)

                vbox:
                    xysize(600,100)
                    textbutton "If you could have any superpower," action If(qw3_<1, Jump("lover"))
                    textbutton "what would it be?" action If(qw3_<1, Jump("lover"))
                    #action Jump("here")

label stuck:
    hide screen longone
    hide book menu1
    $ robo_con += 1
    $ qw1_ += 1
    show robo norm wave left face right
    d "...yeah. I was working out, getting my pump up for tonight, then I tripped and fell right into the horse glue factory"
    show robo norm wave left face left
    d "Next thing I know i'm trapped!"
    show robo norm flex
    d "I keep trying to get the boxes off by flexing my big juicy muscles, but I'm so stuck"
    show robo norm 
    d "It smells like horse in here..."
    while robo_con < 4:
        jump Poop
    jump headcheck

label built:
    hide screen longone
    hide book menu1
    $ robo_con += 1
    $ qw2_ += 1
    show robo norm flex
    d "The only thing hidden about me is these big juicy muscles!"
    show robo norm wave right face right
    d "Baby just wait for me, I'll show you these muscles as soon as i can!"
    while robo_con < 4:
        jump Poop
    jump headcheck

label lover:
    hide screen longone
    hide book menu1
    $ robo_con += 1
    $ qw3_ += 1
    show robo norm wave left face left
    d "The greatest superpower in the world is {i}love{/i}!"
    show robo norm wave left
    d "Without love we have nothing! What would life be worth?"
    show robo norm
    d "My juicy muscles, your juicy posterior, {b}It's love that makes these things worth it!{/b}"
    while robo_con < 4:
        jump Poop
    jump headcheck








label headcheck:
    while head_kill < 1:
        a "NEXT!!!"
        jump headconvo2
    jump Eliminate2



label headconvo2:

    hide long top norm with moveoutleft
    hide robo norm with moveoutleft
    play sound "audio/new screech.mp3" volume 0.5
    show head norm wave right with moveinright
    h "Beep beep! Hello again home-slice!"
    show head both arm
    h "This speed dating truly IS going {i}fast{/i}, though according to my calender the date hasn't changed..."
    show head norm
    h "Perhaps they are talking about the fruit 'dates'? hmmm"
    show head norm tilt right
    h "Tell me Daddy-O, why do you think we are born?"
    menu:
        "Biologically, to breed":
            show head norm both arm
            h "OH YEAH DADDY-O! BREEDING! The coolest of tasks! I love to engage in reproductive activities!"
        "There is no reason, we are insignificant":
            show head norm tilt right
            h "A speck on a speck on a speck, truely meaningless..."
        "There is no reason, we are free":
            show head norm tilt left
            h "Freedom is truly daunting. Whatever to do with all this potential..."
    show head norm
    h "Whether i like it or not I may spent the rest of my life considering this question"
    jump Q3_2

label Q3_2:

    show book menu1
    call screen ploww
#h "I always drempt of running away, somewhere far away where nobody knows me"
    screen ploww:


        textbutton "How are you finding the move?" action If(qw1_<2, Jump("movee")):
            xalign 0.275
            yalign 0.70
        textbutton "What is your dream date?" action If(qw3_<2, Jump("sand")):
            xalign 0.70
            yalign 0.70
        textbutton "Do you have any hidden talents?" action If(qw2_<2, Jump("glorbo")):
            xalign 0.28
            yalign 0.86
        #button:
            #align(0.73,0.735)

            #vbox:
                #xysize(600,100)
                #textbutton "If you could have any superpower," action If(qw3_<1, Jump("lover"))
                #textbutton "what would it be?" action If(qw3_<1, Jump("lover"))
                #action Jump("here")


label movee:
    hide screen longone
    hide book menu1
    $ head_con += 1
    $ qw1_ += 3
    show head norm tilt left
    h "I always drempt of running away, somewhere far away where nobody knows me"
    show head norm
    h "I thought I could be the person I have always fantasised of being. No one would know of my past failures and embarrassments, I would be free of them"
    show head norm tilt right
    h "But you cannot escape your own memories. All of your secrets are still where they have always been. Everything that kept me up at night still keeps me up. They live in my head"
    show head norm 
    h "You cannot escape your head. I must accept my actions and strive to be more than my worst moments. It is not a high bar to set but it is difficult to forget, and harder still to forgive"
    while head_con < 4:
        jump Q3_2
    jump Eliminate2

label glorbo:
    hide screen longone
    hide book menu1
    $ head_con += 1
    $ qw2_ += 3
    show head norm right arm
    h "Oh yeah Big Dog, I am a very good pilot!"
    y "Really? Like for planes?"
    show head norm left arm
    h "Yes, I am capable of piloting planes in addition to all manner of radical vehicles and babe magnets"
    show head norm
    h "As I mentioned previously I am fond of doing so at {i}very high{/i} speeds. Given the oportunity I may even do...{b}stunts!{/b}"
    while head_con < 4:
        jump Q3_2
    jump Eliminate2

label sand:
    hide screen longone
    hide book menu1
    $ head_con += 1
    $ qw3_ += 3
    show head norm
    h "I am fond of the idea of playing a song on the guitar for my significant other...at the super bowl..."
    show head norm up arm
    h "Before slam dunking on some playa haters and riding a sick whip into the horizon"
    show head norm left arm
    h "For a radicle daddy like myself this is very regular activity that i will be resuming after this event"

    while head_con < 4:
        jump Q3_2
    jump Eliminate2





label Eliminate2:
    a "NEXT!!!"
    hide head norm with moveoutleft
    hide robo norm with moveoutleft
    a "That was even faster than the first round!"
    a "I think the time has come! Instead of eliminating someone, this round you will pick your favorite date! May you date happily ever after!"
    #$ head_kill -= 1
    #"[head_kill][long_kill][robo_kill]"

    while 1 <= robo_kill:
        jump seee
    jump bogus

label bogus:
    while 1 <= long_kill:
        jump limon
    jump thunder

label thunder:
    while 1 <= head_kill:
        jump argh
    jump bogus
"bad"
#label seee:
    #"good"

label argh:
    call screen limlim
    screen limlim:
        

        imagebutton:
            xalign 0.75
            yalign 1.0
            idle "robo boxx"
            hover "robo boxxx"
            action Jump("killlong3")

        imagebutton:
            xalign 0.25
            yalign 1.0
            idle "long boxx"
            hover "long boxxx"
            action Jump("killrobo3")

label limon:
    call screen limo
    screen limo:
        

        imagebutton:
            xalign 0.75
            yalign 1.0
            idle "robo boxx"
            hover "robo boxxx"
            action Jump("killhead3")

        imagebutton:
            xalign 0.25
            yalign 1.0
            idle "head boxx"
            hover "head boxxx"
            action Jump("killrobo3")


label seee:
    call screen lima
    screen lima:
        

        imagebutton:
            xalign 0.75
            yalign 1.0
            idle "long boxx"
            hover "long boxxx"
            action Jump("killhead3")

        imagebutton:
            xalign 0.25
            yalign 1.0
            idle "head boxx"
            hover "head boxxx"
            action Jump("killlong3")


init:
    $ screen_head = Position(xpos=0.25, ypos=1.0)


label killrobo3:
    $ robo_kill += 5
    #show robo boxx at center
    #pause 0.2
    #hide robo boxx with moveoutbottom
    jump Fin

label killlong3:
    $ long_kill += 5
    #show long boxx at center
    #pause 0.2
    #hide long boxx with moveoutbottom
    jump Fin

label killhead3:
    $ head_kill += 5
    #show head boxx at center
    #pause 0.2
    #hide head boxx with moveoutbottom
    jump Fin




label Fin:
    #"[head_kill][long_kill][robo_kill]"


    while robo_kill <= 0:
        jump roboend
    jump bogus2

label bogus2:
    while long_kill <= 0:
        jump longend
    jump thunder2

label thunder2:
    while head_kill <=0:
        jump headend
    jump Fin

"bad"
label roboend:
    show robo boxx at center
    pause 1.5
    hide robo boxx with moveouttop
    show robo outer with moveinbottom
    pause
    d "YES BABY, YOU KNOW I LOVE YOU! I LOVE YOU WITH MORE POWER THAN 1000 SUNS! I LOVE YOU WITH THE POWER OF {b}BOTH{/b} OF MY BICEPS"
    "He immediately lifts you up with his big muscly arms and carries you into the sunset"
    jump end


label longend:
    show long outer at center
    show lox at center
    pause 1.5
    hide lox with moveouttop
    pause
    n "Yes! I'm not being turned into glue today! Celebratory milkshakes at my place?"
    "The girl in the box turned out to be a stunner! For your first real date you helped her clean her apartment. Gross but kind!"
    jump end


label headend:
    show head out at center
    show headtopp at center
    pause 
    hide headtopp with moveouttop
    h "Beep beep, thanks for choosing me hot-rod! Do not tell the government I exist!"
    "There was an alien among us all along!? They refuse to show you their ship because it's not what a cool person would do. You go hunting for dinosaurs instead!"
    jump end








    # This ends the game.
label end:
    return
