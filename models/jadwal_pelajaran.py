

class JadwalPelajaran:
    """Menyimpan satu jadwal pelajaran."""

    def __init__(self, nama_kelas, mata_pelajaran, guru, hari, jam):
        self.nama_kelas = nama_kelas
        self.mata_pelajaran = mata_pelajaran
        self.guru = guru
        self.hari = hari
        self.jam = jam

    def tampilkan_jadwal(self):
        return (
            f"{self.hari}, {self.jam} | Kelas: {self.nama_kelas} | "
            f"Mapel: {self.mata_pelajaran} | Guru: {self.guru.nama}"
        )
