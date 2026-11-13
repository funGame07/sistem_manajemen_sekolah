from .pengguna_sekolah import PenggunaSekolah

class Guru(PenggunaSekolah):
    """Menyimpan data seorang guru."""

    def __init__(self, nip, nama, mata_pelajaran):
        super().__init__(nip, nama)
        self._nip = str(nip).strip()
        self._mata_pelajaran = mata_pelajaran.strip()
        self._kelas_wali = None

        if not self._mata_pelajaran:
            raise ValueError("Mata pelajaran tidak boleh kosong.")

    @property
    def nip(self):
        return self._nip

    @property
    def mata_pelajaran(self):
        return self._mata_pelajaran

    @property
    def kelas_wali(self):
        return self._kelas_wali

    def tetapkan_wali_kelas(self, kelas):
        self._kelas_wali = kelas

    def tampilkan_info(self):
        nama_kelas = self._kelas_wali.nama_kelas if self._kelas_wali else "Bukan wali kelas"
        return (
            f"NIP: {self._nip} | Nama: {self._nama} | "
            f"Mata Pelajaran: {self._mata_pelajaran} | Wali Kelas: {nama_kelas}"
        )