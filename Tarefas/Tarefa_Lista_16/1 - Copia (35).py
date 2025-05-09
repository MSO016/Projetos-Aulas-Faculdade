def numero_para_vetor(n):
    return [int(digito) for digito in str(n)][::-1]

def soma_vetores(v1, v2):
    tamanho = max(len(v1), len(v2))
    resultado = []
    carry = 0

    for i in range(tamanho):
        digito1 = v1[i] if i < len(v1) else 0
        digito2 = v2[i] if i < len(v2) else 0
        soma = digito1 + digito2 + carry
        resultado.append(soma % 10)
        carry = soma // 10

    if carry:
        resultado.append(carry)

    return resultado

a = int(input("Digite o número a (positivo e menor que 10000): "))
b = int(input("Digite o número b (positivo e menor que 10000): "))

vetor_a = numero_para_vetor(a)
vetor_b = numero_para_vetor(b)

vetor_soma = soma_vetores(vetor_a, vetor_b)

print("Vetor de a:", vetor_a)
print("Vetor de b:", vetor_b)
print("Vetor da soma de a e b:", vetor_soma)
