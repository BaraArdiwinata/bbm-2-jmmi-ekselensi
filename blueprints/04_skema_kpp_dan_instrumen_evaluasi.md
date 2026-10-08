# 04 — Skema KPP dan Instrumen Evaluasi

**Program:** BBM 2 JMMI ITS Kabinet Ekselensi 2026
**Pengelola:** Badan Personalia (Sie Registrasi dan Data, Sie Simulasi, dan tim Evaluasi)
**Versi:** 1.0, 8 Oktober 2026
**Status KPP:** Konsep disetujui sebagai arahan Ketua Pelaksana pada 8 Oktober 2026. Status "HOLD" sebelumnya dicabut.

> **Isi dokumen.** Bagian 1 memuat instrumen evaluasi hari-H (pre-test, post-test, form umpan balik). Bagian 2 memuat KPP Output 1 "Ngopi Khidmah" dan Form Minat Peran. Bagian 3 memuat KPP Output 2 "1-Page Canvas Biro Masa Depan". Bagian 4 memuat timeline dan monitoring. Bagian 5 memuat tindak lanjut database kader. Bagian 6 memuat rangkuman TUK dan sumber datanya.

---

## 1. Mekanisme Evaluasi Hari-H

### 1.1 Rancangan Umum

| Unsur | Rancangan |
|---|---|
| Medium | Google Form, diakses melalui **QR code** (poster di meja registrasi dan di layar) |
| Pre-test | 08.00–08.20 saat registrasi (±8 menit pengerjaan) |
| Post-test | 16.00–16.10 (±8 menit pengerjaan), sebelum penutupan |
| Isi | 13 butir pengetahuan (pilihan ganda, skor 0–100), 6 butir sikap (skala 1–5), 1–2 butir terbuka |
| Tujuan | Mengukur **kenaikan pemahaman** dan **perubahan sikap** peserta, serta menjadi sumber TUK K2–K5 dan K10 |
| Identitas | **Kode Peserta** (contoh `BBM2-17`) yang tercetak pada name tag. Digunakan untuk memasangkan pre dan post tanpa menampilkan nama pada analisis |
| Bentuk butir | **Butir sama** pada pre dan post, dengan **urutan opsi diacak** oleh Google Form. Keterbatasan: efek ingatan. Dicatat sebagai keterbatasan, bukan dihilangkan |

### 1.2 Pengaturan Google Form

1. Aktifkan **mode kuis** (skor otomatis) untuk Bagian B (pengetahuan). Bagian C (sikap) dan D (terbuka) tidak diskor.
2. Kunci jawaban dimasukkan sesuai 1.4. Jangan tampilkan jawaban benar setelah mengirim (supaya pre-test tidak membocorkan post-test).
3. Bagian A: **Kode Peserta** (jawaban singkat, validasi ekspresi reguler `^BBM2-[0-9]{2}$`) dan **Biro Asal** (dropdown 8 biro). Wajib diisi.
4. Pilihan: acak urutan opsi; satu respons per orang (batasi lewat kode); tidak mengumpulkan alamat surel; batas waktu tidak dipasang (ditutup panitia).
5. Buat dua formulir terpisah: **BBM2-PRETEST** dan **BBM2-POSTTEST**. Kedua formulir menautkan ke satu Google Sheet analisis.
6. Uji coba dengan 5 orang pada **H-6 (9 November)**.

### 1.3 Struktur Formulir

| Bagian | Isi | Skor |
|---|---|---|
| A. Identitas | Kode Peserta, Biro Asal | Tidak diskor |
| B. Pengetahuan | 13 butir pilihan ganda | 1 poin per butir, skor akhir = (benar ÷ 13) × 100 |
| C. Sikap dan kesiapan | 6 butir skala 1–5 | Tidak diskor, dianalisis sebagai rerata |
| D. Terbuka | Pre: 1 butir; Post: 2 butir (opsional) | Dianalisis kualitatif |

### 1.4 Butir Pengetahuan dan Kunci Jawaban

Rujukan pasal mengacu pada dokumen `tata_kelola_organisasi_jmmi_kabinet_ekselensi_2026.pdf`.

**Butir 1.** Menurut Tata Kelola, kelompok yang termasuk **Fungsionaris** adalah...
- A. Kepala Biro, Staf Ahli Biro, dan Staf Muda Biro
- B. Ketua Badan, Asisten Badan, Sekretaris Badan, Ketua Departemen, dan Sekretaris Departemen
- C. Ketua Umum, Wakil Ketua, Sekretaris Umum, dan Bendahara Umum
- D. Staf Ahli Badan, Kepala Biro, dan Sekretaris Pelaksana

**Kunci: B** (5.3.1.2). *Modul: M1. Indikator: membedakan Fungsionaris dan Eksekutif.*

**Butir 2.** Kepala Biro termasuk unsur...
- A. Badan Pengurus Inti
- B. Fungsionaris
- C. Eksekutif
- D. Unit (Badan Semi Otonom)

**Kunci: C** (5.3.2). *Modul: M1.*

**Butir 3.** Terhadap operasional biro, Kepala Departemen berwenang untuk...
- A. mengambil alih pelaksanaan program biro apabila lambat
- B. mengangkat dan memberhentikan Staf Muda
- C. menyetujui kerja sama eksternal biro secara mandiri
- D. memberi arahan, rekomendasi, asistensi, monitoring, dan evaluasi **tanpa mengambil alih kewenangan operasional biro**

**Kunci: D** (5.5.2.5; 5.6.6). *Modul: M1. Kelompok K5.*

**Butir 4.** Arahan Staf Ahli kepada Staf Muda bersifat...
- A. arahan teknis sesuai bidang keahlian, dan permintaan data dilakukan dengan sepengetahuan Kabiro
- B. instruksi penugasan penuh atas nama Kabiro
- C. keputusan final pembagian tugas biro
- D. persetujuan anggaran biro

**Kunci: A** (5.6.10). *Modul: M1. Kelompok K5.*

**Butir 5.** Untuk kebutuhan sumber daya dan anggaran biro, Kepala Biro...
- A. memutuskan sendiri lalu melapor setelahnya
- B. meminta langsung ke Bendahara Umum tanpa melalui Kadep
- C. **mengusulkan** kepada Kepala Departemen
- D. meminta persetujuan Staf Ahli

**Kunci: C** (5.6.9 c). *Modul: M1. Kelompok K5.*

**Butir 6.** Laporan progres dan kendala Staf Muda disampaikan...
- A. langsung ke Wakil Ketua
- B. melalui atasan langsung secara berjenjang
- C. kepada biro lain
- D. kepada Sekretaris Umum

**Kunci: B** (5.5.1). *Modul: M2. Kelompok K5.*

**Butir 7.** Koordinasi langsung antarbiro diperbolehkan dengan syarat...
- A. memiliki izin tertulis dari BPI
- B. hanya bila kedua biro berada pada satu departemen
- C. hanya melalui grup umum
- D. tetap diketahui koordinator masing-masing

**Kunci: D** (5.5.1). *Modul: M2. Kelompok K5.*

**Butir 8.** Tawaran kerja sama dari pihak eksternal disalurkan melalui jalur...
- A. Biro Relasi dan Hubungan Eksternal → Kadep Relasi dan Advokasi + Waket III → biro yang sesuai
- B. langsung ke Kepala Biro terkait
- C. Biro Digital Production
- D. Sekretaris Umum saja

**Kunci: A** (5.5.2.7). *Modul: M2.*

**Butir 9.** Keputusan yang wajib mendapat persetujuan BPI adalah...
- A. pembagian tugas internal biro
- B. jadwal piket staf
- C. perubahan kebijakan organisasi, program kerja lintas bidang, atau tata kelola organisasi
- D. format caption unggahan

**Kunci: C** (5.5.2.7 penutup). *Modul: M2.*

**Butir 10.** Tim media (Digipro atau Medsist) berhak menolak atau menunda request apabila...
- A. request diajukan melalui Google Form
- B. brief tidak jelas atau diajukan terlalu dekat dengan deadline
- C. requester adalah Kepala Biro
- D. request menyangkut kajian keislaman

**Kunci: B** (6.4.12). *Modul: M2.*

**Butir 11.** Batas waktu asistensi proposal kegiatan dan batas penyerahan proposal ke Sekretaris Umum secara berurutan adalah...
- A. H-2 minggu dan H-1 minggu
- B. H-2 bulan dan H-1 bulan
- C. H-1 minggu dan H-3 hari
- D. H-1 bulan dan H-2 minggu

**Kunci: D** (6.1.2 c; asistensi H-1 bulan, penyerahan ke Sekum H-2 minggu). *Modul: M2.*

**Butir 12.** Asistensi SPJ dan LPJ kepada Sekretaris Umum dan Bendahara Umum dilakukan paling lambat...
- A. SPJ H+3 dan LPJ H+14
- B. SPJ H+7 dan LPJ H+30
- C. SPJ H+14 dan LPJ H+3
- D. keduanya H+7

**Kunci: A** (6.1.6 b). *Modul: M2.*

**Butir 13 (kasus).** Seorang Waket memberi instruksi lisan langsung kepada Anda sebagai Staf Muda, dan instruksi itu bertentangan dengan arahan Kabiro Anda. Langkah paling tepat adalah...
- A. mengeksekusi karena Waket lebih tinggi
- B. mengabaikan instruksi tersebut
- C. menyampaikan ke Kabiro agar dikonfirmasi ke Kadep melalui jalur koordinasi
- D. membahasnya di grup angkatan

**Kunci: C** (5.5.1 dan 5.5.2.3; pelaporan melalui atasan langsung). *Modul: M1, M2, Simulasi (inject B). Kelompok K5.*

**Ringkasan kunci:** 1B · 2C · 3D · 4A · 5C · 6B · 7D · 8A · 9C · 10B · 11D · 12A · 13C.

**Pemetaan butir ke modul:** M1: butir 1–5. M2: butir 6–12. Simulasi dan M1/M2: butir 13.

**Kelompok butir jalur dan wewenang (K5):** butir 3, 4, 5, 6, 7, 13.

> **Catatan validasi:** kunci disusun dari teks Tata Kelola yang telah dibaca. Pasal 6.4.12 dan 6.1.6 sudah dikonfirmasi pada teks. Sebelum formulir dikunci, Badan Keorganisasian dan Sekum meninjau butir 9, 11, dan 12 supaya sejalan dengan interpretasi resmi terbaru.

### 1.5 Butir Sikap dan Kesiapan (Skala 1–5)

Skala: 1 = Sangat tidak setuju, 2 = Tidak setuju, 3 = Netral, 4 = Setuju, 5 = Sangat setuju.

| Kode | Pernyataan | Dimensi |
|---|---|---|
| L1 | Saya memahami batas wewenang Kabiro, Staf Ahli, dan Staf Muda. | Pemahaman peran |
| L2 | Saya tahu langkah yang harus ditempuh ketika koordinasi dengan biro lain menemui jalan buntu. | Pemahaman jalur |
| L3 | Saya percaya diri memimpin sebuah tim biro. | Kepercayaan diri |
| L4 | Saya merasa organisasi memberi dukungan memadai bagi pengurus yang naik ke peran struktural. | Persepsi dukungan |
| L5 | Saya bangga menjadi bagian dari JMMI ITS. | Kebanggaan |
| L6 | Saya siap berkhidmah pada peran struktural di kepengurusan berikutnya. | Kesiapan berkhidmah |

### 1.6 Butir Terbuka

| Formulir | Butir | Wajib |
|---|---|---|
| Pre-test | "Satu hal yang paling Anda khawatirkan jika diberi peran struktural di kepengurusan berikutnya." | Tidak |
| Post-test | "Satu hal yang paling mengubah cara pandang Anda hari ini." | Tidak |
| Post-test | "Satu hal yang masih Anda ragukan (boleh dikosongkan)." | Tidak |

Butir terbuka dibuat opsional dan tidak dipaksa. Isinya dipakai untuk pembinaan, bukan penilaian.

### 1.7 Analisis Data

**A. Skor pengetahuan:**
- Skor = (jumlah benar ÷ 13) × 100.
- Rerata pre, rerata post, dan selisih.

**B. N-Gain per peserta dan kelompok (Hake):**

> g = (skor post − skor pre) ÷ (100 − skor pre)

Kategori: **g ≥ 0,70** tinggi · **0,30 ≤ g < 0,70** sedang · **g < 0,30** rendah. Peserta dengan skor pre 100 dikeluarkan dari perhitungan g. Rerata kelompok dihitung sebagai g rerata dari data yang dipasangkan.

**C. Rumus di Google Sheets (contoh):** bila `A2` = kode peserta, `B2` = skor pre, dan sheet `POST` memuat kode di kolom A dan skor di kolom B:
- Skor post: `=IFERROR(VLOOKUP(A2,POST!A:B,2,FALSE),"")`
- N-Gain: `=IF(OR(B2="",C2="",B2=100),"",(C2-B2)/(100-B2))`
- Rerata g: `=AVERAGE(D2:D71)`
- Proporsi post ≥ 70: `=COUNTIF(C2:C71,">=70")/COUNT(C2:C71)`
- Proporsi benar kelompok K5: tabulasi butir 3, 4, 5, 6, 7, 13 dari data respons kuis.

**D. Butir sikap:** rerata per butir untuk pre dan post; selisih rerata. K10 memakai selisih rerata L6. Untuk menghindari kesalahan membaca, laporkan juga **sebaran** (persentase pilihan 1–2, 3, 4–5), bukan hanya rerata.

**E. Butir terbuka:** pengodean tema oleh dua anggota tim (kategori contoh: beban waktu, kemampuan diri, ketidakjelasan peran, dukungan, kebanggaan, relasi antar-pengurus). Hasil dibagikan sebagai ringkasan tanpa nama.

### 1.8 Interpretasi dan Tindak Lanjut

| Temuan | Tafsir | Tindak lanjut |
|---|---|---|
| Butir tertentu menunjukkan < 60% benar pada post-test | Materi terkait kurang tersampaikan atau butir ambigu | Evaluasi pemateri dan butir. Sertakan penjelasan pada ringkasan pasca-acara |
| N-Gain rerata < 0,30 | Efek materi rendah | Telaah desain sesi dan tindak lanjut lewat Ngopi Khidmah |
| L4 (dukungan organisasi) rendah | Persepsi dukungan kurang | Catat sebagai masukan ke Badan Keorganisasian dan BPI |
| L6 turun atau tetap rendah | Keraguan berkhidmah belum terjawab | Prioritaskan peserta tersebut untuk pendampingan Ngopi Khidmah, dengan persetujuan mereka |
| Jawaban terbuka memuat hambatan akademik berulang | Beban akademik adalah faktor utama | Bahas di rapat Personalia: mekanisme kelonggaran peran atau peran ringan |

### 1.9 Form Umpan Balik (H+1)

Dikirim **16 November (H+1)** lewat tautan agar waktu penutupan hari-H tidak terpotong. Tidak diskor.

| Bagian | Butir |
|---|---|
| Penilaian per sesi (skala 1–5) | Untuk M1, M2, M3, Simulasi, dan M4: (a) relevansi, (b) kejelasan penyampaian, (c) kebermanfaatan bagi persiapan peran |
| Simulasi | Tingkat kesulitan (terlalu mudah, pas, terlalu sulit); kejelasan aturan; keadilan |
| Panitia | Registrasi, konsumsi, venue, dan audio-visual (skala 1–5) |
| Terbuka | Hal terbaik; hal yang perlu diperbaiki; saran untuk BBM berikutnya |

K9 (rerata kepuasan ≥ 4,2) dihitung dari rata-rata relevansi, kejelasan, dan kebermanfaatan tiap sesi.

---

## 2. KPP Output 1 (Individu): "Ngopi Khidmah"

### 2.1 Tujuan

1. Memberi peserta gambaran jujur dan langsung tentang realitas peran struktural dari orang yang menjalaninya.
2. Menghubungkan calon penerus dengan Kabiro atau Staf Ahli aktif sehingga serah-terima pengetahuan terjadi secara manusiawi.
3. Memberi ruang aman bagi peserta untuk menyampaikan keraguan dan harapannya.
4. Menghasilkan **Lembar Refleksi** yang menjadi bahan portofolio suksesi dan masukan bagi organisasi.

### 2.2 Konsep

Ngopi Khidmah adalah **wawancara santai 1-on-1** antara satu peserta (Staf Muda angkatan 2025) dan satu narasumber (Kepala Biro atau Staf Ahli yang sedang aktif). Suasananya seperti ngobrol sambil ngopi: hangat, bukan interogasi dan bukan ujian. Tempat bebas dan nyaman: kantin, selasar masjid, atau sekretariat.

### 2.3 Aturan Pairing

| Aturan | Isi |
|---|---|
| Ketersediaan narasumber | Seluruh Kabiro (8 orang) dan Staf Ahli aktif. Jumlah Staf Ahli riil belum dikonfirmasi (deck menunjukkan beberapa biro memiliki 5–6 Staf Ahli), sehingga total narasumber diperkirakan ≥ 24 |
| Beban narasumber | **Maksimal 3 peserta per narasumber** selama jendela pelaksanaan. Dengan 24 narasumber, kapasitas 72 sesi, cukup untuk 50–70 peserta |
| Pilihan peserta | Peserta mengisi dua pilihan peran minat (Kabiro atau Staf Ahli) dan dua pilihan biro minat pada Form Minat Peran |
| Penugasan | Badan Personalia memasangkan: pilihan 1 diutamakan; bila penuh, pilihan 2. **Peserta tidak dipasangkan dengan narasumber dari biro asalnya** pada pilihan 1 agar peserta mendapat perspektif baru; boleh sama bila peserta menghendaki |
| Pengumuman | Daftar pairing diumumkan **H+2 (17 November)** |
| Pengganti | Bila narasumber berhalangan, Personalia menunjuk pengganti dari biro yang sama atau terdekat |

### 2.4 Pedoman Pelaksanaan

| Unsur | Ketentuan |
|---|---|
| Durasi | 45–60 menit |
| Jendela | **H+4 s.d. H+10** (19–25 November) |
| Inisiatif | **Peserta** menghubungi narasumber dan menentukan jadwal (melatih adab komunikasi) |
| Format | Tatap muka (utama). Daring hanya bila darurat |
| Biaya | Tidak diwajibkan. Konsumsi ditanggung masing-masing atau sukarela. Tidak ada anggaran dalam RAB KPP kecuali diputuskan lain |
| Catatan | Peserta meminta izin mencatat. Tidak merekam tanpa izin eksplisit |
| Privasi | Hal yang disampaikan narasumber tentang orang lain tidak disebarluaskan. Lembar Refleksi tidak memuat nama pihak ketiga |

### 2.5 Panduan Wawancara

**Sebelum bertemu (5 menit):** baca Tata Kelola 5.6.9 (Ketua Biro) atau 5.6.10 (Staf Ahli); siapkan 3 pertanyaan pilihan sendiri.

**Alur 4 sesi:**

| Sesi | Durasi | Tema | Pertanyaan inti | Pertanyaan lanjutan |
|---|---|---|---|---|
| 1. Awal Mula | 10' | Mengapa bertahan | (1) Apa yang membuat Kakak memilih bertahan setelah menjadi Staf Muda? (2) Momen paling berkesan di JMMI? | Siapa yang paling berjasa membimbing Kakak? |
| 2. Realitas Peran | 20' | Gambaran harian | (3) Ceritakan satu hari kerja terbaik dan satu hari terberat sebagai Kabiro/Staf Ahli. (4) Apa yang paling mengejutkan saat transisi ke struktur Biro? (5) Bagaimana Kakak membagi waktu dengan akademik? (6) Apa yang tidak tertulis di Tata Kelola tapi harus dipelajari? | Apa yang akan Kakak lakukan berbeda? |
| 3. Jalur dan Hubungan | 15' | Koordinasi | (7) Ceritakan koordinasi lintas biro yang paling alot dan bagaimana menyelesaikannya. (8) Kapan Kakak mengeskalasi ke Kadep, dan kapan menyelesaikan sendiri? (9) Bagaimana hubungan Kabiro dan Staf Ahli di biro Kakak? | Adakah pasal yang menurut Kakak perlu dirapikan? |
| 4. Estafet | 10' | Pesan | (10) Pesan Kakak untuk calon penerus? (11) Hal yang ingin Kakak wariskan, dan hal yang ingin Kakak hentikan? (12) Satu saran untuk Kadep atau BPI? | Apa yang Kakak harapkan dari saya? |

**Etika pewawancara (peserta):** mendengarkan lebih banyak daripada berbicara; tidak menghakimi; boleh menyampaikan kekhawatiran sendiri; menutup dengan terima kasih dan tindak lanjut kecil.

**Kartu panduan narasumber:**
1. Jawab jujur, termasuk tentang beban. Tidak perlu mengagungkan maupun menakut-nakuti.
2. Jangan menekan peserta untuk menyatakan siap. Tujuannya berbagi, bukan merekrut.
3. Jaga privasi pihak ketiga.
4. Bila peserta menyampaikan keraguan, tanggapi dengan empati dan tawarkan pendampingan lanjutan.
5. Boleh mengarahkan peserta ke Kadep atau Badan Personalia untuk persoalan yang di luar kewenangan Anda.

### 2.6 Output: Lembar Refleksi (1 halaman)

Berformat dokumen satu halaman (Times New Roman 12, spasi 1,15 sesuai 6.1(a)). Dikumpulkan lewat formulir atau folder bersama.

| No | Bagian | Isi | Panjang |
|---|---|---|---|
| 1 | Identitas | Kode peserta, biro asal, peran dan biro narasumber (nama boleh dicantumkan atas persetujuan narasumber), tanggal | 1 baris |
| 2 | Tiga pelajaran utama | Tiga hal paling berharga yang dipelajari | 3 butir |
| 3 | Dua fakta mengejutkan | Dua hal yang berbeda dari dugaan | 2 butir |
| 4 | Praktik baik untuk diadopsi | Satu praktik konkret yang akan dipakai bila menjabat | 2–3 kalimat |
| 5 | Kekhawatiran yang terjawab dan yang belum | Dua daftar pendek | 2–4 kalimat |
| 6 | Saran untuk organisasi | Satu saran untuk Kadep, BPI, atau Badan Personalia (opsional, boleh kosong) | 1–2 kalimat |
| 7 | Komitmen kecil | Satu langkah kecil dalam 30 hari | 1 kalimat |

**Rubrik kelengkapan (bukan penilaian ketat):**

| Kriteria | Skor 25 | Skor 15 | Skor 5 |
|---|---|---|---|
| Kelengkapan bagian | Semua bagian terisi | Satu bagian kosong | Banyak bagian kosong |
| Kedalaman refleksi | Spesifik dan menyebut contoh | Cukup spesifik | Umum |
| Keterhubungan dengan Tata Kelola dan materi | Mengaitkan dengan pasal atau konsep BBM 2 | Menyebut sebagian | Tidak terhubung |
| Kejujuran dan ketulusan | Menyampaikan keraguan atau harapan nyata | Netral | Normatif |

Skor dipakai untuk memberi umpan balik, bukan peringkat. Pengumpulan tepat waktu dan lengkap sudah dianggap memenuhi TUK K12.

### 2.7 Instrumen: Form Minat Peran Suksesi

Form Minat Peran adalah instrumen pasangan Ngopi Khidmah. Peserta mengisinya **setelah** Ngopi (disarankan) tetapi tenggat tetap H+14. Tujuannya mengetahui kesiapan dan hambatan, bukan menyeleksi.

**Bagian 1 — Persetujuan dan identitas**

| No | Butir | Jenis | Wajib |
|---|---|---|---|
| 1.1 | Pernyataan: "Saya memahami bahwa data ini dipakai Badan Personalia untuk pembinaan dan perencanaan suksesi, diakses terbatas, dan **tidak** dipakai untuk menghukum atau menandai saya." | Centang persetujuan | Ya |
| 1.2 | Nama lengkap | Jawaban singkat | Ya |
| 1.3 | Kode peserta | Jawaban singkat | Ya |
| 1.4 | Angkatan dan jurusan | Jawaban singkat | Ya |
| 1.5 | Biro asal | Dropdown | Ya |

**Bagian 2 — Minat peran**

| No | Butir | Pilihan |
|---|---|---|
| 2.1 | Peran yang paling Anda minati pada kepengurusan berikutnya | Kepala Biro · Staf Ahli Biro · Staf Ahli Badan · Peran di Badan (Asisten atau Sekretaris) · Belum yakin · Tidak melanjutkan pada periode berikutnya |
| 2.2 | Biro atau badan yang diminati (pilihan 1) | 8 biro dan 3 badan |
| 2.3 | Biro atau badan yang diminati (pilihan 2) | Sama |
| 2.4 | Alasan pilihan 1 | Jawaban paragraf |
| 2.5 | Tingkat kesiapan saat ini | Skala 1–5 (1 = belum siap, 5 = sangat siap) |

**Bagian 3 — Hambatan dan dukungan**

| No | Butir | Jenis |
|---|---|---|
| 3.1 | Hal yang paling menghambat Anda melanjutkan (pilih hingga 3) | Waktu akademik · Praktikum atau tugas akhir · Kesehatan · Keluarga · Merasa belum mampu · Peran tidak jelas · Beban organisasi terlalu berat · Iklim koordinasi · Minat lain · Lainnya |
| 3.2 | Dukungan yang Anda butuhkan (pilih hingga 3) | Pendampingan mentor · Pelatihan tambahan · Peran yang lebih ringan · Kejelasan jalur dan SOP · Dukungan Kadep · Fleksibilitas jadwal · Lainnya |
| 3.3 | Tiga hal yang membuat Anda bertahan di JMMI | Jawaban singkat (3 baris) |
| 3.4 | Tiga hal yang membuat Anda ragu | Jawaban singkat (3 baris) |

**Bagian 4 — Tindak lanjut**

| No | Butir | Jenis |
|---|---|---|
| 4.1 | Apakah Anda bersedia dihubungi Badan Personalia untuk pendampingan? | Ya · Tidak · Nanti saja |
| 4.2 | Catatan bebas | Paragraf (opsional) |

**Pengodean untuk database** (oleh Personalia setelah H+14):

| Kategori | Kriteria | Tindakan |
|---|---|---|
| **Siap** | 2.1 menyebut peran dan 2.5 ≥ 4 | Masuk daftar kandidat pipeline |
| **Siap dengan syarat** | 2.1 menyebut peran dan 2.5 = 3, atau memilih dukungan tertentu | Pendampingan sesuai kebutuhan |
| **Ragu** | 2.1 "Belum yakin" atau 2.5 ≤ 2 | Percakapan 1-on-1 oleh Personalia (jika bersedia, 4.1) |
| **Belum bisa periode depan** | 2.1 "Tidak melanjutkan" | Catat alasan (3.1), tetap jaga hubungan dan tawarkan peran ringan di periode lain |

Kategori dipakai untuk **perencanaan dan pembinaan**, bukan untuk menekan atau menyeleksi.

---

## 3. KPP Output 2 (Kelompok): "1-Page Canvas Biro Masa Depan"

### 3.1 Tujuan

1. Memetakan kondisi biro hari ini secara jujur: kendala, praktik yang bekerja, dan jalur koordinasi.
2. Merumuskan inovasi kepengurusan depan secara terukur (format OKR).
3. Menyusun satu dokumen ringkas yang dapat langsung dipakai sebagai bahan serah-terima biro.

### 3.2 Kelompok

- **Satu kelompok = satu biro asal peserta.** Jumlah kelompok 8: Biro Manajemen Event, Biro Pengabdian Masyarakat, Biro Kajian & Inovasi Dakwah, Biro Usaha Mandiri, Biro Amaliyah Yaumiyah, Biro Digital Production, Biro Media Analysis & Strategi, dan Biro Relasi & Hubungan Eksternal. Ukuran kelompok mengikuti jumlah Staf Muda tiap biro.
- Kelompok Canvas **tidak** mengikuti penggabungan meja pada Simulasi Taktis. Meski dua biro duduk satu meja karena hadir kurang dari 3 orang, tiap biro tetap menyusun Canvas sendiri.
- Satu **koordinator** dipilih kelompok. Seluruh anggota berkontribusi.
- Kelompok **boleh** meminta masukan dari Kabiro dan Staf Ahli biro sendiri (dan dari hasil Ngopi Khidmah).

### 3.3 Format Canvas

**Satu halaman** A4 landscape (PDF), satu slide Google Slides berukuran A4, atau gambar tercetak digital. Nama berkas `Canvas_Biro_[Nama Biro]_BBM2.pdf` (contoh `Canvas_Biro_Kajian dan Inovasi Dakwah_BBM2.pdf`), mengikuti pola penamaan arsip SOP 6.2.

| Blok | Judul | Pertanyaan pemandu | Isi minimal |
|---|---|---|---|
| 0 | Identitas | Biro apa, proker utama apa, siapa saja yang menyusun? | Nama biro, proker unggulan, nama anggota |
| 1 | Kondisi Hari Ini: Kendala | Apa tiga kendala terbesar yang dialami biro pada kepengurusan ini? | **3 kendala** dengan bukti singkat (kejadian, frekuensi, dampak) |
| 2 | Akar Masalah | Mengapa kendala itu terjadi? | Satu analisis "mengapa" bertingkat per kendala (minimal dua tingkat) |
| 3 | Yang Sudah Bekerja | Praktik apa yang bagus dan perlu dipertahankan? | **2 praktik** dengan alasan |
| 4 | Peta Jalur Koordinasi Biro | Dengan biro mana kita paling sering berinteraksi, apa yang diminta dan diberikan, kapan eskalasi? | **2–4 biro mitra**; arah (kita meminta atau diminta), isi, jalur, dan titik eskalasi menurut Tata Kelola |
| 5 | Inovasi Kepengurusan Depan | Apa tiga inisiatif perbaikan untuk periode berikutnya? | **3 inisiatif**, tiap inisiatif disertai Objective dan 2 Key Results terukur |
| 6 | Kebutuhan Dukungan | Apa yang dibutuhkan dari Kadep, Waket, BPI, atau badan? | 2–3 butir konkret |
| 7 | Risiko dan Mitigasi | Apa risiko utama dan rencana menghadapinya? | **2 risiko** dengan mitigasi |
| 8 | Rencana Serah-Terima | Dokumen dan pengetahuan apa yang harus diwariskan? | Daftar minimal 4 dokumen, mis. kalender kerja tahunan, riwayat proker, kontak dan alur, templat, pelajaran |
| 9 | Pesan Tim | Satu kalimat untuk penerus. | 1 kalimat |

**Panduan tata letak:** grid 3 kolom × 3 baris di bawah header identitas; blok 1–2 di kolom kiri, 3–5 di tengah, 6–9 di kanan. Font minimal 9 pt supaya terbaca.

**Contoh ilustratif satu blok** (fiktif, hanya untuk memperjelas bentuk):

> *Blok 1 — Kendala (contoh untuk "Biro X"):*
> *1. Permintaan dari biro lain datang mendadak (±3 kali per bulan), mengganggu jadwal produksi.*
> *2. Tidak ada pembagian tugas tertulis antara Kabiro dan Staf Ahli, sehingga dua orang memberi arahan berbeda ke Staf Muda.*
> *3. Dokumen proker tersebar di banyak tempat, sehingga serah-terima lambat.*

> *Blok 5 — Inovasi (contoh):*
> *Inisiatif 1: Kalender request bulanan.*
> *Objective: permintaan lintas biro terencana.*
> *KR1: 80% permintaan masuk ≥ 7 hari sebelum tenggat. KR2: ≤ 2 permintaan mendadak per bulan.*

### 3.4 Rubrik Canvas (100 poin)

| Kriteria | Bobot | Skor tinggi | Skor sedang | Skor rendah |
|---|---|---|---|---|
| **1. Kedalaman diagnosis** | 20 | Kendala berbukti dan akar masalah tingkat dalam | Kendala jelas, akar masalah dangkal | Kendala umum tanpa bukti |
| **2. Kekonkretan dan keterukuran inovasi** | 25 | Tiga inisiatif dengan Objective dan 2 KR terukur | KR sebagian tidak terukur | Inisiatif umum tanpa KR |
| **3. Kelayakan** | 20 | Sesuai kapasitas biro, dukungan realistis, risiko ditangani | Sebagian ambisius tanpa dukungan | Tidak realistis |
| **4. Keterkaitan dengan Tata Kelola dan Peta Jalur** | 20 | Jalur koordinasi dan eskalasi sesuai pasal dan akurat | Sebagian benar | Keliru atau kosong |
| **5. Kualitas serah-terima dan kejelasan visual** | 15 | Daftar dokumen lengkap, tata letak rapi, dan terbaca | Cukup | Berantakan atau tidak lengkap |

**Predikat:** ≥ 85 Sangat baik · 70–84 Baik · 55–69 Cukup · < 55 Perlu revisi. Predikat dipakai untuk umpan balik. Pengumpulan memenuhi TUK K13.

### 3.5 Umpan Balik dan Pemanfaatan

1. **Draf** dikumpulkan **H+7 (22 November)** untuk umpan balik cepat dari Badan Personalia.
2. **Sesi umpan balik** 15 menit per biro bersama Kadep biro tersebut dan Personalia pada **H+11–H+13 (26–28 November)** (daring atau tatap muka).
3. **Final** dikumpulkan **H+14 (29 November)**.
4. Hasil terpilih dapat diteruskan sebagai bahan Musyker atau rapat evaluasi kepengurusan, bila Ketua menghendaki. Hal ini perlu keputusan terpisah.
5. Badan Keorganisasian menerima ringkasan **kendala yang berulang lintas biro** sebagai masukan perbaikan tata kelola.

---

## 4. Timeline dan Monitoring KPP

### 4.1 Kalender

| Hari | Tanggal | Kegiatan | PIC |
|---|---|---|---|
| H+0 | Minggu, 15 November | BBM 2: pre-test, post-test, pengumuman ringkas KPP pada penutupan | Panitia |
| H+1 | Senin, 16 November | Peluncuran KPP: **Form Minat Peran** dibuka; Form Umpan Balik dikirim; pedoman Ngopi Khidmah dan templat Canvas dibagikan; kelompok Canvas dibentuk | Sie Registrasi dan Data |
| H+2 | Selasa, 17 November | Pengumuman daftar **pairing** Ngopi Khidmah | Badan Personalia |
| H+3 | Rabu, 18 November | Batas asistensi SPJ BBM 2 kepada Sekum dan Bendum (urusan panitia, bukan KPP) | Sekretaris Pelaksana dan Bendahara Pelaksana |
| H+4 s.d. H+10 | 19–25 November | **Jendela Ngopi Khidmah** | Peserta |
| H+4 | Kamis, 19 November | Pengingat 1: mulai jadwalkan Ngopi | Personalia |
| H+7 | Minggu, 22 November | **Draf Canvas** dikumpulkan; pengingat 2: sisa 3 hari Ngopi | Koordinator kelompok |
| H+10 | Rabu, 25 November | **Batas Lembar Refleksi Ngopi**; pengingat 3 | Peserta |
| H+11 | Kamis, 26 November | **Snapshot data KPP** diserahkan ke Sekretaris Pelaksana untuk draf LPJ | Sie Registrasi dan Data |
| H+11–H+13 | 26–28 November | Sesi umpan balik Canvas per biro | Personalia, Kadep |
| H+13 | Sabtu, 28 November | Pengingat 4: final Form Minat Peran dan Canvas besok | Personalia |
| H+14 | Minggu, 29 November | **Batas final:** Form Minat Peran, Canvas final. **Batas asistensi LPJ** kepada Sekum dan Bendum | Peserta, Sekretaris Pelaksana |
| H+15–H+18 | 30 November–3 Desember | Tabulasi data dan pengodean kategori | Badan Personalia |
| H+19–H+21 | 4–6 Desember | Laporan KPP kepada Waket II dan Ketum; rencana pendampingan | Badan Personalia |

### 4.2 Penyiasatan Jadwal LPJ

LPJ wajib mencantumkan Realisasi TUK, tetapi asistensi LPJ jatuh pada **H+14 (Minggu, 29 November)**, bersamaan dengan batas KPP. Oleh karena itu:
- **Opsi A (disarankan):** LPJ disiapkan lebih dulu dengan **snapshot KPP H+11 (26 November)**; angka KPP final dilampirkan sebagai addendum bila Sekum dan Bendum menerima.
- **Opsi B:** bila addendum tidak diterima, tenggat KPP dimajukan menjadi **H+12 (27 November)** dan hari H+13–H+14 hanya untuk perbaikan.
- Keputusan antara A dan B dikonfirmasi ke Sekum dan Bendum paling lambat **H+3 (18 November)**.

### 4.3 Dashboard Monitoring (Google Sheets)

| Kolom | Isi |
|---|---|
| Kode peserta | `BBM2-01` … |
| Biro asal | 8 biro |
| Narasumber Ngopi | Nama peran dan biro |
| Status pairing | Belum, Terjadwal, Selesai |
| Tanggal Ngopi | Tanggal |
| Lembar Refleksi | Belum, Diterima, Direvisi |
| Form Minat Peran | Belum, Diisi |
| Kategori minat | Siap, Siap dengan syarat, Ragu, Belum bisa |
| Kelompok Canvas | Kode biro |
| Status Canvas | Belum, Draf, Final |
| Catatan Personalia | Teks bebas |

**Ringkasan otomatis:** persentase pairing terjadwal dan selesai, persentase Lembar Refleksi diterima (K12), persentase Form Minat Peran diisi (K11), jumlah biro dengan Canvas final (K13), sebaran kategori minat.

### 4.4 Pengingat dan Eskalasi

| Kondisi | Tindakan |
|---|---|
| Peserta belum menjadwalkan Ngopi pada H+7 | Personalia menghubungi lewat pesan pribadi dan menanyakan hambatan |
| Narasumber tidak merespons 3 hari | Personalia menghubungi narasumber dan memberi alternatif |
| Biro belum menyerahkan draf Canvas pada H+7 | Personalia menghubungi koordinator |
| Kelompok Canvas macet | Pendampingan 15 menit oleh anggota Personalia |
| Tingkat pengumpulan < 60% pada H+10 | Pengingat dari Waket II kepada Kabiro terkait |

---

## 5. Tindak Lanjut Database Kader untuk Badan Personalia

### 5.1 Skema Data

| Tabel | Sumber | Isi inti |
|---|---|---|
| Profil peserta | Registrasi dan Form Minat Peran | Nama, angkatan, jurusan, biro asal |
| Kesiapan dan minat | Form Minat Peran | Peran minat, pilihan biro, tingkat kesiapan, kategori |
| Hambatan dan dukungan | Form Minat Peran | Hambatan, kebutuhan dukungan, hal yang membuat bertahan dan ragu |
| Hasil belajar | Pre-test dan post-test | Skor pre, post, N-Gain, sikap L1–L6 |
| Hasil KPP | Dashboard | Status Ngopi, Lembar Refleksi, Canvas |
| Observasi kontribusi (Simulasi Taktis) | Lembar Observasi Kepemimpinan Emergen (formulir terpisah, dokumen 03 bagian 10) | Skor 1–4 pada 6 dimensi perilaku dengan bukti singkat per kode peserta; momen kunci saat Inject B dan C. **Bukan peringkat dan bukan dasar tunggal seleksi** |
| Pendampingan | Catatan Personalia | Tanggal, bentuk, ringkasan, tindak lanjut |

### 5.2 Tata Kelola Data

| Prinsip | Ketentuan |
|---|---|
| Akses | Terbatas pada anggota Badan Personalia yang ditunjuk, Waket II, dan Ketua Umum |
| Tujuan | Pembinaan, perencanaan suksesi, dan perbaikan program. **Bukan** untuk menghukum atau menandai peserta |
| Persetujuan | Peserta menyetujui pada Bagian 1 formulir |
| Keputusan seleksi peran | Tetap mengikuti mekanisme BPI. KPP dan catatan observasi simulasi **hanya** masukan, bukan penentu |
| Transparansi observasi | Peserta diberi tahu pada briefing simulasi bahwa pola kontribusi dicatat untuk pembinaan (naskah di dokumen 03, bagian 4.1) |
| Retensi | Disimpan selama satu periode kepengurusan untuk keperluan serah-terima. Setelah itu dihapus atau dianonimkan kecuali ada persetujuan lain |
| Penyimpanan | Folder bersama dengan akses dibatasi di Google Drive JMMI ITS 2026 (SOP 6.1.2) |
| Pelaporan | Hanya agregat anonim ke forum yang lebih luas |

### 5.3 Tindakan Badan Personalia

| Waktu | Tindakan |
|---|---|
| H+15–H+18 | Tabulasi dan pengodean kategori (Siap, Siap dengan syarat, Ragu, Belum bisa) |
| H+16–H+19 | Peta kekosongan dan kebutuhan peran per biro (berapa calon Kabiro dan Staf Ahli per biro) |
| H+19–H+21 | Percakapan 1-on-1 dengan peserta kategori **Ragu** yang bersedia dihubungi |
| H+21 | Laporan kepada Waket II dan Ketum: ringkasan kesiapan, hambatan dominan, rekomendasi dukungan |
| Berkelanjutan | Rencana pendampingan (mentoring, pelatihan tambahan, peran ringan) untuk kategori **Siap dengan syarat** dan **Ragu** |

### 5.4 Indikator Pemanfaatan

1. Seluruh peserta yang menyatakan bersedia dihubungi memperoleh tindak lanjut maksimal 14 hari setelah data final.
2. Peta kekosongan peran per biro tersedia sebelum proses seleksi peran dimulai.
3. Ringkasan kendala lintas biro dari Canvas diterima Badan Keorganisasian.

---

## 6. Rangkuman TUK dan Sumber Datanya

| Kode | Indikator | Target usulan | Instrumen | Waktu |
|---|---|---|---|---|
| K1 | Kehadiran | ≥ 90% | Daftar hadir digital | 15 Nov |
| K2 | Rerata skor post-test | ≥ 75 | Post-test | 15 Nov |
| K3 | N-Gain rerata | ≥ 0,40 | Pre dan post-test | 15 Nov |
| K4 | Peserta dengan skor post ≥ 70 | ≥ 80% | Post-test | 15 Nov |
| K5 | Ketepatan butir jalur dan wewenang (butir 3, 4, 5, 6, 7, 13) | ≥ 80% benar | Post-test | 15 Nov |
| K6 | Relasi Deal pada Papan Jaring | ≥ 12 dari 16 | `PAPAN_JARING` | 15 Nov |
| K7 | Pelanggaran arah per biro | Rata-rata ≤ 1 | `SKOR_EVALUASI` | 15 Nov |
| K8 | Biro dengan Blok E dan persetujuan Kadep | 8 dari 8 | `PAPAN_JARING` | 15 Nov |
| K9 | Kepuasan per materi | ≥ 4,2 | Form Umpan Balik | 16 Nov |
| K10 | Kenaikan rerata L6 | ≥ +0,5 | Pre dan post-test | 15 Nov |
| K11 | Pengisian Form Minat Peran | ≥ 85% | Form Minat Peran | 29 Nov |
| K12 | Lembar Refleksi Ngopi | ≥ 85% | Dashboard | 25–29 Nov |
| K13 | Biro menyerahkan Canvas | 8 dari 8 | Dashboard | 29 Nov |

**Penyajian dalam LPJ (BAB II 2.4):** tiap TUK ditampilkan dengan kolom *Target*, *Realisasi*, *Persentase capaian*, dan *Keterangan* (alasan bila belum tercapai). Evaluasi (BAB III) memuat kendala, solusi, serta keberhasilan dan hal yang perlu ditingkatkan.

**Catatan:** seluruh target adalah usulan sampai disetujui Ketua. Perubahan angka cukup dilakukan pada tabel ini dan pada dokumen 01 bagian 4.4.

---

## 7. Risiko KPP dan Mitigasi

| Risiko | Dampak | Mitigasi |
|---|---|---|
| Peserta menganggap KPP sebagai beban tambahan | Pengumpulan rendah | Batasi ukuran output (1 halaman), beri panduan jelas, jendela cukup panjang, dan pengingat ramah |
| Narasumber kewalahan | Sesi tertunda | Batas maksimal 3 peserta per narasumber dan cadangan |
| Form Minat Peran dipahami sebagai alat seleksi | Peserta tidak jujur | Pernyataan privasi tegas, penjelasan lisan pada penutupan, dan kategori dipakai untuk pembinaan |
| Data sensitif bocor | Kepercayaan hilang | Akses terbatas dan retensi jelas |
| Jadwal KPP berbenturan dengan ujian atau tugas akademik | Pengumpulan rendah | Pantau kalender akademik. Bila bentrok, longgarkan tenggat Ngopi sampai H+12 dan tetap pertahankan H+14 untuk final |
| Canvas hanya dikerjakan koordinator | Beban tidak merata | Setiap blok diberi penanggung jawab dalam kelompok, dan koordinator melaporkan kontribusi |
| Tumpang tindih dengan LPJ | Realisasi TUK terlambat | Gunakan opsi A atau B pada 4.2 |
