import texttable as tt
import getpass
from Perhitungan.penilaian import nilai_mahasiswa
from Perhitungan.uang_kuliah import pembayaran
from Perhitungan.calculator import menu_cal


def menu():
    print("================================================")
    print("\n\t---pilihan---")
    print("\t1. penilaian mahasiswa")
    print("\t2. pembayaran mahasiswa")
    print("\t3. calculator")

    pilih = input("\n\tsilahkan pilih : ")
    if pilih == "1":
        nilai_mahasiswa()
    elif pilih== "2" :
        pembayaran()
    elif pilih== "3" :
        menu_cal()
    else:
        exit
    tanya()

def tanya():
    tanya = input("\nkembali ke menu (y/t)? ")
    if tanya == "y":
        menu()
    elif tanya == "t":
        exit
    else:
        print("\n\tSalah input.................!!!")

username = input("\nUsername : ")
password = getpass.getpass()
print("===============================================")

if username == "kilibon" and password == "pb17":
    menu()

else:
    print ("Maaf, Username atau Password Anda Salah..!!")

