with open('Data.txt') as f:
    lines = f.readlines()

class Spill():
    def __init__(self, streng, poeng = []):
        self.streng = streng
        self.kamp = []
        self.poeng = poeng
        
    def get_value(self):
        self.alv = self.streng[0:1]
        self.forslag = self.streng[2:3]
        self.kamp.append(self.alv)
        self.kamp.append(self.forslag)
        Spill(0).runde(self.kamp)
        print(self.kamp)

    def runde(self, kamp):
        self.kamp = kamp
        if self.kamp[1] == "X":
            #self.poeng.append(1)
            if self.kamp[0] == "A":
                self.poeng.append(3)
            if self.kamp[0] == "B":
                self.poeng.append(1)
            if self.kamp[0] == "C":
                self.poeng.append(2) 
        if self.kamp[1] == "Y":
            #self.poeng.append(2)
            if self.kamp[0] == "A":
                self.poeng.append(3+1)
            if self.kamp[0] == "B":
                self.poeng.append(3+2)
            if self.kamp[0] == "C":
                self.poeng.append(3+3)
        if self.kamp[1] == "Z":
            #self.poeng.append(3)
            if self.kamp[0] == "A":
                self.poeng.append(6+2)
            if self.kamp[0] == "B":
                self.poeng.append(6+3)
            if self.kamp[0] == "C":
                self.poeng.append(6+1)
        #print(sum(self.poeng))
        self.kamp = []
        

for i in range(0,len(lines)):
    Spill(lines[i]).get_value()



