
def create_user(name, email, password):
    cursor.execute('''
        INSERT INTO users 
            (name, email, password)
        VALUES
            (\'{}\', \'{}\', \'{}\')
        ;
    '''.format(name, email, password))
    return connection.commit()

name = input('Digite seu nome:')
email = input ('Digite seu email:')
password = input ('Digite sua senha:')

create_user(name, email, password)