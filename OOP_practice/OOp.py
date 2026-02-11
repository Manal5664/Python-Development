class point:
    x=0
    y=0
    def setx(self,xcoord):
        self.x=xcoord
    def sety(self,ycoord):
        self.y=ycoord
    def get(self):
        return self.x,self.y
    def move(self,dx,dy):
        self.x+=dx
        self.y+=dy
p1=point()
print(p1.get())
p1.setx(4)
p1.sety(7)
print(p1.get())
p1.move(1,1)
print(p1.get())
        

class Animal:
    specie = 'cat'
    language = 'meow'
    count=0

    def setSpecie (self, s):
        self.specie = s
    def setLanguage (self, l):
        self.language = l
    def speak (self):
        print('I am a',self.specie,'and I can',self.language)
    def speakAlot(self):
        for i in range(5):
            print(self.language)
    def countAnimal(self):
        Animal.count+=1
        self.assignID(Animal.count)
        return Animal.count
    def assignID(self,id):
        self.ID=id
    def getID (self):
        return self.ID
a1=Animal()
a1.setSpecie('mouse')
a1.setLanguage('squeak')
a1.speakAlot()
a1.speak()
print('Animal')


class fraction:
    def setnum(self,x):
        self.num=x
    def setdenom(self,y):
        if y!=0:
            self.denom=y
        else:
            print('invalid value,setting to 1 instead')
            self.denom=1
    def getFraction(self):
        return self.num,self.denom
    def convertdecimal(self):
        return self.num/self.denom
            
# object call fraction class
f1=fraction()
f1.setnum(9)
f1.setdenom(5)
print(f1.convertdecimal())
