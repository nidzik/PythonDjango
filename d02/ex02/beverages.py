class HotBeverage:

    price = 0.30
    name = "hot beverage"
    desc = "Just some hot water in a cup."

    def description(self):
        return self.desc

    def __str__(self):
        return('name : ' + self.name + '\nprice : ' + '%.2f' % self.price + '\ndescription : ' + HotBeverage.description(self) + '\n')

class Coffee(HotBeverage):
    
    price = 0.40
    name = "coffee"
    desc = "A coffee, to stay awake."

class Tea(HotBeverage):
    name = "tea"

class Chocolate(HotBeverage):
    price = 0.50
    name = "chocolate"
    desc = "Chocolate, sweet chocolate..."

class Capuccino(HotBeverage):
    price = 0.45
    name = "capuccino"
    desc = "Un po' di Italia nella sua tazza!"

if  __name__ == '__main__' :
    h = HotBeverage()
    co = Coffee()
    t = Tea()
    ch = Chocolate()
    ca = Capuccino()
    print(h)
    print(co)
    print(t)
    print(ch)
    print(ca)
    
