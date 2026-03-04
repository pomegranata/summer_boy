define teq = Character("Tequila", color="#d7cead")
define doc = Character("Doctor", color="#2596be")
define myst = Character("?????", color="#ffffff")


label start:
    define def_pos = Position(xalign=0.5, yalign=-0.2)

    "Friday. 3:43 PM. Clear."
    "Meeting with Dr. Kal'tsit..."
    "Check."
    "Strategy preparation for next week..."
    "Check."
    "Annihilation for this week..."
    "Check."
    "And last..."
    "Stationary Security Service..."
    "Check."

    scene bg corridor

    play music "farce.mp3"

    doc "Well, that wraps up this week."
    doc "Huh."
    doc "I finished up everything before my shift ends."
    doc "And now..."
    doc "What?"

    "....."

    doc "Uhhh, what should I do now?"
    doc "I have nothing to do for the rest of the day..."
    doc "I guess I can just wander around the ship for a bit..."
    doc "Maybe something interesting will happen?"
    doc "Or maybe I can just have a nice walk and enjoy the scenery?"
    doc "To the upper deck, maybe?"
    doc "The weather is nice up there..."
    doc "Or to the lower deck?"
    doc "Maybe I missed something down there?"
    doc "Or maybe to the cafetaria?"
    doc "But I'm not hungry yet..."

    "{i} Thud! {/i}"

    myst "Whoa, wha-"

    show teq surprise viewer at def_pos
    
    teq "Doctor! You startled me!"
    teq "I thought you were a ghost or something!"

    doc "Oh, I'm so sorry! I didn't mean to-"

    show teq normal at def_pos

    teq "Jeez, what's going on inside that briliant head of yours, huh?"
    teq "To the point of bumping me?"

    doc "It's nothing really..."
    
    teq "Liar."
    teq "Spill it out, Doctor."
    teq "What's going on inside that head of yours?"
    
    show teq happy at def_pos

    teq "You know your secret is safe with me, right?"

    show teq normal at def_pos

    teq "What? Did Amiya scold you again?"
    teq "Or did Dr. Kal'tsit give you a hard time again?"
    teq "Or a bad day?"

    doc "No, no, no."
    doc "It's not like that"
    doc "I did meet Amiya and Dr. Kal'tsit today."
    doc "But they didn't scold me or give me a hard time at all."
    doc "I was just busy wondering what should I do..."
    doc "I finished all of my work for the week already."
    doc "And I have nothing to do for the rest of the day..."

    show teq happy at def_pos
    
    teq "So, that's it, huh?"

    show teq normal at def_pos

    teq "I thought you ######"
    teq "How about this."
    teq "I'm going to the training compound to test out my newly polished sword"
    teq "Maybe I'll teach you one or two moves of swordmanship."
    teq "In case you need to defend yourself on the battlefield."

    doc "That sounds..."
    doc "Scary."
    doc "Really scary..."
    doc "But, don't get me wrong though!"
    doc "I haven't trained my physical combat skills for a long time."
    doc "I might be a little rusty..."

    show teq happy at def_pos

    teq "Worry not, Doctor!"
    teq "I'll go gentle on you."

    show teq smile at def_pos

    teq "Probably."
    teq "Maybe yes, I'll go gentle."
    teq "Or maybe not."

    show teq happy at def_pos

    teq "No promises though."

    show teq normal at def_pos

    "Tequila took my hand and pulled me alongside him."
    "Dragging me away to the training compound."
    
    teq "Anyway, let's get to it, Doctor!"

    doc "Wait, wait, wait!"
    doc "I just remembered something!"
    doc "I have to go back to my quarters and finish up some work!"
    doc "I can't just leave it there!"

    teq "Oh, you're such a bad liar, Doctor!"
    teq "Just loosen up a bit and have fun with me!"
    teq "I will ensure that you experience the greatest joy of your life!"

    doc "I-I'm not so sure about that..."
    doc "{i} Amiya, help me... {/i}"

    hide bg corridor
    hide teq normal

    "After walking along for a moment, Tequila comes in halt in front of Training Compund Room."
    "He turns his head around and looking at me dead in the eye."
    "Yet still with that sunny smile on his face."

    scene bg_trainingcom
    
    show teq smile at def_pos


    return
