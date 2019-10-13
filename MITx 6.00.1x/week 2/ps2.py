paid=0
for i in range(1,13):
    print "Month: ", i
    minimum=round(monthlyPaymentRate*balance,2)
    print "Minimum monthly payment: ", minimum
    paid+=minimum
    balance=balance-minimum
    balance+=balance*annualInterestRate/12
    print "Remaining balance: ", round(balance,2)
    i+=1
print "Total paid: ", paid
print "Remaining balance: ", round(balance,2)


minimum=0
t=balance
while t>0:
    cnt=0
    t=balance
    minimum+=10
    while cnt<12:
        t=t-minimum
        t=t+(t*annualInterestRate/12.0)
        cnt+=1
print "Lowest Payment: ", minimum


minimum=0
t=balance
while t>0:
    cnt=0
    t=balance
    minimum+=0.01
    while cnt<12:
        t=t-minimum
        t=t+(t*annualInterestRate/12.0)
        cnt+=1
print "Lowest Payment: ", round(minimum,2)