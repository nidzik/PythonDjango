import sys


def find_cap(states, capital_cities, av):
    for cle,valeur in capital_cities.items():
        if valeur == av:
            for c,v in states.items():
                if v == cle:
                    print (av + " is the capital of " + cle)

def find_sta(states, capital_cities, av):
    for cle,valeur in states.items():
        if cle == av:
            print ( capital_cities[valeur] + " is the capital of " + av)

def find_both():
    states = {
        "Oregon"        : "OR",
        "Alabama"       : "AL",
        "New Jersey"    : "NJ",
        "Colorado"      : "CO"
    }

    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    
    if(len(sys.argv) != 2):
        exit()
    
    av = str(sys.argv[1])
    cleart = av.strip(" ")
    tab = cleart.split(',')

    for j in tab :
        if not j:
            exit()
    for i in tab:
        i = i.replace(" ", "").title()
        
        try:
            list(capital_cities.keys())[list(capital_cities.values()).index(i)]
        except ValueError:
            try:
                list(states.values())[list(states.keys()).index(i)]
            except ValueError:
                if i :
                    print (i + " is neither a capital nor a state")
        find_sta(states, capital_cities, i)
        find_cap(states, capital_cities, i)
            

if __name__ == '__main__':
    find_both()
