#This is the main page of our python project

def perkenalan (nim, name):
    print("Nama : " + name)
    print("NIM : " + nim)
    print("Kelas : TI A")

jumlah = input ("Masukkan jumlah murid : ")
for i in range (int(jumlah)):
    nim = input("Masukkan NIM : ")
    name = input("Masukkan Nama : ")
    perkenalan(nim, name)
    print("\n")
    #code co-engineered with Copilot
