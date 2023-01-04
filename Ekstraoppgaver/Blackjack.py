                        # Er ikke helt ferdig med denne koden, men den funker på det mest grunnleggende nivå. Skal kommentere den senere
import random
import os
command = 'cls'

sort = ["hjerter", "ruter", "spa", "kløver"]
kortstokk = {
    "hjerter": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
    "ruter": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 
    "spa": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 
    "kløver": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
}

""""
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
"""
def closest(lst, K):
      
    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]



class Blackjack:
    def __init__(self, d_take, d_hand = [], runde=0, players=1):
        self.runde = runde
        self.players = players
        self.d_take = d_take
        self.d_hand = d_hand
    
    def motta(self):
        self.d_hand.append(self.d_take)
        
    def holding(self, vis):
        if vis == True:
            print(f"Dealers hånd:\n{self.d_hand}\nSum: {sum(self.d_hand)}")
        
        if sum(self.d_hand) > 21:
            print("Dealer overtrådde 21")
            return "Vinn"
        return sum(self.d_hand)

    def spill(self): 
        os.system(command)
        Kort(2, Player).valg()
        Kort(1, Blackjack).valg()
        Player(0).holding(True)
        Blackjack(0).holding(True)

        while Player(0).spill() == True:
            os.system(command)
            Kort(1,Player).valg()
            Player(0).holding(True)

        if Player(0).holding(False) == "Tap":
            return

        while Blackjack(0).holding(False) < 19:
            os.system(command)
            Kort(1,Blackjack).valg()
        
        if Blackjack(0).holding(False) == "Vinn":
            return

        resultat = []
        resultat.append(Player(0).holding(False))
        resultat.append(Blackjack(0).holding(False))
        print(f"Du fikk {resultat[0]} og dealer fikk {resultat[1]}")

        if resultat[0] == closest(resultat, 21):
            print("Du vant")
            

        if resultat[1] == closest(resultat, 21):
            print("Du tapte")



class Kort:
    def __init__(self, antall, person, valgt = []):
        self.antall = antall
        self.valgt = valgt
        self.person = person

    def stokk(self):
        self.valgt.clear()  
        s = random.randint(0, 3)
        n = random.randint(0, len(kortstokk[sort[s]])-1)
        #self.valgt.insert(0, kortstokk[s][n])
        self.kort = kortstokk[sort[s]][n]
        kortstokk[sort[s]].remove(self.kort)
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

    def holding(self, vis):
        if vis == True:
            print(f"Din hånd:\n{self.hand}\nSum: {sum(self.hand)}")

        if sum(self.hand) > 21:
            print("Du overtrådde 21")
            return "Tap"
        return sum(self.hand)

    def spill(self):
        hit = input("Hit eller stand? \n>> ")
        if hit == "hit":
            self.hit = True
        #print(self.hit)    
        return self.hit
        

Blackjack(0).spill()