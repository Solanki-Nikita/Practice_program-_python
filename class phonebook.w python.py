class contact :

    def __init__(self,contact_num,contact_name):
        self.contact_num=contact_num
        self.contact_name= contact_name
    def PutData(self):
        f=open("contact.txt","w")
        f.write( self.contact_num)
        f.write(self.contact_name)
        f.close()
    def GetData(self):
        f=open("contact.txt","r")
        x=f.read()
        print(x)
        f.close()


a=int(input("Enter a contact_num:"))
b=input("Enter a contact_name:")

x=contact(a,b)
x.PutData()
x.GetData()
