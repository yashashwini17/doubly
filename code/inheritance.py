class Parent:
    def func1(self):
        print("this function is in parent class.")
class Child(Parent):
    def func2(self):
        print("this function is in child class.")
object=Child()
object.func1()
object.func2()
                
