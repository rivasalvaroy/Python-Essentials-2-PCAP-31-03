def bad_fun(n):
    return 1 / n


try:
    bad_fun(0)
except ArithmeticError:
    print("¿Que pasó? ¡Se generó una excepción!")

print("FIN.")
