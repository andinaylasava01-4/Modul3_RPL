
# Mengimpor class Database untuk koneksi MySQL
from config.database import Database


class BukuModel:
    def __init__(self):
        # Membuat koneksi ke database
        self.db = Database()
        self.conn = self.db.get_connection()
        self.table_name = "buku"

    def get_all_buku(self):
        # Mengambil seluruh data buku
        if self.conn and self.conn.is_connected():
            cursor = self.conn.cursor(dictionary=True)
            query = f"SELECT * FROM {self.table_name}"
            cursor.execute(query)
            hasil = cursor.fetchall()
            cursor.close()
            return hasil
        return []

    def create_buku(self, judul, penulis, tahun_terbit):
        # Menambahkan data buku
        if self.conn and self.conn.is_connected():
            cursor = self.conn.cursor()
            query = """
                INSERT INTO buku (judul, penulis, tahun_terbit)
                VALUES (%s, %s, %s)
            """
            cursor.execute(query, (judul, penulis, tahun_terbit))
            self.conn.commit()
            berhasil = cursor.rowcount > 0
            cursor.close()
            return berhasil
        return False

    def update_buku(self, id_buku, judul, penulis, tahun_terbit):
        # Memperbarui data buku berdasarkan ID
        if self.conn and self.conn.is_connected():
            cursor = self.conn.cursor()
            query = """
                UPDATE buku
                SET judul = %s, penulis = %s, tahun_terbit = %s
                WHERE id_buku = %s
            """
            cursor.execute(
                query, (judul, penulis, tahun_terbit, id_buku)
            )
            self.conn.commit()
            berhasil = cursor.rowcount > 0
            cursor.close()
            return berhasil
        return False

    def delete_buku(self, id_buku):
        # Menghapus data buku berdasarkan ID
        if self.conn and self.conn.is_connected():
            cursor = self.conn.cursor()
            query = "DELETE FROM buku WHERE id_buku = %s"
            cursor.execute(query, (id_buku,))
            self.conn.commit()
            berhasil = cursor.rowcount > 0
            cursor.close()
            return berhasil
        return False
