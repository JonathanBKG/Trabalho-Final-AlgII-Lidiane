file = open("bweb_1t_SC_091020241636.csv", "r")
for linha in file.readlines():
    print(linha)
file.close