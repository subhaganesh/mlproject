'''data      = attributes
   functions = methods 

   class             = it is a blueprint for creating instances
   instance of class = each unique employee will be an instance of class


'''
class employee:

    num_of_emp=0
    raiseamount=1.04         # raiseamount is class variable of class employee

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first + "_" + last + "@company.com"

        employee.num_of_emp += 1

    #each method in class always takes the instance as the first argument
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    def apply_raise(self):
        #self.pay=int(self.pay * employee.raiseamount)
        self.pay=int(self.pay * self.raiseamount)
# how we can access raiseamount from instance variable?
  #the instance variable (emp1) first check the instance that contains this attribute if doesnt contain it go and check the class  

emp1=employee('ashok','selvan',40000)  # emp1 was instance variable  of class employee
emp2=employee('test','user',70000)

print(emp1.first)
print(emp2.last)

print(emp1.email)

#here the first, last ,pay are the attributes of the class

#now we are going to see the methods (functions) of the class
print(emp1.fullname())

#when we use instance to call method
emp1.fullname()
#when we use class to call method
employee.fullname(emp1)

#instance variables are unique for each instance 
    #example: emp1 ,emp2
#class variables are same for each instance
    #example:raiseamount

print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)

#here we print value of the raise amount
print(employee.raiseamount)
print(emp1.raiseamount)
print(emp2.raiseamount)

print(employee.__dict__)
print(emp1.__dict__)

#here we are changing the value of the raise amount for emp1
emp1.raiseamount=2

print(emp1.__dict__)

print(employee.raiseamount)
print(emp1.raiseamount)
print(emp2.raiseamount)

print("num of emp" ,employee.num_of_emp)

