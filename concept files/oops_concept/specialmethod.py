class employee:

    raiseamount=1.04

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first + "_" + last + "@company.com"


    def fullname(self):
        return '{} {}'.format(self.first,self.last)    
    
    def apply_raise(self):
        self.pay=int(self.pay * self.raiseamount)

    def __repr__(self) -> str:
        return "employee('{}', '{}','{}')".format(self.first,self.last,self.pay)

    def __str__(self) -> str:
        return '{}-{}'.format(self.fullname(),self.email)

    def __add__(self,other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())


emp1=employee('ashok','selvan',40000)  
emp2=employee('test','user',70000)

print(emp1)

print(repr(emp1))
print(str(emp1))

print(emp1.__repr__())
print(emp1.__str__())

print(int.__add__(1,2))      #---dunder add method
print(str.__add__('a','b'))

print(emp1 + emp2)     #--__add__

print(len('test'))

print('test'.__len__()) 

print(len(emp1))        #--__len__



