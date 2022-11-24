M = int(input('Qual a idade de dona Mônica? '))
A = int(input('Qual a idade de um dos filhos de dona Mônica? '))
B = int(input('Qual a idade de algum outro filho de dona Mônica? '))

C = (M - A) - B

print(f'A idade do último filho é: {C} anos.')

if A > B and A > C:
    print(f'A idade do filho mais velho é igual a: {A} anos.')

elif B > A and B > C:
    print(f'A idade do filho mais velho é igual a: {B} anos.')

else:
    print(f'A idade do filho mais velho é igual a: {C} anos.')