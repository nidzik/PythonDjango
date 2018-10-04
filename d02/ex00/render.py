import sys, os, re
import settings

def hi():

    if len(sys.argv) != 2 :
        print ("usage : python3 render.py <file>.template")
        exit()

    arg = sys.argv[1]

    if arg.endswith('.template'):
        pass
    else:
        print ("Error : the file has to be a .template")
        exit()

    try :
        f = open(arg, 'r')
        data = f.read()
        f.close
    except IOError:
        print (arg + " file does not exist")
        exit()

    data = data.replace("{name}",settings.name)
    data = data.replace("{firstname}",settings.firstname)
    data = data.replace("{age}",settings.age)
    data = data.replace("{profession}",settings.profession)
    data = data.replace("{title}",settings.title)
    
    arg = arg.replace(".template", ".html")
    f = open(arg, 'w')
    f.write(data)
    f.close()

hi()
