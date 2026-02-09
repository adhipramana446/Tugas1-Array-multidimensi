MAX_CAPACITY = 10
mahasiswa = [[None] * 3 for _ in range(MAX_CAPACITY)]
count = 0

def show_data():
    print("\n--- DAFTAR MAHASISWA ---")
    if count == 0:
        print("Array Kosong.")
    else:
        for i in range(count):
            print(f"{i}. [NIM: {mahasiswa[i][0]}, Nama: {mahasiswa[i][1]}, Kelas: {mahasiswa[i][2]}]")
    print("------------------------")

def insert_at_beginning():
    global count
    if count >= MAX_CAPACITY: return print("Penuh!")
    nim, nama, kelas = input("NIM: "), input("Nama: "), input("Kelas: ")
    for i in range(count, 0, -1): mahasiswa[i] = mahasiswa[i-1]
    mahasiswa[0] = [nim, nama, kelas]
    count += 1

def insert_at_position():
    global count
    if count >= MAX_CAPACITY: return print("Penuh!")
    pos = int(input(f"Posisi (0-{count}): "))
    if 0 <= pos <= count:
        nim, nama, kelas = input("NIM: "), input("Nama: "), input("Kelas: ")
        for i in range(count, pos, -1): mahasiswa[i] = mahasiswa[i-1]
        mahasiswa[pos] = [nim, nama, kelas]
        count += 1
    else: print("Posisi tidak valid")

def insert_at_end():
    global count
    if count >= MAX_CAPACITY: return print("Penuh!")
    mahasiswa[count] = [input("NIM: "), input("Nama: "), input("Kelas: ")]
    count += 1

def delete_from_beginning():
    global count
    if count == 0: return print("Kosong!")
    for i in range(count - 1): mahasiswa[i] = mahasiswa[i+1]
    count -= 1

def delete_given_position():
    global count
    pos = int(input(f"Hapus posisi (0-{count-1}): "))
    if 0 <= pos < count:
        for i in range(pos, count - 1): mahasiswa[i] = mahasiswa[i+1]
        count -= 1
    else: print("Posisi tidak valid")

def delete_from_end():
    global count
    if count > 0: count -= 1
    else: print("Kosong!")

def delete_first_occurrence():
    global count
    target = input("NIM yang dihapus: ")
    for i in range(count):
        if mahasiswa[i][0] == target:
            for j in range(i, count - 1): mahasiswa[j] = mahasiswa[j+1]
            count -= 1
            print("Berhasil dihapus.")
            return
    print("Tidak ditemukan.")

# --- MAIN LOOP ---
while True:
    print("\n=== Pilih Menu ===")
    print("1.Insert at beginning")
    print("2.Insert at given position") 
    print("3.Insert at end") 
    print("4.Delete from beginningn") 
    print("5.Delete given position") 
    print("6.Delete from end") 
    print("7.Delete first occurence") 
    print("8.Show Data")
    print("9.Exit")

    menu = input("\nPilih: ")
    if menu == "1": insert_at_beginning()
    elif menu == "2": insert_at_position()
    elif menu == "3": insert_at_end()
    elif menu == "4": delete_from_beginning()
    elif menu == "5": delete_given_position()
    elif menu == "6": delete_from_end()
    elif menu == "7": delete_first_occurrence()
    elif menu == "8": show_data()
    elif menu == "9": break
