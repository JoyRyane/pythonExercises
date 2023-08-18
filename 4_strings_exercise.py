Exercise: String in Python
#1. Create 3 variables to store street, city and country, now create address variable to store entire address. Use two ways of creating this variable, one using + operator and the other using f-string. Now Print the address in such a way that the street, city and country prints in a separate line
    street = "Avenue"
    city = "Johannesburg"
    country = "South Africa"
    address1 = street+","+city+","+country
    address2 = f"{street},{city},{country}"
    print(address1)
    print(address2)
'''2. Create a variable to store the string "Earth revolves around the sun"
    i. Print "revolves" using slice operator
    ii. Print "sun" using negative index'''
    
   txt = "Earth revolves around the sun"
   result = slice(6,14)
   print(txt[result])
#3. Create two variables to store how many fruits and vegetables you eat in a day. Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat everyday. Use python f string for this.
    fruits = 5
    veggies = 2
    txt = f"I eat {veggies} veggies and {fruits} fruits daily"
    print(txt)
#4. I have a string variable called s='maine 200 banana khaye'. This of course is a wrong statement, the correct statement is 'maine 10 samosa khaye'. Replace incorrect words in original strong with new ones and print the new string. Also try to do this in one line.
    s='maine 200 banana khaye'
    txt = s.replace("200","10")
    result = txt.replace("banana","samosa")
    print(result)
