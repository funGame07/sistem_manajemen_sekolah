
class Absensi:
    """Mencatat status kehadiran siswa."""

    STATUS_VALID = ("Hadir", "Izin", "Sakit", "Alpa")

    def __init__(self, siswa):
        self.siswa = siswa
        self._catatan_absensi = []

    @staticmethod
    def validasi_status(status):
        return status.strip().capitalize() in Absensi.STATUS_VALID

    def catat_absensi(self, status):
        status = status.strip().capitalize()
        if not self.validasi_status(status):
            raise ValueError("Status harus Hadir, Izin, Sakit, atau Alpa.")
        self._catatan_absensi.append(status)

    def hitung_persentase(self):
        if not self._catatan_absensi:
            return 0.0
        jumlah_hadir = self._catatan_absensi.count("Hadir")
        return jumlah_hadir / len(self._catatan_absensi) * 100

    def tampilkan_absensi(self):
        return list(self._catatan_absensi)
