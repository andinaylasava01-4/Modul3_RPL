# AndiNayla_F5212510005

# Mengimpor library mysql.connector untuk menghubungkan Python dengan MySQL
import mysql.connector

# Mengimpor Error untuk menangani kesalahan saat koneksi database
from mysql.connector import Error


# Membuat class Database untuk mengatur koneksi ke database
class Database:

    # Fungsi yang otomatis dijalankan saat object Database dibuat
    def __init__(self):

        # Menentukan alamat server MySQL
        self.host = "localhost"

        # Menentukan nama database yang akan digunakan
        self.db_name = "perpustakaan"

        # Menentukan username MySQL
        self.username = "root"

        # Menentukan password MySQL
        # Jika MySQL menggunakan password, isi password di bagian ini
        self.password = ""

        # Menyimpan koneksi database
        # Awalnya belum ada koneksi, sehingga nilainya None
        self.conn = None


    # Fungsi untuk membuat dan mendapatkan koneksi ke database
    def get_connection(self):

        # Mencoba menjalankan proses koneksi
        try:

            # Menghubungkan Python dengan database MySQL
            self.conn = mysql.connector.connect(

                # Menentukan server MySQL
                host=self.host,

                # Menentukan database yang digunakan
                database=self.db_name,

                # Menentukan username untuk login ke MySQL
                user=self.username,

                # Menentukan password untuk login ke MySQL
                password=self.password
            )

            # Mengecek apakah koneksi berhasil
            if self.conn.is_connected():

                # Jika berhasil, mengembalikan koneksi database
                return self.conn

        # Jika terjadi kesalahan saat koneksi
        except Error as e:

            # Menampilkan pesan kesalahan ke layar
            print(f"Koneksi Gagal: {e}")

            # Mengembalikan None karena koneksi gagal
            return None