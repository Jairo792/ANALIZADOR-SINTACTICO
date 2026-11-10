tokens = [12, 41, 1000, 42, 16, 1000]

def analizar_programa(tokens):
    i = 0
    error = ''

    while i < len(tokens):
        if tokens[i] in (12,):
            i, error = impresion(tokens, i)
        elif tokens[i] in (16,):
            i, error = retorno(tokens, i)
        else:
            return f'ERROR: TOKEN DESCONOCIDO EN LA POSICIÓN {i}'
        
        if error != '':
            return error

    return 'VÁLIDO'

def impresion(tokens, i):
    if i < len(tokens) and tokens[i] == 12:
        i = i + 1
    else:
        return i, 'ERROR: SE ESPERABA LA SENTENCIA DE IMPRESIÓN (fmt.Println)'
    
    if i < len(tokens) and tokens[i] == 41:
        i = i + 1
    else:
        return i, 'ERROR: SE ESPERABA UN PARÉNTESIS QUE ABRA'
    
    i, error = lista_expresiones(tokens, i)
    if error != '':
        return i, error
        
    if i < len(tokens) and tokens[i] == 42:
        i = i + 1
    else:
        return i, 'ERROR: SE ESPERABA UN PARÉNTESIS QUE CIERRE'
        
    return i, ''

def retorno(tokens, i):
    if i < len(tokens) and tokens[i] == 16:
        i = i + 1
    else:
        return i, 'ERROR: SE ESPERABA LA PALABRA RESERVADA RETURN'
    
    if i < len(tokens) and tokens[i] in (1000, 2000):
        i, error = expresion(tokens, i)
        if error != '':
            return i, error
            
    return i, ''

def lista_expresiones(tokens, i):
    if i < len(tokens) and tokens[i] in (1000, 2000):
        i, error = expresion(tokens, i)
        if error != '':
            return i, error
    else:
        return i, 'ERROR: SE ESPERABA UNA EXPRESIÓN VÁLIDA'
    return i, ''

def expresion(tokens, i):
    if i < len(tokens) and tokens[i] in (1000, 2000):
        i = i + 1
    else:
        return i, 'ERROR: SE ESPERABA UN VALOR O IDENTIFICADOR'
    return i, ''

print(analizar_programa(tokens))
