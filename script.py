
n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
n3 = float(input('Terceiro valor: '))
n4 = float(input('Quarto valor: '))
n5 = float(input('Quinto valor: '))
consumo  = (n1 + n2 + n3 + n4 + n5 ) 

porcentagem = (consumo/100) * 10 

valorTotal = (consumo + porcentagem )

print('a conta com os 10% fica por:'+str (valorTotal))
