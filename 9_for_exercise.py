#Exercise: Python for loop
# 1. After flipping a coin 10 times you got this result,

#result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
#Using for loop figure out how many times you got heads
METHOD 1

i = 0
for x in result:
    if x == "heads":
        i+=1
    print(i)

METHOD 2

for x in result:
   number = result.count("heads")
   print(number)

# 2. Print square of all numbers between 1 to 10 except even numbers
for number in range(1,10):
    if number%2 == 1:
        number = number**2
    else:
        continue
    print(number)

# 3. Your monthly expense list (from Jan to May) looks like this,
expense_list = [2340, 2500, 2100, 3100, 2980]
#Write a program that asks you to enter an expense amount and program should tell you in which month that expense occurred. If expense is not found then it should print that as well.

expense_list = [2340, 2500, 2100, 3100, 2980]
amount = int(input("Enter an amount\n"))
for x in expense_list:
    if amount in expense_list:
        print(str(amount),"found in the list")
    else:
        print(str(amount), "not found")

# 4. Lets say you are running a 5 km race. Write a program that,

# i. Upon completing each 1 km asks you "are you tired?"
# ii. If you reply "yes" then it should break and print "you didn't finish the race"
# iii. If you reply "no" then it should continue and ask "are you tired" on every km
# iv. If you finish all 5 km then it should print congratulations message

for distance in range(1,6):
        if distance <5:
            print("You have covered",str(distance),"km")
            response = input("Are you tired?(yes/no)\n")
            if response == "yes":
                print("You have not finished the race")
                break
            elif response == "no":
                continue
        if distance == 5:
            print("Congratulation! You have completed the race")

# 5. Write a program that prints following shape
''' *
    **
    ***
    ****
    *****'''
for exp in range(1,6):
    print('*'*exp)