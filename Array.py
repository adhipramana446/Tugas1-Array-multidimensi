# Inisialisasi array 2D dengan kapasitas 10 baris dan 4 kolom (Nama, NIM, Kelas, Alamat)
# Kita isi dengan None untuk mensimulasikan fixed-size array
data = [[None for _ in range(4)] for _ in range(10)]
count = 0

def insert_data(pos):
    global count
    if count >= 10:
        print("\n[!] Error: Array Penuh! Kapasitas maksimal adalah 10.")
        return
    if pos < 0 or pos > count:
        print(f"\n[!] Error: Posisi tidak valid! Masukkan antara 0 sampai {count}.")
        return

    print(f"\n--- Input Data Mahasiswa (Posisi: {pos}) ---")
    nama = input("Nama   : ")
    nim = input("NIM    : ")
    kelas = input("Kelas  : ")
    alamat = input("Alamat : ")

    # Shifting/Menggeser data ke bawah (kanan) untuk memberi ruang
    for i in range(count, pos, -1):
        data[i] = data[i-1][:] # Salin baris sebelumnya ke baris setelahnya
    
    # Isi data pada posisi yang ditentukan
    data[pos] = [nama, nim, kelas, alamat]
    count += 1
    print("[+] Data berhasil ditambahkan.")

def delete_data(pos):
    global count
    if count == 0:
        print("\n[!] Error: Array Kosong!")
        return
    if pos < 0 or pos >= count:
        print("\n[!] Error: Posisi tidak valid!")
        return

    # Shifting/Menggeser data ke atas (kiri) untuk mengisi kekosongan
    for i in range(pos, count - 1):
        data[i] = data[i+1]
    
    # Reset baris terakhir yang sudah kosong
    data[count-1] = [None, None, None, None]
    count -= 1
    print("[-] Data pada posisi tersebut berhasil dihapus.")

def delete_first_occurrence():
    target = input("\nMasukkan NIM yang ingin dihapus: ")
    for i in range(count):
        if data[i][1] == target: # Kolom indeks 1 adalah NIM
            delete_data(i)
            return
    print("[!] NIM tidak ditemukan.")

def show_data():
    if count == 0:
        print("\n[i] Data masih kosong.")
        return
    
    print("\n" + "="*70)
    print(f"{'No':<3} | {'NIM':<10} | {'Nama':<15} | {'Kls':<5} | {'Alamat':<15}")
    print("-" * 70)
    for i in range(count):
        print(f"{i:<3} | {data[i][1]:<10} | {data[i][0]:<15} | {data[i][2]:<5} | {data[i][3]:<15}")
    print("="*70)

# Main Menu Loop
while True:
    print(f"\n--- MENU ARRAY MAHASISWA (Data Terisi: {count}/10) ---")
    print("1. Insert Beginning")
    print("2. Insert at Given Position")
    print("3. Insert End")
    print("4. Delete from Beginning")
    print("5. Delete Given Position")
    print("6. Delete from End")
    print("7. Delete First Occurrence (by NIM)")
    print("8. Show Data")
    print("9. Exit")
    
    pilihan = input("\nPilih menu (1-9): ")
    
    if pilihan == '1':
        insert_data(0)
    elif pilihan == '2':
        try:
            p = int(input(f"Masukkan posisi (0-{count}): "))
            insert_data(p)
        except ValueError:
            print("[!] Harap masukkan angka untuk posisi.")
    elif pilihan == '3':
        insert_data(count)
    elif pilihan == '4':
        delete_data(0)
    elif pilihan == '5':
        try:
            p = int(input(f"Masukkan posisi yang dihapus (0-{count-1}): "))
            delete_data(p)
        except ValueError:
            print("[!] Harap masukkan angka.")
    elif pilihan == '6':
        delete_data(count - 1)
    elif pilihan == '7':
        delete_first_occurrence()
    elif pilihan == '8':
        show_data()
    elif pilihan == '9':
        print("Program selesai. Sampai jumpa!")
        break
    else:
        print("[!] Pilihan tidak tersedia.")

        