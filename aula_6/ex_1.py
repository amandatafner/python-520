
import psycopg2
import psycopg2.extras


connection = psycopg2.connect(
    user='admin',
    password='4linux',
    host='localhost',
    port=5432,
    database='projeto'
)
cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

# Funcao que busca a informacao no banco de dados

def find_user_by_email(email):
    cursor.execute('''

        SELECT * FROM users

        WHERE users.email = \'{}\';

    '''.format(email))
    return cursor.fetchone()

email = input('Digite seu email: ')

user = find_user_by_email(email)

print(user)