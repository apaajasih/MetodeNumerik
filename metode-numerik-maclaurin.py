import math

def maclaurin_sin(x):
    return x - (x**3)/math.factorial(3) + (x**5)/math.factorial(5)
def maclaurin_cos(x):
    return 1 - (x**2)/math.factorial(2) + (x**4)/math.factorial(4)
def maclaurin_tan(x):
    # # Menghitung nilai tan(x) menggunakan sin(x) dan cos(x)
    # sin_value = sin_maclaurin(x)
    # cos_value = cos_maclaurin(x)
    # return sin_value/cos_value
    return x + (x**3)/3

x = 0 #bisa diubah
sin_x = maclaurin_sin(x)
cos_x = maclaurin_cos(x)
tan_x = maclaurin_tan(x)

print(f'sin ({x}) = ({sin_x})')
print(f'cos ({x}) = ({cos_x})')
print(f'tan ({x}) = ({tan_x})')
