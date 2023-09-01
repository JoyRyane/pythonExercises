#EXERCISE 1
monthlyExpenses = [2200,2350,2600,2130,2190]
#1. In Feb, how many dollars you spent extra compare to January?
extraFebruaryBill = monthlyExpenses[1] - monthlyExpenses[0]
print(extraFebruaryBill)

#2. Find out your total expense in first quarter (first three months) of the year.
firstQuarterExpenses = monthlyExpenses[0] + monthlyExpenses[1] +monthlyExpenses[2]
print(firstQuarterExpenses)

#3. Find out if you spent exactly 2000 dollars in any month
check = [x for x in monthlyExpenses if x == 2000]
if(len(check)>0):
    print('Month found')
else:
    print('Month not found')
#4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
monthlyExpenses.append(1980)
print(monthlyExpenses)

'''5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this'''
monthlyExpenses[3] = monthlyExpenses[3] - 200
print(monthlyExpenses[3])


#EXERCISE 2
heros=['spider man','thor','hulk','iron man','captain america']
#1. Length of the list
print(len(heros))

#2. Add 'black panther' at the end of this list
heros.append('black panther')
print(heros)

"""3. You realize that you need to add 'black panther' after 'hulk',
so remove it from the list first and then add it after 'hulk'"""
heros.pop()
print(heros)
heros.insert(3,'black panther')
print(heros)

'''4. Now you don't like thor and hulk because they get angry easily :)
So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
Do that with one line of code.'''
heros[1:3] = ['doctor strange']
print(heros)

#5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
heros.sort()
print(heros)