def load_file(filename: str) -> str:
    with open(filename) as f:
        return f.read()
Path = "/Users/persicovincenzo/Downloads/Simulazione01-test/06-file"

def roma(filename):    
    f = load_file(f"{Path}/{filename}")
    f_splt = [x.split(",") for x in f.splitlines()]
    print(f_splt)

roma("file04.csv")

    f = load_file(f"{Path}/{filename}")
    f_spl = [x.split(",") for x in f.splitlines()]
    if empties == True:
        f_spl = [[None if x == "" else x for x in sottolista] for sottolista in f_spl]
        lista = [{f_spl[0][0]: f_spl[i][0] ,f_spl[0][1]: f_spl[i][1] ,f_spl[0][2]: f_spl[i][2] ,f_spl[0][3]:f_spl[i][3]} for i in range(1,len(f_spl))]
    else:
        