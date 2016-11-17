import inve
import guess


def enter():
    """function for print stuff in console"""
    input("\nClick Enter to continue ")


def bum(backpack):
    """function for interaction with bum, buying vodka for coins + error handling"""
    loot = [["vodka", "food", 1]]
    loot2 = [["gold coin", "other", 1]]
    print("\nBum says: ")
    if "gold coin" in backpack:
        if backpack['gold coin'][0] >= 1:
            vodka_sell = input("-I see gold in your pocket!\nDo u wanna change 1 gold coin for 1 vodka?\n(write yes to accept or no for reject)\n")
            if vodka_sell == "yes":
                try:
                    vodka_ask = int(input("-How much vodka u need my friend?\n"))
                    if vodka_ask <= backpack["gold coin"][0]:
                        print("GLUP ")
                        inve.remove_item(backpack, loot2, vodka_ask)        # removing coins from backpack
                        inve.add_to_inventory(backpack, loot, vodka_ask)    # adding vodka
                        enter()
                    else:  # handling situation when u have no gold coins
                        print("-U dont have coins for this...god's drink, f... off! ")
                        enter()
                except ValueError:   # handling bugs with writing some other stuff then int
                    print("(U need to write a number) ")
                    enter()
            elif vodka_sell == "no":
                print("-Bye, come to papa again :0 ")
                enter()
            else:
                print("-I dont know what you talking about ")
                enter()
        else:
            print("-You must have at least 1 gold coin to buy vodka! ")
            enter()
    else:
        print("-U dont have coins for this...god's drink, f... off! ")
        enter()
    return backpack


def host(backpack, name="Mariusz"):
    """function for interaction with host"""
    namei = str(name)
    print("\nHost says: ")
    if ("clothes" not in backpack) or (backpack['clothes'][0] < 5):
        print("""-Hey {}! You don't look good...
I never expect that farmer can drink so much alcohol in one night.
You are naked so before you come back to your wife
find your clothes, they are close to tavern.""".format(namei))
        enter()
    else:
        print("-Now you look like a badass! Go fast to your \nhome before your wife will be very angry. ")
        enter()
        return True         # return True to change lvl


def wife(backpack):
    """function for interaction with wife <3 """
    print("\nYour wife says: ")
    if "corn" in backpack:
        if backpack['corn'][0] < 20:
            print("-You need to gather 20 corn cob so get back to work! ")
            enter()
        else:
            print("-Ahh you are a bastard but I know your dream...\nNow go to city and buy your ticket my love :* ")
            enter()
            return True         # because of this we can change lvl
    if "corn" not in backpack:
        print("-Where have u been u f...... drunkard, \nget back to work and collect 20 corn cobs! ")
        enter()


def trader(backpack):
    """interaction with trader selling corn for gold coins + error handling """
    loot = [["gold coin", "other", 1]]
    loot2 = [["corn", "food", 1]]
    print("\nTrader says: ")
    if "corn" in backpack:
        x = input("-Hey! So you want sell some corn mate?\n(write yes or no): ")
        x = x.lower()
        if x == "yes":
            try:
                remove_corn = int(input("-How much u wanna sell?: "))
                if remove_corn > backpack["corn"][0]:
                    print("-You dont have that much corn in ur backpack ")
                    enter()
                else:
                    print("-Thanks for corn :) ")
                    inve.remove_item(backpack, loot2, remove_corn)
                    inve.add_to_inventory(backpack, loot, remove_corn)
                    enter()
            except ValueError:
                print("(U need to write a number): ")
                enter()
        elif x == "no":
            print("-Come to me when u wanna sell corn ")
            enter()
        else:
            print("(Your answer need to be yes or no) ")
            enter()
    else:
        print("-You dont have any corn, come to me when u get some ")
        enter()
    return backpack


def boss(backpack):
    """interaction with boss, MEMBER u need to have vodka if u wanna play boss game :> """
    loot = [["vodka", "food", 1]]
    print("\nTicket seller says: ")
    if "vodka" in backpack:
        print("""-It's time to play! If you win in my game,
you will win ticket for ship travel.
If you lose, I take your vodka omomom!""")
        enter()
        guess.main(backpack["vodka"][0])
        inve.remove_item(backpack, loot, backpack["vodka"][0])
        input("\033[94m" + "\n-Go away and never go back when you still got a chance." + "\033[00m")

    else:
        print("""-Do you want tickets? You can win them in my game.
But you need to have a vodka to play with!
Come back when u got some boy! """)
        enter()
