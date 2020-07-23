string = '1 0 0 1 0 1'
bin = string[::2]
num = 0
for i in range(len(bin)):
    if bin[-(i + 1)] == '1':
        num = num + 2 ** i

print(f'Znaleziona liczba: {num}')

# rozwiazanie
string = '1 0 0 1 0 1'
binary = string[::2]
number = int(binary, 2)
print(f'Znaleziona liczba: {number}')
