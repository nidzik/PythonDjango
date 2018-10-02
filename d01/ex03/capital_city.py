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

    if  av in states:
        for cle,valeur in states.items():
            if cle == av:
                print (capital_cities[valeur])
    else:
        print ("Unknow state")

if __name__ == '__main__':
    find_capital()
