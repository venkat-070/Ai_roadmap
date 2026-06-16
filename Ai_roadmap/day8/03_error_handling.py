def safe_divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Error: cannot divide by zero")
        return None
    except TypeError:
        print("Error: Enter numbers only!")
        return None
safe_divide(10,0)
safe_divide(30,'a')
print(safe_divide(10,5))