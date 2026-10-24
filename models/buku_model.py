# AndiNayla_F5212510005

# Mengambil class Database dari file database.py
# Database digunakan untuk menghubungkan program dengan MySQL
from config.database import Database


# Membuat class BukuModel untuk mengatur data buku
class BukuModel:

    # Fungsi yang otomatis dijalankan saat BukuModel dibuat
    def __init__(self):

        # Membuat object Database
        self.db = Database()

        # Membuat koneksi ke database MySQL
        self.conn = self.db.get_connection()

        # Menentukan nama tabel yang digunakan, yaitu tabel buku
        self.table_name = "buku"


    # Fungsi untuk mengambil semua data buku dari database
    def get_all_buku(self):

        # Mengecek apakah koneksi database tersedia
        if self.conn:

            # Membuat cursor untuk menjalankan perintah SQL
            # dictionary=True membuat hasil data berbentuk dictionary
            cursor = self.conn.cursor(dictionary=True)

            # Membuat perintah SQL untuk mengambil semua data dari tabel buku
            query = f"SELECT * FROM {self.table_name}"

            # Menjalankan perintah SQL
            cursor.execute(query)

            # Mengambil semua hasil data dari database
            result = cursor.fetchall()

            # Menutup cursor setelah selesai digunakan
            cursor.close()

            # Mengembalikan hasil data buku
            return result

        # Jika tidak ada koneksi database,
        # mengembalikan data kosong
        return []


    # Fungsi untuk menambahkan data buku ke database
    # Parameter yang diterima: judul, penulis, dan tahun terbit
    def create_buku(self, judul, penulis, tahun_terbit):

        # Mengecek apakah koneksi database tersedia
        if self.conn:

            # Membuat cursor untuk menjalankan perintah SQL
            cursor = self.conn.cursor()

            # Membuat perintah SQL untuk memasukkan data buku
            query = f"INSERT INTO {self.table_name} (judul, penulis, tahun_terbit) VALUES (%s, %s, %s)"

            # Menyimpan nilai yang akan dimasukkan ke database
            val = (judul, penulis, tahun_terbit)

            # Menjalankan perintah INSERT dengan nilai yang sudah dibuat
            cursor.execute(query, val)

            # Menyimpan perubahan ke database
            self.conn.commit()

            # Menutup cursor setelah selesai digunakan
            cursor.close()

            # Mengembalikan True yang berarti data berhasil ditambahkan
            return True

        # Jika tidak ada koneksi database,
        # mengembalikan False yang berarti gagal
        return False


    # Fungsi untuk menghapus data buku berdasarkan ID
    def delete_buku(self, id_buku):
        if self.conn:
            cursor = self.conn.cursor()

            query = f"DELETE FROM {self.table_name} WHERE id_buku = %s"
            cursor.execute(query, (id_buku,))

            # Memastikan apakah ada data yang terhapus
            berhasil = cursor.rowcount > 0

            self.conn.commit()
            cursor.close()

            return berhasil

        return False


    # Fungsi untuk memperbarui data buku berdasarkan ID
    def update_buku(self, id_buku, judul, penulis, tahun_terbit):
        if self.conn:
            cursor = self.conn.cursor()

            query = f"""
                UPDATE {self.table_name}
                SET judul = %s, penulis = %s, tahun_terbit = %s
                WHERE id_buku = %s
            """

            val = (judul, penulis, tahun_terbit, id_buku)
            cursor.execute(query, val)

            # Memeriksa apakah ada baris yang berubah
            berhasil = cursor.rowcount > 0

            self.conn.commit()
            cursor.close()

            return berhasil

        return False