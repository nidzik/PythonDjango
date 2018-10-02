import sys

def find_capital():
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

    try:
        list(capital_cities.keys())[list(capital_cities.values()).index(av)]
    except ValueError:
        print ("Unknow capital city")
        
            

    for cle,valeur in capital_cities.items():
        if valeur == av:
            for c,v in states.items():
                if v == cle:
                    print (c)

if __name__ == '__main__':
    find_capital()
