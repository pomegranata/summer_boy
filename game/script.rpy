define teq = Character("Tequila", color="#d7cead")
define doc = Character("Doctor", color="#2596be")
define myst = Character("?????", color="#ffffff")


label start:
    define def_pos = Position(xalign=0.5, yalign=-0.2)

    "Friday. 3:43 PM. Clear."
    "Meeting with Dr. Kal'tsit and Amiya..."
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
    doc "Hmm..."

    "{i} Thud! {/i}"
    # thud sfx and screen shake

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
    doc "It's not like that..."
    doc "I did meet Amiya and Dr. Kal'tsit today."
    doc "But they didn't scold me or give me a hard time at all."
    doc "I was just busy wondering what should I do..."
    doc "I finished all of my work for the week already."
    doc "And I have nothing to do for the rest of the day..."

    show teq happy at def_pos
    
    teq "So, that's it, huh?"

    show teq normal at def_pos

    teq "I thought you were having another terrible day."

    show teq concern at def_pos

    teq "I don't want to see you having that sad face, Doctor..."
    
    show teq normal at def_pos

    teq "How about this."
    teq "I'm going to the training compound to test out my newly polished sword."
    
    show teq happy at def_pos

    teq "Maybe I'll teach you one or two moves of swordmanship."
    teq "In case you need to defend yourself on the battlefield."

    show teq normal at def_pos

    doc "That sounds..."
    doc "Scary."
    doc "Really scary."
    doc "But, don't get me wrong though!"
    doc "It's just, I haven't trained my physical combat skills for a long time."
    doc "I might be a little rusty..."
    doc "{i} Did I ever do some training at all? {/i}"

    show teq happy at def_pos

    teq "Worry not, Doctor!"
    teq "I'll go gentle on you."

    show teq normal at def_pos

    teq "Probably."
    teq "Maybe yes, I'll go gentle."
    teq "Or maybe not."

    show teq happy at def_pos

    teq "No promises though."

    show teq normal at def_pos

    teq "Anyway..."

    doc "!!!!!"

    "Tequila took my hand and pulled me alongside him."
    "Dragging me away from the landship corridor."

    scene bg black screen
    hide teq normal

    "Rushing our way out to the training compound."
    "Sucessfully pulling me out of my wandering thoughts."

    doc "Wait, wait, wait!"
    doc "I just remembered something!"
    doc "I have to go back to my office and finish up some work!"
    doc "I can't just leave it there!"

    show teq happy at def_pos

    teq "Oh, you're such a bad liar, Doctor!"
    teq "Just loosen up a bit and have fun with me!"
    teq "I will ensure that you experience the greatest joy of your life!"

    doc "I-I'm not so sure about that..."
    doc "{i} Amiya, help me... {/i}"

    hide teq normal
    ## play running sfx

    "After running along for a moment, Tequila comes in halt when we reached the Training Compund."
    "Not even the closed door could stop his radiant energy."
    "He opens the door and walks in without even knocking,"
    "As if he lives in this place."

    scene bg training
    
    show teq normal at def_pos

    "Then he stops abruptly so suddenly."
    "{i} Thud! {/i}"
    ## thud sfx. again

    doc "{i} That was twice for this afternoon already... {/i}"

    "He turns his head around and looking at me straight in the eye."
    "Yet still with that sunny smile on his face."

    teq "Here we are, Doctor!"

    show teq happy at def_pos

    teq "Get ready for the most exciting swordmanship duel of your life!"

    doc "W-wait a minute, Tequila..."
    doc "I need to take a deep breath first..."
    doc "{i} Inhale...{/i}"
    doc "{i} Exhale...{/i}"
    doc "{i} Inhale...{/i}"
    doc "{i} Exhale...{/i}"
    doc "{i} I can do this. I can do this...{/i}"
    doc "{i} It's just a friendly duel, right? It's not like he's going to actually hurt me or anything...{/i}"
    
    show teq normal at def_pos

    teq "Does running that short already take all of your breath away?"

    doc "It-it was so sudden."
    doc "Give me an early warning first next time, please."

    show teq happy at def_pos

    teq "Where's the fun if I told you first?"
    teq "Surprises are way more exciting, don't you think?"

    show teq normal at def_pos

    teq "So, still with me, Doc?"
    teq "Or have you already planned another escape route?"

    doc "No..."
    doc "I won't back down from a challenge now."
    doc "{i} As if I could outran him if he truly chase me... {/i}"
    doc "I'm ready to do this, Tequila."
    doc "Come on, bring it on!"

    show teq happy at def_pos

    teq "That's what I like to hear, Doctor!"
    teq "All right, let's get to it!"

    doc "{i} Huh? {/i}"
    doc "{i} Did his tail just wag? {/i}" 

    show teq normal at def_pos

    teq "Now, now, first thing first, Doctor..."
    teq "Let's get you all warmed up first, alright?"
    teq "Don't want you to put sudden strain on those delicate muscles, do we?"
    
    show teq happy at def_pos

    teq "Or Amiya will kill me."

    doc "That..."
    doc "Probably is the best idea..."

    show teq normal at def_pos

    teq "All right, let's start with some basic arm stretches, shall we?"

    hide teq normal

    "I just nods along and follows this energetic perro's lead."
    "Lifting my arms up and down."
    "Left and right."
    "Forward and backward."
    "Rotating my arms, shoulders, and even my neck a little bit."

    doc "{i} Whoa, this feels really good.{/i}"
    doc "{i} All these muscles tension just melts away.{/i}"
    doc "{i} It's been truly a while huh...{/i}"

    teq "It looks like you're enjoying yourself there, Doctor."

    doc "I am."
    doc "I can really feel all these tensions melting away."

    show teq happy at def_pos

    teq "Next, lets do some leg stretches too."
    teq "I know you spend most of your days sitting down in your office."
    teq "Writing down reports, planning strategies, and all of that paperwork stuff."
    
    show teq normal at def_pos

    doc "I'm ashamed to admit but that sums up my entire week..."
    doc "{i} Or maybe my entire life here since I woke up...{/i}"

    show teq happy at def_pos

    teq "See?"
    teq "I know I'm right!"

    show teq normal at def_pos
    
    teq "All right, let's do some leg stretches now."
    teq "Lift your leg up and hold it there for a few seconds."
    teq "Hold it there, Doctor. Don't let it drop down."
    teq "Just a bit more..."
    teq "And a bit more..."

    doc "{i} I'm losing my balance!{/i}"
    doc "{i} I can't hold it up anymore!{/i}"

    teq "A few seconds left."
    
    doc "{i} It's not a few seconds left. It's eternity! {/i}"

    show teq happy at def_pos

    teq "All right, you can drop your leg now."

    doc "{i} Phew, that was a close one... {/i}"

    teq "Now, the other leg too!"

    doc "{i} Oh no, not again...{/i}"

    teq "Lift it up and hold it."

    doc "{i} I can do it. I can do it. I can do it.{/i}"

    hide teq normal at def_pos

    "Slowly but surely, I managed to lift my foot slightly off the ground."
    
    doc "!!!!!"

    "Suddenly, my leg just gave away."
    "I stagger around, bouncing my standing leg left and right trying to keep my balance."
    
    doc "{i} Oh crap, I'm going to fall!{/i}"
    
    "No, no, no."
    "Uh, w-what did they taught me..."
    "Uhhh, relax my muscles.."
    "Bend my knees..."
    "And roll to the side-"

    myst "Careful there!"

    "As I prepare myself to land on the concrete surface of the Training Compund"
    "I feel something firm and solid on my back."
    "The lingering scent of fresh summer breeze and sea salt vaguely introducing themselves into my sense of smell."
    "A warm pair of strong arms securing my unsteady figure."

    "{i} Thud! {/i}"

    #sfx thud. again and again.

    doc "{i} That was three times already! {/i}"

    teq "Doctor!"
    teq "A-are you alright?"
    
    "Like a ghostly touch, a lukewarm puff of breath caresses my right cheek."
    "A pair of steady biceps around my torso."
    "There I lay..."
    "Securely wrapped around his arms."
    "Him, anchoring my upper body upright."
    
    doc "Umm..."
    doc "I-I'm alright..."
    doc "{i} What is this unusual feeling... {/i}"
    doc "{i} A creeping fervor trailing my cheeks...{/i}"
    
    "Cautiously, he lift my upper body up."
    "Slowly until my feet standing upright."
    "Yet still, he keep his one arm around my back."
    "Offering his own way of a nonvocal support"

    show teq concern at def_pos
    
    teq "You scared me there, Doctor!"

    doc "I'm so sorry for that."

    show teq serious at def_pos

    teq "No."
    teq "I'm the one who should apologise."

    doc "No, Tequila."
    doc "It was my fault."
    doc "I know I should have said no when I felt I couldn't do it."
    doc "Now, I almost injured myself..."
    doc "Because of my own ego..."

    show teq normal at def_pos
    
    teq "Still, Doctor..."
    teq "It was my idea to bring you all the way here."
    teq "That was also my idea to have you do all that warm-up."
    teq "I'm the one responsible for your injury."

    doc "Tequila, don't say that—"

    teq "Stop taking all the blame, Doctor."
    teq "I saw you apologizing for everything."
    teq "Even if it wasn't your fault."
    
    show teq happy at def_pos

    teq "You should be a little bit stricter to your operators, Doc."
    teq "Including me."

    show teq normal at def_pos

    teq "So, how about this..."
    teq "I'll treat you for a drink tonight."
    
    show teq happy at def_pos

    teq "Anything you want, however you want."
    teq "Specially, in my bar."
    teq "You call my name and I'll go to your table right away"
    teq "As long as you can handle the alcohol."

    doc "But tonight is Friday night."
    doc "Tonight will be busy night for a bar known for its exceptional quality like yours."

    teq "Hahaha, worry not, Doctor."
    teq "Rafaela and I have survived many busy weekend nights."
    teq "Nothing phase us anymore."
    teq "And having a special guest for once in a while is a novel experience."

    show teq normal at def_pos

    teq "So, how about it, Doctor?"
    teq "Free drink and special service."

    # branch out yes or no
    # if yes:

    doc "All right, I accept your offer."
    doc "But, in one condition..."

    show teq happy at def_pos

    teq "A rare demand from our cherised Doctor."
    
    show teq normal at def_pos

    teq "Shot the shoot, Doctor."
    teq "I'm all ears."

    doc "Tonight will be my off-duty."
    doc "So, please.."
    doc "Just call my name." # ask for the player's name, use input text

    teq "Easy enough."
    teq "I want you to do the same to me."

    doc "Calling you by your real name?"

    show teq happy at def_pos

    teq "Yup."
    teq "Ernesto Salas,"
    teq "Will be at your service tonight."

    # describe the smile

    teq "Take a rest, Doctor."
    teq "And see you tonight in my bar."
    teq "I'll be waiting for you, " # add player's name

    # if no:

    show teq surprised viewer at def_pos

    doc "I'm sorry, Tequila."
    doc "I don't think I have the time for a night out tonight..."
    doc "No hard feelings, alright?"

    show teq concern at def_pos

    teq "It's alright, Doctor..."
    teq "I should've known you're a busy person."
    teq "With busy schedules and such."
    teq "It's my my own stupidity and indifference."
    teq "Sorry for forcing you all the way here."
    teq "And asking you out without knowing your schedule."

    doc "... I'll bid my goodbye then."

    teq "Right..."
    teq "Hope you gave a pleasant weekend, Doc."

    return
