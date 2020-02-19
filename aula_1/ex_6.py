
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
email = input('Digite seu email: ')

user = {
    'nome': nome,
    'idade': idade,
    'email': email
}

idade = int(user['idade'])

if idade > 18:
    print('Maior de 18')
else:
    print('Menor de 18')





    usuario = {
    'nome' : input('Digite seu nome '),
    'idade' : input('Digite sua idade '),
    'n_filhos' : input('Quantos filhos voce tem? ')
}
print(usuario)