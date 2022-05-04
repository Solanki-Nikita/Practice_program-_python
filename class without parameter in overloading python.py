## classes without parameter in overloading.....


class school():

    def __init__(self):
        self.name = input("Enter school name:")
        self.address = input("Enter school address:")

    def show(self):
        print("{} is situated at {}".format (self.name,self.address))
        
item1 = school()
item1.show()

