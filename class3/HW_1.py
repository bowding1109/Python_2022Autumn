class People:
    def __init__(self,height,weight,age):
        self.height = height
        self.weight = weight
        self.age = age
    def printAttribute(self):
        print("someone height"+str(self.height)+"weight"+str(self.weight)+"age"+str(self.age))
father = People(200,78,65)  
father.printAttribute()
mother = People(175,60,60)
mother.printAttribute()
