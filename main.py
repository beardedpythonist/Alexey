with open('stroki_simwoly') as f:
    content = f.readlines()
    print(len(content))

for string in content:
    string = string.replace(' ', '')
    print(f' длина строки = {len(string) - 1}')


