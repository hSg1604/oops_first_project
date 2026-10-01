# #num1=23
# #num2=25
#  #def addition(num1,num2):
# #    # result=num1+num2
# #     #print(result)
# # #def GoodMorning(city="lucknow"):
# #     #print("good morning",city)


# # #GoodMorning("mathura")
# # #def odd_even(number):
# #     #if number%2==0:
# #         #print("This number is even")
# #     #else:
# #         #print("this no. is odd")

# # #odd_even(54)
# # #def multiplication(num1,num2):
# #     #result=num1*num2
# #     #return result

# # #a=multiplication(23,25)
# # #print(a)
# # #def factorial(number):
# #     #factorial=1
# #     #for n in range(1,number+1):
# #         #factorial=factorial*n

# #     #return factorial

# # #print(factorial(9))
# # #def sum1():
# #     #sum=0
# #     #for n in range(1,11):
# #        #sum=sum+n

# #     #return sum

# # #print(sum1())

# # #def sum():
# #     #number=0
# #     #for i in range(1,11):
# #         #if i%2==1:
# #          #number=number+i

# #     #return number
# # #print(sum())
# # #def good_night(state):
# #     #print("good night",state)

# # #good_night("Uttar Pradesh")
# # """
# # def sum(num):
# #      if num==0:
# #           #return 0
# #      return num+sum(num-1)
# # print(sum(9))
# # """
# # """
# # #to get element from from fibbonacci series
# # def fibbo(num):
# #     if num==0:
# #         return 0
# #     elif num==1:
# #         return 1
# #     return fibbo(num-1)+fibbo(num-2)
# # print(fibbo(9))
# # """
# # """
# # #to get fibbonacci series
# # def fibbonacci(num):
# #      if num==0:
# #           return 0
# #      elif num==1:
# #           return 1
    
# #      return fibbonacci(num-1)+fibbonacci(num-2)
# # for i in range(11):
# #      print(fibbonacci(i))
# #      """
# # """
# # #to count args
# # def count_arg(*zeeC):
# #      count_v=0
# #      for num in zeeC:
# #           count_v+=1
# #      return count_v
# # print(count_arg(12,45,284,47,939,344))
# #          """
# # """
# # n=2662
# # temp=n
# # rev=0
# # while temp>0:
# #     rem=temp%10
# #     rev=rev*10+rem
# #     temp//=10
# # if n==rev:
# #     print("palindrome")
# # else:
# #     print("not ")
# #     """
# # """
# # name="AttA"
# # name1=""
# # for i in name:
# #     name1=i+name1
# # print(name1)
# # """    
# # """
# # num =99

# # temporary= num
# # digits = len(str(num))
# # sum = 0

# # while num > 0:
# #     digit = num % 10
# #     sum += digit ** digits
# #     num //= 10

# # if sum == temporary:
# #     print("This number is an Armstrong number")
# # else:
# #     print("This no.is not an Armstrong number")
# # """
# # """

# # name="Shrestha" 
# # s=name.replace("Shrestha","varun")
# # print(s)
# # """
# # """
# # name="Lal Bahadur Shastri Jii"
# # name1=name.split()
# # print("".join(name))
# # """
# # """
# # name=" SHRESTHA  "
# # print(name.strip())
# # """
# # """
# # name="Shreshita"
# # print(name.isalpha())
# # print(name.isnumeric())
# # print(name.isalnum())
# # print(name.isspace())
# # """
# # """
# # name="Saurabh Kumar Nayak"
# # count=0
# # for i in name:
# #     if i not in "aeiou":

# #        count+=1
# # print(count)
# # """
# # """

# # name="rahul"
# # count=0
# # for i in name:
# #     if i=="h":
# #         break
# #     count+=1
# # print(count)
# # """
# # """
# # print(ord("s"))
# # """
# # """
# # name="python"
# # for i in name:
# #     result= chr(ord(i)-32)
# #     print(result,end="")
# # """
# # """
# # name="I am ravi kishan Money follows Paisan"
# # count=0
# # for i
# # """

# # """
# # nmee="i am 24"
# # for i in name:
# #         if i.isnumeric():
# #             print(i,end="")
# #             """
# # """
# # name="I am ravi kishan money follows paisan"
# # largest=""
# # current=""
# # for s in name:
# #     if s!=" ":
# #         current+=s
# #     else:
# #         if len(current)>len(largest):
# #             largest=current
# #             current=""
# #         else:
# #             current=""
# # if len(current)>len(largest):
# #     largest=current
# # print(largest)
# # """
# # """
# # list=[1,64,80,5,12,-89]
# # count=0
# # for i in list:
# #     if i%2==0:
# #         count+=i
# # print(count)
# # """
# # """
# # list3=[122,22,3,45,38]
# # largest=list3[0]
# # second=list3[1]
# # for i in list3:
# #     if i>largest:
# #         second=largest
# #         largest=i
# #         i=0
# #     elif i>second and i!=largest:
# #         second=i
# # print(second)
# # """
# # """
# # section=[12,34,70,2,8,33,67]
# # numbers=[x*10 for x in section if x%2==0]
# # print(numbers)
# # number=[x**2 for x in section if x%2==1]
# # print(number)
# # """ 
# # """
# # section=[12,34,70,2,8,33,67]
# # for x in section:
# #     if x%2==0:
# #         print((x*10))
# # """
# # """
# # none=[12.89,88,72,92]
# # num=[x if x%2==1 else"Nonu hua hua" for x in none]
# # print(num)
# # """
# # """
# # number=[25,62,43,47,77]
# # num=[x if x%2==0 else x*4 for x in number]
# # print(num)
# # """
# # """
# # list1=[[12,24,36],[17,51,85],[69,115,161]]
# # print(list1[0])
# # """
# # """
# # name=["Shresth","Mahima","Hanshita","Aryan","Gauri"]
# # print(sorted(name))
# # """
# # """
# # a=0
# # print(bool(a))
# # a=1
# # print(bool(a))
# # a=[]
# # print(bool(a)+bool(1))
# # """
# # """
# # a=[0]
# # print(bool(a)+bool(1))
# # x=""
# # if x:
# #     print("x")
# # else:
# #     print("y")
# #     """
# # """
# # x=None
# # if x:
# #     print("XMas")
# # else:
# #     print("Mera Yashu Yashu")
# # """
# # """
# # x=[1,2,7,3,4,6,5,9,10]
# # expect=0
# # real=0
# # for i in range(1,11):
# #     expect+=i
# # for y in x:
# #     real+=y
# # print(expect-real)
# # """
# # """
# # days=("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday",)
# # print(days.index("Wednesday"))
# # print(days.count("Saturday"))
# # b,*a=days
# # print(a)
# # """
# # """
# # num=(1,2,34,66,75,35)
# # count=0
# # for i in num:
# #     count+=i
# #     print(count)
# #     """
# # """
# # number=(4,7,8,1,2)
# # target=10
# # for i,j in number:
# #         for j in number:
# #          if i+j==target:
# #             print(i)
# # """
# # """
# # num=[23,34,45,56,67,78,89,90]
# # for i in range(8//2):
# #     num[i],num[len(num)-1-i]=num[len(num)-1-i],num[i]
# # print(num)
# # """
# # """
# # set={1,23,24,19,18,15}
# # set.add([28,32,47,55])
# # print(set)
# # """
# # """
# # num={1,23,44,"56,6,7",8}
# # num.discard(75)
# # num.remove(57)
# # print(num)
# # """
# # """
# # setting={23,34,45,56,67,78,89,90}
# # setting.pop()
# # print(setting)
# # """
# # """
# # setting={23,27,65,54}
# # del setting
# # print(setting)
# # """
# # """
# # set1={12,23,24,43,46}
# # set2={12,46,45,57,69}
# # print(set1&(set2))
# # print(set1|(set2))
# # print(set1.difference(set2))
# # print(set1.symmetric_difference(set2))
# # """
# # """
# # a={12,34,65,67,76}
# # b={12,34,65,67,76,84,99}
# # print(a.issubset(b))
# # print(a.issuperset(b))
# # print(a.isdisjoint(b))
# # """
# # """
# # dictionary={"name":"rishabh",
# #             "daam":"100000000"}
# # dictionary["roll_number"]=345
# # dictionary.update({"class":11,"stream":"PCM"})
# # for i in dictionary:
# #     print(i,dictionary[i])
# # print(dictionary.keys())
# # """
# # """
# # dictionary={"name":"rishabh",
# #             "daam":"100000000"}
# # dictionary["roll_number"]=345
# # dictionary.update({"class":11,"stream":"PCM"})
# # for i in dictionary:
# #     print(dictionary.values())
# # """
# # """
# # dictionary={"name":"rishabh",
# #             "daam":"100000000"}
# # for i in dictionary.values():
# #     for j in dictionary.keys():
# #         print(i,j)
# # """
# # """
# # dict1={"naam":"amendra","class":"11","subject":"biology"}
# # print(dict1.popitem())
# # print((dict1))
# # """
# # """
# # name={"stats1":{"student":"shrestha"},"stats2":{"class":"14"}}
# # print(name["stats2"])
# # """
# # """
# # roll_num=[1,2,3,4,5,6]
# # name=["rahul","gaurav","ranu","harsh","nandu","me been"]
# # dict1={i:y for i,y in zip(roll_num,name)}
# # print(dict1)
# # """
# # """
# # name=["rahul","gaurav","ranu","harsh","nandu","me been"]
# # print(dict.fromkeys(name,"Chutki"))
# # """
# # """
# # naaam=["12","34","43","15","7"]
# # #map(function,iterable)
# # int_num=map(int,naaam)
# # #int_num=map(lambda x:int(x)*2,naaam)
# # #print(list(int_num))
# # #even=list(filter(lambda x:x%2==0,int_num))
# # #print(even)
# # from functools import reduce
# # sum_list=reduce(lambda a,b:a+b,int_num)
# # print(sum_list)
# # """
# # """
# # square=lambda x:x*x
# # print(square(29))
# # """
# # """
# # dict1={"shrestha":95,"sakshi":89,"mahima":75,"hanshita":96,"aryan":65,"arun":33}
# # marks=sorted(dict1.items(), key=lambda x:x[1], reverse=True)
# # print(marks)
# # """
# # """

# # dict1={"shrestha":95,"sakshi":89,"mahima":75,"hanshita":96,"aryan":65,"arun":33}
# # #marks=sorted(dict1.items(), key=lambda)
# # #num=list(filter(lambda x:x[1]>50,dict1.items()))
# # print(num)
# # """
# # """
# # dict1=[12,23,54,44,123]
# # print(list(map(lambda x:"even" if x%2==0 else"odd",dict1)))
# # """
# # class Student:
# #    school_name="aps"
# # #Constructor
# #    def __init__(self,name,roll_no,class_name,age,marks):

# #       #Attributes
# #       self.name=name
# #       self.roll_no=roll_no
# #       self.class_name=class_name
# #       self.age=age
# #       self.marks=marks
# # s1=Student("Shrestha",12,"12th",20,75)
# # s2=Student("Hanshita",8,"12th",18,80)
# # s3=Student("Mahima",13,"12th",19,87)
# # Student.school_name="CMS"
# # print(s2.school_name)

# # class Office:
# #    Office_name="Aditya Birla"
# #    def __init__(self,Employee,salary,Department,Age,City):
# #       self.Employee=Employee
# #       self.salary=salary
# #       self.Department=Department
# #       self.Age=Age
# #       self.City=City
# #       #method1
# #    def display_details(self):
# #          print("Employee",self.Employee)
# #          print("salary",self.salary)
# #          print("Department",self.Department)
# #          print("Age",self.Age)
# #          print("City",self.City)
# #          #method2
# #    def check_salary(self):
# #        if self.salary>=30000:
# #            print("Result:Good salary")
# #        else:
# #            print("Result:Average salary")

# # s1=Office("Mahima",26700,"IT",19,"Mathura")
# # s2=Office("Apeksha",35000,"Hr",25,"Lucknow")
# # s3=Office("Riddhima",30000,"Finance",30,"Gujrat")
# # s4=Office("Raunak",28500,"Sales",35,"Allahabad")
# # s5=Office("Purav",30500,"Market",28,"Gurgaon")
# # s3.check_salary()
# # s5.display_details()
# class ATM:
#     def __init__(self,Account_no,Pin,Balance,Ifsc):
#         self.Account_no=Account_no
#         self.__Pin=Pin
#         self.__Balance=Balance
#         self.Ifscfsc
#     def bank_balance(self):
#         return f"Your balance is {self.__Balance}"
#     def deposit(self,value):
#         self.__Balance=self.__Balance+value
#         return self.__Balance
#     def withdraw(self,value):
#         self.__Balance=self.__Balance-value
#         return self.__Balance
# s=ATM(8960841350,88742,87500,"sbjc2ntn")
# print(s.bank_balance())   
# print(s.withdraw(3500))

# class Student:
#      def __init__(self,Name,Marks):
#          self.Name=Name
#          self.__Marks=Marks
#      def Marks(self,value):
#          self.__Marks+=value
#          return f"marks updated to{self.__Marks}"
# s1=Student("Shrestha",55)
# print(s1.update_Marks(30))

# class Office:
#     def __init__(self,name,department,salary):
#         self.name=name
#         self.department=department
#         self.__salary=salary
#     @property
#     def SalaryS(self):
#         return f"Salary is {self.__salary}"
#     @SalaryS.setter
#     def SalaryS(self,value):
#         self.__salary=self.__salary+value
#         return f"Updated salary{self.__salary}"
# s1=Office("hanshita","IT",35000)
# print(s1.SalaryS)
# s1.SalaryS=9000
# print(s1.SalaryS)
# class Animal:
#     def __init__(self,name,age,color):
#         self.name=name
#         self.age=age
#         self.color=color
# class Dog(Animal):
#     def __init__(self, name, age, color,breed):
#         super().__init__(name,age,color)
#         self.breed=breed

# d=Dog("Dusky",15,"Brown","Pug")
# print(d.breed)
# print(d.name)
# print(d.age)
# print(d.color)
# class Animal:
#     def eat(self):
#         print("Eating")
# class Mammal(Animal):
#     def walk(self):
#         print("Walking")
# class Dog(Mammal):
#     def bark(self):
#         print("Barking")
# d=Dog()
# print(d.walk)
# class Mother:
#     def mataji(self):
#         print("nana ki saari propert apni")
# class Father:
#     def papaji(self):
#         print("dada ki property bhi apni")
# class ME(Father,Mother):
#     def meri(self):
#         print("dadu nanu ki property se Ameer")
# s=ME()
# s.mataji()
# class Father:
#     def __init__(self,land):
#         self.land=land
#     def papaji(self):
#         print("papa di property")
# class Mother:
#     def __init__(self,Jewellery):
#         self.Jewellery=Jewellery
#     def mataji(self):
#         print("mataji di property")
# class Son(Father,Mother):
#     def __init__(self, land,Jewellery,car,house):
#         Father.__init__(self,land)
#         Mother.__init__(self,Jewellery)
#         self.car=car
#         self.house=house
# my=Son(3,"Necklace","Tata Sierra","2BHk Flat")
# print(my.land)
# class Grandfather:
#     def __init__(self,land):
#         self.land=land
# class Father(Grandfather):
#     def __init__(self, land):
#         super().__init__(land)
# class son(Grandfather):
#     def __init__(self, land):
#         super().__init__(land)
# s=son("Gaon ka Makaan")
# print(s.land)
# class Payment:
#     def pay(self):
#         print("Payment in progress")
# class COD(Payment):
#     def pay(self):
#         print("Payment through Cash")
# class Online(Payment):
#     def pay(self):
#       print("Paid Online")
# s=Online()
# s.pay()
# class Email:
#     def send(self):
#         print("Notify through Email")
# class Whatsapp:
#     def send(self):
#         print("Notify through whatsapp")
# class Sms:
#     def send(self):
#         print("Notify through Sms")

# notify=[Email(),Whatsapp(),Sms()]
# def make_notification(notify):
#     for i in notify:
#         i.send()
# make_notification(notify)
# from abc import ABC, abstractmethod
# class Payment(ABC):
#     @abstractmethod
#     def pay(self):
#         print("Payment in progress")
# class PhonePe(Payment):
#     def pay(self):
#         print("Pay through PhonePe")
# class BhimUPI(Payment):
#     def pay(self):
#         print("Pay through BhimUPI")
# class GooglePay(Payment):
#     def pay(self):
#         print("Pay through GooglePay")
#     def payment(self):
#         print("Payment Done")
# c=GooglePay()
# print(c.payment())
# class Office:
#     Office_name="TATA Motors"
#     def __init__(self,Employee,Salary,age):
#         self.Employee=Employee
#         self.Salary=Salary
#         self.age=age
#     @classmethod
#     def Change_nameofOffice(cls,change_name):
#         cls.Office_name=change_name
#         return cls.Office_name
# print(Office.Change_nameofOffice("Mahesh dalla"))
# print(Office.Office_name)

# class Salary:
#      @staticmethod
#      def format_emp_id(number):
#         return f"emp_id {number:1>3d}"

# print(Salary.format_emp_id(34))
# class Employee:
#     def __init__(self,value):
#         self.value=value
#     def __str__(self):
#         return f"Employee name is {self.value}"
#     def __len__(self):
#         return len(self.value)
# s=Employee("Saurabh")
# print(len(s))
# class Employee:
#     def __init__(self,value):
#         self.value=value
#     def __add__(self, other):
#         result=self.value+other.value
#         return result
# s=Employee(34)
# r=Employee(74)
# print(r+s)
# class School:
#     School_name="Bright Start Convent"
#     def __init__(self,student,roll_no,std,age,marks):
#         self.student=student
#         self.roll_no=roll_no
#         self.std=std
#         self.age=age
#         self.marks=marks
#     def display_info(self):
#         print("student",self.student)
#         print("Roll_no",self.roll_no)
#         print("Std",self.std)
#         print("age",self.age)
#         print("marks",self.marks)
#         print(self.School_name)
#     def add_marks(self,subject,add_marks):
#         self.marks[subject]=self.marks[subject]+add_marks
#         return self.marks

# s=School("Shrestha",12,"XII",18,{"Maths":67,"Science":78,"English":72})
# s1=School("Hanshita",9,"XI",16,{"Maths":70,"Science":84,"English":90})
# s2=School("Mahima",11,"XII",18,{"Maths":80,"Science":82,"English":92})
# print(s1.add_marks("Maths",2))
# class Product:
#     def __init__(self,Prooduct_id,name,stock,price):
#         self.Product_id=Prooduct_id
#         self.name=name
#         self.stock=stock
#         self.price=price
#     def display_Product_info(self):
#         print("Product_id",self.Product_id)
#         print("name",self.name)
#         print("stock",self.stock)
#         print("price",self.price)
#     def P_is_available(self):
#         if self.stock>0:
#             print("Product is available right now")
#         else:
#             print("Better luck next time")
#     def restocking(self,value):
#         new_stock=self.stock+value
#         return new_stock
#     def reduce(self,value):
#         reduce=self.stock-value
#         return reduce
# s=Product(101,"Cosmetics",700,350)
# t=Product(111,"Appliances",500,650)
# u=Product(123,"Utensils",900,250)
# u.display_Product_info()
# s.P_is_available()
# print(t.restocking(50))
# print(s.reduce(90))
# class CartItem:
#     def __init__(self,product,id,price,quantity,usagein):
#         self.product=product
#         self.id=id
#         self.price=price
#         self.quantity=quantity
#         self.usage=usagein
#     def display(self):
#         print("product",self.product)
#         print("id",self.id)
#         print("price",self.price)
#         print("quantity",self.quantity)
#         print("usage",self.usage)
#     def subtotal(self):
#         subtotal=self.price*self.quantity
#         return subtotal
#     def quantity_inc(self,value):
#         inc=self.quantity+value
#         return inc
# s1=CartItem("Perfume",102,250,4,"For fragnance")
# s2=CartItem("Goggles",120,400,1,"Style")
# s3=CartItem("Watch",321,3000,2,"show time")
# s3.display()
# print(s2.subtotal())
# print(s3.quantity_inc(4))
# class ShoppingCart:
#     def __init__(self,user_id,discount_code):
#         self.user_id=user_id
#         self.items={}
#         self.discount=discount_code
#     def display_Cart(self):
#         print("user_id",self.user_id)
#         print("items",self.items)
#         print("Discount",self.discount)
#     def add_items(self,product,quantity):
#         self.items[product]=quantity
#         return self.items
#     def update(self,quantity,product):
#         self.items[product]=quantity
#         print(f"Updated quantity to{quantity}")
#     def remove_from_cart(self,product):
#         if product in self.items:
#             remove=self.items.pop(product)
#             print(f"items '{product}' removed from Cart")
#         else:
#             print("Items not found")
#     def clearing_Cart(self):
#         self.items.clear
#         print("Cart cleaned successfully")
# w=ShoppingCart("qweew",20)
# w.add_items(s2.product,s2.quantity)
# w.display_Cart()
# x=ShoppingCart("eddff",35)
# x.add_items(s3.product,s3.quantity)
# x.display_Cart()
# x.update(3,"Watch")
# w.remove_from_cart("Goggles")
# x.clearing_Cart()
# class Customer:
#     def __init__(self,customer_id,Customer_name,phoneNumber):
#         self.Customer_id=customer_id
#         self.Customer_name=Customer_name
#         self.Contact_no=phoneNumber
#         self.items=ShoppingCart(s,t)
#     def add_items(self, product, quantity):
#         return super().add_items(product, quantity)

#     def display_Custom_info(self):
#         print("Customer_id",self.Customer_id)
#         print("Customer_name",self.Customer_name)
#         print("Contact_no",self.Contact_no)
#         print("Shopping_cart",self.items)
# A=Customer("C101","shrestha",8725289012)
# print(A.items.add_items(s1.product,s1.quantity))
# import time
# def addd_num(func):
#     def wrapper(*args):
#         print("Takle ke Jeb m Kanghi")
#         time.sleep(1)
#         print(func(*args))
#     return wrapper

# @addd_num
# def multiply(a,b):
#     return a*b

# multiply(23,27)
import streamlit as st

# ==========================================
# 1. CLASS DEFINITIONS (Refactored)
# ==========================================

class Product:
    def __init__(self, product_id, name, stock, price):
        self.product_id = product_id
        self.name = name
        self.stock = stock
        self.price = price

    def is_available(self):
        return self.stock > 0

    def restocking(self, value):
        self.stock += value

    def reduce_stock(self, value):
        if value <= self.stock:
            self.stock -= value
            return True
        return False


class CartItem:
    def __init__(self, product: Product, quantity: int, usage: str = ""):
        self.product = product
        self.quantity = quantity
        self.usage = usage

    def subtotal(self):
        return self.product.price * self.quantity


class ShoppingCart:
    def __init__(self, user_id, discount_percent=0):
        self.user_id = user_id
        self.items = {}  # key: product_id, value: CartItem
        self.discount_percent = discount_percent

    def add_item(self, product: Product, quantity: int, usage: str = ""):
        if product.product_id in self.items:
            self.items[product.product_id].quantity += quantity
        else:
            self.items[product.product_id] = CartItem(product, quantity, usage)

    def update_quantity(self, product_id: int, quantity: int):
        if product_id in self.items:
            if quantity > 0:
                self.items[product_id].quantity = quantity
            else:
                self.remove_item(product_id)

    def remove_item(self, product_id: int):
        if product_id in self.items:
            del self.items[product_id]

    def clear_cart(self):
        self.items.clear()

    def get_total(self):
        subtotal = sum(item.subtotal() for item in self.items.values())
        discount_amount = (subtotal * self.discount_percent) / 100
        return subtotal - discount_amount


class Customer:
    def __init__(self, customer_id, name, phone_number, discount_code=10):
        self.customer_id = customer_id
        self.name = name
        self.phone_number = phone_number
        self.cart = ShoppingCart(customer_id, discount_percent=discount_code)


# ==========================================
# 2. STREAMLIT SESSION STATE INITIALIZATION
# ==========================================

st.set_page_config(page_title="Streamlit Store", page_icon="🛍️", layout="wide")

# Initialize default products in session state so stock updates persist
if "inventory" not in st.session_state:
    st.session_state.inventory = {
        101: Product(101, "Cosmetics", 700, 350),
        111: Product(111, "Appliances", 500, 650),
        123: Product(123, "Utensils", 900, 250),
        102: Product(102, "Perfume", 50, 250),
        120: Product(120, "Goggles", 30, 400),
        321: Product(321, "Watch", 15, 3000),
    }

# Initialize Customer and Shopping Cart
if "customer" not in st.session_state:
    st.session_state.customer = Customer("C101", "Shrestha", "8725289012", discount_code=10)


# ==========================================
# 3. USER INTERFACE (UI)
# ==========================================

st.title("🛍️ E-Commerce Store & Cart Management")

# Sidebar: Customer Profile & Store Info
with st.sidebar:
    st.header("👤 Customer Details")
    customer = st.session_state.customer
    st.write(f"**ID:** {customer.customer_id}")
    st.write(f"**Name:** {customer.name}")
    st.write(f"**Phone:** {customer.phone_number}")
    st.write(f"**Discount Active:** {customer.cart.discount_percent}%")
    st.divider()

    st.header("📦 Inventory Restock (Admin)")
    restock_pid = st.selectbox("Select Product to Restock", list(st.session_state.inventory.keys()), format_func=lambda pid: st.session_state.inventory[pid].name)
    restock_qty = st.number_input("Add Stock Quantity", min_value=1, value=50, step=10)
    if st.button("Restock Product"):
        st.session_state.inventory[restock_pid].restocking(restock_qty)
        st.success(f"Added {restock_qty} units to {st.session_state.inventory[restock_pid].name}!")
        st.rerun()

# Main Layout Tabs
tab1, tab2 = st.tabs(["🛒 Browse Products", "🛍️ View Shopping Cart"])

# --- TAB 1: BROWSE PRODUCTS ---
with tab1:
    st.subheader("Available Products")
    cols = st.columns(3)

    for idx, (pid, product) in enumerate(st.session_state.inventory.items()):
        col = cols[idx % 3]
        with col:
            st.markdown(f"### {product.name}")
            st.write(f"**Product ID:** `{product.product_id}`")
            st.write(f"**Price:** ₹{product.price}")
            st.write(f"**Stock:** {product.stock} units")

            if product.is_available():
                st.caption("🟢 In Stock")
                qty = st.number_input(f"Quantity", min_value=1, max_value=product.stock, value=1, key=f"qty_{pid}")
                usage = st.text_input("Usage Note (optional)", key=f"usage_{pid}")
                
                if st.button("Add to Cart", key=f"add_{pid}"):
                    st.session_state.customer.cart.add_item(product, qty, usage)
                    st.toast(f"Added {qty} x {product.name} to cart!", icon="✅")
            else:
                st.caption("🔴 Better luck next time (Out of Stock)")
                st.button("Add to Cart", key=f"add_{pid}", disabled=True)

# --- TAB 2: SHOPPING CART ---
with tab2:
    st.subheader("Your Cart")
    cart = st.session_state.customer.cart

    if not cart.items:
        st.info("Your shopping cart is empty!")
    else:
        # Cart Items Table Header
        header_col1, header_col2, header_col3, header_col4, header_col5 = st.columns([2, 1, 1, 1, 1])
        header_col1.write("**Product**")
        header_col2.write("**Price**")
        header_col3.write("**Quantity**")
        header_col4.write("**Subtotal**")
        header_col5.write("**Action**")

        st.divider()

        # Render Cart Items
        for pid, item in list(cart.items.items()):
            col1, col2, col3, col4, col5 = st.columns([2, 1, 1, 1, 1])
            
            col1.write(f"**{item.product.name}**\n\n_{item.usage}_")
            col2.write(f"₹{item.product.price}")
            
            # Quantity Update
            new_qty = col3.number_input(
                "Qty", 
                min_value=1, 
                max_value=item.product.stock, 
                value=item.quantity, 
                key=f"cart_qty_{pid}",
                label_visibility="collapsed"
            )
            if new_qty != item.quantity:
                cart.update_quantity(pid, new_qty)
                st.rerun()

            col4.write(f"₹{item.subtotal()}")

            # Remove Item
            if col5.button("🗑️", key=f"remove_{pid}"):
                cart.remove_item(pid)
                st.toast(f"Removed {item.product.name} from cart.")
                st.rerun()

        st.divider()

        # Pricing Summary
        col_summary1, col_summary2 = st.columns([2, 1])
        
        with col_summary1:
            if st.button("Clear Cart"):
                cart.clear_cart()
                st.rerun()

        with col_summary2:
            raw_subtotal = sum(i.subtotal() for i in cart.items.values())
            discount_val = (raw_subtotal * cart.discount_percent) / 100
            total = cart.get_total()

            st.write(f"**Subtotal:** ₹{raw_subtotal}")
            st.write(f"**Discount ({cart.discount_percent}%):** -₹{discount_val:.2f}")
            st.markdown(f"### **Total:** ₹{total:.2f}")

            if st.button("Proceed to Checkout", type="primary"):
                # Reduce stock in inventory upon purchase
                success = True
                for item in cart.items.values():
                    if not item.product.reduce_stock(item.quantity):
                        st.error(f"Not enough stock for {item.product.name}!")
                        success = False
                        break
                
                if success:
                    cart.clear_cart()
                    st.balloons()
                    st.success("Order placed successfully! Thank you for shopping with us.")