import java.util.Scanner;

public class Array1 {
    // Kapasitas array 10 sesuai instruksi
    static String[][] mahasiswa = new String[10][3]; 
    static int count = 0;
    static Scanner input = new Scanner(System.in);

    public static void main(String[] args) {
        int pilihan;
        do {
            System.out.println("\n=== PROGRAM DATA MAHASISWA ===");
            System.out.println("1. Insert at Beginning");
            System.out.println("2. Insert at Given Position");
            System.out.println("3. Insert at End");
            System.out.println("4. Delete from Beginning");
            System.out.println("5. Delete Given Position");
            System.out.println("6. Delete from End");
            System.out.println("7. Delete First Occurrence (by NIM)");
            System.out.println("8. Show Data");
            System.out.println("9. Exit");
            System.out.print("Pilih menu: ");
            
            pilihan = input.nextInt();
            input.nextLine(); // Membersihkan buffer

            switch (pilihan) {
                case 1: insertAtBeginning(); break;
                case 2: insertAtPosition(); break;
                case 3: insertAtEnd(); break;
                case 4: deleteFromBeginning(); break;
                case 5: deleteGivenPosition(); break;
                case 6: deleteFromEnd(); break;
                case 7: deleteFirstOccurrence(); break;
                case 8: showData(); break;
                case 9: System.out.println("Program Selesai."); break;
                default: System.out.println("Pilihan tidak valid!");
            }
        } while (pilihan != 9);
    }

    // --- FUNGSI INSERT ---

    public static void insertAtBeginning() {
        if (count >= 10) {
            System.out.println("Error: Array Penuh!");
            return;
        }
        System.out.print("NIM: "); String nim = input.nextLine();
        System.out.print("Nama: "); String nama = input.nextLine();
        System.out.print("Kelas: "); String kelas = input.nextLine();

        // Geser semua ke kanan
        for (int i = count; i > 0; i--) {
            mahasiswa[i] = mahasiswa[i - 1];
        }
        mahasiswa[0] = new String[]{nim, nama, kelas};
        count++;
        System.out.println("Data berhasil ditambah di awal.");
    }

    public static void insertAtPosition() {
        if (count >= 10) {
            System.out.println("Error: Array Penuh!");
            return;
        }
        System.out.print("Masukkan posisi index (0-" + count + "): ");
        int pos = input.nextInt(); input.nextLine();

        if (pos >= 0 && pos <= count) {
            System.out.print("NIM: "); String nim = input.nextLine();
            System.out.print("Nama: "); String nama = input.nextLine();
            System.out.print("Kelas: "); String kelas = input.nextLine();

            for (int i = count; i > pos; i--) {
                mahasiswa[i] = mahasiswa[i - 1];
            }
            mahasiswa[pos] = new String[]{nim, nama, kelas};
            count++;
            System.out.println("Data berhasil ditambah di posisi " + pos);
        } else {
            System.out.println("Posisi tidak valid!");
        }
    }

    public static void insertAtEnd() {
        if (count >= 10) {
            System.out.println("Error: Array Penuh!");
            return;
        }
        System.out.print("NIM: "); String nim = input.nextLine();
        System.out.print("Nama: "); String nama = input.nextLine();
        System.out.print("Kelas: "); String kelas = input.nextLine();

        mahasiswa[count] = new String[]{nim, nama, kelas};
        count++;
        System.out.println("Data berhasil ditambah di akhir.");
    }

    // --- FUNGSI DELETE ---

    public static void deleteFromBeginning() {
        if (count == 0) {
            System.out.println("Error: Array Kosong!");
            return;
        }
        for (int i = 0; i < count - 1; i++) {
            mahasiswa[i] = mahasiswa[i + 1];
        }
        count--;
        System.out.println("Data di awal berhasil dihapus.");
    }

    public static void deleteGivenPosition() {
        if (count == 0) {
            System.out.println("Error: Array Kosong!");
            return;
        }
        System.out.print("Hapus index ke: ");
        int pos = input.nextInt(); input.nextLine();

        if (pos >= 0 && pos < count) {
            for (int i = pos; i < count - 1; i++) {
                mahasiswa[i] = mahasiswa[i + 1];
            }
            count--;
            System.out.println("Data di posisi " + pos + " dihapus.");
        } else {
            System.out.println("Posisi tidak ditemukan!");
        }
    }

    public static void deleteFromEnd() {
        if (count == 0) {
            System.out.println("Error: Array Kosong!");
            return;
        }
        count--;
        System.out.println("Data terakhir berhasil dihapus.");
    }

    public static void deleteFirstOccurrence() {
        if (count == 0) {
            System.out.println("Error: Array Kosong!");
            return;
        }
        System.out.print("Masukkan NIM yang ingin dihapus: ");
        String target = input.nextLine();

        for (int i = 0; i < count; i++) {
            if (mahasiswa[i][0].equals(target)) {
                for (int j = i; j < count - 1; j++) {
                    mahasiswa[j] = mahasiswa[j + 1];
                }
                count--;
                System.out.println("NIM " + target + " berhasil dihapus.");
                return;
            }
        }
        System.out.println("NIM tidak ditemukan.");
    }

    // --- TAMPILKAN DATA ---

    public static void showData() {
        System.out.println("\n--- DATA MAHASISWA ---");
        if (count == 0) {
            System.out.println("Kosong.");
        } else {
            for (int i = 0; i < count; i++) {
                System.out.println("[" + i + "] NIM: " + mahasiswa[i][0] + 
                                   " | Nama: " + mahasiswa[i][1] + 
                                   " | Kelas: " + mahasiswa[i][2]);
            }
        }
    }
}