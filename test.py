from main import es_palindromo, es_primo, suma_lista

def test_palindromo():
    assert es_palindromo("oso") == True
    assert es_palindromo("hola") == False


def test_primo():
    assert es_primo(7) == True
    assert es_primo(4) == False


def test_suma():
    assert suma_lista([1, 2, 3]) == 6
    assert suma_lista([]) == 0