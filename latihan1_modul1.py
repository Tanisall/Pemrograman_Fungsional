# KEGIATAN 1

#  deklarasi fungsi penjumlahan
# def add(x, y):
#     return x + y
# result = add(3, 5)
# print("Hasil Penjumlahan: ", result)


# deklarasi fungsi pengurangan
# def minus(x, y):
#     return x - y


# result = minus(10, 5)
# print("Hasil Pengurangan: ", result)


# deklarasi fungsi perkalian
# def mult(x, y):
#     return x * y


# result = mult(20, 2)
# print("Hasil Perkalian: ", result)


# deklarasi fungsi pembagian
# def div(x, y):
#     return x / y


# result = div(10, 2)
# print("Hasil Pembagian: ", result)


# KOMBINASI FUNGSI TREE
# Deklarasi fungsi penjumlahan
def add(x, y):
    return x + y


# Deklarasi fungsi pengurangan
def minus(x, y):
    return x - y


# Deklarasi fungsi perkalian
def mult(x, y):
    return x * y


# Deklarasi fungsi pembagian
def div(x, y):
    if y == 0:
        return "Pembagian oleh nol tidak valid"
    return x / y


def tree(expression):
    if isinstance(expression, tuple):
        left = expression[0]
        operator = expression[1]
        right = expression[2]

        if operator == "+":
            return add(tree(left), tree(right))
        elif operator == "-":
            return minus(tree(left), tree(right))
        elif operator == "*":
            return mult(tree(left), tree(right))
        elif operator == "/":
            return div(tree(left), tree(right))
        else:
            return "Operator tidak valid"
    else:
        return expression


# Contoh penggunaan pohon ekspresi
expression_tree = ((2, "+", 3), "*", (5, "-", 1))
result = tree(expression_tree)
print("Hasil evaluasi pohon ekspresi: ", result)
