#1) მომხმარებელს შემოატანინეთ 4 სხავდასხვა რიცხვი და ამ ოთხივე რიცხვზე მოახდინეთ არითმეტიკური ოპერაციები. +,-,*,//,**
#ცვლადები
num1 =int(input('enter first num: '))
num2 = int(input('enter second num: '))
num3 = int(input('enter third num: '))
num4 = int(input('enter fourth num: '))
#მაგალითები

print(num1 + num2 + num3 + num4)
print(num1 - num2 - num3 - num4)
print(num1 * num2 * num3 * num4)
print(num1 // num2 // num3 // num4)
print(num1 ** num2 ** num3 ** num4)
#2) დაწერეთ პროგრამა სადაც შემოიტანთ თქვენი ოჯახის წევრების ასაკს და გამოიტანეთ ის თუ რამდენი წლის იქნებიან 20 წლის შემდეგ.
name = input("your parents names:")
lastname = input("your parents lastnames:")
age = input("your parents age:")
job = input("your parents job:")

num1 = 20



#3) შექმენით ცვლადები სადაც შეინახავთ თქვენს თავზე ინფორმაციას(სახელი, გვარი, ასაკი, ქვეყანა, ქალაქი, საყვარელი ფერი, საყვარელი მანქანა, საყვარელი საჭმელი, საყვარელი სპორტი და ა.შ)შემდეგ შემოტანილი მნიშვნელობებით ააწყვეტ ერთი დიდი წინადადება.
myname = 'nika'
mylastname = 'mikeladze'
myage = '14 years old'
myjob = 'student'


print(myname)
print(mylastname)
print(myage)
print(myjob)

print(myname, mylastname, myage, myjob)

name = input('enter your name: ')
print("happy birthday, wish you all the best", name + "!")