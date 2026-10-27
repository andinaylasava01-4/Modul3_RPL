
from models.buku_model import BukuModel


def test_get_all_buku():
    model = BukuModel()

    try:
        hasil = model.get_all_buku()

        # Memastikan hasil pengambilan data berbentuk list
        assert isinstance(hasil, list)

        # Memastikan setiap data buku memiliki kolom yang diperlukan
        for buku in hasil:
            assert "id_buku" in buku
            assert "judul" in buku
            assert "penulis" in buku
            assert "tahun_terbit" in buku

    finally:
        if model.conn and model.conn.is_connected():
            model.conn.close()
