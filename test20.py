# def calculate_wire_weight(input_str):
#     A_str, N_str = input_str.split('*')
#     A = int(A_str)
#     N = int(N_str)
#     weight = A * N / 1000000 * 8900
#     return weight

# result = calculate_wire_weight("16*4")
# print(result, "kg")

def calculate_wire_length(size, weight):
    A_str, N_str = size.split('*')
    A = int(A_str)
    N = int(N_str)
    r = A / 2
    area = 3.14 * (r ** 2)
    m = weight / (area * 8900)
    length = m / (A / 1000)
    
    return length

result = calculate_wire_length("16*4", 20)
print(result,"meter")