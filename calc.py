def calc(num1,num2,oper):

    try:
        if oper=='+':
                print(num1+num2)
        elif oper=='-':
                print(num1-num2)
        elif oper=='*':
                print(num1*num2)
        elif oper=='/':
                print(num1/num2)
        else:
               print("Invalid operation") 
    except:
           print("Invalid operation")
    else:
           print("successfully calculated")
    
    






num1=int(input("num1: "))
num2=int(input("num2: "))
oper=input("enter the operation want to perform('+','-','*','/'):")
calc(num1,num2,oper)


    


