from abc import ABC, abstractmethod

class PenggunaSekolah(ABC):
    """Kelas induk abstrak untuk pengguna sekolah."""

    def __init__(self, id_pengguna, nama):
        self._id = str(id_pengguna).strip()
        self._nama = nama.strip()

        if not self._id:
            raise ValueError("ID tidak boleh kosong.")
        if not self._nama:
            raise ValueError("Nama tidak boleh kosong.")

    @property
    def id(self):
        return self._id

    @property
    def nama(self):
        return self._nama

    @abstractmethod
    def tampilkan_info(self):
        """Wajib diimplementasikan oleh kelas turunan."""
        pass