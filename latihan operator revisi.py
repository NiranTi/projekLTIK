#Nama: Niranti Salmanabilah NIM: 2401336
#kelas 1C RPL
jumlahBarang = int(input("Berapa jumlah barang yang akan dihitung total harganya? "))

if jumlahBarang > 0:
    if jumlahBarang < 100:
        print(f"Total harga barang tersebut adalah Rp. {jumlahBarang*5000}")
    elif jumlahBarang >= 100 and jumlahBarang <= 150:
        print(f"Total harga barang tersebut adalah Rp. {jumlahBarang*4000}")
    elif jumlahBarang > 150:
        print(f"Total harga barang tersebut adalah Rp. {jumlahBarang*2500}")
else :
    print("Input error")
