
# balance - o saldo devedor no cartão de crédito
# annualInterestRate - taxa de juros anual em decimal
# monthlyPaymentRate - taxa de pagamento mensal mínima como decimal
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

mensalInterestRate = annualInterestRate / 12.0

for m in range(1,13):
    pgtoMinMensal = balance * monthlyPaymentRate
    balance = balance - pgtoMinMensal # Retira o pagamento mínimo
    balance = balance + (balance * mensalInterestRate) # Aplica os juros mensais
    # print('Month {} Remaining balance: {}'.format(m, round(balance, 2)))

print('Remaining balance: {}'.format(round(balance,2)))


