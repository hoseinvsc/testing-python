def calculate_wire_weight(input_str):
    A_str, N_str = input_str.split('*')
    A = int(A_str)
    N = int(N_str)
    weight = A * N / 1000000 * 8900
    return weight

result = calculate_wire_weight("16*4")
print(result, "kg")