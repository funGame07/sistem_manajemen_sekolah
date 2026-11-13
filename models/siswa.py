from .pengguna_sekolah import PenggunaSekolah

class Siswa(PenggunaSekolah):
    """Menyimpan data seorang siswa."""

    def __init__(self, nis, nama, wali_murid):
        super().__init__(nis, nama)
        self._nis = str(nis).strip()
        self._wali_murid = wali_murid.strip()
        self._kelas = None

        if not self._wali_murid:
            raise ValueError("Nama wali murid tidak boleh kosong.")

    @property
    def nis(self):
        return self._nis

    @property
    def wali_murid(self):
        return self._wali_murid

    @property
    def kelas(self):
        return self._kelas

    def ubah_kelas(self, kelas):
        self._kelas = kelas

    def tampilkan_info(self):
        nama_kelas = self._kelas.nama_kelas if self._kelas else "Belum ditempatkan"
        return (
            f"NIS: {self._nis} | Nama: {self._nama} | "
            f"Wali Murid: {self._wali_murid} | Kelas: {nama_kelas}"
        )