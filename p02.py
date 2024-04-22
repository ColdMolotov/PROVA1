pais_A = 8000
pais_B = 200000
taxa_A = 3/100
taxa_B = 1.5/100
anos_necessarios = 0
while pais_A < pais_B:
    pais_A = pais_A + int((pais_A * taxa_A))
    pais_B = pais_B + int((pais_B * taxa_B))
    anos_necessarios = anos_necessarios + 1
    if pais_B < pais_A:
        print(f"O país A levou {anos_necessarios} para superar em população o país B")
        print(f"população do país A: {pais_A}")
        print(f"população do país B: {pais_B}")