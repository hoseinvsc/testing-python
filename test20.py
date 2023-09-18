def calculate_wire_weight(A, N):
    weight = A * N / 1000000 * 8900
    return weight

result = calculate_wire_weight(16, 4)
print(result,"kg")