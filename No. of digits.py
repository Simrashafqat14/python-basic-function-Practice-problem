'''
 Write a program, which 
   ==> inputs a whole number (which is >0)
   ==> calculates the numbers of digits in a number
   ==> outputs the number of digits and the original number
'''
Number=int(input("Enter a whole number greater than 0 : "))
i=0
while(Number>0):
    i=i+1
    Number=Number//10

print(f"number of digits are: {i}")