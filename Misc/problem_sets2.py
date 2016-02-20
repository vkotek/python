total = 0

def first():
    for n in range(1,13):
        fee = balance * monthlyPaymentRate
        balance = balance-fee + ((balance-fee) * (annualInterestRate/12.0))
        total+=fee

        print('Month:', n)
        print('Minimum monthly payment:', round(fee,2))
        print('Remaining balance:', round(balance,2))
        
    print('Total paid:', round(total,2))
    print('Remaining balance:', round(balance,2))

def bal(balance,annualInterestRate):
    balance = (balance * ( 1 + (annualInterestRate/12))**12.0) / 12
    print('Lowest Payment:', balance)
    
bal(3329,0.2)
bal(4773,0.2)
bal(3926,0.2)
    
