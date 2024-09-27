
while True:
        try:
            x = int(input("Masukkan angka "))
            break
        except:
            print("\033[91mAngka woy!!!\033[0m")

if x > 0:
    print("x adalah bilangan positif")
elif x == 0:
    print("x adalah 0")
else:
    print("x adalah bilangan negatif")
