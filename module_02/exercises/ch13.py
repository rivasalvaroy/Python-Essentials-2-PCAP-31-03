try:
    print("alpha"[1/0])
except ZeroDivisionError:
    print("cero")
except IndexError:
    print("índice")
except:
    print("algo")
