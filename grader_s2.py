# -*- coding: utf-8 -*-
"""
Exercícios da 2ª Semana do curso
2nd week exercises of the course
"""
import math


def polysum(n, s):
    """:arg:n = int, number of sides of a regular polygon;
            s = float, side's length;

        out: float (4 decimal places), sum the area and square of the perimeter of the regular polygon."""

    perimetro = n * s
    area = (0.25 * n * s ** 2) / math.tan(math.pi / n)
    return round(area + (perimetro ** 2), 4)

"""
Introduction

Each month, a credit card statement will come with the option for you to pay a minimum amount of your charge, 
usually 2% of the balance due. However, the credit card company earns money by charging interest on 
the balance that you don't pay. So even if you pay credit card payments on time, interest is still 
accruing on the outstanding balance.

Say you've made a $5,000 purchase on a credit card with an 18% annual interest rate and a 2% minimum monthly payment rate. 
If you only pay the minimum monthly amount for a year, how much is the remaining balance?

You can think about this in the following way.

At the beginning of month 0 (when the credit card statement arrives), assume you owe an amount we will 
call  b0  (b for balance; subscript 0 to indicate this is the balance at month 0).

Any payment you make during that month is deducted from the balance. 
Let's call the payment you make in month 0,  p0. 
Thus, your unpaid balance for month 0,  ub0 , is equal to  b0−p0.

ub0=b0−p0 

At the beginning of month 1, the credit card company will charge you interest on your unpaid balance. 
So if your annual interest rate is  r , then at the beginning of month 1, your new balance is 
your previous unpaid balance  ub0 , plus the interest on this unpaid balance for the month. 
In algebra, this new balance would be:
b1=ub0+(r/12.0)*ub0 

In month 1, we will make another payment,  p1. That payment has to cover some of the interest costs, 
so it does not completely go towards paying off the original charge. 
The balance at the beginning of month 2,  b2 , can be calculated by first calculating 
the unpaid balance after paying  p1, then by adding the interest accrued:
ub1=b1−p1 
b2=ub1+(r/12.0)*ub1
 
If you choose just to pay off the minimum monthly payment each month, 
you will see that the compound interest will dramatically reduce your ability to lower your debt.

Let's look at an example. If you've got a $5,000 balance on a credit card with 18% annual interest rate, 
and the minimum monthly payment is 2% of the current balance, we would have the following 
repayment schedule if you only pay the minimum payment each month:

Month|	Balance|	Minimum Payment|	Unpaid Balance|	Interest
0|	5000.00|	100 (= 5000 * 0.02)|	4900 (= 5000 - 100)|	73.50 (= 0.18/12.0 * 4900)
1|	4973.50 (= 4900 + 73.50)|	99.47 (= 4973.50 * 0.02)|	4874.03 (= 4973.50 - 99.47)|	73.11 (= 0.18/12.0 * 4874.03)
2|	4947.14 (= 4874.03 + 73.11)|	98.94 (= 4947.14 * 0.02)|	4848.20 (= 4947.14 - 98.94)|	72.72 (= 0.18/12.0 * 4848.20)

You can see that a lot of your payment is going to cover interest, 
and if you work this through month 12, you will see that after a year, 
you will have paid $1165.63 and yet you will still owe $4691.11 
on what was originally a $5000.00 debt. Pretty depressing!
"""

"""
Problem 1 - Paying Debt off in a Year
10.0/10.0 points (graded)
Write a program to calculate the credit card balance after one year 
if a person only pays the minimum monthly payment required 
by the credit card company each month.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining balance. 
At the end of 12 months, print out the remaining balance. 
Be sure to print out no more than two decimal digits of accuracy - so print:
Remaining balance: 813.41

instead of:
Remaining balance: 813.4141998135 

So your program only prints out one thing: the remaining balance 
at the end of the year in the format:
Remaining balance: 4784.0

A summary of the required math is found below:
Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
"""
def payingDebt(PreviousBalance, annualInterestRate, monthlyPaymentRate, tempo=12):
    """:arg: PreviousBalance - saldo pendente no cartão de crédito
            annualInterestRate - Taxa de juros anual as a decimal
            monthlyPaymentRate - Pagamento mínimo (percentual) as a decimal
            tempo - período de tempo a ser avaliado
        
        ;out: None. print the remaining balance with two decimal digits of accuracy
        ex.: Remaining balance: 361.61
    """

    # Taxa de Juros mensal
    monthly_interest_rate = annualInterestRate/12
    # Pagamento mensal mínimo
    minimum_monthly_payment = monthlyPaymentRate * PreviousBalance
    #Saldo mensal não pago
    monthly_unpaid_balance = PreviousBalance - minimum_monthly_payment
    #Saldo atualizado a cada mês
    updated_balance_each_month = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)

    if tempo == 1:
        print("Remaining balance:",  round(updated_balance_each_month, 2))
    else:
        tempo -= 1
        payingDebt(updated_balance_each_month, annualInterestRate, monthlyPaymentRate, tempo)
"""
Problem 2 - Paying Debt Off in a Year
15.0/15.0 points (graded)
Now write a program that calculates the minimum fixed monthly payment 
needed in order pay off a credit card balance within 12 months. 
By a fixed monthly payment, we mean a single number which does not change each month, 
but instead is a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

The program should print out one line: the lowest monthly payment that 
will pay off all debt in under 1 year, for example:
Lowest Payment: 180 

Assume that the interest is compounded monthly according to the balance 
at the end of the month (after the payment for that month is made). 
The monthly payment must be a multiple of $10 and is the same for all months. 
Notice that it is possible for the balance to become negative using this payment scheme, 
which is okay. A summary of the required math is found below:

Monthly interest rate = (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
"""
def pagando(saldo, juros_anuais, valor_minimo, tempo=12):

    taxa_mensal = juros_anuais/12
    saldo_mes_sem_pagar = saldo - valor_minimo
    novo_saldo = saldo_mes_sem_pagar + (taxa_mensal * saldo_mes_sem_pagar)

    if tempo == 1:
        if novo_saldo <= 0 :
            return True
        else:
            return False
    else:
        tempo -= 1
        return pagando(novo_saldo, juros_anuais, valor_minimo, tempo)


def PayingDebtOff(balance, annualInterestRate, tempo=12):
    """
    :arg
    balance - float, o saldo pendente no cartão de crédito
    annualInterestRate - float, taxa de juros anual em decimal
    tempo - int, tempo a ser considerado

    Calcula qual é o valor fixo mínimo que se deve pagar por mês para quitar a dívida do cartão em um tempo
    :out
    int, imprime o valor do pagamento mínimo
    ex.: Lowest Payment: 180
    """
    taxa_mensal = annualInterestRate / 12
    valor_minimo = balance / 12
    valor_maximo = (balance * (1 + taxa_mensal)**2)/12

    while True:
        if pagando(balance, annualInterestRate, valor_minimo):
            return valor_minimo
        else:
            valor_minimo += 10

    return valor_minimo


print("Lowest Payment=", round(PayingDebtOff(3926, 0.2),2))


