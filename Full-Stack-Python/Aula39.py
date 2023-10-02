"""
Iterando strings com while
"""
#       012345678910
#nome = 'Raul Maximiliano'  # Iteráveis
#      1110987654321
#tamanho_nome = len(nome)
#print(tamanho_nome)
#print(nome[3])

#nova_string = ''
#nova_string += '*R*a*u*l* *M*a*x*i*m*i*l*i*a*n*o*'

nome = 'Maria Helena'  # Iteráveis

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)