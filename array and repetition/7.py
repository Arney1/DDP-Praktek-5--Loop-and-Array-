n = 10

x = [0] * n # Initialize list 'x' with n elements, with a value of 0 (or you can start with an empty list `x = []`)

for i in range(n):
    while True:
            try:
                x[i] = int(input(f"Masukkan angka ke-{i+1}: "))
                break
            except:
                print("\033[91mAngka woy!!!\033[0m")

if n % 2 == 1:
    ganjil = True
    indexMedian = n//2
else:
    ganjil = False
    indexMedian = n//2


for i in range(n):
    minimum = x[i]
    p = 0
    for j in range(i, n):
        if x[j] < minimum:
            minimum = x[j]
            p = j
    if minimum != x[i]:
        x[p] = x[i]
        x[i] = minimum

print(x)

if ganjil:
    median = x[n//2]
else:
    median = (x[n//2] + x[n//2-1])/2

print(f"\nNilai median nya adalah {median}")
