class People:
    def __init__(self,height,weight,age):
        self.height = height
        self.weight = weight
        self.age = age
    def print(self):
        print("My father height,weight,age is "+ self.father)
        print("My mother height,weight,age is "+ self.mother)
father = People(200,78,65)
mother = People(175,60,60)
