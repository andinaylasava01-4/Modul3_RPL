import customtkinter as ctk
from tkinter import ttk

class BukuView(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sistem Manajemen Perpustakaan")
        self.geometry("1100x600")
        self.minsize(900, 500)

        # Konfigurasi tampilan tabel
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "Treeview",
            rowheight=35,
            font=("Arial", 11),
            background="#FFFFFF",
            foreground="#222222",
            fieldbackground="#FFFFFF"
        )
        style.configure(
            "Treeview.Heading",
            font=("Arial", 11, "bold"),
            padding=10
        )
        style.map(
            "Treeview",
            background=[("selected", "#D6EAF8")],
            foreground=[("selected", "#222222")]
        )

        # Grid utama
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

        # FRAME KIRI: FORM BUKU
        self.frame_kiri = ctk.CTkFrame(self)
        self.frame_kiri.grid(
            row=0, column=0, padx=12, pady=12, sticky="nsew"
        )

        ctk.CTkLabel(
            self.frame_kiri,
            text="Form Data Buku",
            font=("Arial", 20, "bold")
        ).pack(pady=(25, 20))

        self.entry_judul = ctk.CTkEntry(
            self.frame_kiri,
            placeholder_text="Masukkan Judul Buku",
            height=38
        )
        self.entry_judul.pack(pady=8, padx=18, fill="x")

        self.entry_penulis = ctk.CTkEntry(
            self.frame_kiri,
            placeholder_text="Masukkan Nama Penulis",
            height=38
        )
        self.entry_penulis.pack(pady=8, padx=18, fill="x")

        self.entry_tahun = ctk.CTkEntry(
            self.frame_kiri,
            placeholder_text="Tahun Terbit (Misal: 2024)",
            height=38
        )
        self.entry_tahun.pack(pady=8, padx=18, fill="x")

        self.btn_simpan = ctk.CTkButton(
            self.frame_kiri,
            text="Simpan Data",
            fg_color="#16803C",
            hover_color="#11632E",
            height=38
        )
        self.btn_simpan.pack(pady=(20, 6), padx=18, fill="x")

        self.btn_update = ctk.CTkButton(
            self.frame_kiri,
            text="Perbarui Data",
            fg_color="#2563EB",
            hover_color="#1D4ED8",
            height=38
        )
        self.btn_update.pack(pady=6, padx=18, fill="x")

        self.btn_hapus = ctk.CTkButton(
            self.frame_kiri,
            text="Hapus Data",
            fg_color="#DC2626",
            hover_color="#B91C1C",
            height=38
        )
        self.btn_hapus.pack(pady=6, padx=18, fill="x")

        # FRAME KANAN: DAFTAR BUKU
        self.frame_kanan = ctk.CTkFrame(self)
        self.frame_kanan.grid(
            row=0, column=1, padx=12, pady=12, sticky="nsew"
        )
        self.frame_kanan.grid_columnconfigure(0, weight=1)
        self.frame_kanan.grid_rowconfigure(1, weight=1)

        ctk.CTkLabel(
            self.frame_kanan,
            text="Daftar Koleksi Buku",
            font=("Arial", 22, "bold")
        ).grid(row=0, column=0, pady=(22, 15))

        # Tabel buku
        kolom = ("id", "judul", "penulis", "tahun")

        self.tabel = ttk.Treeview(
            self.frame_kanan,
            columns=kolom,
            show="headings"
        )

        self.tabel.heading("id", text="ID")
        self.tabel.heading("judul", text="Judul Buku")
        self.tabel.heading("penulis", text="Penulis")
        self.tabel.heading("tahun", text="Tahun")

        self.tabel.column("id", width=55, minwidth=45, anchor="center")
        self.tabel.column("judul", width=230, minwidth=150, anchor="w")
        self.tabel.column("penulis", width=190, minwidth=130, anchor="w")
        self.tabel.column("tahun", width=85, minwidth=70, anchor="center")

        # Scrollbar vertikal
        scrollbar = ttk.Scrollbar(
            self.frame_kanan,
            orient="vertical",
            command=self.tabel.yview
        )
        self.tabel.configure(yscrollcommand=scrollbar.set)

        self.tabel.grid(
            row=1, column=0, padx=(15, 0), pady=(0, 15), sticky="nsew"
        )
        scrollbar.grid(
            row=1, column=1, padx=(0, 15), pady=(0, 15), sticky="ns"
        )


if __name__ == "__main__":
    app = BukuView()
    app.mainloop()
