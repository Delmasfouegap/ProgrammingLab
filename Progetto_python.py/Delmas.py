# with open('/workspaces/ProgrammingLab/Progetto_python.py/data.csv', 'r') as file:
#     for line in file:
#         print(line)

my_file = open('/workspaces/ProgrammingLab/Progetto_python.py/data.csv', 'r')
diz = {}
for element in my_file:
    data = element.strip().split(',')
    chiave = data[0]
    valore = data[1]
    diz[chiave] = valore
    # if not chiave in diz.keys():
    #     diz[chiave] = []

print(diz)
