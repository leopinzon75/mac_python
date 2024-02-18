# Python-Object-Oriented-Programming


# class Employee:
#     pass

# When you create methods within a class they receive the instance (self)
# as the first argument automatically, and after self we can specify what
# other arguments we want to accept

class Employee:
    def __init__(self, first, last, pay, a, b, c):# note on init:self d and h can be out but no errors
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + ',' + last + '@company.com'
        self.a = a
        self.b = b 
        self.c = c
        self.d = first + 'bbbb'
        self.h = last + 'gggg'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)



emp_1 = Employee('Corey', 'Shafer',  500000, 'a', 'b', 'c')# note on init: self d and h can be out but no errors
emp_2 = Employee('Test', 'User',  60000, 'a', 'b', 'c')

# print(emp_1.d)
# Output: Coreybbbb

# print(emp_1.a)
# Output: Coreybbbb
# a

# print(emp_1.h)
# Output: Shafergggg


# print(emp_1)
# print(emp_2)
        
    
# emp_1.first = 'Corey'
# emp_1.last = 'Shafer'
# emp_1.email = 'Corey.Shafer@company.com'
# emp_1.pay = 50000
    
  
# emp_2.first = 'Test'
# emp_2.last = 'User'
# emp_2.email = ' Test.user@company.com'
# emp_2.pay = 60000
      

# print(emp_1.email)
# print(emp_2.email)
  
# print('{} {}'.format(emp_1.first, emp_1.last))


# Use parentesis after the fullname method or you get this
#print(emp_1.fullname)
#Output: <bound method Employee.fullname of <__main__.Employee instance at 0x102df3248>>

print(emp_2.fullname())
# Output: Test User


# We can also run this methods using the class name

#print(Employee.fullname(emp_1))
