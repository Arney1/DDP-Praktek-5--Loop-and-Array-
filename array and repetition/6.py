n = 10

x = [0] * n # Initialize list 'x' with n elements, with a value of 0 (or you can start with an empty list `x = []`)

for i in range(n):
    while True:
            try:
                x[i] = int(input(f"Masukkan angka ke-{i+1}: "))
                break
            except:
                print("\033[91mAngka woy!!!\033[0m")

maksimum = x[0]
minimum = x[0]

for i in range(1, n):
    if x[i] > maksimum:
        maksimum = x[i]
    if x[i] < minimum:
        minimum = x[i]

print(f"\nNilai maksimum nya adalah {maksimum}")
print(f"Nilai minimum nya adalah {minimum}")
print(f"Selisih nilai maksimum dan minimum = {maksimum - minimum}")
