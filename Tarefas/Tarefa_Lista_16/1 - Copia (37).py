def ordenar_vetor(A):

    parte1 = A[:6]
    parte2 = A[6:]

    parte1.sort()

    parte2.sort()
 
    A_ordenado = parte1 + parte2

    return A_ordenado

A = [1, 3, 5, 7, 9, 11, 10, 8, 6, 4, 2]
A_ordenado = ordenar_vetor(A)
print("Vetor ordenado:", A_ordenado)
