
usuarios = [

    {
        'id': 1,
        'email': 'user_l@email.com',
        'pagou_conta': False

    }
]

def filtro(usuario):
    if usuario['pagou_conta']:
        return False
    return True
    
def filtar_usuarios(lista):
    return list(filter(filtro, lista))

