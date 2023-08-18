Exercise: Numbers in python
            SOLUTION
#1. You have a football field that is 92 meter long and 48.8 meter wide. Find out total area using python and print it.
    length = 92
    width = 48.8
    area = length * width
    print(area)

'''2. You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar and you gave shopkeeper 20 dollar. 
    Find out using python, how many dollars is the shopkeeper going to give you back?'''
    numberOfPotatoChipsPackets = 9
    unitPrice = 1.49
    amountGiven = 20
    cost =  numberOfPotatoChipsPackets * unitPrice
    amountReturned = amountGiven - cost
    print(amountReturned,"$")

'''3. You want to replace tiles in your bathroom which is exactly square and 5.5 feet is its length. If tiles cost 500 rs per square feet, 
    how much will be the total cost to replace all tiles. Calculate and print the cost using python (Hint: Use power operator ** to find area of a square)'''
    side = 5.5
    area = side**2
    costPerSquareFeet = 500
    totalCost = area * costPerSquareFeet
    print(int(totalCost),"rs")

#4. Print binary representation of number 17
    def conversion(num):
        if num > 1:
            conversion(num // 2)
        print(num % 2, end='')

    input = int(input("Enter any decimal number: "))

    conversion(input)