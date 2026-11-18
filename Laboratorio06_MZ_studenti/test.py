#def seleziona_studenti(input_file: str, output_file: str, corso: str, soglia: int) -> int:
#    with open(input_file) as f:
#        st = [x.split(",") for x in f.read().splitlines() if x.split(",") != [""]]
#        intestazione = st.pop(0)
#        st = sorted([(x[0],int(x[1])) for x in st if int(x[1]) >= soglia and x[2] == corso],key= lambda x: (-x[1],x[0]))
#    with open(output_file,"w") as f:
#        f.write(f"{intestazione[0]},{intestazione[1]}")
#        f.write("\n")
#        for x in st:
#            f.write(f"{x[0]},{x[1]}")
#            f.write("\n")
#    return len(st)
#seleziona_studenti('studenti.csv', 'out.csv', 'Python', 25)

