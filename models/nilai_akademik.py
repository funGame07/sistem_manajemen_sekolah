from .exceptions import InvalidGradeException

class NilaiAkademik:
    """Menyimpan dan menghitung nilai akademik siswa."""

    def __init__(self, siswa):
        self.siswa = siswa
        self.nilai_ulangan = None
        self.nilai_uts = None
        self.nilai_uas = None

    @staticmethod
    def validasi_nilai(nilai):
        try:
            nilai = float(nilai)
        except (ValueError, TypeError):
            raise InvalidGradeException("Nilai harus berupa angka.")

        if nilai < 0 or nilai > 100:
            raise InvalidGradeException(
                f"Nilai {nilai} tidak valid. Nilai harus berada pada rentang 0-100."
            )
        return nilai

    def input_nilai(self, ulangan, uts, uas):
        # Validasi seluruh nilai terlebih dahulu sebelum menyimpan.
        nilai_ulangan = self.validasi_nilai(ulangan)
        nilai_uts = self.validasi_nilai(uts)
        nilai_uas = self.validasi_nilai(uas)

        self.nilai_ulangan = nilai_ulangan
        self.nilai_uts = nilai_uts
        self.nilai_uas = nilai_uas

    def hitung_nilai_akhir(self):
        if None in (self.nilai_ulangan, self.nilai_uts, self.nilai_uas):
            raise ValueError("Nilai Ulangan, UTS, dan UAS belum lengkap.")

        return (
            self.nilai_ulangan * 0.40
            + self.nilai_uts * 0.30
            + self.nilai_uas * 0.30
        )