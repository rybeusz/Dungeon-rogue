import inve
boss = "!"
wife = "B"
host = "O"
menel = "&"
backpack = {}

def menel():
    if "wheat" in backpack:
        if backpack['wheat'][0] > 20:
            menelll = input("Wanna change 20 food for 2 vodka? / write Y to accept or N for reject ")

            if menelll = ""
    else:
        print("elo")

def host(name):
    namei = str(name)
    if "clothes" not in backpack:
        print("{} ubierz sie!".format(namei))
    else:
        print("")


def wife(): # ogarnąć ta ku.... tylko pierwsze podejsice
    if "scythe" and "corn" in backpack:
        if backpack['corn'][0] < 100:
            print("You need to gather 100  corn cob get back to work ")
        else:
            print("DZIEKI ZIa")

def trader(backpack):
    if "corn" in backpack:
        x = input("Do u wanna sell some corn mate? write yes or no: ")
        x = x.lower()
        if x == "yes":
            z = int(input("How much u wanna sell?: "))
                if z > backpack["corn"][0]:
                    print("u dont have that much corn in ur backpack ")
                else:
                    inve.remove_item



def boss():
    if "vodka" not in backpack:
        negotiate = input("if u wanna negotiate write N, if u wanna sell write Q ")
        negotiate = negotiate.lower()
        if negotiate == "n":
            print("You need to bring me vodka if wanna to negotiate with me  ")
        if negotiate == "q":
            print("GJ u win the game")  # + dodac okreslana liczbe kasy
            quit()
    else:
        input("So how much u wanna for rearaeare")





