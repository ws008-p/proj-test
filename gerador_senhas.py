class Numero_errado(Exception):
    pass

import random 
import string 

print("Gerador de senhas")
while True:
    try:
        tamanho_senha = int(input("Indique o tamanho da senha entre 1 e 30 caracteres:"))
        if tamanho_senha < 1 or tamanho_senha > 30:
            raise Numero_errado("Numero fora do que e pedido")
        else:
            break
    except Numero_errado as a:
        print(a)
    except:
        print("coloque um numero")

caracteres = (
    string.ascii_letters +
    string.digits +
    string.punctuation
)
senha=""
for i in range(tamanho_senha):
    senha += random.choice(caracteres)

print("senha gerada",senha)




