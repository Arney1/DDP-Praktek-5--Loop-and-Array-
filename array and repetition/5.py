n = 10

x = [0] * n # Initialize list 'x' with n elements, with a value of 0 (or you can start with an empty list `x = []`)

for i in range(n):
    while True:
            try:
                x[i] = int(input(f"Masukkan angka ke-{i+1}: "))
                break
            except:
                print("\033[91mAngka woy!!!\033[0m")

total = x[0]

for i in range(1, n):
    total += x[i]

print(f"\nRata-rata nilai array X adalah {total/n}")
