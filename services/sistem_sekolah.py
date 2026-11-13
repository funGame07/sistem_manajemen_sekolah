import sys
sys.path.append("..")

from models.kelas import Kelas
from models.jadwal_pelajaran import JadwalPelajaran
from models.absensi import Absensi
from models.nilai_akademik import NilaiAkademik

class SistemManajemenSekolah:
    def __init__(self):
        self._daftar_siswa = {}
        self._daftar_guru = {}
        self._daftar_kelas = {}
        self._daftar_jadwal = []
        self._daftar_absensi = {}
        self._daftar_nilai = {}

    # F1
    def registrasi_siswa(self, siswa):
        if siswa.nis in self._daftar_siswa:
            raise ValueError("NIS sudah terdaftar.")
        self._daftar_siswa[siswa.nis] = siswa

    # F2
    def registrasi_guru(self, guru):
        if guru.nip in self._daftar_guru:
            raise ValueError("NIP sudah terdaftar.")
        self._daftar_guru[guru.nip] = guru

    # F3
    def buat_kelas(self, nama_kelas):
        nama_kelas = nama_kelas.strip()
        if nama_kelas in self._daftar_kelas:
            raise ValueError("Nama kelas sudah terdaftar.")
        self._daftar_kelas[nama_kelas] = Kelas(nama_kelas)

    def tetapkan_wali_kelas(self, nama_kelas, nip):
        if nama_kelas not in self._daftar_kelas:
            raise ValueError("Kelas tidak ditemukan.")
        if nip not in self._daftar_guru:
            raise ValueError("Guru tidak ditemukan.")

        kelas = self._daftar_kelas[nama_kelas]
        guru = self._daftar_guru[nip]

        # Seorang guru hanya menjadi wali untuk satu kelas dalam program ini.
        if guru.kelas_wali is not None and guru.kelas_wali is not kelas:
            raise ValueError("Guru tersebut sudah menjadi wali kelas lain.")

        kelas.tetapkan_wali_kelas(guru)

    # F4
    def tambah_siswa_ke_kelas(self, nis, nama_kelas):
        if nis not in self._daftar_siswa:
            raise ValueError("Siswa tidak ditemukan.")
        if nama_kelas not in self._daftar_kelas:
            raise ValueError("Kelas tidak ditemukan.")
        self._daftar_kelas[nama_kelas].tambah_siswa(self._daftar_siswa[nis])

    # F5
    def tambah_jadwal(self, nama_kelas, mata_pelajaran, nip, hari, jam):
        if nama_kelas not in self._daftar_kelas:
            raise ValueError("Kelas tidak ditemukan.")
        if nip not in self._daftar_guru:
            raise ValueError("Guru tidak ditemukan.")

        guru = self._daftar_guru[nip]
        self._daftar_jadwal.append(
            JadwalPelajaran(nama_kelas, mata_pelajaran, guru, hari, jam)
        )

    # F6
    def catat_absensi(self, nis, status):
        if nis not in self._daftar_siswa:
            raise ValueError("Siswa tidak ditemukan.")

        if nis not in self._daftar_absensi:
            self._daftar_absensi[nis] = Absensi(self._daftar_siswa[nis])

        self._daftar_absensi[nis].catat_absensi(status)

    # F7
    def hitung_persentase_kehadiran(self, nis):
        if nis not in self._daftar_siswa:
            raise ValueError("Siswa tidak ditemukan.")
        if nis not in self._daftar_absensi:
            return 0.0
        return self._daftar_absensi[nis].hitung_persentase()

    # F8
    def input_nilai(self, nis, ulangan, uts, uas):
        if nis not in self._daftar_siswa:
            raise ValueError("Siswa tidak ditemukan.")

        if nis not in self._daftar_nilai:
            self._daftar_nilai[nis] = NilaiAkademik(self._daftar_siswa[nis])

        self._daftar_nilai[nis].input_nilai(ulangan, uts, uas)

    # F9 dilakukan oleh NilaiAkademik.validasi_nilai()
    # dan InvalidGradeException.

    # F10
    def hitung_nilai_akhir(self, nis):
        if nis not in self._daftar_nilai:
            raise ValueError("Nilai siswa belum diinput.")
        return self._daftar_nilai[nis].hitung_nilai_akhir()

    def iter_semua_pengguna(self):
        # Generator untuk mengiterasi seluruh pengguna sekolah (Siswa dan Guru)
        for siswa in self._daftar_siswa.values():
            yield siswa
        for guru in self._daftar_guru.values():
            yield guru

    def tampilkan_semua_pengguna(self):
        # contoh polymorphism & iterator pattern (generator pada for loop)
        if not self._daftar_siswa and not self._daftar_guru:
            print("Belum ada data siswa atau guru.")
            return

        for item in self.iter_semua_pengguna():
            print(item.tampilkan_info())

    # Helper untuk menampilkan data
    def tampilkan_siswa(self):
        if not self._daftar_siswa:
            print("Belum ada data siswa.")
            return
        for siswa in self._daftar_siswa.values():
            print(siswa.tampilkan_info())

    def tampilkan_guru(self):
        if not self._daftar_guru:
            print("Belum ada data guru.")
            return
        for guru in self._daftar_guru.values():
            print(guru.tampilkan_info())

    def tampilkan_kelas(self):
        if not self._daftar_kelas:
            print("Belum ada data kelas.")
            return
        for kelas in self._daftar_kelas.values():
            wali = kelas.wali_kelas.nama if kelas.wali_kelas else "Belum ditetapkan"
            print(f"\nKelas: {kelas.nama_kelas} | Wali Kelas: {wali}")
            if kelas.daftar_siswa:
                # Menggunakan custom iterator pada for loop (__iter__ dan __next__)
                for siswa in kelas:
                    print(f"  - {siswa.nis}: {siswa.nama}")
            else:
                print("  Belum ada siswa.")

    def tampilkan_jadwal(self):
        if not self._daftar_jadwal:
            print("Belum ada jadwal pelajaran.")
            return
        for nomor, jadwal in enumerate(self._daftar_jadwal, start=1):
            print(f"{nomor}. {jadwal.tampilkan_jadwal()}")

    def tampilkan_absensi(self, nis):
        if nis not in self._daftar_siswa:
            raise ValueError("Siswa tidak ditemukan.")
        if nis not in self._daftar_absensi:
            print("Belum ada catatan absensi.")
            return
        catatan = self._daftar_absensi[nis].tampilkan_absensi()
        print(f"Absensi {self._daftar_siswa[nis].nama}: {', '.join(catatan)}")
        print(f"Persentase kehadiran: {self.hitung_persentase_kehadiran(nis):.2f}%")

    def tampilkan_nilai(self, nis):
        if nis not in self._daftar_siswa:
            raise ValueError("Siswa tidak ditemukan.")
        if nis not in self._daftar_nilai:
            print("Nilai siswa belum diinput.")
            return
        nilai = self._daftar_nilai[nis]
        print(f"Nama: {nilai.siswa.nama}")
        print(f"Ulangan: {nilai.nilai_ulangan}")
        print(f"UTS: {nilai.nilai_uts}")
        print(f"UAS: {nilai.nilai_uas}")
        print(f"Nilai akhir: {nilai.hitung_nilai_akhir():.2f}")