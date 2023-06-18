#regular instance method     (self)
#class method  @classmethod  (cls)
#static method @staticmethod (day) any argument

'''In summary, the key differences between these three method types 
lie in the scope of their operations and the parameters they receive. 

Instance methods operate on instance-specific data, 
class methods operate on class-level data, and 
static methods are independent of both instance and class data.
'''


class employee:

    num_of_emp=0
    raiseamount=1.04

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first + "-" + last + "@company.com"

        employee.num_of_emp += 1

    def fullname(self):
        return '{} {}'.format(self.first,self.last)    
    
    def apply_raise(self):
        self.pay=int(self.pay * self.raiseamount)

    #how to use class method over instance method?
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raiseamount= amount

    @classmethod
    def from_string(cls,emp_str):
        first,last,pay=emp_str.split('-')
        return cls(first,last,pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or  day.weekday() == 6 :
            return False
        return True



emp1=employee('ashok','selvan',40000)
emp2=employee('test','user',70000) 

employee.set_raise_amt(4)

print(employee.raiseamount)
print(emp1.raiseamount)
print(emp2.raiseamount)

emp_str_1='john-doe-10000'

new=employee.from_string(emp_str_1)
print(new.pay)
print(new.email)

import datetime
my_date= datetime.date(2023,6,19)

print(employee.is_workday(my_date))



