from datetime import date
# method today() shows the today's date
today=date.today()
Str_today=str(today)
today_year=Str_today[0:4]
int_today_year=int(today_year)
today_mounth=Str_today[5:7]
int_today_mounth=int(today_mounth)
import random

List_Id_Number_Account_Holders=[];List_Name_Account_Holders=[];List_Balence_Account=[];List_Account_Numbers=[];List_Card=[];List_CVV=[];List_Exp_Year=[];List_Exp_Mounth=[];List_Cell_No=[]
d={"Name":List_Name_Account_Holders,"Account No":List_Account_Numbers,"Account":List_Balence_Account,"Card No":List_Card,"Exp Year":List_Exp_Year,"Exp Mounth":List_Exp_Mounth,"Cell Number":List_Cell_No}
def CreateAccount(acname,idnum,cell_no):
    if (idnum not in List_Id_Number_Account_Holders and cell_no in range(7000000000,10000000000))==True:
        List_Id_Number_Account_Holders.append(idnum)
        List_Name_Account_Holders.append(acname)
        List_Account_Numbers.append(len(List_Account_Numbers)+1000000)
        List_Balence_Account.append(0.0)
        List_Card.append(len(List_Account_Numbers)+1000000000000000)
        List_Exp_Mounth.append(int_today_mounth)
        List_Exp_Year.append(int_today_year+5)
        List_CVV.append(random.randint(111,999))
        List_Cell_No.append(cell_no)
        
        print("Account is Created successfully\nAnd your Account Number={}\nCard Number={}\nRegistered Cell Number{}".format(List_Account_Numbers[-1],List_Card[-1],List_Cell_No[-1]))
    else:
        print("This Adhar user already have an account or your entered invalied cell No")
    return
def doCredit(acnum,amount):
    if (acnum in List_Account_Numbers)==True:
        List_Balence_Account[acnum-1000000]=(List_Balence_Account[acnum-1000000])+amount
    else:
        print("account number not matching")
    return List_Balence_Account[acnum-1000000]
def doDebit(acnum,amount):
    if (acnum in List_Account_Numbers)==True:
        if amount<List_Balence_Account[acnum-1000000]:
            List_Balence_Account[acnum-1000000]=(List_Balence_Account[acnum-1000000])-amount
        else:
            print("Insuffesent Funds")
    else:
        print("account number not matching")
    return List_Balence_Account[acnum-1000000]
def getBalance(acnum):
    if (acnum in List_Account_Numbers)==True:
        print("Your Account Balence is:",List_Balence_Account[acnum-1000000])
    else:
        print("account number not matching")
    return List_Balence_Account[acnum-1000000]
def getDetails(acnum):
    if (acnum in List_Account_Numbers)==True:
        
        print("Account Number:{}\nAccount Holder Name:{}\nAccount Balance:{}\nAccount Holder Adhar Number:{}".format(List_Name_Account_Holders[acnum-1000000],List_Account_Numbers[acnum-1000000],List_Balence_Account[acnum-1000000],List_Id_Number_Account_Holders[acnum-1000000]))
        print("\nCard No:{}\nCVV:{}\nExpire Date:{} / {} \nCell Number:{}".format(List_Card[acnum-1000000],List_CVV[acnum-1000000],List_Exp_Mounth[acnum-1000000],List_Exp_Year[acnum-1000000],List_Cell_No[acnum-1000000]))
    else:
        print("account number not matching")
    return
def otp(Index,Otp_Sent):
    from twilio.rest import Client
    # Your Account SID from twilio.com/console
    account_sid = "AC4eda8dd106368363e0d0a5a5462ae7e5"
    # Your Auth Token from twilio.com/console
    s="+91"+str(List_Cell_No[Index])
    auth_token  = "1226a2d7c6ccd55b41d652c3d1eb722c"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to=s, 
        from_="+12015094946",
        body=Otp_Sent)

    print(message.sid)
    return

def CardDebit(Index,Amount):
    
    if Amount<List_Balence_Account[Index]:
        List_Balence_Account[Index]=(List_Balence_Account[Index])-Amount
    else:
        print("Insuffesent Funds")
    return List_Balence_Account[Index]

def doDebitCard():
    Card_Number=int(input("Enter your  card number"))
    Exp_mounth=int(input("Enter mounth of expiry"))
    Exp_year=int(input("Enter year of expiry"))
    CVV=int(input("Enter CVV"))
    Amount=float(input("Enter Amount"))
    if Card_Number in List_Card:
        Index=List_Card.index(Card_Number)
        print("enter card number matches")
        if Exp_year==List_Exp_Year[Index] and Exp_mounth==List_Exp_Mounth[Index]:
            if Exp_year>int_today_year or (Exp_mounth>int_today_mounth and Exp_year==int_today_year):
                print("Your card is valied")
                if CVV==List_CVV[Index]:
                    
                    Otp_Sent=random.randint(100000,999999)
                    Otp_From_User=int(input("Enter OTP Recived To Your Regestered Mobile Number:"))
                    otp(Index,Otp_Sent)
                    if Otp_From_User==Otp_Sent:
                        CardDebit(Index,Amount)
                    else:
                        print("Invalid Otp")
                else:
                    print("Invalid CVV")
                    
                        
            else:
                print("your card expired")
        else:
            print("Expire data not match")
    else:
        print("Invalid Card number")
def Bank():
    Choice=int(input("Note:   0=CreateAccount\n\t1=doCredit\n\t2=doDebit\n\t3=getBalance\n\t4=getDetails\n\t5)Card Transaction\n\t6)Exit\nEnter you Choice:"))
    getChoice(Choice)
    return
def getChoice(Choice):
    if Choice==0:
        idnum=input("Enter your Adhar Number")        
        acname=input("Enter Name of Account holder")
        cell_no=int(input("Enter phone number"))
        CreateAccount(acname,idnum,cell_no)
    elif Choice==1:
        acnum=int(input("Enter your Account No"))
        amount=float(input("Enter Credit amount"))
        doCredit(acnum,amount)
    elif Choice==2:
        acnum=int(input("Enter your Account No"))
        amount=float(input("Enter Debit amount"))
        doDebit(acnum,amount)
    elif Choice==3:
        acnum=int(input("Enter your Account No"))
        getBalance(acnum)
    elif Choice==4:
        acnum=int(input("Enter your Account No"))
        getDetails(acnum)
    elif Choice==5:
        doDebitCard()
    elif Choice==6:
        print("Exit")
    else:
        print("Enter a valied input")
    return