def load_file(filename: str) -> str:
    with open(filename) as f:
        return f.read()
Path = "/Users/persicovincenzo/Downloads/Simulazione01-test/06-file/ripasso"
def search_word(filename: str, word: str) -> int:
    f = load_file(f"{Path}/{filename}")
    r = ""
    for y in f:
        if y.isalnum() or y.isspace():
            r += y  
    return r.strip().count(word)
print(search_word('file01.txt', 'buon'))