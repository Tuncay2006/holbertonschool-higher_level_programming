#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        # Her satır için tüm sayıları str.format ile yazdıracağız.
        # Sayıları boşluk ile ayırıp, satır sonunda yeni satıra geçeceğiz.
        for i, num in enumerate(row):
            # Eğer son sayı değilse, sonrasında boşluk bırak
            if i < len(row) - 1:
                print("{:d}".format(num), end=" ")
            else:
                print("{:d}".format(num))  # satır sonu
