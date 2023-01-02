                        # Er ikke helt ferdig med denne koden, men den funker på det mest grunnleggende nivå. Skal kommentere den senere
import random 

hjerter = ["h_ace"]
ruter = ["r_ace"]
spa = ["s_ace"]
kløver = ["k_ace"]

for i in range(2,14):
    hjerter.append("h" + str(i))
    ruter.append("r" + str(i))
    spa.append("s" + str(i))
    kløver.append("k" + str(i))

kortstokk = [hjerter, ruter, spa, kløver]



class Blackjack:
    def __init__(self, d_take, d_hand = [], runde=0, players=1):
        self.runde = runde
        self.players = players
        self.d_take = d_take
        self.d_hand = d_hand
    
    def motta(self):
        self.d_hand.append(self.d_take)
        
    def holding(self):
        print(f"Dealers hånd:\n{self.d_hand}")

    #def spill(self):


class Kort:
    def __init__(self, antall, person, valgt = []):
        self.antall = antall
        self.valgt = valgt
        self.person = person

    def stokk(self):
        self.valgt.clear()  
        s = random.randint(0, 3)
        n = random.randint(0, len(kortstokk[s])-1)
        #self.valgt.insert(0, kortstokk[s][n])
        self.kort = kortstokk[s][n]
        kortstokk[s].remove(self.kort)
        #print(kortstokk)
        return self.kort
        
    def valg(self):
        for i in range(0, self.antall):
            #print(self.person)
            self.person(Kort(self.antall, self.person).stokk()).motta()
       
    
class Player:
    def __init__(self, take, bank = 500, hand = []):
        self.bank = bank
        self.take = take
        self.hand = hand
        self.hit = False
        
    def motta(self):
        self.hand.append(self.take)

    def holding(self):
        print(f"Din hånd:\n{self.hand}")

    def spill(self):
        hit = input("Hit eller stand? \n>> ")
        if hit == "hit":
            self.hit = True
        #print(self.hit)    
        return self.hit
        


Kort(2, Player).valg()
Kort(1, Blackjack).valg()
Player(0).holding()
Blackjack(0).holding()

while Player(0).spill() == True:
    Kort(1,Player).valg()
    Player(0).holding()

