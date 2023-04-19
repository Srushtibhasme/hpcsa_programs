#create a game for  FIZZ BUZZ and keeping playing with the user untill the user chooses to skip the game

'''def fuzz_buzz():
    print("i am playing fizz buzz game")


a=int(input("enter the number"))
if(a%5==0):
    print("fizz")
elif (a%3==0):
    print("buzz")
else:
    print("invalid")


choice = 'Y'
while(choice == 'Y' or choice == 'y'):
    fuzz_buzz()
    choice = input("to continue don't press Y:")'''




#addition/squaring/exponenation should be done as part of single function named "my_calculator"

'''first_num = int(input("enter the number:"))
second_num = int(input("enter the number:"))
returned_value = (first_num+second_num)
print("answer:",returned_value)

returned_value = (first_num*first_num)
print("answer:",returned_value)

returned_value = (first_num*second_num)
print("answer:",returned_value)'''

#calculator in function



while(1):
    first_num = int(input("enter the number:"))
    second_num = int(input("enter the number:"))
    print("Enter your choice: *,/,+,")
    #choice='+','*','/'
    choice= input("enter the choice:") 
 
    if(choice == '+'):
        ans = first_num+second_num
        print("add:",ans)
    
    elif(choice == '*'):
        ans = first_num*first_num
        print("square:",ans)
    
    elif(choice == '/'):
        ans = first_num/second_num
        print("divide",ans)

