with open('old-tsetmc.txt', 'r') as file:
    data = file.read()
lines = data.split(';')
for line in lines:
    company_data = line.split(',')
    company_name = company_data[0].split('@')
    company_symbol = company_data[1].split('@')

    print("نام شرکت:", company_name, "، نماد شرکت:", company_symbol)
