palabras_reservadas = {
    'package', 'import', 'type', 'struct', 'func', 
    'var', 'int', 'float64', 'string', 'bool', 
    'if', 'else', 'for', 'return'
}

class Token:
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor

    def __repr__(self):
        return f"Token({self.tipo}, '{self.valor}')"

def tokenizar(cadena):
    tokens = []
    i = 0
    operadores = {'+', '-', '*', '/', '=', '<', '>', '%', ':', '!'}
    delimitadores = {'{': 'LLAVE_ABRE', '}': 'LLAVE_CIERRA', '(': 'PAR_ABRE', ')': 'PAR_CIERRA', ',': 'COMA'}

    while i < len(cadena):
        c = cadena[i]

        if c.isspace():
            i += 1
            continue

        if c in delimitadores:
            tokens.append(Token(delimitadores[c], c))
            i += 1
            continue

        if c.isalpha() or c == '_':
            lexema = ""
            while i < len(cadena) and (cadena[i].isalnum() or cadena[i] == '_'):
                lexema += cadena[i]
                i += 1
            if lexema in palabras_reservadas:
                tokens.append(Token('KEYWORD', lexema))
            else:
                tokens.append(Token('IDENTIFICADOR', lexema))
            continue

        if c.isdigit():
            lexema = ""
            while i < len(cadena) and (cadena[i].isdigit() or cadena[i] == '.'):
                lexema += cadena[i]
                i += 1
            tokens.append(Token('NUMERO', lexema))
            continue

        if c in operadores:
            tokens.append(Token('OPERADOR', c))
            i += 1
            continue

        raise SyntaxError(f"Carácter no reconocido en el Léxico: '{c}'")

    tokens.append(Token('EOF', 'EOF'))
    return tokens


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.token_actual = self.tokens[self.pos]

    def coincidir(self, tipo_o_valor_esperado):
        if self.token_actual.tipo == tipo_o_valor_esperado or self.token_actual.valor == tipo_o_valor_esperado:
            token_consumido = self.token_actual
            self.pos += 1
            if self.pos < len(self.tokens):
                self.token_actual = self.tokens[self.pos]
            return token_consumido
        else:
            raise SyntaxError(
                f"Error Sintáctico: Se esperaba '{tipo_o_valor_esperado}', pero se encontró '{self.token_actual.valor}'"
            )

    def parse_declaracion_var(self):
        self.coincidir("var")
        id_token = self.coincidir("IDENTIFICADOR")
        tipo_token = self.parse_tipo()
        init_nodo = self.parse_inicializacion_opcional()

        return {
            "nodo": "<declaracion_var>",
            "identificador": id_token.valor,
            "tipo": tipo_token,
            "inicializacion": init_nodo
        }

    def parse_tipo(self):
        if self.token_actual.valor in ['int', 'float64', 'string', 'bool']:
            t = self.coincidir(self.token_actual.valor)
            return t.valor
        elif self.token_actual.tipo == 'IDENTIFICADOR':
            t = self.coincidir('IDENTIFICADOR')
            return t.valor
        else:
            raise SyntaxError(f"Tipo de dato no válido: '{self.token_actual.valor}'")

    def parse_inicializacion_opcional(self):
        if self.token_actual.valor == '=':
            self.coincidir('=')
            return self.parse_expresion()
        return None

    def parse_condicional(self):
        self.coincidir("if")
        condicion_nodo = self.parse_condicion()
        bloque_then = self.parse_bloque()
        bloque_else = self.parse_opcional_else()

        return {
            "nodo": "<condicional>",
            "condicion": condicion_nodo,
            "bloque_then": bloque_then,
            "bloque_else": bloque_else
        }

    def parse_condicion(self):
        val_izq = self.token_actual.valor
        self.pos += 1
        
        op = self.coincidir("OPERADOR").valor
        

        return {"izq": val_izq, "operador": op        val_der = self.token_actual.valor
        self.pos += 1
        self.token_actual = self.tokens[self.pos]

