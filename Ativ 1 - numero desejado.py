import random
 
numero=random.randint(1,5)
palpite=int(input("Digite um número de 1 a 5\f"))
 
if palpite==numero:
    print("acertou")
else:
    print(f"errou, o número sorteado foi {numero}")
