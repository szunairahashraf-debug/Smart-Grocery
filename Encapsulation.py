#Question
class Person:
    def __init__(self, name):
        self.__name = name  # Private attribute

    # Getter method
    def get_name(self):
        return self.__name

    # Setter method
    def set_name(self, new_name):
        self.__name = new_name

user = Person("Alice")
print(user.get_name()) # Output: Alice


#📝 Practice Question
#Create a Python class called BankAccount with the following requirements:

#Private attribute: __balance (initially set to 0).

#Getter method: get_balance() → returns the current balance.

#Setter method: set_balance(amount) → updates the balance, but only if amount is non-negative. If a negative value is passed, print "Invalid balance amount".

#Add a method deposit(amount) that increases the balance (only if amount > 0).

#Add a method withdraw(amount) that decreases the balance (only if amount <= current balance).

#Finally, write a short script to:

#Create an object of BankAccount.

#Try setting the balance to a negative number (to test validation).

#Deposit some money.

#Withdraw some money.

#Print the final balance using the getter.



#output:


#Invalid balance amount
#Balance after deposit: 500
#Balance after withdrawal: 200
#Final balance: 200


#Question 4
class BankAccount:
    def __init__(self):
        self.__balance = 0   # private attribute

    # getter method
    def get_balance(self):
        return self.__balance

    # setter method with validation
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid balance amount")

    # deposit method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive")

    # withdraw method
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

account = BankAccount()

account.set_balance(-100)   # negative balance test
account.deposit(500)        # deposit money
account.withdraw(200)       # withdraw money

print("Final Balance:", account.get_balance())


#Question 5
class Student:
  def __init__(self, name):
    self.name = name
    self.__grade = 0

def set_grade(self, grade):
    if 0 <= grade <= 100:
      self.__grade = grade
    else:
      print("Grade must be between 0 and 100")

def get_grade(self):
    return self.__grade

def get_status(self):
    if self.__grade >= 60:
      return "Passed"
    else:
      return "Failed"

student = Student("Emil")
student.set_grade(85)
print(student.get_grade())
print(student.get_status())
