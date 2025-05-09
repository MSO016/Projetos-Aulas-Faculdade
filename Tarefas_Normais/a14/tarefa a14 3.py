# Digite o programa abaixo e explique as novidades incluindo comentários

print("=== Usando FOR ===")
palavra = "PYTHON"
contador_vogais = 0

for letra in palavra:
    if letra in "AEIOU": #O USO DO IF e o IN PARA VERIFICAR SE DENTRO DA VARIAVEL "POISÇÃO" TEM UMAS DAS VARIAVEIS DESTACADAS "AEIOU" E AS DESTACAR NO PRINT
        contador_vogais = contador_vogais + 1
print(f"A palavra {palavra} tem {contador_vogais} vogais")


print("\n=== Usando WHILE ===") #O USO DO /n PARA A VARIAVEL É NOTAVEL TAMBÉM
palavra = "PAPIBAQUIGRAFO"
contador_vogais = 0
posicao = 0

while posicao < len(palavra): #LEN, NÃO ENTENDI O USO 
    if palavra[posicao] in "AEIOU": #O USO DO IF e o IN PARA VERIFICAR SE DENTRO DA VARIAVEL "POSIÇÃO" TEM UMAS DAS VARIAVEIS DESTACADAS "AEIOU" E AS DESTACAR NO PRINT
        contador_vogais = contador_vogais + 1
    posicao = posicao + 1
print(f"A palavra {palavra} tem {contador_vogais} vogais")

