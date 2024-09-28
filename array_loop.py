
while True:
        try:
            x = int(input("Masukkan angka: "))
            break
        except:
            print("\033[91mAngka woy!!!\033[0m")

if x > 0:
    print("angka tersebut adalah bilangan positif")
elif x == 0:
    print("angka tersebut adalah 0")
else:
    print("angka tersebut adalah bilangan negatif")
