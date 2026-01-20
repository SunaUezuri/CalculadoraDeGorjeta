from calculo_gorjeta import *

valor_conta = float(input("Digite o valor da conta: R$ "))
percentual_gorjeta = float(input("Digite o percentual da gorjeta (%): "))

gorjeta = calculo_gorjeta(valor_conta, percentual_gorjeta)
total = total_conta(valor_conta, gorjeta)

print(f"O valor da gorjeta é: R$ {gorjeta:.2f}")
print(f"O valor total da conta é: R$ {total:.2f}")