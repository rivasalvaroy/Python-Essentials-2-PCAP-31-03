def bad_fun(n):
    raise ZeroDivisionError


try:
    bad_fun(0)
except ArithmeticError:
    print("¿Que pasó? ¿Un error?")

print("FIN.")
