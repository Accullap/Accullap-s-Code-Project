from difflib import get_close_matches

def ask(question, options):
    while True:
        answer = input(question + " ").lower().strip()
        matches = get_close_matches(answer, options, n=1, cutoff=0.6)
        if matches:
            return matches[0]
        print("Sorry, I didn't understand. Please type one of: " + "/".join(options))

name = input("Type your name: ")
print("Welcome", name, "to this adventure!")
print("You wake up on a beach with no memory of how you got here.")
print("The sun is setting. You need to find shelter and figure out where you are.")
print("")

answer = ask("You see a jungle to the north, a cliff face to the east, an old shipwreck on the shore, and a dirt road heading west. Where do you go? (jungle/cliff/shipwreck/road):", ["jungle", "cliff", "shipwreck", "road"])

# path 1 jungle

if answer == "jungle":
    answer = ask("You enter the jungle. It is dense and dark. You hear animals in the distance. You find a fork in the path. Do you go left toward the sound of water or right toward a faint light? (left/right):", ["left", "right"])

    if answer == "left":
        answer = ask("You follow the sound and find a waterfall with a crystal clear pool. A woman is sitting beside it. She looks up and smiles. Do you approach her or hide and watch? (approach/hide):", ["approach", "hide"])

        if answer == "approach":
            answer = ask("She tells you her name is Mara. She has been stranded here for three years. She knows the island well. She offers to guide you. Do you trust her or go alone? (trust/alone):", ["trust", "alone"])

            if answer == "trust":
                answer = ask("Mara leads you through the jungle for hours. You reach the ruins of an old temple. She says there is treasure inside but also danger. Do you enter the temple or set up camp outside? (enter/camp):", ["enter", "camp"])

                if answer == "enter":
                    answer = ask("Inside the temple you find a long corridor with two doors. One is made of stone and one of wood. Which do you open? (stone/wood):", ["stone", "wood"])

                    if answer == "stone":
                        answer = ask("Behind the stone door is a giant chamber filled with gold coins and jewels. In the center is a glowing amulet. Do you take the amulet or leave it and just take the gold? (amulet/gold):", ["amulet", "gold"])

                        if answer == "amulet":
                            answer = ask("The moment you touch the amulet the room shakes. A trapdoor opens beneath you. You fall into a tunnel. You slide down and land in a cave near the beach. Do you go back to the temple or head to the beach? (temple/beach):", ["temple", "beach"])

                            if answer == "temple":
                                print("You find your way back to the temple but it has collapsed. Mara is gone. You are trapped on the island forever. You died!")

                            elif answer == "beach":
                                answer = ask("On the beach you see a rescue boat in the distance. Do you signal it with the glowing amulet or build a fire to signal it? (signal/fire):", ["signal", "fire"])

                                if answer == "signal":
                                    print("The amulet shoots a beam of light into the sky. The boat sees it and heads toward you. You are rescued and the amulet makes you famous worldwide. You win!")

                                elif answer == "fire":
                                    print("You build a fire but it takes too long. The boat passes. You are stranded. You died!")

                        elif answer == "gold":
                            answer = ask("You fill your pockets with gold. Mara warns you not to take too much. Do you listen to her or take as much as you can carry? (listen/take):", ["listen", "take"])

                            if answer == "listen":
                                print("You take a modest amount. The temple remains stable. You and Mara find a path to a fishing village on the other side of the island. You trade the gold for passage home. You win!")

                            elif answer == "take":
                                print("You overload yourself with gold. You are too heavy to run when the ceiling starts crumbling. You are buried alive. You died!")

                    elif answer == "wood":
                        answer = ask("Behind the wooden door is a small room with an old man sitting on the floor. He says he is the guardian of the temple. He offers you a choice: wisdom or wealth. Which do you choose? (wisdom/wealth):", ["wisdom", "wealth"])

                        if answer == "wisdom":
                            answer = ask("The old man touches your forehead. Suddenly you understand the island perfectly. You know every path and every danger. You lead Mara safely to a hidden harbor where a boat is anchored. Do you take the boat or look for the owner? (take/owner):", ["take", "owner"])

                            if answer == "take":
                                print("You sail home successfully. The wisdom stays with you forever and you become a great explorer. You win!")

                            elif answer == "owner":
                                answer = ask("You find the owner, an old fisherman named Tomas. He agrees to take you home in exchange for help repairing the boat. Do you help him or try to convince him with words? (help/convince):", ["help", "convince"])

                                if answer == "help":
                                    print("You spend two days repairing the boat together. Tomas becomes a lifelong friend and takes you home safely. You win!")

                                elif answer == "convince":
                                    print("Tomas does not trust words alone. He sends you away. You are stranded. You died!")

                        elif answer == "wealth":
                            print("The old man sighs and hands you a heavy bag of coins. As you leave the temple the bag gets heavier and heavier until you cannot move. You are rooted to the spot forever. You died!")

                elif answer == "camp":
                    answer = ask("You set up camp outside the temple. In the night you hear footsteps. Someone is approaching. Do you call out or stay quiet? (callout/quiet):", ["callout", "quiet"])

                    if answer == "callout":
                        print("A group of bandits hears you and raids your camp. They take everything and leave you tied to a tree. Days later you die of thirst. You died!")

                    elif answer == "quiet":
                        answer = ask("The footsteps pass. In the morning you find a map on the ground near where the footsteps were. It shows a path to a harbor. Do you follow the map or show it to Mara first? (follow/mara):", ["follow", "mara"])

                        if answer == "follow":
                            print("You follow the map and reach the harbor. A ship is docked there. You sneak aboard and hide until it reaches the mainland. You win!")

                        elif answer == "mara":
                            answer = ask("Mara studies the map and says she knows a shortcut. She leads you through a swamp. The swamp has quicksand. Do you stick to the path she chooses or trust your own instincts? (mara/instincts):", ["mara", "instincts"])

                            if answer == "mara":
                                print("Mara knows the safe route through the swamp. You reach the harbor together and both escape the island. You win!")

                            elif answer == "instincts":
                                print("You step off the safe path and sink into quicksand. You died!")

            elif answer == "alone":
                answer = ask("You leave Mara behind and continue through the jungle alone. You find an old rope bridge over a deep ravine. Do you cross it or look for another way? (cross/look):", ["cross", "look"])

                if answer == "cross":
                    answer = ask("Halfway across the bridge one of the planks breaks under your foot. You grab the ropes. Do you climb back or keep going forward? (back/forward):", ["back", "forward"])

                    if answer == "back":
                        print("You slowly climb back to safety. But as you step off the bridge it collapses entirely. You are now stuck on this side of the ravine. You find a cave and wait for rescue that never comes. You died!")

                    elif answer == "forward":
                        print("You push forward carefully and make it across. On the other side is a road leading to a small town. You find help and eventually get home. You win!")

                elif answer == "look":
                    answer = ask("You follow the ravine for a while and find a narrow point where you could jump across. It is risky but possible. Do you jump or keep looking for a safer crossing? (jump/keep):", ["jump", "keep"])

                    if answer == "jump":
                        answer = ask("You make the jump! You land hard but safe. Ahead is a clearing with a small village. Do you enter the village or observe it from the trees first? (enter/observe):", ["enter", "observe"])

                        if answer == "enter":
                            print("The villagers welcome you warmly. They feed you and help you find a boat. You sail home safely. You win!")

                        elif answer == "observe":
                            print("While hiding in the trees you get bitten by a venomous spider. The venom acts fast. You died!")

                    elif answer == "keep":
                        print("You walk for hours along the ravine but it never narrows again. Darkness falls. You get lost. You died!")

        elif answer == "hide":
            answer = ask("You hide behind a bush and watch Mara. She appears to be writing in a journal. After a while she leaves. She dropped her journal by the pool. Do you read it or leave it? (read/leave):", ["read", "leave"])

            if answer == "read":
                answer = ask("The journal describes a hidden path out of the jungle and a boat hidden in a sea cave on the north coast. Do you follow the journal's instructions or head back to the beach? (follow/beach):", ["follow", "beach"])

                if answer == "follow":
                    answer = ask("You find the sea cave. Inside is a small motorboat with fuel. Do you take the boat immediately or wait until morning? (now/morning):", ["now", "morning"])

                    if answer == "now":
                        print("You navigate out of the cave in the dark and hit rocks. The boat sinks. You died!")

                    elif answer == "morning":
                        print("You sleep in the cave and leave at dawn. You navigate safely to the mainland. You win!")

                elif answer == "beach":
                    print("You head back to the beach but get lost along the way. You wander the jungle for days. You died!")

            elif answer == "leave":
                print("You leave the journal and wander deeper into the jungle. You walk in circles for days and eventually collapse. You died!")

    elif answer == "right":
        answer = ask("You follow the light and find a campfire. Three strangers are sitting around it. They invite you to join them. Do you join them or keep your distance? (join/distance):", ["join", "distance"])

        if answer == "join":
            answer = ask("The strangers are friendly. They say they have a boat but it needs a spare part from the shipwreck on the beach. They ask you to get it. Do you agree or refuse? (agree/refuse):", ["agree", "refuse"])

            if answer == "agree":
                answer = ask("You head back to the beach and find the shipwreck. Inside you find the part they need but also a chest. Do you take only the part or open the chest too? (part/chest):", ["part", "chest"])

                if answer == "part":
                    print("You bring the part back to the strangers. They fix the boat and take you home as promised. You win!")

                elif answer == "chest":
                    answer = ask("The chest is locked. You find a rusty crowbar nearby. Do you force it open or bring it to the strangers first? (force/bring):", ["force", "bring"])

                    if answer == "force":
                        answer = ask("Inside the chest is a compass and old map of the island. The map shows a treasure location. Do you share it with the strangers or keep it to yourself? (share/keep):", ["share", "keep"])

                        if answer == "share":
                            print("The strangers are excited. Together you find the treasure, share it equally, and they take you home. You win!")

                        elif answer == "keep":
                            print("You hide the map. The strangers notice you acting suspicious and leave without you. You are stranded. You died!")

                    elif answer == "bring":
                        print("The strangers recognise the chest as belonging to a dangerous pirate. They panic and abandon their camp. You are left alone. You died!")

            elif answer == "refuse":
                print("The strangers shrug and leave without you. Without their boat you are stranded. Days later you collapse on the beach. You died!")

        elif answer == "distance":
            answer = ask("You watch them from the trees. You notice one of them is looking at a map. When they fall asleep you could steal the map. Do you steal it or approach them honestly in the morning? (steal/honest):", ["steal", "honest"])

            if answer == "steal":
                answer = ask("You steal the map. It shows the way to a harbor on the south coast. Do you head to the harbor immediately or wait for daylight? (immediately/wait):", ["immediately", "wait"])

                if answer == "immediately":
                    print("You get lost in the dark jungle. You died!")

                elif answer == "wait":
                    print("At dawn you follow the map to the harbor. A ferry is departing. You board it just in time and make it home. You win!")

            elif answer == "honest":
                answer = ask("In the morning you approach the strangers. They are suspicious but hear you out. Their leader asks you to prove your worth by finding food for the group. Do you go hunting or look for fruit? (hunt/fruit):", ["hunt", "fruit"])

                if answer == "hunt":
                    print("You catch a wild boar. The strangers are impressed and invite you onto their boat. You sail home together. You win!")

                elif answer == "fruit":
                    print("You return with fruit. The strangers eat and feel better. They agree to take you with them but the boat engine fails. You are all stranded. You died!")

# path 2 cliff

elif answer == "cliff":
    answer = ask("You reach the base of a tall cliff. There is a rope hanging down the face and also a narrow path winding upward. Do you climb the rope or take the path? (rope/path):", ["rope", "path"])

    if answer == "rope":
        answer = ask("You grab the rope and start climbing. Halfway up you hear the rope starting to fray. Do you climb faster or tie yourself to the cliff wall using your belt? (faster/tie):", ["faster", "tie"])

        if answer == "faster":
            answer = ask("You scramble upward and reach the top just as the rope snaps. At the top you find a lighthouse. The light is on but the door is locked. Do you break the door down or look for another way in? (break/search):", ["break", "search"])

            if answer == "break":
                print("You break the door down. Inside is an automated lighthouse with a radio. You call for help and a coastguard helicopter arrives the next morning. You win!")

            elif answer == "search":
                answer = ask("You find a window around the back that is slightly open. You climb in. Inside you find the radio and also a logbook. Do you call for help immediately or read the logbook first? (call/read):", ["call", "read"])

                if answer == "call":
                    print("You call for help. A rescue team arrives within hours. You win!")

                elif answer == "read":
                    answer = ask("The logbook describes a secret cave below the cliff that contains supplies left by a previous castaway. Do you go look for the cave or call for help first? (cave/call):", ["cave", "call"])

                    if answer == "cave":
                        print("You find the cave and the supplies including a flare gun. You fire it into the sky and a passing ship sees it. You are rescued. You win!")

                    elif answer == "call":
                        print("You call for help on the radio. A coastguard boat arrives the next day. You win!")

        elif answer == "tie":
            print("You tie yourself securely but the rope snaps anyway. You are left dangling by your belt. Your belt slowly tears. You fall into the ocean below. You died!")

    elif answer == "path":
        answer = ask("You take the winding path upward. It takes two hours but you reach the top safely. You find a lighthouse and a small cottage next to it. Do you go to the lighthouse or the cottage? (lighthouse/cottage):", ["lighthouse", "cottage"])

        if answer == "lighthouse":
            answer = ask("The lighthouse door is unlocked. Inside is a radio and a map of the island. The map shows a harbor. Do you call for help on the radio or head to the harbor on the map? (radio/harbor):", ["radio", "harbor"])

            if answer == "radio":
                print("You call for help. A coastguard team arrives within hours and takes you home safely. You win!")

            elif answer == "harbor":
                answer = ask("You follow the map and reach the harbor. A fishing boat is docked there. The fisherman is fixing his nets. Do you ask him for help or sneak onto the boat? (ask/sneak):", ["ask", "sneak"])

                if answer == "ask":
                    print("The fisherman is happy to help. He has heard reports of a stranded person on the island. He takes you home and you are reunited with your family. You win!")

                elif answer == "sneak":
                    print("The fisherman catches you hiding on his boat. He is furious and kicks you off. The boat leaves without you. You died!")

        elif answer == "cottage":
            answer = ask("You knock on the cottage door. An old keeper opens it. He is surprised to see you. He invites you in for tea. Do you accept or ask him immediately for help leaving the island? (accept/help):", ["accept", "help"])

            if answer == "accept":
                answer = ask("Over tea the keeper tells you he has a shortwave radio but it is broken. He needs a component from his storage shed. Do you help him fix it or ask about another way off the island? (fix/other):", ["fix", "other"])

                if answer == "fix":
                    answer = ask("You find the component in the shed. While searching you also find an old motorcycle. Do you fix the radio or take the motorcycle to find the harbor? (radio/motorcycle):", ["radio", "motorcycle"])

                    if answer == "radio":
                        print("You fix the radio together. The keeper contacts the coastguard and you are rescued by evening. You win!")

                    elif answer == "motorcycle":
                        answer = ask("The motorcycle starts after some effort. You ride it down a mountain road. Do you go fast or take it slowly? (fast/slow):", ["fast", "slow"])

                        if answer == "fast":
                            print("You lose control on a bend and fly off the cliff. You died!")

                        elif answer == "slow":
                            print("You take it slow and reach the harbor safely. You flag down a passing boat and make it home. You win!")

                elif answer == "other":
                    print("The keeper says the radio is the only way. Without your help he cannot fix it. He cannot help you further. You wander the island alone and eventually collapse. You died!")

            elif answer == "help":
                print("The keeper is offended by your rudeness. He slams the door. You are left outside alone. You died!")

# path 3 shipwreck

elif answer == "shipwreck":
    answer = ask("You climb into the shipwreck. It is old and creaking. You find a staircase leading below deck and a ladder leading to the upper deck. Where do you go? (below/upper):", ["below", "upper"])

    if answer == "below":
        answer = ask("Below deck it is dark and wet. You find three rooms. A storage room, a captain's cabin, and an engine room. Where do you go? (storage/cabin/engine):", ["storage", "cabin", "engine"])

        if answer == "storage":
            answer = ask("The storage room contains canned food, rope, a flare gun, and a waterproof bag. Do you take the flare gun or the food? (flare/food):", ["flare", "food"])

            if answer == "flare":
                answer = ask("You take the flare gun and head back to the beach. A ship is faintly visible on the horizon. Do you fire the flare now or wait until the ship is closer? (now/wait):", ["now", "wait"])

                if answer == "now":
                    print("The flare goes up too early. The ship does not see it. The flare gun is now empty. You are stranded. You died!")

                elif answer == "wait":
                    print("You wait patiently. When the ship is close enough you fire. They see it and come to rescue you. You win!")

            elif answer == "food":
                answer = ask("You eat and feel stronger. Now you can think clearly. Do you explore more of the ship or head back to the beach to build a shelter? (explore/shelter):", ["explore", "shelter"])

                if answer == "explore":
                    answer = ask("You find the captain's cabin and inside it a logbook and a working emergency beacon. Do you activate the beacon or read the logbook first? (activate/read):", ["activate", "read"])

                    if answer == "activate":
                        print("The beacon sends a signal. A rescue plane arrives the next morning. You win!")

                    elif answer == "read":
                        print("The logbook describes rocks beneath the ship that make it unstable. As you read the ship shifts and begins to sink. You panic and cannot get out in time. You died!")

                elif answer == "shelter":
                    print("You build a shelter on the beach. Days pass. No one comes. Your food runs out. You died!")

        elif answer == "cabin":
            answer = ask("The captain's cabin has a desk with charts and a locked safe. Do you study the charts or try to open the safe? (charts/safe):", ["charts", "safe"])

            if answer == "charts":
                answer = ask("The charts show you are on a small island about 40 miles from the mainland. There is a marked shipping lane nearby. Do you head to the beach to signal ships or look for a working radio? (beach/radio):", ["beach", "radio"])

                if answer == "beach":
                    answer = ask("On the beach you build a large SOS sign out of rocks. A drone flies overhead that evening. Do you wave at it or stay still? (wave/still):", ["wave", "still"])

                    if answer == "wave":
                        print("The drone spots you and transmits your location. A rescue team arrives the next morning. You win!")

                    elif answer == "still":
                        print("The drone scans the area and sees only the SOS sign. It logs the location. A team arrives eventually but too late. You died!")

                elif answer == "radio":
                    answer = ask("You find a radio in the engine room but it needs power. The ship's generator might still work. Do you try to start it or look for batteries? (generator/batteries):", ["generator", "batteries"])

                    if answer == "generator":
                        answer = ask("The generator sputters to life! The radio powers on. Do you broadcast on all channels or on the emergency channel only? (all/emergency):", ["all", "emergency"])

                        if answer == "all":
                            print("A nearby vessel hears you on a general channel and alters course to find you. You are rescued. You win!")

                        elif answer == "emergency":
                            print("The coastguard hears your emergency broadcast and dispatches a helicopter. You are airlifted to safety. You win!")

                    elif answer == "batteries":
                        print("You cannot find any working batteries. The radio stays dead. You are stranded. You died!")

            elif answer == "safe":
                answer = ask("You try different combinations. After a long time it opens. Inside is a flare gun, a gold watch, and a folded letter. Do you take the flare gun or read the letter first? (flare/letter):", ["flare", "letter"])

                if answer == "flare":
                    print("You take the flare gun to the beach. A cargo ship passes and you fire. They see it and rescue you. You win!")

                elif answer == "letter":
                    answer = ask("The letter is from the captain to his family. It mentions a hidden lifeboat on the north side of the wreck. Do you go look for the lifeboat or take the flare gun to the beach? (lifeboat/flare):", ["lifeboat", "flare"])

                    if answer == "lifeboat":
                        answer = ask("You find the lifeboat. It is in decent condition. Do you launch it immediately or spend the night preparing supplies first? (launch/prepare):", ["launch", "prepare"])

                        if answer == "launch":
                            print("You launch the lifeboat without supplies. Three days into the open ocean you run out of water. You died!")

                        elif answer == "prepare":
                            print("You spend the night gathering food and water from the ship. The next morning you launch and navigate toward the mainland. A coastguard patrol spots you on day two. You win!")

                    elif answer == "flare":
                        print("You take the flare gun to the beach. A passing yacht sees your flare and rescues you. You win!")

        elif answer == "engine":
            answer = ask("The engine room is flooded up to your knees. You can see the generator and also a hatch in the floor. Do you try to start the generator or open the hatch? (generator/hatch):", ["generator", "hatch"])

            if answer == "generator":
                print("You try to start the generator while standing in water. You are electrocuted. You died!")

            elif answer == "hatch":
                answer = ask("The hatch leads to a dry lower compartment. Inside you find emergency supplies and a hand-cranked radio. Do you use the radio or take the supplies to the beach? (radio/supplies):", ["radio", "supplies"])

                if answer == "radio":
                    print("You crank the radio and get through to a coastguard station. They triangulate your signal and send a rescue boat. You win!")

                elif answer == "supplies":
                    print("You take the supplies to the beach and settle in for a long wait. Weeks pass. No one comes. You died!")

    elif answer == "upper":
        answer = ask("On the upper deck you get a good view of the island. You can see a lighthouse to the east, smoke rising from the jungle, and a harbor to the south. Where do you head? (lighthouse/jungle/harbor):", ["lighthouse", "jungle", "harbor"])

        if answer == "lighthouse":
            print("You head to the lighthouse and find a working radio inside. You call for help and are rescued by morning. You win!")

        elif answer == "jungle":
            answer = ask("You head into the jungle toward the smoke. You find a small camp with a fire still burning but nobody around. There is food cooking on the fire and a backpack on the ground. Do you eat the food or search the backpack? (eat/search):", ["eat", "search"])

            if answer == "eat":
                print("The food was poisoned by the plants used to cook it. You died!")

            elif answer == "search":
                answer = ask("The backpack contains a map, a knife, a lighter, and a satellite phone with low battery. Do you use the phone or follow the map? (phone/map):", ["phone", "map"])

                if answer == "phone":
                    print("You dial emergency services with the last of the battery. They trace the signal and rescue you within hours. You win!")

                elif answer == "map":
                    answer = ask("The map shows a path to the harbor. You follow it carefully. At the harbor you find a small sailboat. Do you take it or wait for the camp owner to return? (take/wait):", ["take", "wait"])

                    if answer == "take":
                        print("You sail the boat toward the mainland. It takes two days but you make it. You win!")

                    elif answer == "wait":
                        print("You wait at the harbor. The camp owner arrives and turns out to be a smuggler. He locks you up. You never escape. You died!")

        elif answer == "harbor":
            answer = ask("You make your way south to the harbor. A fishing boat is docked and the fisherman is onboard. Do you call out to him or sneak aboard while he is busy? (callout/sneak):", ["callout", "sneak"])

            if answer == "callout":
                print("The fisherman is relieved to see another person. He has been lost himself. Together you figure out a route home and make it back safely. You win!")

            elif answer == "sneak":
                print("You hide on the boat. It sets off. Hours later the fisherman finds you and panics. He radios the coastguard thinking you are an attacker. You are arrested on arrival. Not the best ending. You survived but lost your freedom for a while.")

# path 4 road

elif answer == "road":
    answer = ask("You follow the dirt road west. After an hour you reach a small abandoned town. There is a petrol station, a church, and a hotel. Where do you go? (petrol/church/hotel):", ["petrol", "church", "hotel"])

    if answer == "petrol":
        answer = ask("The petrol station has an old truck out front. The keys might be inside. Do you search for the keys or look for a phone inside the station? (keys/phone):", ["keys", "phone"])

        if answer == "keys":
            answer = ask("You find the keys behind the counter. The truck starts! Do you drive along the road heading out of town or check the other buildings first? (drive/check):", ["drive", "check"])

            if answer == "drive":
                answer = ask("You drive for an hour. The road forks. A sign points left to PORT and right to MOUNTAIN PASS. Which way? (port/mountain):", ["port", "mountain"])

                if answer == "port":
                    print("You reach the port. A ferry is about to depart. You make it just in time and ride it to the mainland. You win!")

                elif answer == "mountain":
                    answer = ask("The mountain pass is beautiful but the road deteriorates. The truck struggles. Do you push on or turn back? (push/back):", ["push", "back"])

                    if answer == "push":
                        print("The truck breaks down on the pass. You are stranded in the mountains with no shelter. You died!")

                    elif answer == "back":
                        print("You turn back and take the port road instead. You reach the ferry terminal just before the last sailing. You win!")

            elif answer == "check":
                answer = ask("In the hotel you find a guest register with recent entries. Someone was here just days ago. You also find a working landline phone. Do you call for help or follow the trail of the recent guest? (call/follow):", ["call", "follow"])

                if answer == "call":
                    print("You reach emergency services on the landline. They know the island and send a coastguard boat. You win!")

                elif answer == "follow":
                    answer = ask("The register shows the guest headed to a marina on the east coast. Do you drive the truck to the marina or explore the church first? (marina/church):", ["marina", "church"])

                    if answer == "marina":
                        print("You reach the marina. The recent guest is still there, a journalist stranded like you. She has a satellite phone. Together you call for rescue. You win!")

                    elif answer == "church":
                        answer = ask("Inside the church you find an old priest who has lived alone on the island for decades. He knows every inch of it. He offers to guide you to safety. Do you accept? (yes/no):", ["yes", "no"])

                        if answer == "yes":
                            print("The priest leads you through hidden paths to a cove where a rescue boat makes monthly supply runs. It arrives the next day. You win!")

                        elif answer == "no":
                            print("You leave the priest and try to find the marina alone. You get lost. You died!")

        elif answer == "phone":
            answer = ask("You find an old landline phone. Amazingly it has a dial tone. Do you call emergency services or try to call someone you know? (emergency/personal):", ["emergency", "personal"])

            if answer == "emergency":
                print("Emergency services know the island. They dispatch a helicopter that finds you within two hours. You win!")

            elif answer == "personal":
                answer = ask("You call a friend. They are shocked and want to help but do not know who to call. Do you tell them to call emergency services or try to guide them through it yourself? (emergency/guide):", ["emergency", "guide"])

                if answer == "emergency":
                    print("Your friend calls emergency services who contact the island coastguard. You are rescued. You win!")

                elif answer == "guide":
                    print("The process takes too long and the phone line cuts out before help is arranged. You are stranded. You died!")

    elif answer == "church":
        answer = ask("You enter the church. It is dusty but intact. You find an old priest sitting in a pew. He looks up calmly as if he expected you. Do you speak to him or explore the church yourself? (speak/explore):", ["speak", "explore"])

        if answer == "speak":
            answer = ask("The priest tells you he has lived here for forty years by choice. He knows the island perfectly. He offers you three options: he can guide you to a harbor, give you a map, or let you rest and think. What do you choose? (harbor/map/rest):", ["harbor", "map", "rest"])

            if answer == "harbor":
                print("The priest guides you through back roads to a small harbor. A supply boat arrives the next morning. You sail home with the crew. You win!")

            elif answer == "map":
                answer = ask("He gives you a hand drawn map showing the whole island. You study it and see a shortcut to the lighthouse. Do you head to the lighthouse or the harbor marked on the map? (lighthouse/harbor):", ["lighthouse", "harbor"])

                if answer == "lighthouse":
                    print("You reach the lighthouse and find a working radio. You call for help and are rescued. You win!")

                elif answer == "harbor":
                    print("You follow the map to the harbor. A fishing boat is there and the crew agrees to take you to the mainland. You win!")

            elif answer == "rest":
                answer = ask("You rest for a full day. You feel restored. The priest gives you food and water for your journey. He recommends heading to the lighthouse. Do you take his advice or head to the road instead? (lighthouse/road):", ["lighthouse", "road"])

                if answer == "lighthouse":
                    print("You reach the lighthouse rested and prepared. You contact the coastguard and are rescued. You win!")

                elif answer == "road":
                    answer = ask("You follow the road and find an abandoned truck with keys still in it. Do you drive toward the port or toward the mountain pass? (port/mountain):", ["port", "mountain"])

                    if answer == "port":
                        print("You reach the port and board a ferry to the mainland. You win!")

                    elif answer == "mountain":
                        print("The mountain road ends in a dead end. The truck runs out of fuel. You are stranded in the highlands. You died!")

        elif answer == "explore":
            answer = ask("You explore the church and find a trapdoor behind the altar. Below is a tunnel. Do you go through the tunnel or go back and talk to the priest? (tunnel/priest):", ["tunnel", "priest"])

            if answer == "tunnel":
                answer = ask("The tunnel is long and dark. After twenty minutes you see light ahead. You emerge into a cave by the sea. A small speedboat is moored inside. Do you take the speedboat or go back? (speedboat/back):", ["speedboat", "back"])

                if answer == "speedboat":
                    answer = ask("The speedboat starts easily. Do you head toward the mainland immediately or go back to get the priest? (mainland/priest):", ["mainland", "priest"])

                    if answer == "mainland":
                        print("You navigate out of the cave and head for the mainland at full speed. You arrive safely. You win!")

                    elif answer == "priest":
                        print("You go back for the priest. He declines to leave. He gives you his blessing. You take the speedboat alone and reach the mainland. You win!")

                elif answer == "back":
                    print("You turn back through the tunnel. The priest tells you about the speedboat himself. You take it and escape. You win!")

            elif answer == "priest":
                print("You talk to the priest. He guides you to the harbor where a supply boat arrives weekly. You wait two days and sail home. You win!")

    elif answer == "hotel":
        answer = ask("You enter the hotel lobby. The lights are on. Someone is still supplying power. You find a reception desk and a staircase. Do you check behind the desk or go upstairs? (desk/upstairs):", ["desk", "upstairs"])

        if answer == "desk":
            answer = ask("Behind the desk you find a radio, a map, and a room key with the number 7 on it. Do you use the radio or go to room 7? (radio/room):", ["radio", "room"])

            if answer == "radio":
                print("You get through to a coastguard station on the radio. They know the island and send a boat. You are rescued by nightfall. You win!")

            elif answer == "room":
                answer = ask("Room 7 is unlocked. Inside is a person asleep on the bed. You wake them. They are a photographer who got stranded two weeks ago. They have a satellite phone but it needs charging. There is a solar charger by the window. Do you wait for it to charge or look for another way? (wait/other):", ["wait", "other"])

                if answer == "wait":
                    print("The phone charges in two hours. The photographer calls for rescue. A helicopter arrives the next morning. You both get home. You win!")

                elif answer == "other":
                    answer = ask("You leave the photographer and go back to explore. You find a generator in the basement. Do you start it to power the whole hotel or just find the radio at the desk? (generator/radio):", ["generator", "radio"])

                    if answer == "generator":
                        print("The generator powers the hotel including the phone charger. Within an hour the photographer's phone is charged. You both call for help and are rescued. You win!")

                    elif answer == "radio":
                        print("You use the desk radio and get through to the coastguard. They rescue both of you. You win!")

        elif answer == "upstairs":
            answer = ask("Upstairs you find a long corridor. At the end is a room with light coming under the door. Do you knock or open it directly? (knock/open):", ["knock", "open"])

            if answer == "knock":
                answer = ask("A voice calls out to come in. Inside is an elderly woman who has been living in the hotel for months. She has food, water, and a radio but says it is broken. Do you try to fix the radio or ask her about other ways off the island? (fix/ask):", ["fix", "ask"])

                if answer == "fix":
                    answer = ask("You look at the radio. It just has a loose wire. A simple fix. Do you repair it yourself or ask the woman if she has tools? (repair/tools):", ["repair", "tools"])

                    if answer == "repair":
                        print("You fix the wire with what you have. The radio crackles to life. You call the coastguard and both of you are rescued. You win!")

                    elif answer == "tools":
                        print("She has a full toolbox. You repair the radio quickly. You call for help and a rescue team arrives. You win!")

                elif answer == "ask":
                    print("She tells you about a harbor to the south where boats pass weekly. The next one is tomorrow. She walks you there herself. You sail home. You win!")

            elif answer == "open":
                print("You burst in. The elderly woman inside screams in fright and hits you with a lamp. You are knocked unconscious. When you wake up you are tied to a chair. She is too frightened to let you go. You are stuck. You died!")
