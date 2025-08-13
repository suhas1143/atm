bal=10000
print("welcom to atm")
input("insert card")
pin=input("enter pin:")
if pin =="1234":
    print("pin accepted")
print("1.withdraw\n2.deposit\n3.balance")
opt=input("Select option:")
if opt=="1":
    amt=int(input("enter amount to withdrawl"))
    if amt <= bal:
        bal-=amt
        print("please collect the cash")
        if input("see balance ? (yes/no):").lower()=="yes":
            print("balance is ",bal)
        else:
            print("insufficient balance")
elif opt=="2":
    bal += int(input("enter amount to deposit:"))
    print("deposit successful.balance is", bal)
elif opt==3:
    print("balance is",bal)
    
print("thank u")
            
            
            
            