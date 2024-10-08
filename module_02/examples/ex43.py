# Validador IBAN.
iban = input("Ingresa un IBAN, por favor: ")
iban = iban.replace(' ', '')

if not iban.isalnum():
    print("Has introducido caracteres no válidos.")
elif len(iban) < 15:
    print("El IBAN ingresado es demasiado corto.")
elif len(iban) > 31:
    print("El IBAN ingresado es demasiado largo.")
else:
    iban = (iban[4:] + iban[0:4]).upper()
    iban2 = ''
    for ch in iban:
        if ch.isdigit():
            iban2 += ch
        else:
            iban2 += str(10 + ord(ch) - ord('A'))
    iban = int(iban2)
    if iban % 97 == 1:
        print("El IBAN ingresado es válido.")
    else:
        print("El IBAN ingresado no es válido.")

"""
Datos de prueba:
Inglés: GB72 HBZU 7006 7212 1253 00
Francés: FR76 30003 03620 00020216907 50
Alemán: DE02100100100152517108
"""
