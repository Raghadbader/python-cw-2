my_name=input("your name")

my_age=input("your age")

print(f"my name is {my_name} and I am {my_age} years old")

first_number=eval(input("enter first number"))

secound_number=eval(input("enter second number"))

operation=input("enter your operation?")

if operation=="+":

    print("first_number + secound_number")
 
elif operation=="-":
   print("first_number - secound_number")

elif operation=="*":
    print("first_number * secound_number")
 
elif operation=="/":
   print("first_number/secound_number")

else:
   print("the operation is not valid")

bus_capacity=70
people_inbus =int(input("who many people are in the bus?"))
waiting=int(input("how many people are you waiting?"))
empty_seats = bus_capacity -people_inbus
if empty_seats>=waiting :
   print("join!")
else:
   print("the bus is full")



