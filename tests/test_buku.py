
from unittest.mock import MagicMock
from models.buku_model import BukuModel


def test_create_buku_berhasil():
    model = BukuModel()

    model.conn = MagicMock()
    model.conn.is_connected.return_value = True

    mock_cursor = MagicMock()
    mock_cursor.rowcount = 1
    model.conn.cursor.return_value = mock_cursor

    hasil = model.create_buku("Buku Testing", "Penulis QA", 2026)

    assert hasil is True
    mock_cursor.execute.assert_called_once()
    model.conn.commit.assert_called_once()


def test_get_all_buku_berhasil():
    model = BukuModel()

    model.conn = MagicMock()
    model.conn.is_connected.return_value = True

    mock_cursor = MagicMock()
    model.conn.cursor.return_value = mock_cursor

    mock_cursor.fetchall.return_value = [
        (1, "Pemrograman Python", "Tim QA", 2025),
        (2, "Struktur Data", "Admin", 2026)
    ]

    hasil = model.get_all_buku()

    assert isinstance(hasil, list)
    assert len(hasil) == 2
    mock_cursor.execute.assert_called_once()
