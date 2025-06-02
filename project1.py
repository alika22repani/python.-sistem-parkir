import random 
# pilihan yang tersedia 
pilihan = ["batu", "gunting", "kertas"]

# komputer memilih secara random 
komputer = random.choice(pilihan)

# pemain memilih 
pemain = input("pilih batu, gunting, atau kertas: ").lower()

# tampilkan pilihan 
print(f"batu: {pemain}")
print(f"komputer memilih: {komputer}")

# Tentukan siapa yang menang 
if pemain == komputer:
    print("seri!")
elif (pemain == "batu" and komputer == "gunting") or\
     (pemain == "gunting" and komputer == "kertas") or\
     (pemain == "kertas" and komputer == "batu"):
    print("kamu menang!")
else:
    print("komputer menang!")
