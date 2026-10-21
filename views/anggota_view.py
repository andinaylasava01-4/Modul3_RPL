# Mengambil library customtkinter dan disingkat menjadi ctk
# customtkinter digunakan untuk membuat tampilan GUI
import customtkinter as ctk

# Mengambil ttk dari tkinter
# ttk digunakan untuk membuat tabel (Treeview)
from tkinter import ttk


# Membuat class bernama AnggotaView
# ctk.CTk adalah dasar untuk membuat jendela GUI
class AnggotaView(ctk.CTk):

    # __init__ dijalankan otomatis saat AnggotaView dibuat
    def __init__(self):

        # Menjalankan pengaturan awal dari ctk.CTk
        # Supaya jendela GUI dapat dibuat
        super().__init__()

        # Memberikan judul pada jendela
        self.title("Sistem Manajemen Perpustakaan - Data Anggota")

        # Menentukan ukuran jendela
        # Lebar = 800, tinggi = 480
        self.geometry("800x480")


        # ==============================
        # KONFIGURASI GRID UTAMA
        # ==============================

        # Membuat 2 kolom pada jendela utama
        # Kolom 0 = bagian kiri/form
        # weight=1 berarti mendapatkan ruang lebih kecil
        self.grid_columnconfigure(0, weight=1)

        # Kolom 1 = bagian kanan/tabel
        # weight=2 berarti mendapatkan ruang lebih besar
        self.grid_columnconfigure(1, weight=2)

        # Membuat baris pertama dapat menyesuaikan ukuran jendela
        self.grid_rowconfigure(0, weight=1)


        # ==============================
        # FRAME KIRI: FORM ANGGOTA
        # ==============================

        # Membuat frame untuk bagian kiri
        # Frame digunakan sebagai wadah untuk komponen form
        self.frame_kiri = ctk.CTkFrame(self)

        # Menempatkan frame kiri pada:
        # row=0    → baris pertama
        # column=0 → kolom pertama/kiri
        # padx=10  → jarak kiri-kanan
        # pady=10  → jarak atas-bawah
        # sticky="nsew" → frame mengikuti ukuran ruang yang tersedia
        self.frame_kiri.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            sticky="nsew"
        )


        # Membuat tulisan "Form Data Anggota"
        # CTkLabel digunakan untuk menampilkan teks
        # font Arial ukuran 16 dan dibuat tebal
        ctk.CTkLabel(
            self.frame_kiri,
            text="Form Data Anggota",
            font=("Arial", 16, "bold")
        ).pack(pady=15)


        # ==============================
        # INPUT NAMA ANGGOTA
        # ==============================

        # Membuat kotak input untuk memasukkan nama anggota
        self.entry_nama = ctk.CTkEntry(
            self.frame_kiri,
            placeholder_text="Masukkan Nama Anggota"
        )

        # Menempatkan kotak input
        # pady=8 → jarak atas dan bawah
        # padx=15 → jarak kiri dan kanan
        # fill="x" → kotak diperlebar secara horizontal
        self.entry_nama.pack(
            pady=8,
            padx=15,
            fill="x"
        )


        # ==============================
        # INPUT ALAMAT ANGGOTA
        # ==============================

        # Membuat kotak input untuk memasukkan alamat anggota
        self.entry_alamat = ctk.CTkEntry(
            self.frame_kiri,
            placeholder_text="Masukkan Alamat Anggota"
        )

        # Menempatkan kotak input alamat
        self.entry_alamat.pack(
            pady=8,
            padx=15,
            fill="x"
        )


        # ==============================
        # TOMBOL AKSI
        # ==============================

        # Membuat tombol untuk menyimpan data
        # fg_color="green" → warna tombol hijau
        self.btn_simpan = ctk.CTkButton(
            self.frame_kiri,
            text="Simpan Data",
            fg_color="green"
        )

        # Menempatkan tombol Simpan
        self.btn_simpan.pack(
            pady=(15, 5),
            padx=15,
            fill="x"
        )


        # Membuat tombol untuk memperbarui data
        # fg_color="blue" → warna tombol biru
        self.btn_update = ctk.CTkButton(
            self.frame_kiri,
            text="Perbarui Data (Update)",
            fg_color="blue"
        )

        # Menempatkan tombol Update
        self.btn_update.pack(
            pady=5,
            padx=15,
            fill="x"
        )


        # Membuat tombol untuk menghapus data
        # fg_color="red" → warna tombol merah
        self.btn_delete = ctk.CTkButton(
            self.frame_kiri,
            text="Hapus Data (Delete)",
            fg_color="red"
        )

        # Menempatkan tombol Delete
        self.btn_delete.pack(
            pady=5,
            padx=15,
            fill="x"
        )


        # ==============================
        # FRAME KANAN: TABEL ANGGOTA
        # ==============================

        # Membuat frame untuk bagian kanan
        # Frame ini menjadi wadah untuk tabel
        self.frame_kanan = ctk.CTkFrame(self)

        # Menempatkan frame kanan pada:
        # row=0 → baris pertama
        # column=1 → kolom kedua/kanan
        self.frame_kanan.grid(
            row=0,
            column=1,
            padx=10,
            pady=10,
            sticky="nsew"
        )


        # Membuat judul di atas tabel
        ctk.CTkLabel(
            self.frame_kanan,
            text="Daftar Anggota Perpustakaan",
            font=("Arial", 16, "bold")
        ).pack(pady=15)


        # ==============================
        # MEMBUAT TABEL
        # ==============================

        # Menentukan nama kolom tabel
        # id_anggota → ID anggota
        # nama_anggota → nama anggota
        # alamat → alamat anggota
        kolom = (
            "id_anggota",
            "nama_anggota",
            "alamat"
        )


        # Membuat tabel menggunakan Treeview
        # columns=kolom → menggunakan kolom yang sudah dibuat
        # show="headings" → hanya menampilkan bagian judul kolom
        # height=15 → tinggi tabel sekitar 15 baris
        self.tabel = ttk.Treeview(
            self.frame_kanan,
            columns=kolom,
            show="headings",
            height=15
        )


        # ==============================
        # JUDUL SETIAP KOLOM
        # ==============================

        # Kolom id_anggota ditampilkan dengan nama "ID Anggota"
        self.tabel.heading(
            "id_anggota",
            text="ID Anggota"
        )

        # Kolom nama_anggota ditampilkan dengan nama "Nama Anggota"
        self.tabel.heading(
            "nama_anggota",
            text="Nama Anggota"
        )

        # Kolom alamat ditampilkan dengan nama "Alamat"
        self.tabel.heading(
            "alamat",
            text="Alamat"
        )


        # ==============================
        # MENGATUR LEBAR KOLOM
        # ==============================

        # Mengatur lebar kolom ID menjadi 80
        # anchor="center" → isi berada di tengah
        self.tabel.column(
            "id_anggota",
            width=80,
            anchor="center"
        )

        # Mengatur lebar kolom nama menjadi 160
        self.tabel.column(
            "nama_anggota",
            width=160
        )

        # Mengatur lebar kolom alamat menjadi 200
        self.tabel.column(
            "alamat",
            width=200
        )


        # Menempatkan tabel ke dalam frame kanan
        # fill="both" → tabel dapat melebar ke horizontal dan vertikal
        # expand=True → tabel ikut memperbesar diri ketika jendela diperbesar
        self.tabel.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=10
        )


# Mengecek apakah file ini dijalankan secara langsung
if __name__ == "__main__":

    # Membuat objek dari class AnggotaView
    # Saat ini dijalankan, __init__() otomatis dipanggil
    app = AnggotaView()

    # Menjalankan jendela GUI
    # Supaya jendela tetap terbuka dan dapat menerima interaksi
    app.mainloop()