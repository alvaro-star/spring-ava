def firstLetterLowerCase(string:str):
    if not string:  # Verifica se a string está vazia
        return string
    return string[0].lower() + string[1:]
