
from config.database import Database


class AnggotaModel:
    def __init__(self):
        # Membuat koneksi ke database
        self.db = Database()
        self.conn = self.db.get_connection()
        self.table_name = "anggota"

    def get_all_anggota(self):
        # Mengambil seluruh data anggota
        if self.conn:
            cursor = self.conn.cursor(dictionary=True)
            query = f"SELECT * FROM {self.table_name}"
            cursor.execute(query)
            hasil = cursor.fetchall()
            cursor.close()
            return hasil
        return []

    def create_anggota(self, nama_anggota, alamat):
        # Menambahkan data anggota baru
        if self.conn:
            cursor = self.conn.cursor()
            query = f"""
                INSERT INTO {self.table_name}
                (nama_anggota, alamat)
                VALUES (%s, %s)
            """
            cursor.execute(query, (nama_anggota, alamat))
            self.conn.commit()
            berhasil = cursor.rowcount > 0
            cursor.close()
            return berhasil
        return False

    def update_anggota(self, id_anggota, nama_anggota, alamat):
        # Memperbarui data anggota berdasarkan ID
        if self.conn:
            cursor = self.conn.cursor()
            query = f"""
                UPDATE {self.table_name}
                SET nama_anggota = %s, alamat = %s
                WHERE id_anggota = %s
            """
            cursor.execute(
                query, (nama_anggota, alamat, id_anggota)
            )
            self.conn.commit()
            berhasil = cursor.rowcount > 0
            cursor.close()
            return berhasil
        return False

    def delete_anggota(self, id_anggota):
        # Menghapus data anggota berdasarkan ID
        if self.conn:
            cursor = self.conn.cursor()
            query = f"""
                DELETE FROM {self.table_name}
                WHERE id_anggota = %s
            """
            cursor.execute(query, (id_anggota,))
            self.conn.commit()
            berhasil = cursor.rowcount > 0
            cursor.close()
            return berhasil
        return False
