
import tkinter.messagebox as messagebox

from models.buku_model import BukuModel
from views.buku_view import BukuView


class BukuController:
    def __init__(self):
        # Membuat Model dan View
        self.model = BukuModel()
        self.view = BukuView()

        # Menyimpan ID buku yang sedang dipilih
        self.id_buku_dipilih = None

        # Menghubungkan tombol dengan fungsi Controller
        self.view.btn_simpan.configure(command=self.simpan_data)
        self.view.btn_hapus.configure(command=self.hapus_buku)
        self.view.btn_update.configure(command=self.perbarui_buku)

        # Menghubungkan pemilihan baris tabel
        self.view.tabel.bind(
            "<<TreeviewSelect>>",
            self.pilih_buku
        )

        # Memuat data buku ketika aplikasi dibuka
        self.muat_data_tabel()

    def muat_data_tabel(self):
        # Menghapus data lama dari tabel
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        # Mengambil data buku dari Model
        data_buku = self.model.get_all_buku()

        # Menampilkan data buku pada tabel
        for buku in data_buku:
            self.view.tabel.insert(
                "",
                "end",
                values=(
                    buku["id_buku"],
                    buku["judul"],
                    buku["penulis"],
                    buku["tahun_terbit"]
                )
            )

    def pilih_buku(self, event=None):
        # Mendapatkan baris yang dipilih
        pilihan = self.view.tabel.selection()

        if not pilihan:
            self.id_buku_dipilih = None
            return

        # Mengambil nilai dari baris tabel
        data = self.view.tabel.item(
            pilihan[0],
            "values"
        )

        # Menyimpan ID buku
        self.id_buku_dipilih = data[0]

        # Memasukkan data terpilih ke form
        self.view.entry_judul.delete(0, "end")
        self.view.entry_judul.insert(0, data[1])

        self.view.entry_penulis.delete(0, "end")
        self.view.entry_penulis.insert(0, data[2])

        self.view.entry_tahun.delete(0, "end")
        self.view.entry_tahun.insert(0, data[3])

    def simpan_data(self):
        # Mengambil nilai dari form
        judul = self.view.entry_judul.get().strip()
        penulis = self.view.entry_penulis.get().strip()
        tahun = self.view.entry_tahun.get().strip()

        # Memeriksa apakah semua kolom sudah diisi
        if not judul or not penulis or not tahun:
            messagebox.showwarning(
                "Peringatan",
                "Semua kolom form harus diisi!",
                parent=self.view
            )
            return

        # Memastikan tahun terbit berupa angka
        if not tahun.isdigit():
            messagebox.showwarning(
                "Peringatan",
                "Tahun terbit harus berupa angka!",
                parent=self.view
            )
            return

        try:
            berhasil = self.model.create_buku(
                judul,
                penulis,
                int(tahun)
            )

            if berhasil:
                self.muat_data_tabel()
                self.bersihkan_form()

                messagebox.showinfo(
                    "Sukses",
                    "Data buku berhasil disimpan!",
                    parent=self.view
                )
            else:
                messagebox.showerror(
                    "Gagal",
                    "Data buku gagal disimpan. Periksa koneksi database.",
                    parent=self.view
                )

        except Exception as e:
            messagebox.showerror(
                "Error",
                f"Terjadi kesalahan saat menyimpan data:\n{e}",
                parent=self.view
            )

    def perbarui_buku(self):
        # Memastikan ada buku yang dipilih
        if self.id_buku_dipilih is None:
            messagebox.showwarning(
                "Peringatan",
                "Pilih data buku dari tabel terlebih dahulu!",
                parent=self.view
            )
            return

        judul = self.view.entry_judul.get().strip()
        penulis = self.view.entry_penulis.get().strip()
        tahun = self.view.entry_tahun.get().strip()

        # Memeriksa kelengkapan form
        if not judul or not penulis or not tahun:
            messagebox.showwarning(
                "Peringatan",
                "Semua kolom form harus diisi!",
                parent=self.view
            )
            return

        if not tahun.isdigit():
            messagebox.showwarning(
                "Peringatan",
                "Tahun terbit harus berupa angka!",
                parent=self.view
            )
            return

        try:
            berhasil = self.model.update_buku(
                self.id_buku_dipilih,
                judul,
                penulis,
                int(tahun)
            )

            if berhasil:
                self.muat_data_tabel()
                self.bersihkan_form()

                messagebox.showinfo(
                    "Sukses",
                    "Data buku berhasil diperbarui!",
                    parent=self.view
                )
                self.id_buku_dipilih = None

            else:
                messagebox.showwarning(
                    "Informasi",
                    "Data tidak berubah atau buku tidak ditemukan.",
                    parent=self.view
                )

        except Exception as e:
            messagebox.showerror(
                "Error",
                f"Terjadi kesalahan saat memperbarui data:\n{e}",
                parent=self.view
            )

    def hapus_buku(self):
        # Memastikan ada buku yang dipilih
        if self.id_buku_dipilih is None:
            messagebox.showwarning(
                "Peringatan",
                "Pilih data buku yang ingin dihapus!",
                parent=self.view
            )
            return

        # Meminta konfirmasi pengguna
        konfirmasi = messagebox.askyesno(
            "Konfirmasi",
            "Apakah kamu yakin ingin menghapus data buku ini?",
            parent=self.view
        )

        if not konfirmasi:
            return

        try:
            berhasil = self.model.delete_buku(
                self.id_buku_dipilih
            )

            if berhasil:
                self.id_buku_dipilih = None
                self.muat_data_tabel()
                self.bersihkan_form()

                messagebox.showinfo(
                    "Sukses",
                    "Data buku berhasil dihapus!",
                    parent=self.view
                )
            else:
                messagebox.showerror(
                    "Gagal",
                    "Data buku gagal dihapus atau tidak ditemukan.",
                    parent=self.view
                )

        except Exception as e:
            messagebox.showerror(
                "Error",
                f"Terjadi kesalahan saat menghapus data:\n{e}",
                parent=self.view
            )

    def bersihkan_form(self):
        # Mengosongkan seluruh kolom input
        self.view.entry_judul.delete(0, "end")
        self.view.entry_penulis.delete(0, "end")
        self.view.entry_tahun.delete(0, "end")

        # Menghapus pilihan baris tabel
        pilihan = self.view.tabel.selection()

        if pilihan:
            self.view.tabel.selection_remove(*pilihan)

        self.id_buku_dipilih = None

    def run(self):
        # Menjalankan jendela aplikasi
        self.view.mainloop()


if __name__ == "__main__":
    app = BukuController()
    app.run()
