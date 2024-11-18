def find_left_right(matrix, word_str):
    """
    Función que busca una palabra de izquierda a derecha en una matriz (sopa de letras).

    Parámetros:
    matrix: Una matriz que representa la sopa de letras, donde cada elemento es una letra. (Lista de listas)
    word_str: La palabra que se desea buscar de izquierda a derecha. (Str)

    Retorna:
    Valor booleano: True si la palabra se encuentra en la dirección de izquierda a derecha en la matriz, de lo contrario False.

    Es una función.
    """
    ans = False
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if j + len(word_str) <= len(matrix[0]):
                found = True
                for k in range(len(word_str)):
                    if matrix[i][j + k] != word_str[k]:
                        found = False
                if found:
                    ans = True
    return ans

def find_up_down(matrix, word_str):
    """
    Función que busca una palabra de arriba hacia abajo en una matriz (sopa de letras).

    Parámetros:
    matrix: Una matriz que representa la sopa de letras, donde cada elemento es una letra. (Lista de listas)
    word_str: La palabra que se desea buscar de arriba hacia abajo.(Str)

    Retorna:
    bool: True si la palabra se encuentra en la dirección de arriba hacia abajo en la matriz,de lo contrario False.

    Es una función.
    """
    ans = False
    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            if i + len(word_str) <= len(matrix):
                found = True
                for k in range(len(word_str)):
                    if matrix[i + k][j] != word_str[k]:
                        found = False
                if found:
                    ans = True
    return ans

def find_diag_l_r(matrix, word_str):
    """
    Función que busca una palabra en la diagonal de izquierda a derecha en una matriz (sopa de letras).

    Parámetros:
    matrix: Una matriz que representa la sopa de letras, donde cada elemento es una letra. (Lista de listas)
    word_str: La palabra que se desea buscar en la diagonal de izquierda a derecha. (Str)

    Retorna:
    Valor booleano: True si la palabra se encuentra en la diagonal de izquierda a derecha en la matriz, de lo contrario False.

    Es una función.
    """
    ans = False
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i + len(word_str) <= len(matrix) and j + len(word_str) <= len(matrix[0]):
                found = True
                for k in range(len(word_str)):
                    if matrix[i + k][j + k] != word_str[k]:
                        found = False
                if found:
                    ans = True
    return ans

