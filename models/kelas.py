class SiswaKelasIterator:
    """Custom Iterator untuk menjelajahi daftar siswa di dalam kelas satu per satu."""

    def __init__(self, daftar_siswa):
        self._daftar_siswa = daftar_siswa
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._daftar_siswa):
            siswa = self._daftar_siswa[self._index]
            self._index += 1
            return siswa
        raise StopIteration


class Kelas:
    """Mengelola kelas, wali kelas, dan daftar siswa."""

    def __init__(self, nama_kelas):
        self.nama_kelas = nama_kelas.strip()
        self.wali_kelas = None
        self._daftar_siswa = []

        if not self.nama_kelas:
            raise ValueError("Nama kelas tidak boleh kosong.")

    @property
    def daftar_siswa(self):
        return list(self._daftar_siswa)

    def __iter__(self):
        # Custom iterator method yang mengembalikan iterator untuk daftar siswa."""
        return SiswaKelasIterator(self._daftar_siswa)


    def tambah_siswa(self, siswa):
        if any(item.nis == siswa.nis for item in self):
            raise ValueError("Siswa tersebut sudah terdaftar di kelas ini.")

        if siswa.kelas is not None and siswa.kelas is not self:
            siswa.kelas.hapus_siswa(siswa)

        self._daftar_siswa.append(siswa)
        siswa.ubah_kelas(self)

    def hapus_siswa(self, siswa):
        if siswa in self._daftar_siswa:
            self._daftar_siswa.remove(siswa)
            siswa.ubah_kelas(None)

    def tetapkan_wali_kelas(self, guru):
        if self.wali_kelas is not None:
            self.wali_kelas.tetapkan_wali_kelas(None)

        self.wali_kelas = guru
        guru.tetapkan_wali_kelas(self)

    def tampilkan_daftar_siswa(self):
        # Mengambil daftar siswa menggunakan iterator pattern (iter dan next)."""
        hasil = []
        iterator = iter(self)
        while True:
            try:
                hasil.append(next(iterator))
            except StopIteration:
                break
        return hasil
