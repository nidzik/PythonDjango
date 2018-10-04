import random
import beverages

class CoffeeMachine:

    def __init__(self):
        self.count = 0
        
    class EmptyCup(beverages.HotBeverage):
        name = "empty cup"
        price = 0.90
        desc = "An empty cup?! Gimme my money back!"
    
    class BrokenMachineException(Exception):
        def __init__(self):
            self.txt = "This coffee machine has to be repaired."
            
    def repair(self):
            self.count = 0

    def serve(self, type):
            try:
                if isinstance(type, beverages.HotBeverage) == False:
                    raise Exception ("Type Error")
            except Exception as e:
                print (e)
                type = self.EmptyCup()
            self.count += 1
            if self.count > 10:
                raise self.BrokenMachineException()
            return random.choice([type, self.EmptyCup()])
        

if  __name__ == '__main__' :
    
    coco = CoffeeMachine()
    i = 0;
    try :
        while i < 15 :
            gg = (coco.serve(beverages.Coffee()))
            print(gg.desc)
            i+=1
    except Exception as e :
        print(e.txt)
        coco.repair()
    i = 0 
    try:
        while i < 15:
            bev = coco.serve(type = random.choice([beverages.Coffee(), beverages.Tea(), beverages.Chocolate(), beverages.Capuccino()]))
            print(bev.desc)
    except Exception as e:
        print(e.txt)
        coco.repair()
