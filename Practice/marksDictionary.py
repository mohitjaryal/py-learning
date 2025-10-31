# WAP to enter the marks of 3 subjects from user and store it in a dictionary
marks = {} # Created an empty dictionary

a = int(input("Enter marks of phy:"))
marks.update({'phy':a}) # Updating the marks dictionary 

b =int(input("Enter marks of math:")) # Updating the marks dictionary 
marks.update({'phy':b})

c = int(input("Enter marks of psychology:")) # Updating the marks dictionary 
marks.update({'phy':c})

d = int(input("Enter marks of chem:")) # Updating the marks dictionary 
marks.update({'phy':d})

print('Detailed marks :',marks) # Displaying the detailed marks