import random, string

caracteres = string.ascii_letters + string.digits + string.punctuation
senha = ''.join(random.choices(caracteres, k=15))
print(f'Sua nova senha é: {senha}')
