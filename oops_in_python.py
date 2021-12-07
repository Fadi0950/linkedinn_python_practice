class myclass():
    def mymethod_1(self):
        print("This is method one")
    def mymethod_2(self,somestring):
        print(f"this is my method {somestring}")
class another_class(myclass):
    def mymethod_1(self):
        myclass.mymethod_1(self)
        print("This is another class method 1")

    def mymethod_2(self,somestring):
        myclass.mymethod_2(self,somestring)
        print(f"this is another class method2 ")

obj=myclass()
obj.mymethod_1()
obj.mymethod_2("two")
obj_2=another_class()
obj_2.mymethod_1()
obj_2.mymethod_2("hello")
