import random
import datetime
import time
class Bankapp:
    global credentials,accountdetails,stransactions,rtransactions
    credentials={}
    accountdetails={}
    stransactions={}
    rtransactions={}
    def __init__(self):
        ch=input('Do you have account if yes enter Y else enter N')
        if ch.upper()=='Y':
            self.login()
        else:
            self.create_user()

    def create_user(self):
        res=True
        while res:
            username=input('Enter Username')
            pwd=input('Enter password')

            if username not in credentials:
                credentials[username]=pwd
                print('User created please login with credentials')
                res=False
            else:
                print('user name already exists')
        self.login()

    def login(self):
        print('login here')
        res=True
        while res:
            username=input('Enter Username')
            pwd=input('Enter password')
            if username in credentials and credentials[username]==pwd:
                print('Welcome User. explore our services')
                res=False
            else:
                print('Enter valid username and password')
        self.services()
    
    def create_account(self):
        acc=random.randint(1000000000,10000000000)
        print(acc)
        name=input('Enter Account Holder name')
        amount=int(input('Enter Amount'))
        pin=int(input('Enter pin'))
        if acc not in accountdetails:
            accountdetails[acc]={'name':name,'amount':amount,'pin':pin}
            print(accountdetails)
            print('Account Created')
        else:
            print('Account exists already')
        self.services()

    def view(self):
        acc=int(input('Enter account number'))
        res=True
        while res:
            if acc in accountdetails:
                print(accountdetails[acc])
                res=False
            else:
                print('enter valid account number')
        self.services()

    def withdraw(self):
        dtt=0
        tm=0
        dt=0
        status='Debited'
        acc=int(input('Enter account number'))
        pin=int(input('enter your pin'))
        if acc in accountdetails and accountdetails[acc]['pin']==pin:
            amount=int(input('Enter amount to withdraw'))
            if amount < accountdetails[acc]['amount']:
                print('amount',amount,'withdrawn succesfully')
                accountdetails[acc]['amount']=accountdetails[acc]['amount']-amount
                tm=time.strftime("%H:%M:%S", time.localtime())
                dt=datetime.datetime.now()
                dtt=dt.date()
                stransactions[tm]=[str(dtt),amount,status]
                accountdetails[acc]['transaction']=stransactions
            else:
                print('insufficient balance')
        else:
            print('invalid account number or pin')
        self.services()

    def Deposit(self):
        tm=0
        dt=0
        dtt=0
        status='Credited'
        acc=int(input('Enter account number'))
        pin=int(input('enter your pin'))
        if acc in accountdetails and accountdetails[acc]['pin']==pin:
            amount=int(input('Enter amount to Deposit'))
            accountdetails[acc]['amount']=accountdetails[acc]['amount']+amount
            accountdetails[acc]['amount']=accountdetails[acc]['amount']-amount
            tm=time.strftime("%H:%M:%S", time.localtime())
            dt=datetime.datetime.now()
            dtt=dt.date()
            stransactions[tm]=[str(dtt),amount,status]
            accountdetails[acc]['transaction']=stransactions
        else:
            print('invalid account number or pin ')
        self.services()

    def Transfer(self):
        tm=0
        dt=0
        dtt=0
        status1='Credited'
        status2='Debited'
        acc1=int(input('Enter sender account number'))
        acc2=int(input(' Enter receiver account number'))
        pin=int(input('enter your pin'))
        if acc1 in accountdetails and acc2 in accountdetails and accountdetails[acc1]['pin']==pin:
            amount=int(input('Enter amount to Transfer'))
            if amount < accountdetails[acc1]['amount']:
                accountdetails[acc1]['amount']=accountdetails[acc1]['amount']-amount
                accountdetails[acc2]['amount']=accountdetails[acc2]['amount']+amount
                tm=time.strftime("%H:%M:%S", time.localtime())
                dt=datetime.datetime.now()
                dtt=dt.date()
                stransactions[tm]=[str(dtt),amount,status2]
                rtransactions[tm]=[str(dtt),amount,status1]
                accountdetails[acc1]['transaction']=stransactions
                accountdetails[acc2]['transaction']=rtransactions
            else:
                print('insufficient balance')
        else:
            print('invalid account number or pin')
        self.services()

    def transaction(self):
        acc=int(input('Enter account number'))
        pin=int(input('enter your pin'))
        if acc in accountdetails and accountdetails[acc]['pin']==pin:
            print(accountdetails[acc]['transaction'])
        else:
            print('invalid account number')
        self.services()
    
            

    def services(self):
        res=True
        while res:
            print('''
1.create account
2.View acoount
3.withdraw
4.Deposit
5.Fund Transfer
6.Print Transaction
7.Exit
''')
            choice=int(input('enter your choice'))

            match(choice):
                case 1:
                    self.create_account()
                    break
                case 2:
                    self.view()
                    break
                case 3:
                    self.withdraw()
                    break
                case 4:
                    self.Deposit()
                    break
                case 5:
                    self.Transfer()
                    break
                case 6:
                    self.transaction()
                    break
                case 7:
                    res=False


users=Bankapp()
