W = 10  
N = int(input("Número representando a quantidade de itens: "))
mochila = {}
pesos = []
valores = []

peso_total = 0

for i in range(N):
    item = input("Item: ")
    peso = float(input("Peso do item: "))
    
    if peso_total + peso > W:
        print(f"Não é possível adicionar '{item}' (peso: {peso}). A mochila já está cheia.")
    else:
        mochila[item] = peso  
        peso_total += peso 

print("Itens na mochila:", mochila)
print("Peso total na mochila:", peso_total)
