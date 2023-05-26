nome = 'Raul Maximiliano'
altura = 1.90
peso = 83
imc = peso / altura ** 2

"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

# Raul Maximiliano tem 1.90 de altura,
# pesa 83 quilos e seu IMC é
# 22.991689750692522