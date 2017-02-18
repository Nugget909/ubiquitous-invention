from random import randint
pmoves=["Tackle","Thunderbolt","Cut","Electroball"]
aimoves=["Gust","Tackle","Fly","Cut"]
pshp=randint(99,101)
aishp=randint(99,101)

# First player move
def pmove1():
    print("Move 1: ",pmoves[0])
    print("Move 2: ",pmoves[1])
    print("Move 3: ",pmoves[2])
    print("Move 4: ",pmoves[3])
    select=input("Select move 1-4 ")
    
    if select=="1":
        print("Pikachu used Tackle")
        damage=randint(5,10)
        aihp=(aishp-damage)
        print("Pikachu did",damage,"damage")
        if aihp < 0:
            print("Oppenent's Pidgot fainted")
            print("You win")
        if aihp>0:
            aimove1(aihp)
            
    elif select=="2":
        print("Pikachu used Thunderbolt")
        damage=randint(12,20)
        aihp=(aishp-damage)
        print("Pikachu did",damage,"damage")
        if aihp < 0:
            print("Oppenent's Pidgot fainted")
            print("You win")
        if aihp>0:
            aimove1(aihp)
            
    elif select=="3":
         print("Pikachu used Cut")
         damage=randint(14,16)
         aihp=(aishp-damage)
         print("Pikachu did",damage,"damage")
         if aihp < 0:
            print("Oppenent's Pidgot fainted")
            print("You win")
         if aihp>0:
            aimove1(aihp)

    elif select=="4":
        print("Pikachu used Electroball")
        damage=randint(15,23)
        aihp=(aishp-damage)
        print("Pikachu did",damage,"damage")
        if aihp < 0:
            print("Oppenent's Pidgot fainted")
            print("You win")
        if aihp>0:
            aimove1(aihp)
    else:
        print("not valid entry.")
        pmove1()

# First AI move
def aimove1(aihp):
    numb=randint(0,3)

    if numb==0:
        print("Pidgot used Gust")
        dmg=randint(12,20)
        php=(pshp-dmg)
        if php < 0:
            print("Your Pikachu fainted")
            print("You lose")
        if php>0:
            print("Pikachu: ",php,"HP")
            print("Pidgot: ",aihp,"HP")
            pmove(php,aihp)

    if numb==1:
        print ("Pidgot used Tackle")
        dmg=randint(5,10)
        php=(pshp-dmg)
        if php < 0:
            print("Your Pikachu fainted")
            print("You lose")
        if php>0:
            print("Pikachu: ",php,"HP")
            print("Pidgot: ",aihp,"HP")
            pmove(php,aihp)

    if numb==2:
        print("Pidgot used Fly")
        dmg=randint(15,23)
        php=(pshp-dmg)
        if php < 0:
            print("Your Pikachu fainted")
            print("You lose")
        if php>0:
            print("Pikachu: ",php,"HP")
            print("Pidgot: ",aihp,"HP")
            pmove(php,aihp)

    if numb==3:
        print("Pidgot used Cut")
        dmg=randint(14,16)
        php=(pshp-dmg)
        if php < 0:
            print("Your Pikachu fainted")
            print("You lose")
        if php>0:
            print("Pikachu: ",php,"HP")
            print("Pidgot: ",aihp,"HP")
            pmove(php,aihp)

# All player moves after first
def pmove(php,aihp):
    print("Move 1: ",pmoves[0])
    print("Move 2: ",pmoves[1])
    print("Move 3: ",pmoves[2])
    print("Move 4: ",pmoves[3])
    select=input("Select move 1-4 ")
    
    if select=="1":
        print("Pikachu used Tackle")
        damage=randint(5,10)
        aihp=(aihp-damage)
        print("Pikachu did",damage,"damage")
        if aihp < 0:
            print("Oppenent's Pidgot fainted")
            print("You win")
        if aihp>0:
            aimove(php,aihp)
            
    if select=="2":
        print("Pikachu used Thunderbolt")
        damage=randint(12,20)
        aihp=(aihp-damage)
        print("Pikachu did",damage,"damage")
        if aihp < 0:
            print("Oppenent's Pidgot fainted")
            print("You win")
        if aihp>0:
            aimove(php,aihp)
            
    if select=="3":
         print("Pikachu used Cut")
         damage=randint(14,16)
         aihp=(aihp-damage)
         print("Pikachu did",damage,"damage")
         if aihp < 0:
            print("Oppenent's Pidgot fainted")
            print("You win")
         if aihp>0:
            aimove(php,aihp)

    if select=="4":
        print("Pikachu used Electroball")
        damage=randint(15,23)
        aihp=(aihp-damage)
        print("Pikachu did",damage,"damage")
        if aihp < 0:
            print("Oppenent's Pidgot fainted")
            print("You win")
        if aihp>0:
            aimove(php,aihp)

# All AI moves after first
def aimove(php,aihp):
    numb=randint(0,3)

    if numb==0:
        print("Pidgot used Gust")
        dmg=randint(12,20)
        php=(php-dmg)
        if php < 0:
            print("Your Pikachu fainted")
            print("You lose")
        if php>0:
            print("Pikachu: ",php,"HP")
            print("Pidgot: ",aihp,"HP")
            pmove(php,aihp)

    if numb==1:
        print ("Pidgot used Tackle")
        dmg=randint(5,10)
        php=(php-dmg)
        if php < 0:
            print("Your Pikachu fainted")
            print("You lose")
        if php>0:
            print("Pikachu: ",php,"HP")
            print("Pidgot: ",aihp,"HP")
            pmove(php,aihp)

    if numb==2:
        print("Pidgot used Fly")
        dmg=randint(15,23)
        php=(php-dmg)
        if php < 0:
            print("Your Pikachu fainted")
            print("You lose")
        if php>0:
            print("Pikachu: ",php,"HP")
            print("Pidgot: ",aihp,"HP")
            pmove(php,aihp)

    if numb==3:
        print("Pidgot used Cut")
        dmg=randint(14,16)
        php=(php-dmg)
        if php < 0:
            print("Your Pikachu fainted")
            print("You lose")
        if php>0:
            print("Pikachu: ",php,"HP")
            print("Pidgot: ",aihp,"HP")
            pmove(php,aihp)



print("Pikachu [HP: 100]")
print("Red sends out Pidgot [HP: 100]")
move=input("Fight or Quit? ")
if move=="fight" or move=="Fight":
    pmove1()

