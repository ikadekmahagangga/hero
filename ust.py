from collections import deque
import sys

code2 = deque()
totalPesanan = 0
class resto():

    def insertData(self,data):
        code2.append(data)

    def showData(self):
        print("==========menu===========")
        print(code2)
        print("===================================")
        pilihan = str(input("Kembali ke menu utama ? (y) "))
        if (pilihan == "y") or (pilihan == "Y"):
            self.mainMenu()

    def haci(self):
        print("Telah Di bayar:")
        for i in range(totalPesanan):
            print(code2[i])
        pilihan = str(input("mau pesan lagi ? silakan ketik ya atau tidak : "))
        if (pilihan == "y") or (pilihan == "Y"):
            self.mainMenu()

    def mainMenu(self):
        print("===================================")
        print("Nama : i kadek mahagangga")
        print("NIM  : 21101203")
        print("===================================")
        print("Masukan Pilihan anda")
        print("===================================")
        print("1. Pesan")
        print("2. Lihat Pesanan")
        print("3. Bayar")
        print("4. Hapus")
        pilihan = str(input("Masukan pesanan anda : "))
        if(pilihan=="1"):
            self.cross()
        elif(pilihan =="2"):
            self.haci()
        elif(pilihan =="3"):
            self.showData()
        elif(pilihan =="4"):
            print("===================================")
            print("makasi sudah memesan makan")
            print("===================================")
            sys.exit(0)

    def cross(self):
        ulang = 1
        global totalPesanan
        while (ulang != "5"):
            print("===================================")
            print("Masukan Pilihan Menu")
            print("===================================")
            print("1. Paket Gurami Pedas Manis")
            print("2. Paket Ikan Bakar")
            print("3. Paket Lalapan Ayam")
            print("4. Paket lalapan lele")
            print("5. Menu utama")
            obj = str(input("Masukan data anda : "))
            if obj == "5":
                self.mainMenu()
            elif(obj == "1"):
                totalPesanan = totalPesanan + 1
                self.insertData("Paket Gurami Pedas Manis")
            elif(obj == "2"):
                totalPesanan += 1
                self.insertData("Paket Ikan Bakar")
            elif(obj == "3"):
                totalPesanan += 1
                self.insertData("Paket Lalapan Ayam")
            elif(obj == "4"):
                totalPesanan += 1
                self.insertData("Paket lalapan lele")

l = resto()
l.mainMenu()