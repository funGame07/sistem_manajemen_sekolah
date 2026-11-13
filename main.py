from models.exceptions import InvalidGradeException
from services.sistem_sekolah import SistemManajemenSekolah
from models.siswa import Siswa
from models.guru import Guru
from models.nilai_akademik import NilaiAkademik

def input_teks(pesan):
    while True:
        nilai = input(pesan).strip()
        if nilai:
            return nilai
        print("Input tidak boleh kosong.")

def input_angka(pesan):
    while True:
        try:
            return float(input(pesan).strip())
        except ValueError:
            print("Masukkan angka yang valid.")

def tampilkan_menu_utama():
    print("\n" + "=" * 58)
    print("          SISTEM MANAJEMEN SEKOLAH")
    print("=" * 58)
    print(" 1. Registrasi siswa")
    print(" 2. Registrasi guru")
    print(" 3. Membuat kelas dan tetapkan walikelas")
    print(" 4. Pilih kelas (Manajemen Kelas)")
    print(" 5. Menampilkan seluruh data siswa")
    print(" 6. Menampilkan seluruh data guru")
    print(" 7. Menampilkan seluruh kelas dan daftar siswa")
    print(" 8. Menampilkan seluruh pengguna")
    print(" 0. Keluar")
    print("-" * 58)

def tampilkan_menu_kelas(nama_kelas):
    print("\n" + "=" * 58)
    print(f"          MANAJEMEN KELAS: {nama_kelas}")
    print("=" * 58)
    print(" 1. Menetapkan wali kelas")
    print(" 2. Menambahkan siswa ke kelas")
    print(" 3. Input jadwal pelajaran kelas")
    print(" 4. Mencatat absensi harian")
    print(" 5. Menghitung persentase kehadiran siswa")
    print(" 6. Menghitung persentase kehadiran seluruh siswa")
    print(" 7. Input nilai Ulangan, UTS, dan UAS")
    print(" 8. Nilai akhir berbobot per siswa")
    print(" 9. Nilai akhir berbobot seluruh siswa")
    print("10. Tampilkan jadwal kelas")
    print("11. Tampilkan info kelas")
    print(" 0. Kembali")
    print("-" * 58)

def tampilkan_siswa_di_kelas(sistem, nama_kelas):
    kelas = sistem._daftar_kelas.get(nama_kelas)
    if not kelas or not kelas.daftar_siswa:
        print("Belum ada siswa di kelas ini.")
        return False
    for siswa in kelas.daftar_siswa:
        print(f"  - {siswa.nis}: {siswa.nama}")
    return True

def kelola_kelas(sistem, nama_kelas):
    while True:
        tampilkan_menu_kelas(nama_kelas)
        pilihan = input("Pilih menu kelas (0-11): ").strip()
        try:
            if pilihan == "1":
                print("\n--- Daftar Guru ---")
                sistem.tampilkan_guru()
                nip = input_teks("Masukkan NIP Guru sebagai Wali Kelas: ")
                sistem.tetapkan_wali_kelas(nama_kelas, nip)
                print("Wali kelas berhasil ditetapkan.")
                input("\n[Enter untuk lanjut..]\n")
                
            elif pilihan == "2":
                print("\n--- Daftar Seluruh Siswa ---")
                sistem.tampilkan_siswa()
                nis = input_teks("Masukkan NIS siswa yang ingin ditambahkan: ")
                sistem.tambah_siswa_ke_kelas(nis, nama_kelas)
                print(f"Siswa berhasil ditambahkan ke kelas {nama_kelas}.")
                input("\n[Enter untuk lanjut..]\n")
                
            elif pilihan == "3":
                print("\n--- Daftar Guru ---")
                sistem.tampilkan_guru()
                mapel = input_teks("Mata pelajaran: ")
                nip = input_teks("NIP guru pengajar: ")
                hari = input_teks("Hari: ")
                jam = input_teks("Jam pelajaran (contoh 08:00-09:30): ")
                sistem.tambah_jadwal(nama_kelas, mapel, nip, hari, jam)
                print("Jadwal berhasil ditambahkan.")
                input("\n[Enter untuk lanjut..]\n")
                
            elif pilihan == "4":
                print("\n--- Daftar Siswa di Kelas Ini ---")
                if tampilkan_siswa_di_kelas(sistem, nama_kelas):
                    nis = input_teks("NIS siswa: ")
                    print("Status: Hadir / Izin / Sakit / Alpa")
                    status = input_teks("Masukkan status: ")
                    sistem.catat_absensi(nis, status)
                    print("Absensi berhasil dicatat.")
                input("\n[Enter untuk lanjut..]\n")
                
            elif pilihan == "5":
                print("\n--- Daftar Siswa di Kelas Ini ---")
                if tampilkan_siswa_di_kelas(sistem, nama_kelas):
                    nis = input_teks("NIS siswa: ")
                    persen = sistem.hitung_persentase_kehadiran(nis)
                    print(f"Persentase kehadiran: {persen:.2f}%")
                input("\n[Enter untuk lanjut..]\n")
                
            elif pilihan == "6":
                print(f"\n--- Persentase Kehadiran Seluruh Siswa Kelas {nama_kelas} ---")
                kelas = sistem._daftar_kelas.get(nama_kelas)
                if not kelas or not kelas.daftar_siswa:
                    print("Belum ada siswa di kelas ini.")
                else:
                    for siswa in kelas.daftar_siswa:
                        persen = sistem.hitung_persentase_kehadiran(siswa.nis)
                        print(f"- {siswa.nama} ({siswa.nis}): {persen:.2f}%")
                input("\n[Enter untuk lanjut..]\n")
                
            elif pilihan == "7":
                print("\n--- Daftar Siswa di Kelas Ini ---")
                if tampilkan_siswa_di_kelas(sistem, nama_kelas):
                    nis = input_teks("NIS siswa: ")
                    ulangan = input_angka("Nilai Ulangan (0-100): ")
                    uts = input_angka("Nilai UTS (0-100): ")
                    uas = input_angka("Nilai UAS (0-100): ")
                    sistem.input_nilai(nis, ulangan, uts, uas)
                    print("Nilai berhasil disimpan.")
                input("\n[Enter untuk lanjut..]\n")
                
            elif pilihan == "8":
                print("\n--- Daftar Siswa di Kelas Ini ---")
                if tampilkan_siswa_di_kelas(sistem, nama_kelas):
                    nis = input_teks("NIS siswa: ")
                    nilai_akhir = sistem.hitung_nilai_akhir(nis)
                    print(f"Nilai akhir untuk {nis}: {nilai_akhir:.2f}")
                input("\n[Enter untuk lanjut..]\n")
                
            elif pilihan == "9":
                print(f"\n--- Nilai Akhir Seluruh Siswa Kelas {nama_kelas} ---")
                kelas = sistem._daftar_kelas.get(nama_kelas)
                if not kelas or not kelas.daftar_siswa:
                    print("Belum ada siswa di kelas ini.")
                else:
                    for siswa in kelas.daftar_siswa:
                        try:
                            nilai_akhir = sistem.hitung_nilai_akhir(siswa.nis)
                            print(f"- {siswa.nama} ({siswa.nis}): {nilai_akhir:.2f}")
                        except ValueError:
                            print(f"- {siswa.nama} ({siswa.nis}): Nilai belum lengkap diinput.")
                input("\n[Enter untuk lanjut..]\n")
                
            elif pilihan == "10":
                print(f"\n--- Jadwal Pelajaran Kelas {nama_kelas} ---")
                jadwal_ditemukan = False
                for jadwal in sistem._daftar_jadwal:
                    if jadwal.nama_kelas == nama_kelas:
                        print(f"- {jadwal.hari}, {jadwal.jam} | Mapel: {jadwal.mata_pelajaran} | Guru: {jadwal.guru.nama}")
                        jadwal_ditemukan = True
                if not jadwal_ditemukan:
                    print("Belum ada jadwal untuk kelas ini.")
                input("\n[Enter untuk lanjut..]\n")
                
            elif pilihan == "11":
                print(f"\n--- Informasi Kelas {nama_kelas} ---")
                kelas = sistem._daftar_kelas.get(nama_kelas)
                wali = kelas.wali_kelas.nama if kelas.wali_kelas else "Belum ditetapkan"
                print(f"Nama Kelas  : {kelas.nama_kelas}")
                print(f"Wali Kelas  : {wali}")
                print("Daftar Siswa:")
                if kelas.daftar_siswa:
                    for siswa in kelas.daftar_siswa:
                        print(f"  - {siswa.nis}: {siswa.nama}")
                else:
                    print("  Belum ada siswa di kelas ini.")
                input("\n[Enter untuk lanjut..]\n")
                
            elif pilihan == "0":
                print("Kembali ke menu utama.")
                break
            else:
                print("Pilihan tidak tersedia. Masukkan angka 0 sampai 11.")
                
        except InvalidGradeException as error:
            print(f"InvalidGradeException: {error}")
            input("\n[Enter untuk lanjut..]\n")
        except ValueError as error:
            print(f"Terjadi kesalahan: {error}")
            input("\n[Enter untuk lanjut..]\n")
        except Exception as error:
            print(f"Terjadi kesalahan yang tidak terduga: {error}")
            input("\n[Enter untuk lanjut..]\n")


def jalankan_program():
    sistem = SistemManajemenSekolah()
    while True:
        tampilkan_menu_utama()
        pilihan = input("Pilih menu (0-8): ").strip()
        try:
            if pilihan == "1":
                nis = input_teks("NIS: ")
                nama = input_teks("Nama siswa: ")
                wali = input_teks("Nama wali murid: ")
                sistem.registrasi_siswa(Siswa(nis, nama, wali))
                print("Siswa berhasil didaftarkan.")
                input("\n[Enter untuk lanjut..]\n")
                
            elif pilihan == "2":
                nip = input_teks("NIP: ")
                nama = input_teks("Nama guru: ")
                mapel = input_teks("Mata pelajaran: ")
                sistem.registrasi_guru(Guru(nip, nama, mapel))
                print("Guru berhasil didaftarkan.")
                input("\n[Enter untuk lanjut..]\n")
                
            elif pilihan == "3":
                print("\n--- Daftar Kelas Saat Ini ---")
                sistem.tampilkan_kelas()
                nama_kelas = input_teks("Nama kelas baru: ")
                sistem.buat_kelas(nama_kelas)
                print(f"Kelas {nama_kelas} berhasil dibuat.")
                
                jawaban = input("Tetapkan wali kelas sekarang? (y/n): ").strip().lower()
                if jawaban == "y":
                    print("\n--- Daftar Guru ---")
                    sistem.tampilkan_guru()
                    nip = input_teks("NIP guru: ")
                    sistem.tetapkan_wali_kelas(nama_kelas, nip)
                    print("Wali kelas berhasil ditetapkan.")
                input("\n[Enter untuk lanjut..]\n")
                
            elif pilihan == "4":
                print("\n--- Pilih Kelas ---")
                if not sistem._daftar_kelas:
                    print("Belum ada kelas yang terdaftar. Silakan buat kelas terlebih dahulu (Menu 3).")
                    input("\n[Enter untuk lanjut..]\n")
                    continue
                    
                sistem.tampilkan_kelas()
                print("0. Kembali")
                nama_kelas = input_teks("Masukkan nama kelas yang ingin dikelola (atau 0 untuk kembali): ")
                
                if nama_kelas == "0":
                    continue
                if nama_kelas not in sistem._daftar_kelas:
                    print("Kelas tidak ditemukan.")
                    input("\n[Enter untuk lanjut..]\n")
                    continue
                    
                kelola_kelas(sistem, nama_kelas)
                
            elif pilihan == "5":
                print("\n--- Seluruh Data Siswa ---")
                sistem.tampilkan_siswa()
                input("\n[Enter untuk lanjut..]\n")
                
            elif pilihan == "6":
                print("\n--- Seluruh Data Guru ---")
                sistem.tampilkan_guru()
                input("\n[Enter untuk lanjut..]\n")
                
            elif pilihan == "7":
                print("\n--- Seluruh Kelas dan Daftar Siswa ---")
                sistem.tampilkan_kelas()
                input("\n[Enter untuk lanjut..]\n")
                
            elif pilihan == "8":
                print("\n--- Seluruh Pengguna ---")
                sistem.tampilkan_semua_pengguna()
                input("\n[Enter untuk lanjut..]\n")
                
            elif pilihan == "0":
                print("Terima kasih. Program selesai.")
                break
                
            else:
                print("Pilihan tidak tersedia. Masukkan angka 0 sampai 8.")
                
        except ValueError as error:
            print(f"Terjadi kesalahan: {error}")
            input("\n[Enter untuk lanjut..]\n")
        except Exception as error:
            print(f"Terjadi kesalahan yang tidak terduga: {error}")
            input("\n[Enter untuk lanjut..]\n")

if __name__ == "__main__":
    jalankan_program()