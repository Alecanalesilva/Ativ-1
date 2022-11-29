resposta=input("para fazer uma conta nova digite sim: ")
if resposta=="sim":
    novo_usuario=(input("Crie seu nome de usuário: "))
    nova_senha=(input("crie sua senha: "))
    print("login criado")
print("para ter acesso a sua conta é preciso de seu usuario e sua senha")
 
usuario=input("digite seu usuário: ")
senha=input("digite sua senha: ")
if usuario==novo_usuario:
    if senha==nova_senha:
        print("Acesso permitido")
    else:
        print("usuário ou senha incorretos")
else:
    print("usuário ou senha incorretos")
