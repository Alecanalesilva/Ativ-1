import random
from time import sleep
 
nome=input(str("Digite seu nome de usuário "))
print("Olá {}, você foi desafiado para um duelo de arco e flecha".format(nome))
sleep(2)
print("Seu inimigo estará em uma das 10 plataformas existentes, e caso você o errar 3 vezes ele te matará")
sleep(3)
print("Seu inimigo já está posicionado")
number=random.randint(1,10)
c=0
while number<11:
    numero=int(input("diga um número de 1 a 10: "))
    if number>=1 and numero<number:
        print("ele não está lá, numero muito baixo")
    elif numero==number:
        print("parabéns, você ganhou")
        break
    elif number<10 and numero>number:
        print("ele não está lá, numero muito alto")
    else:
        print("numero fora de questao")
    sleep(1)
    c=c+1
    if c==3:
        quit("você errou 3 vezes e seu inimigo o matou")
