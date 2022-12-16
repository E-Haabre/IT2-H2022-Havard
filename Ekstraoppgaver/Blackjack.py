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
    def __init__(self, d_take, runde=0, players=1):
        self.runde = runde
        self.players = players
        self.dealer = []
        self.d_take = d_take
    
    def d_Cards(self):
        self.dealer.append(self.d_take)
        print(f"Dealers hånd:\n{self.dealer}")


class Kort:
    def __init__(self, antall = 1, valgt = []):
        self.antall = antall
        self.valgt = valgt


    def stokk(self):
        self.valgt.clear()
        for i in range(self.antall):
            s = random.randint(0,3)
            n = random.randint(0,len(kortstokk[s])-1)
            self.valgt.insert(0, kortstokk[s][n])
            kstokk = kortstokk[s] 
            kstokk.remove(self.valgt[0])
        
            

    def dele(self):
        kjør = Kort(2)
        kjør.stokk()
        x = Player(self.valgt)
        x.holding()
        kjør = Kort(1)
        kjør.stokk()
        x = Blackjack(self.valgt)
        x.d_Cards()
        kjør = Kort()
        kjør.valg()
        
        
        
    def valg(self):

        svar = input("Hit or stand?(h/s)\n>> ")
        if svar == "h":
            kjør = Kort(1)
            kjør.stokk()
            x = Player(self.valgt)
            x.holding()
        elif svar == "s":
            kjør = Kort(1)
            kjør.stokk()
            Blackjack.d_Cards(self.valgt)
    
class Player:
    def __init__(self,  take, bank = 500,):
        self.bank = bank
        self.take = take
        self.hand = []
    def holding(self):
        self.hand.append(self.take)
        print(f"Din hånd:\n{self.hand}")

kjør = Kort()
kjør.dele()