import random;

class cat:
    def __init__(self, breedname):
        self.breed = breedname
        self.catvalue = random.randint(0,100)
    def printbreed(self):
        print(str(self.breed))
    def printvalue(self):
        print(int(self.catvalue))
    def meow(self):
        print(str("miaow"))
catlist = []

##adding cats to the list
for i in range(0,10):
    newcat=cat("british shorthair") ;
    newcat.printbreed()
    catlist.append(newcat);

for i in range(0, 20):
    newcat = cat("russian blue")
    newcat.printbreed()
    catlist.append(newcat)


##print list of cats with meows and cat values
for i in range(0, len(catlist)):

    catlist[i].printbreed(),
    catlist[i].meow(),
    catlist[i].printvalue()



