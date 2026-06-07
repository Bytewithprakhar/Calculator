print('Welcome to basic calculator :-)')
A=float(input('Enter a number = '))
print("Enter a positive and even number for '+', for example '2'.")
print("Enter a negative and even number for '−', for example '-2'.")
print("Enter a positive and odd number for '÷', for example '1'.")
print("Enter a negative and odd number for '×', for example '-1'.")
print("Don't enter 0, as it will give zero error")
B=int(input('Your desired operation = '))
C=float(input('Enter another number = '))
E=(B/((B**2)**(1/2)))+B%2
NUMBER=(2-(((E)**2)**(1/2)))*((((E)**2)**(1/2))*A+C*(E))+(1-(((E)**2)**(1/2)))*((2-E)/2)*(A*C)+(E/2)*(-1+(((E)**2)**(1/2)))*(A*(1/C))                                                                                                                   
print('Value = ',NUMBER)
print('For more calculations please restart the program. ')
print('Thanks')

        
