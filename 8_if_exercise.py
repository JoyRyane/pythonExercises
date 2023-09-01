#1. Using following list of cities per country
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

#i. Write a program that asks user to enter a city name and it should tell which country the city belongs to

input = input("Enter the name of a city\n")
city = input.lower() 
if city in india:
    print(str(input)+" "+"is a city in India" )
elif city in pakistan:
    print(str(input)+" "+"is a city in pakistan")
elif city in bangladesh:
    print(str(input)+" "+"is a city in bangladesh")
else:
    print(str(input)+" "+"is not a city in India, pakistan or bangladesh")



'''ii. Write a program that asks user to enter two cities and it tells you if they both 
are in same country or not. For example if I enter mumbai and chennai, it will print 
"Both cities are in India" but if I enter mumbai and dhaka it should print "They don't 
belong to same country"'''

#input1,input2 = input("Enter two cities separated by commas\n").split(",")
input1 = input("Enter the first city\n")
input2 = input("Enter the second city\n")
city1 = input1.lower()
city2 = input2.lower()
if city1 in india and city2 in india:
    print("Both are cities in India" )
elif city1 in pakistan and city2 in pakistan:
    print("Both are cities in pakistan")
elif city1 in bangladesh and city2 in bangladesh:
    print("Both are cities in bangladesh")
else:
    print("They don't belong to the same country")

#2. Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.

#i. Ask user to enter his fasting sugar level
sugar_level = int(input("Enter your sugar level\n"))
#ii. If it is below 80 to 100 range then print that sugar is low
if sugar_level < 80:
    print("The sugar level is low")
#iii. If it is above 100 then print that it is high otherwise print that it is normal
elif sugar_level > 100:
    print("Sugar level is higher than normal")
else:
    print("Sugar level is normal")
    