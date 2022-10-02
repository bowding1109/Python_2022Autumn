# 建立類別 class

# class Cars:
#     def __init__(self,color,seat):
#         self.color = color
#         self.seat =seat
#     #方法(method)
#     def move(self, meter):
#         print("My car moves"+str(meter)+"meters")
#     def print(self):
#         print("My car's color is"+self.color)
#         print("My car has "+str(self.seat)+"seats")
# audi = Cars("blue",4)
# audi.move(5)

# 建立物件object
# audi = Cars() 
# print(isinstance(audi, Cars))  #判斷物件之間的關係
# audi.color = "blue" #顏色屬性
# audi.seat = 4  #座位屬性
# #呼叫物件
# print(audi.color)  #執行結果為blue
# print(audi.seat)   #執行結果為4

class FullName:
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname =lastname
    def printAttribute(self):
        print("My name is "+self.name1)
        print("My name is" + self.name2)
        # print("My car has "+str(self.seat)+"seats")
        # print(name1.firstname,name1.lastname)
        # print(name2.firstname,name2.lastname)
name1 = FullName("Andy","Wang")
name2 = FullName("Lulu","Cheng")