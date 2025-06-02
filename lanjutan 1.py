data = [94, 37, 25,82, 22, 11, 90]

for i in range(len(data)):
    for j in range(0, len(data) - i - 1):
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]

print("Hasil bubble sort:", data)