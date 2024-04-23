class bankaccount:
    acno=101
    bal=10000
    ownername='Alice'
    def depfund(self):
        deamt=int(input('Enter amount you want to deposit:'))
        self.bal=self.bal+deamt
        print('Successfully deposit amount')
        choice=input('you want to check balance amount yes /no:')
        if choice=='yes':
            print('your current balance is:',self.bal,'\n')
        else:
            print('Thank you \n')
   
    def withdfund(self):
        nbal=self.bal-500
        wamt=int(input('Enter withraw amount:'))
        note=int(input('Enter which note you want:'))
        if wamt%note==0:
          if nbal>=wamt:
            sbal=self.bal-wamt
            print('Successfully withdraw amount')
            choice=input('you want to check balance amount yes /no:')
            if choice=='yes':
                print('your current balance is:',sbal,'\n')
            else:
                print('Thank you \n')
          else:
            print('insuffient credential')
        else:  
            print(note,'cant withdraw all amount ')   

    def accinfo(self):
        enteraccnu=int(input('Enter account number:'))
        if enteraccnu==self.acno:
            print('Owner name is:',self.ownername)
            print('Owner current balance  is:',self.bal,'\n')
        else:
            print('Account Number doesnot Exist')
class checkingaccount(bankaccount):
    rate=30
    def roi(self):
        print('rate of interest of checkingaccount is 13%:',self.rate)
    def calint(self):
        interest=self.bal*(self.rate/100)
        print('Total Monthly intrest of chekingaccount is:',interest,'\n')
class savingaccount(bankaccount):
    rate=20
    def roi(self):
        print('Rate of interest of saving account is 13%',self.rate)
    def calint(self):
        interest=self.bal*(self.rate/100)
        print('Total monthly interest of savingaccount is:',interest,'\n')
b=bankaccount()
b.depfund()
b.withdfund()
b.accinfo()

c=checkingaccount()
c.roi()
c.calint()

s=savingaccount()
s.roi()
s.calint()
