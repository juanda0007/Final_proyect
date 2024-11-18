def get_file_content(file_path):
    """
    Lee el archivo input.txt y separa la sopa de letras y las palabras a buscar.
    """
    with open(file_path, 'r') as file:
        content = file.read().strip()
    soup_str, words_str = content.split('---')
    soup = [line.split() for line in soup_str.splitlines()]
    words = words_str.splitlines()

    return soup, words
