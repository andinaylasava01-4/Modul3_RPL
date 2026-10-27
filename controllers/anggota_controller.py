import tkinter.messagebox as messagebox
from models.anggota_model import AnggotaModel
from views.anggota_view import AnggotaView


class AnggotaController:
    def __init__(self):
        # Membuat Model dan View
        self.model = AnggotaModel()
        self.view = AnggotaView()

        # Menyimpan ID anggota yang dipilih
        self.id_anggota_dipilih = None

        # Menghubungkan tombol dengan fungsi Controller
        self.view.btn_simpan.configure(command=self.simpan_anggota)
        self.view.btn_update.configure(command=self.update_anggota)
        self.view.btn_delete.configure(command=self.hapus_anggota)

        # Menghubungkan pemilihan baris tabel
        self.view.tabel.bind(
            "<<TreeviewSelect>>",
            self.pilih_anggota
        )

        # Menampilkan data saat aplikasi dibuka
        self.muat_data_tabel()

    def muat_data_tabel(self):
        # Membersihkan isi tabel
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        # Mengambil data anggota dari Model
        data_anggota = self.model.get_all_anggota()

        # Memasukkan data ke tabel
        for anggota in data_anggota:
            self.view.tabel.insert(
                "",
                "end",
                values=(
                    anggota["id_anggota"],
                    anggota["nama_anggota"],
                    anggota["alamat"]
                )
            )

    def pilih_anggota(self, event=None):
        # Mengambil baris yang dipilih
        pilihan = self.view.tabel.selection()

        if not pilihan:
            self.id_anggota_dipilih = None
            return

        # Mengambil isi baris tabel
        data = self.view.tabel.item(pilihan[0], "values")

        # Menyimpan ID anggota
        self.id_anggota_dipilih = data[0]

        # Memasukkan data ke form
        self.view.entry_nama.delete(0, "end")
        self.view.entry_nama.insert(0, data[1])

        self.view.entry_alamat.delete(0, "end")
        self.view.entry_alamat.insert(0, data[2])

    def simpan_anggota(self):
        # Mengambil data dari form
        nama = self.view.entry_nama.get()
        alamat = self.view.entry_alamat.get()

        # Memeriksa form kosong
        if not nama or not alamat:
            messagebox.showwarning(
                "Peringatan",
                "Nama dan alamat anggota harus diisi!"
            )
            return

        # Menyimpan data melalui Model
        berhasil = self.model.create_anggota(nama, alamat)

        if berhasil:
            messagebox.showinfo(
                "Sukses",
                "Data anggota berhasil disimpan!"
            )
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Error",
                "Data anggota gagal disimpan."
            )

    def update_anggota(self):
        # Memeriksa apakah ada anggota yang dipilih
        if self.id_anggota_dipilih is None:
            messagebox.showwarning(
                "Peringatan",
                "Pilih data anggota yang ingin diperbarui!"
            )
            return

        nama = self.view.entry_nama.get()
        alamat = self.view.entry_alamat.get()

        if not nama or not alamat:
            messagebox.showwarning(
                "Peringatan",
                "Nama dan alamat anggota harus diisi!"
            )
            return

        # Memperbarui data melalui Model
        berhasil = self.model.update_anggota(
            self.id_anggota_dipilih,
            nama,
            alamat
        )

        if berhasil:
            messagebox.showinfo(
                "Sukses",
                "Data anggota berhasil diperbarui!"
            )
            self.id_anggota_dipilih = None
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Error",
                "Data anggota gagal diperbarui."
            )

    def hapus_anggota(self):
        # Memeriksa apakah ada anggota yang dipilih
        if self.id_anggota_dipilih is None:
            messagebox.showwarning(
                "Peringatan",
                "Pilih data anggota yang ingin dihapus!"
            )
            return

        # Meminta konfirmasi
        konfirmasi = messagebox.askyesno(
            "Konfirmasi",
            "Yakin ingin menghapus data anggota ini?"
        )

        if not konfirmasi:
            return

        # Menghapus data melalui Model
        berhasil = self.model.delete_anggota(
            self.id_anggota_dipilih
        )

        if berhasil:
            messagebox.showinfo(
                "Sukses",
                "Data anggota berhasil dihapus!"
            )
            self.id_anggota_dipilih = None
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Error",
                "Data anggota gagal dihapus."
            )

    def bersihkan_form(self):
        # Mengosongkan form
        self.view.entry_nama.delete(0, "end")
        self.view.entry_alamat.delete(0, "end")

    def run(self):
        self.view.mainloop()


if __name__ == "__main__":
    app = AnggotaController()
    app.run()
    