class Parent1:
    def method1(self):
        print("Method from Parent1")

class Parent2:
    def method2(self):
        print("Method from Parent2")
        
    def method1(self):
        print("m-1")

# Child class inherits from both Parent1 and Parent2
class Child( Parent2,Parent1):
    def child_method(self):
        print("Method from Child")

# Create an instance of the Child class
child_instance = Child()

# Call methods from Parent1, Parent2, and Child
child_instance.method1()  # Calls method1 from Parent1
child_instance.method2()  # Calls method2 from Parent2
child_instance.child_method()  # Calls child_method from Child

child_instance.method1()
