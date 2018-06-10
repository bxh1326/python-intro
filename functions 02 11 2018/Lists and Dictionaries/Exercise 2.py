nameAges = {"Allison":18, "Benson":48, "David":20, "Erik":20, "Galen":15, "Grace":25, "Helene":40, "Janette":18}
ageNames = {}
for k, v in nameAges.items():
    if v not in ageNames:
        ageNames[v] = [k]
    else:
        ageNames[v].append(k)

print(ageNames)

