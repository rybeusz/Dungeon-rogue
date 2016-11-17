import inve
import guess


def enter():
    input("\nClick Enter to continue ")


def bum(backpack):
    loot = [["vodka", "food", 1]]
    loot2 = [["gold coin", "other", 1]]
    if "gold coin" in backpack:
        if backpack['gold coin'][0] >= 10:
            print("Bum say: ")
            vodka_sell = input("Wanna change 1 gold coins for 1 vodka?\n(write yes to accept or no for reject) ")
            if vodka_sell == "yes":
                try:
                    vodka_ask = int(input("How much vodka u need? "))
                    if vodka_ask <= backpack["gold coin"][0]:
                        print("Bum say: ")
                        print("GLUP ")
                        inve.remove_item(backpack, loot2, vodka_ask)
                        inve.add_to_inventory(backpack, loot, vodka_ask)
                        enter()
                    else:
                        print("Bum say: ")
                        print("U dont have coins for this, f... off: ")
                        enter()
                except ValueError:
                    print("U need to write a number: ")
                    enter()
            elif vodka_sell == "no":
                print("Bum say: ")
                print("bye come to papa again :0 ")
                enter()
            else:
                print("Bum say: ")
                print("I dont know whay you talking about ")
                enter()
        else:
            print("Bum say: ")
            print("You must have at least 10 gold coin to buy stuff from me! ")
            enter()
    else:
        print("Bum say: ")
        print("Come back when u earn some money! ")
        enter()
    return backpack


def host(backpack, name="Mariusz"):
    namei = str(name)
    if ("clothes" not in backpack) or (backpack['clothes'][0] < 5):
        print("Host say: ")
        print("{} u need to dress up before u can leave my tavern, so come back with some cloths".format(namei))
        enter()
    else:
        print("Host say: ")
        print("U look like a badass right now u can go ")
        enter()
        return True


def wife(backpack):
    if "corn" in backpack:
        if backpack['corn'][0] <= 20:
            print("Wife say: ")
            print("You need to gather 20 corn cob so get back to work! ")
            enter()
        else:
            print("Wife say: ")
            print("Thanks u can go now ")
            enter()
            return True
    if "corn" not in backpack:
        print("Wife say: ")
        print("Where have u been u f...... drunkard, get back to work and collect 20 corn cobs! ")
        enter()


def trader(backpack):
    loot = [["gold coin", "other", 1]]
    loot2 = [["corn", "food", 1]]
    if "corn" in backpack:
        print("Trader ask: ")
        x = input("Do u wanna sell some corn mate?\n(write yes or no): ")
        x = x.lower()
        if x == "yes":
            try:
                print("Trader ask: ")
                remove_corn = int(input("How much u wanna sell?: "))
                if remove_corn > backpack["corn"][0]:
                    print("Trader say: ")
                    print("You dont have that much corn in ur backpack ")
                    enter()
                else:
                    print("Trader say: ")
                    print("Thanks for corn :) ")
                    inve.remove_item(backpack, loot2, remove_corn)
                    inve.add_to_inventory(backpack, loot, remove_corn)
            except ValueError:
                print("U need to write a number: ")
                enter()
        elif x == "no":
            print("Trader say: ")
            print("Come to me when u wanna sell corn ")
            enter()
        else:
            print("Trader say: ")
            print("(Your answer need to be yes or no) ")
            enter()
    else:
        print("Trader say: ")
        print("You dont have any corn, come to me when u get some ")
        enter()
    return backpack


def boss(backpack):
    loot = [["vodka", "food", 1]]
    if "vodka" in backpack:
        print("Boss say: ")
        print("Lets play!!!!! ")
        guess.main(backpack["vodka"][0])
        inve.remove_item(backpack, loot, backpack["vodka"][0])
        enter()

    else:
        print("Boss say: ")
        print("u need to have a vodka to play with me boy!\nCome back when u got some boy! ")
        enter()
