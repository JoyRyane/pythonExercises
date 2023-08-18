Exercise: Python Variables

			SOLUTION
    #1. Create a variable called break and assign it a value 5. See what happens and find out the reason behind the behavior that you see. 
    break = 5
    #It returns an error because break is a python keyword and cannot be used as a variable name.
    
    #2. Create two variables. One to store your birth year and another one to store current year. Now calculate your age using these two variables 
    yearOfBirth = 2000
    currentYear = 2023
    age = currentYear - yearOfBirth
    print(age)
    
   #3. Store your first, middle and last name in three different variables and then print your full name using these variables 
   firstName   = "Gamuah"
   middleName  = "Ryane"
   lastName    = "Joy"
   fullName    = firstName + " " + middleName + " " + lastName
   print(fullName)
   
   #4. Answer which of these are invalid variable names: _nation 1record record1 record_one record-one record^one continue 
   """1record,record-one,record^one and continue are invalid because python variables must begin with a letter or an underscore, 
   can only contein alpha-numeric characters and underscores. and continue is a keyword"""