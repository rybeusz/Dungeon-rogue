import inve
import guess


def enter():
    input("\nClick Enter to continue ")


def menel(backpack):
    loot = [["vodka", "food", 1], ["gold coin", "other", 1]]
    if "gold coin" in backpack:
        if backpack['gold coin'][0] > 10:
            vodka_sell = input("Wanna change 10 gold coins for 1 vodka? / write yes to accept or no for reject")
            if vodka_sell == "yes":
                inve.remove_item(backpack, loot[1], 10)
                inve.add_to_inventory(backpack, loot[0], 1)
            if vodka_sell == "no":
                print("bye ")
            else:
                print("u need to write yes or no ")
        else:
            print("u must have some money ")

    else:
        print("elo")
    return backpack


def host2(backpack, name="Mariusz"):
    namei = str(name)
    text = ''
    if "clothes" not in backpack:
        print("{} dress up".format(namei))
        enter()
    else:
        print("U look like a badass ")
        enter()

def wife2(backpack):  # ogarnąć ta ku.... tylko pierwsze podejsice
    if "scythe" and "corn" in backpack:
        if backpack['corn'][0] < 20:
            print("You need to gather 20 corn cob so get back to work! ")
        else:
            print("Thanks u can go now ")


def wife1(backpack):
    if "corn" not in backpack:
        print("Where have u been u f...... drunktard, get back to work and collect 20 corn cobs! ")


def trader(backpack):
    loot = [["corn", "food", 1]]
    if "corn" in backpack:
        x = input("Do u wanna sell some corn mate? write yes or no: ")
        x = x.lower()
        if x == "yes":
            remove_corn = int(input("How much u wanna sell?: "))
            if remove_corn > backpack["corn"][0]:
                print("u dont have that much corn in ur backpack ")
            else:
                inve.remove_item(backpack, loot, remove_corn)
        elif x == "no":
            print("Come to me when u wanna sell corn ")
        else:
            print("ur answer need to be yes or no ")
    else:
        print("You dont have any corn come when u get some ")
    return backpack


def boss(backpack):
    if "vodka" in backpack:
        guess.main()
    else:
        print("u need to have a vodka to play with me! ")
