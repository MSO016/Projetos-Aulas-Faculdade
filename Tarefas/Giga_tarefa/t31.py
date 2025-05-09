fatorial1 = 3
fatorial2 = 5
fatorial3 = 6
soma_3_termos = 1 + 1 / fatorial1 + 1 / fatorial2 + 1 / fatorial3

fatorial4 = 1 * 2 * 3
soma_4_termos = soma_3_termos + 1 / fatorial4

fatorial5 = 1 * 2 * 3 * 4
soma_5_termos = soma_4_termos + 1 / fatorial5

print(f"Valor de E considerando 3 termos: {soma_3_termos:.5f}")
print(f"Valor de E considerando 4 termos: {soma_4_termos:.5f}")
print(f"Valor de E considerando 5 termos: {soma_5_termos:.5f}")
