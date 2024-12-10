
import time

print("Hello World\n")

print("****Welcome to the Python Banking System****\n\nFor old User it is always open\nBut, For new User you have to Register frist ")


def ito():
    #Login System
    from openpyxl import Workbook, load_workbook
    book = load_workbook("Bank Data.xlsx")
    sheet = book.active
    print("*****LoGIN pAGE ****")
    naam = str.capitalize(input("Enter Your Name :"))
    a = 1
    b = A + str(a)
    for check in naam:
        if(check in b):
            print("Your account found you can proceed...")
            pass
        a += 1
    passw = D + str(a)
    entpass = input("Enter Your Passward : ")
    if(entpass in sheet[passw].value):
        pass
    else:
        print("Your LOgin Credencials are Wrong ....\nTry again.")
        return naam #Login Done
    
    
    #What User want to check or Do 
    print("Welcome,", naam,"\nYour Login Process has been done..........")
    time.sleep(1)
    print("What service i can give you ?")
    time.sleep(0.5)

    chk = ["chk", "Check" ,"CheckBalance", "Check Balance"]
    balancecoloum = E + str(a)
    BankBalance = int(sheet[balancecoloum].value)

    Dep = ["Dep", "Deposit", "Deposit Money", "DepositMoney"]
    Cre = ["Cre", "Credit", "Credit Money" , "CreditMoney"]
    Upd = ["Update", "Upd", "Update Age"]
    agesheet = B + str(a)
    age = int(sheet[agesheet].value)

    print("Select your Prefable option\nChk = Check Balance\nDep = Deposit Money\nCre = Credit Money\nUpd = Update Your Age")
    
    bsdk = 0
    while bsdk<10:
        userinp = str.capitalize(input("Enter Your Prefable Option : "))
        if(userinp in chk ):
            print("Dear", naam ,"Your Account blanace is = $",BankBalance )
        
        if(userinp in Dep):
            depositamount = int(input("Enter Ammount you whant to Deposit :"))
            time.sleep(2)
            print("\nPlease Wait..!\nAmount is Debiting......................")
            BankBalance -= depositamount
            print("Dear", naam ,"New Upadated BANK Balnace is : ", BankBalance)
        
        
        if(userinp in Cre):
            creditamount = int(input("Enter Amount : "))
            time.sleep(2)
            print("\nPlease Wait..!\nAmount is Crediting......................")
            BankBalance += creditamount
            print("Dear", naam ,"New Upadated BANK Balnace is : ", BankBalance)
        
        
        if(userinp in Upd):
            print("Your Current age Status is : ", age )
            ageinput = int(input("Please Enter the Age You want to change : "))
            print("\n*HUMAN VERIFICATION*\nSolve tthe Below Question\nQuestion = 3 + 2")
            time.sleep(0.5)
            su = int(input("Answer : "))

            print("Plese Wait.......\nProcessing")
            if(su == 5 ):
                print("Our TEam is updating your Request..\nWait a Sec")
                time.sleep(1)
                print("Your uPDATED Age in your bank account is , ",age)
                

    



    with open("accounts.py", "r") as info:
    # created a login system 
        
        av = info.read(input("enter yout name Please : "))
        if (av in info(user1)):
            print("welcome.......")
            pass
        if(av in info(user2)):
             print("Welcome.........")
             pass
        else:
            print("Sorry But Your Name Doesnot match in our Data\nTry Again....")
            a= 2
            while a>=3 :
                return av
            a += 1
def createaccount():
    print("Welcome to the Registrration Portal.")

    with open("accounts.py", "a+") as inc :
        #Creating a registration program.
        det = input("Plese Enter your Name :")
        inc._(det)




a = str.capitalize(input("Do you have account in Python Bank (Yes/No): "))
if( a is "Yes"):
    ito()
else:
    createaccount()
