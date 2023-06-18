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
    
class developer(employee):      #sub class of employee
    raiseamount=3

    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        #employee.__init__(self,first,last,pay) --(both are representing the parent class)
        self.prog_lang=prog_lang
           
class manager(employee):

    def __init__(self, first, last, pay,employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees=[]
        else:
            self.employees=employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('--->',emp.fullname())




     


dev1=developer('ashok','selvan',40000,'python')
dev2=developer('test','user',70000,'java')

print(dev1.email)        #attribute
print(dev2.fullname())   #method 

print(dev1.pay)
dev1.apply_raise()
print(dev1.pay)

print(dev1.email)
print(dev2.prog_lang) 

mgr1=manager('sue','smith',90000,[dev1])

print(mgr1.email)

mgr1.print_emp()

mgr1.add_emp(dev2)

mgr1.print_emp()

mgr1.remove_emp(dev2)

mgr1.print_emp()

print(isinstance(mgr1,employee))
print(isinstance(mgr1,developer))
print(issubclass(developer ,employee))
print(issubclass(developer ,manager))


