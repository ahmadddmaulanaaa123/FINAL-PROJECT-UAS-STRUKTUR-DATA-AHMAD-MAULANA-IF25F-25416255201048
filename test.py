import csv
import os
from collections import deque

FILE_CSV = "pasien.csv"

# =========================
# DATABASE CSV
# =========================

def load_data():
    data = {}

    if os.path.exists(FILE_CSV):
        with open(FILE_CSV, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data[row['id']] = row

    return data


def save_data(data):
    with open(FILE_CSV, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['id', 'nama', 'umur', 'keluhan']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for pasien in data.values():
            writer.writerow(pasien)


# =========================
# CRUD
# =========================

def tambah_pasien(data, antrian):
    id_pasien = input("ID Pasien : ")

    if id_pasien in data:
        print("ID sudah ada!")
        return

    nama = input("Nama      : ")
    umur = input("Umur      : ")
    keluhan = input("Keluhan   : ")

    data[id_pasien] = {
        "id": id_pasien,
        "nama": nama,
        "umur": umur,
        "keluhan": keluhan
    }

    antrian.append(id_pasien)

    save_data(data)

    print("Pasien berhasil ditambahkan.")


def tampil_data(data):
    if not data:
        print("Data kosong.")
        return

    print("\n=== DATA PASIEN ===")

    for pasien in data.values():
        print(
            f"ID: {pasien['id']} | "
            f"Nama: {pasien['nama']} | "
            f"Umur: {pasien['umur']} | "
            f"Keluhan: {pasien['keluhan']}"
        )


def cari_pasien(data):
    keyword = input("Masukkan ID atau Nama: ").lower()

    ditemukan = False

    for pasien in data.values():
        if keyword in pasien['id'].lower() or keyword in pasien['nama'].lower():
            print(
                f"ID: {pasien['id']} | "
                f"Nama: {pasien['nama']} | "
                f"Umur: {pasien['umur']} | "
                f"Keluhan: {pasien['keluhan']}"
            )
            ditemukan = True

    if not ditemukan:
        print("Pasien tidak ditemukan.")


def update_pasien(data):
    id_pasien = input("Masukkan ID pasien: ")

    if id_pasien not in data:
        print("Data tidak ditemukan.")
        return

    nama = input("Nama baru    : ")
    umur = input("Umur baru    : ")
    keluhan = input("Keluhan baru : ")

    data[id_pasien]['nama'] = nama
    data[id_pasien]['umur'] = umur
    data[id_pasien]['keluhan'] = keluhan

    save_data(data)

    print("Data berhasil diperbarui.")


def hapus_pasien(data):
    id_pasien = input("Masukkan ID pasien: ")

    if id_pasien not in data:
        print("Data tidak ditemukan.")
        return

    del data[id_pasien]

    save_data(data)

    print("Data berhasil dihapus.")


# =========================
# QUEUE (ANTRIAN)
# =========================

def panggil_antrian(data, antrian):
    if not antrian:
        print("Tidak ada antrian.")
        return

    id_pasien = antrian.popleft()

    if id_pasien in data:
        print("\nPasien berikutnya:")
        print(f"{data[id_pasien]['nama']} ({id_pasien})")


def tampil_antrian(data, antrian):
    if not antrian:
        print("Antrian kosong.")
        return

    print("\n=== ANTRIAN PASIEN ===")

    nomor = 1

    for id_pasien in antrian:
        if id_pasien in data:
            print(
                f"{nomor}. "
                f"{data[id_pasien]['nama']} "
                f"({id_pasien})"
            )
            nomor += 1


# =========================
# SORTING
# =========================

def sorting_pasien(data):
    print("\n1. Sort Nama")
    print("2. Sort Umur")

    pilih = input("Pilih: ")

    daftar = list(data.values())

    if pilih == "1":
        daftar.sort(key=lambda x: x['nama'])

    elif pilih == "2":
        daftar.sort(key=lambda x: int(x['umur']))

    else:
        print("Pilihan tidak valid.")
        return

    print("\n=== HASIL SORTING ===")

    for pasien in daftar:
        print(
            f"{pasien['id']} | "
            f"{pasien['nama']} | "
            f"{pasien['umur']} | "
            f"{pasien['keluhan']}"
        )


# =========================
# MENU
# =========================

def menu():
    data = load_data()
    antrian = deque()

    while True:
        print("\n")
        print("=" * 40)
        print("SISTEM ANTRIAN RUMAH SAKIT")
        print("=" * 40)
        print("1. Tambah Pasien")
        print("2. Tampilkan Data")
        print("3. Cari Pasien")
        print("4. Update Pasien")
        print("5. Hapus Pasien")
        print("6. Panggil Antrian")
        print("7. Tampilkan Antrian")
        print("8. Sorting Data")
        print("9. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_pasien(data, antrian)

        elif pilihan == "2":
            tampil_data(data)

        elif pilihan == "3":
            cari_pasien(data)

        elif pilihan == "4":
            update_pasien(data)

        elif pilihan == "5":
            hapus_pasien(data)

        elif pilihan == "6":
            panggil_antrian(data, antrian)

        elif pilihan == "7":
            tampil_antrian(data, antrian)

        elif pilihan == "8":
            sorting_pasien(data)

        elif pilihan == "9":
            print("Terima kasih.")
            break

        else:
            print("Pilihan tidak tersedia.")


menu()