import soup_funcions

def find_word(letter_soup, word):
    """
    Función que verifica si una palabra se encuentra en la sopa de letras en cualquiera de las direcciones posibles:
    horizontal, vertical y diagonal.

    Parámetros:
    letter_soup: Una matriz que representa la sopa de letras, donde cada elemento es una letra. (Lista de listas)
    word: La palabra que se desea buscar en la sopa de letras. (Str)

    Retorna:
    Valor booleano: True si la palabra se encuentra en la sopa de letras en alguna dirección, de lo contrario False.

    Es una función.
    """
    ans = False
    reversed_rows = [row[::-1] for row in letter_soup]
    reversed_matrix = letter_soup[::-1]
    reversed_matrix_and_rows = [row[::-1] for row in reversed_matrix]

    # Verificar horizontalmente de izquierda a derecha
    if soup_funcions.find_left_right(letter_soup, word):
        ans = True

    # Verificar horizontalmente de derecha a izquierda
    if not ans:
        if soup_funcions.find_left_right(reversed_rows, word):
            ans = True

    # Verificar verticalmente de arriba hacia abajo
    if not ans:
        if soup_funcions.find_up_down(letter_soup, word):
            ans = True

    # Verificar verticalmente de abajo hacia arriba
    if not ans:
        if soup_funcions.find_up_down(reversed_matrix, word):
            ans = True

    # Verificar diagonal de izquierda a derecha y arriba hacia abajo
    if not ans:
        if soup_funcions.find_diag_l_r(letter_soup, word):
            ans = True

    # Verificar diagonal de derecha a izquierda y arriba hacia abajo
    if not ans:
        if soup_funcions.find_diag_l_r(reversed_rows, word):
            ans = True

    # Verificar diagonal de izquierda a derecha y abajo hacia arriba
    if not ans:
        if soup_funcions.find_diag_l_r(reversed_matrix, word):
            ans = True

    # Verificar diagonal de derecha a izquierda y abajo hacia arriba
    if not ans:
        if soup_funcions.find_diag_l_r(reversed_matrix_and_rows, word):
            ans = True

    return ans

def find_words(letter_soup, words):
    """
    Función que verifica si todas las palabras de una lista se encuentran en la sopa de letras.

    Parámetros:
    letter_soup: Una matriz que representa la sopa de letras, donde cada elemento es una letra. (Lista de listas)
    words: Lista de palabras que se desean buscar en la sopa de letras. (Lista de strings)

    Retorna:
    Valor booleano: True si todas las palabras se encuentran en la sopa de letras, de lo contrario False.

    Es una función.
    """
    ans = True
    for word in words:
        if not find_word(letter_soup, word):
            ans = False

    return ans


def report_generator(letter_soup, words):
    """
    Función que genera un reporte de las palabras encontradas en la sopa de letras.
    Convierte las palabras a mayúsculas antes de la búsqueda y omite las palabras vacías.

    Parámetros:
    letter_soup: Una matriz que representa la sopa de letras, donde cada elemento es una letra. (Lista de listas)
    words: Lista de palabras que se desean buscar en la sopa de letras. (Lista de strings)

    Retorna:
    report: Un diccionario donde las claves son las palabras y los valores son True si la palabra está presente en la sopa de letras, False si no lo está.

    Es una función
    """
    report = {}
    for word in words:
        word = word.strip()
        if word:
            word_upper = word.upper()
            report[word] = find_word(letter_soup, word_upper)

    return report