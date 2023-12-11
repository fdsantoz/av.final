# pedindo para o usuario inserir a senha
num = int(input("qual a senha?: "))
# criar a variavel com a senha correta
senha = 2002
# se o numero colocado for igual a senha correta, liberar o acesso
if num==senha:
    print("Acesso permitido")
# se qualquer outro numero for colocado é para bloquear acesso
else:
    print("Senha invalida")
