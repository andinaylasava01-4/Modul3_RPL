from models.buku_model import BukuModel


def test_get_all_buku():
    model = BukuModel()
    hasil = model.get_all_buku()

    assert isinstance(hasil, list)