def balance_founder(file2, balance2):
    counter = 0
    for char in file2:
        counter = counter + 1

        if char == "(":
            balance2 = balance2 + 1
        elif char == ")":
            balance2 = balance2 - 1
        if balance2 == 12:
            return counter

# balance2 = balance_founder[2]

# Example usage:
file = open("/home/hosein/w/testing-python/test16.txt", "r")
read_file = file.read()

# initial_balance = 0
result = balance_founder(read_file, 12)
print(result)