from tugas.dosen import Dosen
from tugas.mahasiswa import Mahasiswa
from tugas.adminjurusan import AdminJurusan


dosen = Dosen()
mahasiswa = Mahasiswa()
admin_jurusan = AdminJurusan()

dosen.mencatat_kehadiran()
mahasiswa.mencatat_kehadiran()
admin_jurusan.mencatat_kehadiran()

dosen.membuat_ujian()
mahasiswa.mengerjakan_ujian()
admin_jurusan.publikasi_jadwal()