# 03 — Petunjuk Pelaksanaan Simulasi Taktis

**Nama sesi:** Simulasi Taktis (Live Cross-Bureau Coordination Game)
**Waktu:** Sabtu, 14 November 2026. Briefing 13.06–13.11, **simulasi 13.11–13.41 (30 menit)**, presentasi dan ulasan hasil 13.41–14.11
**Peserta:** Staf Muda angkatan 2025, ±50–70 orang, duduk per meja menurut **biro asalnya**
**Fasilitator:** Badan Personalia (Bidang 2)
**Medium:** Google Sheets (`main/template_simulasi_taktis.xlsx`) dan Kartu Rahasia (`main/kartu_skenario_simulasi.md`)
**Versi:** 2.3, topologi 16 relasi diseimbangkan menjadi 2 keluar dan 2 masuk per biro dengan kasus yang disesuaikan pada OKR riil (November 2026). Versi 2.2: durasi simulasi 30 menit dan presentasi hasil 30 menit (1 November 2026, hasil rapat Ketua Pelaksana dan Badan Personalia). Versi 2.3 juga memangkas template Sheets menjadi 11 tab Ultra-Lean (lihat bagian 8). Versi 2.1 menambahkan pembingkaian "simulasi berbasis konvensi struktur kabinet saat ini" (24 Oktober 2026); versi 2.0 adalah revisi atas arahan Ketua

---

## 0. Ringkasan Perubahan dari Versi 1.0

| No | Aspek | Versi 1.0 | Versi 2.0 (arahan Ketua) |
|---|---|---|---|
| 1 | Durasi | 80 menit (P1 10, P2 40, P3 20, P4 10) | **30 menit** (P1 4, P2 17, P3 4, P4 5), direvisi dari 40 menit pada versi 2.2. Inject dimampatkan menjadi menit ke-8, 12, dan 16 |
| 2 | Penamaan | Kode dua huruf pada narasi dan tabel | **Nama biro ditulis lengkap.** Kode hanya tinggal di dalam skrip generator. ID Tiket memakai nomor relasi R-01 sampai R-16 |
| 3 | Peran tim | Kabiro, Staf Ahli, Staf Muda, dan peran lain ditetapkan panitia | **Tidak ada jabatan yang ditunjuk.** Semua setara di awal; kepemimpinan tumbuh organik dan menjadi bahan observasi non-formal Badan Personalia |
| 4 | Pembentukan tim | Acak lintas biro asal | **Berbasis biro asal.** Satu meja diisi Staf Muda dari biro yang sama. Bila hadir kurang dari 3 orang, digabung dengan biro lain dalam **departemen yang sama** |

Dampak lanjutan: debrief diperpanjang menjadi 25 menit (versi 2.0, kini diganti presentasi dan ulasan 30 menit pada versi 2.2), jumlah pengamat bertambah, dan Kartu Rahasia memakai suara "tim biro" tanpa istilah Kabiro atau Staf Ahli.

### 0.1 Pembingkaian: Simulasi Berbasis Konvensi Struktur Kabinet Saat Ini

Tata Kelola Kabinet Ekselensi 2026 belum disahkan secara final dan belum pasti dipertahankan pada kepengurusan berikutnya. Keputusan Ketua Pelaksana (pasca-audiensi): Simulasi Taktis resmi dibingkai sebagai **simulasi berbasis konvensi struktur kabinet saat ini**. Konsekuensinya:

1. Semua rujukan "SOP", "Tata Kelola", jalur eskalasi, dan bagian **"Batasan wewenang dan SOP"** pada Kartu Rahasia adalah **aturan permainan**, bukan pasal baku yang dijamin berlaku pada kepengurusan berikutnya.
2. Yang dilatih adalah **prinsip**: koordinasi asertif (memberi tahu, meminta persetujuan, memutuskan bersama), negosiasi berbasis kepentingan, eskalasi dengan format fakta–opsi–permintaan arahan, dan musyawarah. Prinsip ini sejalan dengan Materi 3.
3. Fasilitator menyampaikan pembingkaian ini pada briefing (4.1) dan mengaitkannya saat presentasi dan ulasan (11.7). Titik ambigu yang muncul dicatat sebagai masukan untuk Badan Keorganisasian (11.8).
4. Pada versi 2.1 tidak ada perubahan pada graf 16 relasi, kasus biro, inject, rubrik, atau template Google Sheets. Graf dan kasus baru dirombak pada versi 2.3 (lihat 3.2 dan 3.3).

---

## 1. Konsep Game

### 1.1 Gambaran Umum

Simulasi Taktis adalah **satu ronde terpadu** berdurasi **30 menit**. Delapan biro, yaitu **Biro Manajemen Event, Biro Pengabdian Masyarakat, Biro Kajian & Inovasi Dakwah, Biro Usaha Mandiri, Biro Amaliyah Yaumiyah, Biro Digital Production, Biro Media Analysis & Strategi, dan Biro Relasi & Hubungan Eksternal**, menjalankan proker amanahnya bersamaan menuju sebuah **Hari Puncak** yang fiktif. Kondisi awal adalah **H-21**. Semua kesepakatan lintas biro harus tuntas dalam satu sesi, yang dianggap sebagai pekan perencanaan.

Ketergantungan antar-biro bersifat **asimetris dan searah** (directed graph). Setiap biro hanya boleh **memulai** koordinasi ke **dua** biro tujuan dan menerima tepat dua biro pengirim, sehingga beban tiap meja seimbang (2 keluar, 2 masuk). Tiket yang diterima dijawab di tiket yang sama. Dengan begitu seluruh delapan biro bergerak serentak membentuk satu jaring kerja.

### 1.2 Tujuan Belajar

1. Menerapkan prinsip koordinasi (memberi tahu, meminta persetujuan, memutuskan bersama) dan memilih jalur yang tepat: koordinasi langsung atau eskalasi, menurut konvensi struktur saat ini (Tata Kelola 5.5.1).
2. Bernegosiasi lintas biro dengan kapasitas terbatas dan menghasilkan kesepakatan konkret dalam waktu singkat.
3. Mengambil keputusan bersama di bawah tekanan tanpa melampaui wewenang biro.
4. Melapor dan meminta arahan Kadep dengan format *fakta → opsi → permintaan arahan*.
5. Merasakan beban peran struktural secara aman, sehingga keraguan bisa dibicarakan jujur pada Materi 4 dan KPP.
6. Menumbuhkan dan mengamati kepemimpinan yang muncul secara alami dalam tim (lihat bagian 10).

### 1.3 Mengapa 30 Menit

| Pertimbangan | Penjelasan |
|---|---|
| Ritme dan tekanan | Waktu yang ketat memaksa tim memprioritaskan, berbagi tugas, dan bergerak tanpa menunggu aba-aba. Itu cermin kondisi nyata ketika banyak biro bersaing untuk sumber daya yang sama |
| Menghindari kejenuhan | Sesi 80 menit berisiko menurun energinya pada sesi siang. Format padat menjaga fokus |
| Pembelajaran tetap dalam | Pendalaman berpindah ke presentasi dan ulasan 30 menit, sehingga pelajaran tidak hilang karena sesi singkat |
| Tetap utuh | Seluruh 16 relasi dan 3 inject dipertahankan, hanya dimampatkan |

### 1.4 Mengapa Tanpa Jabatan yang Ditunjuk

Pada organisasi nyata, orang yang naik ke peran struktural sering tidak dipilih karena jabatannya, melainkan karena sudah terlihat memimpin dalam praktik. Dengan memulai semua peserta dari posisi setara:
- Peserta merasakan sendiri apa yang terjadi ketika tidak ada pembagian peran: siapa yang bergerak lebih dulu, siapa yang merangkum, siapa yang ragu.
- Badan Personalia memperoleh gambaran objektif tentang bibit suksesor, sebagai pelengkap Form Minat Peran dan Canvas Biro Masa Depan.
- Prinsip musyawarah (Tata Kelola 7.1.1) dilatih, bukan hanya dibaca.

Risiko dan pengamannya dibahas di bagian 2.5 dan bagian 10.

---

## 2. Parameter dan Skala

### 2.1 Pembentukan Meja Berbasis Biro Asal

1. **Satu meja = satu biro.** Seluruh Staf Muda dari suatu biro duduk bersama dan memegang Kartu Rahasia biro itu. Contoh: meja Biro Manajemen Event diisi Staf Muda Biro Manajemen Event.
2. **Tujuan:** memperkuat bonding dan rasa memiliki internal biro lebih dulu. Peserta bekerja dengan orang yang sudah dikenal, sementara kesulitan sesungguhnya ada pada negosiasi dengan meja lain.
3. **Dasar data:** biro asal dari form RSVP (ditutup 6 November) dan konfirmasi kehadiran (13 November).
4. **Name tag** berwarna sesuai biro asal. Warna yang sama dipasang pada papan nama meja.
5. **Tidak ada penunjukan** Kepala Biro, Staf Ahli, atau peran lain oleh panitia (lihat 2.3).

### 2.2 Penggabungan Biro bila Hadir Kurang dari 3 Orang

**Ketentuan:** bila suatu biro hadir **kurang dari 3 orang**, biro itu digabung dengan biro lain dalam **departemen yang sama**. Penggabungan **tidak boleh lintas departemen**.

| Departemen | Biro yang dapat saling digabung |
|---|---|
| Syi'ar | Biro Manajemen Event dan Biro Pengabdian Masyarakat |
| Pelayanan Masjid & Dakwah | Biro Kajian & Inovasi Dakwah dan Biro Amaliyah Yaumiyah |
| Media, Informasi & Digitalisasi | Biro Digital Production dan Biro Media Analysis & Strategi |
| Relasi Publik & Advokasi | Biro Relasi & Hubungan Eksternal dan Biro Usaha Mandiri |

**Mekanisme meja gabungan** (interpretasi penyusun atas arahan Ketua; mohon konfirmasi):
- Meja gabungan memegang **dua Kartu Rahasia** dan membuka **dua tab** Google Sheets, agar kedelapan biro tetap hadir dan seluruh 16 relasi tetap utuh.
- Anggota biro kecil bergabung ke meja biro partner. Seluruh anggota meja bekerja untuk kedua biro.
- Bila di antara dua biro yang digabung terdapat relasi resmi (hanya Biro Kajian & Inovasi Dakwah → Biro Amaliyah Yaumiyah, serta Biro Digital Production → Biro Media Analysis & Strategi), relasi itu **tetap dicatat sebagai tiket tertulis** pada kedua tab dan Kadep diinfokan, tidak boleh diselesaikan hanya secara lisan.
- Bila kedua biro dalam satu departemen sama-sama kurang dari 3 orang, keduanya dijadikan satu meja. Bila total hadir satu departemen kurang dari 3 orang, Ketupel dan Sie Simulasi memutuskan apakah anggota Badan Personalia menjadi peserta pengganti (tanpa mengambil kendali).
- Bila satu biro hadir lebih dari 10 orang, tambahkan kursi di meja yang sama; meja tidak dibagi.

**Contoh ilustratif** (bukan data riil; jumlah hadir 58):

| Biro | Hadir | Keputusan |
|---|---|---|
| Biro Manajemen Event | 8 | Meja sendiri |
| Biro Pengabdian Masyarakat | 2 | Kurang dari 3, **digabung ke meja Biro Manajemen Event** (10 orang, 2 kartu) |
| Biro Kajian & Inovasi Dakwah | 9 | Meja sendiri |
| Biro Amaliyah Yaumiyah | 8 | Meja sendiri |
| Biro Digital Production | 7 | Meja sendiri |
| Biro Media Analysis & Strategi | 6 | Meja sendiri |
| Biro Relasi & Hubungan Eksternal | 9 | Meja sendiri |
| Biro Usaha Mandiri | 9 | Meja sendiri |

Keputusan penggabungan final diumumkan pada **13 November (H-2)** berdasarkan konfirmasi kehadiran, dan ditampilkan di meja registrasi pada hari-H.

### 2.3 Prinsip Kepemimpinan Organik (Emergent Leadership)

- **Tidak ada penunjukan** Kepala Biro, Staf Ahli, ketua, juru bicara, atau pencatat oleh panitia. Semua peserta memulai dari posisi setara.
- Fasilitator **tidak menunjuk dan tidak menyarankan** siapa yang memimpin. Bila tim bertanya "siapa yang jadi ketua?", jawabannya: "Itu keputusan tim."
- Peran yang muncul secara alami dapat berupa: pemrakarsa, pengarah diskusi, pencatat, penghubung antarmeja, penjaga waktu, analis kapasitas, penengah, atau pelapor ke Kadep. **Semua peran bernilai**, tidak hanya yang paling vokal.
- Batas wewenang menurut konvensi struktur saat ini tetap berlaku sebagai aturan permainan: keputusan yang melampaui batas wewenang biro tetap harus dieskalasi ke Kadep, sebanyak apa pun anggota yang menyetujuinya.
- Keputusan tim diambil lewat musyawarah (Tata Kelola 7.1.1) dan dicatat pada tab biro.

### 2.4 Fasilitator dan Pengamat

| Peran | Jumlah | Tugas |
|---|---|---|
| Kadep Pelayanan Masjid & Dakwah | 1 | Menerima eskalasi dari Biro Kajian & Inovasi Dakwah dan Biro Amaliyah Yaumiyah |
| Kadep Syi'ar | 1 | Menerima eskalasi dari Biro Manajemen Event dan Biro Pengabdian Masyarakat |
| Kadep Media, Informasi & Digitalisasi | 1 | Menerima eskalasi dari Biro Digital Production dan Biro Media Analysis & Strategi; menyetujui publikasi kilat |
| Kadep Relasi Publik & Advokasi | 1 | Menerima eskalasi dari Biro Relasi & Hubungan Eksternal dan Biro Usaha Mandiri |
| Waket (I dan III) / BPI | 1–2 | Menerima eskalasi lintas departemen atau lintas bidang; menjalankan peran pada Inject B |
| Bendum | 1 | Menjawab pertanyaan kanal donasi, bagi hasil merchandise amal, dana takjil KSSI, dan penerimaan uang |
| Pengendali waktu dan Master Inject | 1 | Menjalankan jam dan mengumumkan inject |
| Operator Papan Jaring | 1 | Menampilkan `PAPAN_JARING` dan memantau Sheets |
| **Pengamat meja (Badan Personalia)** | **8** | **Satu pengamat per meja** mencatat pola kontribusi individu (bagian 10) |
| Penilai kinerja meja | 1–2 | Mengisi rubrik meja di `SKOR_EVALUASI` setelah sesi (dari Tabel 1–3 tab biro dan Papan Jaring) |
| **Total** | **±17–19** | |

Peran Kadep dimainkan oleh anggota Badan Personalia atau pengurus yang memahami wewenang Kadep. Pemateri yang masih hadir boleh mengisi peran, tetapi tidak wajib. **Pengamat meja tidak boleh ikut mengarahkan tim.**

### 2.5 Pengamanan terhadap Bias dan Transparansi

| Risiko | Pengaman |
|---|---|
| Menyamakan "vokal" dengan "mampu memimpin" | Instrumen mencatat enam dimensi perilaku, termasuk mendengarkan, merangkum, dan kontribusi pendukung, bukan hanya intensitas bicara |
| Peserta yang pendiam dianggap tidak berpotensi | Observasi hanyalah satu sumber data. Dilengkapi Form Minat Peran dan Canvas Biro Masa Depan. Tidak ada keputusan seleksi dari satu sumber |
| Pengamat subjektif | Kalibrasi di technical meeting (11 November) dengan contoh perilaku dan skala bersama |
| Peserta tidak tahu sedang diamati | **Transparansi:** pada briefing, fasilitator menyampaikan bahwa pola kontribusi dicatat untuk pembinaan, bukan nilai lulus atau gagal (naskah di 4.1) |
| Kebocoran catatan | Catatan hanya diakses Badan Personalia, Waket II, dan Ketua Umum, di formulir terpisah dari berkas simulasi |
| Dipakai untuk menghukum | Dilarang. Catatan dipakai untuk pembinaan dan pemetaan pipeline, sesuai tata kelola data di dokumen 04 |

---

## 3. Aturan Main dan Directed Graph

### 3.1 Delapan Aturan Rantai Koordinasi Asimetris

| No | Aturan | Dasar |
|---|---|---|
| 1 | Setiap biro hanya boleh **menginisiasi** koordinasi ke **2 biro tujuan** di kartunya (terkunci). Menerima permintaan dari biro mana pun diperbolehkan. | Desain simulasi |
| 2 | Tiket yang **diterima** dijawab di tiket yang sama (membalas, menawar, memberi syarat), bukan dengan membuka tiket baru. Seluruh 16 tiket **searah murni** (asimetris): tidak ada dua biro yang saling memulai tiket satu sama lain. | Desain simulasi |
| 3 | Butuh sesuatu di luar 2 target? **Eskalasi ke Kadep.** Kadep menentukan jalurnya. | 5.5.2.7 (eskalasi) |
| 4 | Koordinasi lintas departemen atau bidang wajib **diinfokan** ke Kadep masing-masing. | 5.5.1 ("diketahui koordinator masing-masing") |
| 5 | Request ke Biro Digital Production dan Biro Media Analysis & Strategi wajib lewat form dan lead time; keduanya **berhak menolak atau menunda** bila brief tidak jelas, terlalu mepet, atau kapasitas penuh. Kontak ke pihak eksternal **hanya** lewat Biro Relasi & Hubungan Eksternal. | 6.4.3, 6.4.12, 5.5.2.7 |
| 6 | Satu tiket = satu kebutuhan = satu ID. ID Tiket adalah **nomor relasi** (R-01 sampai R-16), ditambah huruf bila ada lebih dari satu tiket pada relasi yang sama (R-02a). Biro penerima mencatat ID yang sama. | Desain simulasi |
| 7 | **Tanpa jabatan yang ditunjuk.** Keputusan diambil bersama lewat musyawarah dan dicatat. Komitmen yang melampaui batas wewenang dieskalasi. | 7.1.1 |
| 8 | Kesepakatan yang menyangkut anggaran di luar RAB, perubahan kebijakan, atau program lintas bidang tidak diputuskan sendiri: Kadep → Waket → BPI. | 5.5.2.7 penutup |

**Pelanggaran arah** (membuka tiket ke biro di luar daftar 2 tujuan) dicatat pengamat dan dibahas pada presentasi dan ulasan, tanpa teguran di depan umum. Template tidak memuat penanda otomatis agar peserta fokus bergerak.

### 3.2 Enam Belas Relasi Resmi

Arah panah: **biro pengusung → biro tujuan** (pengusung adalah pihak yang boleh memulai).

| No | Biro Pengusung | Biro Tujuan | Esensi target kesepakatan |
|---|---|---|---|
| R-01 | Biro Manajemen Event | Biro Relasi & Hubungan Eksternal | Medpar dan undangan resmi LDK se-Surabaya untuk Maulid × Milad lewat jalur Relasi: PIC tunggal, tenggat surat, prioritas bila kuota pintu eksternal terbatas |
| R-02 | Biro Manajemen Event | Biro Usaha Mandiri | Pinjam GoRent internal gratis (HT, kabel roll, proyektor, standing banner): ketersediaan unit terhadap booking klien luar, jadwal, PIC, dan jaminan perawatan lewat berita acara |
| R-03 | Biro Pengabdian Masyarakat | Biro Digital Production | Poster darurat open donasi banjir JMMI Peduli ≤ 24 jam: jalur darurat terhadap aturan pengajuan 7 hari, isi wajib (kanal resmi, penanggung jawab, jadwal laporan) |
| R-04 | Biro Pengabdian Masyarakat | Biro Relasi & Hubungan Eksternal | Pilihan 1 mitra penyalur resmi dari kandidat beserta syarat verifikasi, PIC, dan prosedur kerja sama lewat jalur khusus |
| R-05 | Biro Kajian & Inovasi Dakwah | Biro Usaha Mandiri | Paket sarapan SaJi 50–75 porsi per sesi lewat JMMI Commerce: harga rata-rata terhadap plafon, jadwal antar, standar menu, cara bayar |
| R-06 | Biro Kajian & Inovasi Dakwah | Biro Amaliyah Yaumiyah | Penugasan kader da'i dan silabus kultum 10 menit untuk buka bersama KSSI dan penutupan OWOJ: slot, jam kultum terhadap azan, persetujuan silabus |
| R-07 | Biro Usaha Mandiri | Biro Media Analysis & Strategi | Slot kalender konten dan jadwal tayang di Instagram JMMI untuk katalog sewa GoRent dan pre-order merchandise JMMI Store: jumlah slot, bundling, tenggat file final, prioritas terhadap konten donasi |
| R-08 | Biro Usaha Mandiri | Biro Pengabdian Masyarakat | Merchandise amal totebag dan stiker relawan JMMI Mengabdi: jumlah produksi, harga, bagi hasil ke kas JMMI Peduli lewat Bendum, tenggat pre-order |
| R-09 | Biro Amaliyah Yaumiyah | Biro Manajemen Event | Protokol adab masjid, jeda salat di rundown, zonasi makan di luar karpet utama, dan penugasan petugas GDM pada Hari Puncak |
| R-10 | Biro Amaliyah Yaumiyah | Biro Media Analysis & Strategi | Slot dan kalender konten bulanan KSSI (feed, reels, rilis kalender puasa sunnah di Instagram JMMI): format, tenggat brief, jadwal tayang |
| R-11 | Biro Digital Production | Biro Manajemen Event | Fiksasi live streaming kajian akbar Maulid × Milad: titik kamera, jalur listrik dan videotron, rundown dokumentasi, jadwal survei sebelum Aula terkunci, tenaga operator akhir pekan |
| R-12 | Biro Digital Production | Biro Amaliyah Yaumiyah | Teknis STREAMMI khatmil Qur'an OWOJ: posisi kamera dan tripod, jam persiapan sebelum Q-TIME, izin pembaca, PIC lokasi, aftermovie |
| R-13 | Biro Media Analysis & Strategi | Biro Kajian & Inovasi Dakwah | Kurasi dalil, hadits, dan sudut pandang syar'i untuk draf opini dan policy brief: alur, waktu review, PIC, format catatan, batas wewenang |
| R-14 | Biro Media Analysis & Strategi | Biro Pengabdian Masyarakat | Data riil desa mitra JMMI Mengabdi untuk artikel rilis media massa kampus: daftar data, tenggat, izin desa, review draf oleh Pengmas |
| R-15 | Biro Relasi & Hubungan Eksternal | Biro Digital Production | Dokumentasi (1 fotografer) dan e-invitation Jaulah LDK di akhir pekan: cakupan, tenaga akhir pekan, tenggat brief, batas revisi |
| R-16 | Biro Relasi & Hubungan Eksternal | Biro Kajian & Inovasi Dakwah | Sinergi rekomendasi narasumber alumni dan ustadz jejaring luar untuk pemateri kajian: kriteria, nama rekomendasi, etiket kontak langsung oleh biro pemilik acara |

### 3.3 Sifat Graf (Telah Diverifikasi Program)

| Properti | Hasil |
|---|---|
| Jumlah relasi | 16 |
| Jumlah tujuan per biro | Tepat 2 |
| Jumlah pengirim per biro | Tepat 2 |
| Pasangan timbal-balik | 0 (tidak ada A→B bersama B→A; diperiksa oleh assert pada skrip generator) |
| Loop diri | 0 |
| Konektivitas | Terhubung kuat: dari tiap biro dapat dicapai tiap biro lain lewat arah panah |

| Biro | Memulai ke | Menerima dari (jumlah) |
|---|---|---|
| Biro Manajemen Event | Biro Relasi & Hubungan Eksternal, Biro Usaha Mandiri | 2 (Biro Amaliyah Yaumiyah, Biro Digital Production) |
| Biro Pengabdian Masyarakat | Biro Digital Production, Biro Relasi & Hubungan Eksternal | 2 (Biro Usaha Mandiri, Biro Media Analysis & Strategi) |
| Biro Kajian & Inovasi Dakwah | Biro Usaha Mandiri, Biro Amaliyah Yaumiyah | 2 (Biro Media Analysis & Strategi, Biro Relasi & Hubungan Eksternal) |
| Biro Usaha Mandiri | Biro Media Analysis & Strategi, Biro Pengabdian Masyarakat | 2 (Biro Manajemen Event, Biro Kajian & Inovasi Dakwah) |
| Biro Amaliyah Yaumiyah | Biro Manajemen Event, Biro Media Analysis & Strategi | 2 (Biro Kajian & Inovasi Dakwah, Biro Digital Production) |
| Biro Digital Production | Biro Manajemen Event, Biro Amaliyah Yaumiyah | 2 (Biro Pengabdian Masyarakat, Biro Relasi & Hubungan Eksternal) |
| Biro Media Analysis & Strategi | Biro Kajian & Inovasi Dakwah, Biro Pengabdian Masyarakat | 2 (Biro Usaha Mandiri, Biro Amaliyah Yaumiyah) |
| Biro Relasi & Hubungan Eksternal | Biro Digital Production, Biro Kajian & Inovasi Dakwah | 2 (Biro Manajemen Event, Biro Pengabdian Masyarakat) |

**Beban seimbang:** tiap biro memegang 2 tiket keluar dan 2 tiket masuk, sehingga tidak ada meja yang pasif maupun kewalahan. Biro Manajemen Event berperan sebagai konsultan dan fasilitator manajemen teknis acara bagi biro lain (R-09, R-11), sesuai praktik panitia event yang mandiri. Graf searah murni, tanpa pasangan timbal-balik.

**Rantai dampak (cascade):**
1. **Venue Hari Puncak:** Biro Manajemen Event menerima dua permintaan untuk Aula dan sekitarnya: zonasi makan, jeda salat, dan petugas GDM dari Biro Amaliyah Yaumiyah (R-09), serta titik kamera, jalur listrik, dan videotron dari Biro Digital Production (R-11). Keduanya berbagi ruang yang sama dan Aula terkunci mulai H-3 pukul 12.00.
2. **GoRent:** Biro Manajemen Event bersaing dengan booking klien eksternal Biro Usaha Mandiri untuk HT dan proyektor pada H-1 sampai Hari Puncak (R-02). Pinjam internal gratis, jadi yang diuji adalah prioritas dan jaminan perawatan.
3. **Slot eksternal Biro Relasi & Hubungan Eksternal (4):** Medpar dan undangan LDK dari Biro Manajemen Event (R-01) bersaing dengan mitra penyalur dari Biro Pengabdian Masyarakat (R-04). Alumni dan mitra lama adalah jalan keluar.
4. **Antrean Biro Digital Production dan Biro Media Analysis & Strategi:** poster darurat donasi (R-03) dan Jaulah (R-15) masuk ke Biro Digital Production; dokumentasi KSSI (R-10) dan katalog serta pre-order JMMI Store (R-07) masuk ke Biro Media Analysis & Strategi. Inject A memotong keduanya menjadi 3.
5. **Kru akhir pekan Biro Digital Production (1 orang):** live streaming Hari Puncak (R-11) dan dokumentasi Jaulah (R-15) sama-sama jatuh pada hari Sabtu.
6. **Khatmil OWOJ:** siaran STREAMMI (R-12) dan kultum kader da'i Biro Kajian & Inovasi Dakwah (R-06) bertemu di acara yang sama milik Biro Amaliyah Yaumiyah.
7. **Rantai kurasi dan data:** Biro Media Analysis & Strategi bergantung pada kurasi Biro Kajian & Inovasi Dakwah (R-13) dan data Biro Pengabdian Masyarakat (R-14), yang sedang sibuk banjir (R-03, R-04).
8. **Biro Usaha Mandiri:** paket sarapan SaJi (R-05), merchandise amal (R-08), dan konten promosi (R-07) bersaing untuk perhatian tim yang sama.

---

## 4. Alur 30 Menit

### 4.1 Briefing (13.06–13.11, 5 menit)

| Menit | Kegiatan | Penyampai |
|---|---|---|
| 0–1 | Tujuan dan gambaran game; kondisi H-21; ritme 30 menit yang sengaja padat; **pembingkaian: "simulasi berbasis konvensi struktur kabinet saat ini"** (aturan dan batas wewenang di kartu adalah aturan permainan, bukan pasal baku; yang dilatih adalah prinsip) | Ketua Pelaksana |
| 1–2 | Aturan arah (2 keluar, 2 masuk), eskalasi, dan larangan membuka tiket di luar daftar | Fasilitator utama |
| 2–3 | **Tidak ada jabatan.** Semua setara; tim menentukan sendiri cara bekerja. Pengumuman meja dan penggabungan bila ada | Fasilitator utama, Sie Simulasi |
| 3–4 | Pengenalan tab Google Sheets (3 tabel di tab biro: misi keluar, koordinasi masuk, eskalasi; dropdown Status; ID tiket) | Operator Papan Jaring |
| 4–5 | Transparansi pengamatan, tanya jawab kilat, lalu pembagian amplop | Fasilitator utama |

**Naskah transparansi pengamatan (wajib dibacakan):**
> "Di setiap meja ada satu pengamat dari Badan Personalia. Pengamat mencatat pola kontribusi kalian, bukan untuk memberi nilai lulus atau gagal, melainkan untuk membantu kami membina dan menyiapkan calon penerus. Tidak ada jawaban benar tentang siapa yang harus memimpin. Mendengarkan, merangkum, mencatat, dan menengahi sama berharganya dengan memimpin diskusi. Catatan hanya dilihat Badan Personalia dan tidak dipakai untuk menghukum siapa pun."

### 4.2 Fase Permainan

| Fase | Menit game | Aktivitas | Output | Yang dilakukan fasilitator |
|---|---|---|---|---|
| **P1 Persiapan** | 0–4 | Seluruh anggota membaca Kartu Rahasia bersama (disediakan 2 salinan per meja), menuliskan nama anggota di sel kuning header tab, dan menyepakati dua tiket yang dibuka lebih dulu. Boleh langsung bergerak | Nama anggota terisi; arah kerja | Memastikan tiap meja membuka tab yang benar. **Tidak menunjuk siapa pun** |
| **P2 Koordinasi dan Inject** | 4–21 | Mendatangi 2 biro tujuan, melayani 2 tamu yang masuk, bernegosiasi, dan mengeskalasi ke Kadep bila macet. Tiga inject berjalan | Hasil Kesepakatan dan Status Tabel 1 dan 2 terisi | Mengumumkan inject pada menit 8, 12, dan 16; memantau Papan Jaring; Kadep menjawab eskalasi |
| **P3 Finalisasi** | 21–25 | Merapikan poin deal pada Tabel 1 dan 2, memastikan Status benar, dan melapor ke Kadep bila ada hal yang perlu persetujuan | Tabel 1 dan 2 final; Tabel 3 bila ada | Kadep memeriksa kesesuaian hasil dengan batas wewenang |
| **P4 Wrap-up** | 25–30 | Layar menampilkan `PAPAN_JARING`; tiap biro menyebut satu kesepakatan terbaik dan satu kompromi tersulit (±30 detik) | Papan final | Operator menampilkan papan; pengendali waktu menjaga 30 detik per biro |

**Penyesuaian akibat pemadatan:**
- Jumlah tiket minimal tetap **2 per biro** (satu per biro tujuan). Tiket boleh ditutup dengan status *Sepakat* walau rincian akhir bersifat bersyarat, asalkan syarat dicatat pada kolom *Syarat*.
- Waktu respons Kadep **maksimal 3 menit**.
- Komunikasi antar-meja boleh lisan untuk kecepatan, dan **poin deal wajib dicatat** pada Tabel 1 (tiket keluar) dan Tabel 2 (tiket masuk).
- Penutupan P3 tepat pada menit 25 agar presentasi dan Ashar tidak bergeser.

### 4.3 Tiket Koordinasi

- Setiap biro memegang **2 tiket keluar dan 2 tiket masuk**. Kolom ID Tiket, biro lawan, dan ringkasan kebutuhan sudah terisi di Tabel 1 dan 2; peserta hanya mengisi sel kuning.
- Setiap tiket memuat satu baris: kebutuhan atau permintaan (terisi), hasil kesepakatan atau respon (poin konkret seperti jumlah, kuota, harga, tenggat, PIC), dan status.
- Status keluar: `Sepakat` / `Masih Negosiasi` / `Batal`. Status masuk: `Diterima` / `Diterima Bersyarat` / `Ditolak`. Pada `PAPAN_JARING` tiket keluar ditampilkan sebagai *Deal / Pending / Batal*.

---

## 5. Katalog Delapan Kasus Biro

> **Penanda angka:** angka **tanpa tanda** bersumber dari OKR Kabinet Ekselensi 2026. Angka bertanda **(sim)** adalah angka simulasi, bersifat fiktif, dan dapat disesuaikan fasilitator setelah divalidasi Kabiro yang bersangkutan.
> **Kondisi dunia simulasi:** sekarang H-21 menuju Hari Puncak (Maulid Nabi × Milad JMMI ke-37). Waktu masjid (sim): Ashar 15.00; Maghrib 17.30; Q-TIME 17.00–17.30 pada hari kerja.
> **Suara kartu:** setiap kartu berbicara kepada "tim biro" tanpa membedakan jabatan.

### 5.1 Kasus 1 — Biro Manajemen Event

| | |
|---|---|
| Departemen / Bidang | Syi'ar · Bidang 1 (Kadep Syi'ar → Waket I) |
| Proker Amanah | **Maulid Nabi × Milad JMMI ke-37** (event Hari Puncak), plus peran konsultan teknis acara bagi biro lain |
| Tiket yang dimulai | **R-01** ke Biro Relasi & Hubungan Eksternal · **R-02** ke Biro Usaha Mandiri |
| Sumber deck | Maulid Nabi dan Milad JMMI: target ≥ 750 peserta, sponsor atau donatur 5, kolaborasi media 5, publikasi konten dan poster, banner di kampus dan masjid, survei kepuasan ≥ 80%. Tiap event membentuk panitia mandiri dengan tupoksi lengkap, sehingga biro ini lebih berperan sebagai konsultan dan fasilitator manajemen teknis acara bagi biro lain |

**Latar belakang / trigger (sim).** Kita lagi nyiapin Maulid Nabi × Milad JMMI ke-37, dan sekarang **H-21**. Panitia kita mandiri dan tupoksinya lengkap, tapi dua hal belum beres: belum ada **Medpar (media partner)** dan **undangan resmi ke LDK se-Surabaya**, dan **alat event** dari GoRent belum dipastikan. Kita tidak boleh menghubungi pihak luar sendiri. Di sisi lain, biro lain akan datang minta izin dan aturan main di venue Hari Puncak.

**Limitasi dan kapasitas.**
- Panitia 55 orang (sim). Target peserta ≥ **750**. Medpar yang dicari minimal 2, idealnya 5 media.
- Undangan resmi ke LDK se-Surabaya (sim: 10 LDK, cukup 1 surat edaran lewat forum LDK).
- Venue Hari Puncak (sim): kajian di **Aula**, yang **terkunci** untuk pasang-bongkar mulai **H-3 pukul 12.00**. Area makan di luar karpet utama (serambi dan pelataran) muat ±250 orang per gelombang.
- Aula punya satu panel listrik dan videotron di sisi panggung (sim). **Semua panitia terikat tugas**, jadi tidak ada tenaga cadangan untuk Hari Puncak.
- Alat yang kita butuhkan H-2 sampai H+1 (4 hari) dari GoRent: **HT 12 (minimal 8), kabel roll 6, proyektor 2 (minimal 1), standing banner 4 (minimal 3)**.
- Pihak luar hanya lewat Biro Relasi & Hubungan Eksternal. Pemateri kajian kita hubungi sendiri.
- Aula tidak boleh dipinjamkan saat terkunci.
- Isi dan urutan kajian utama, serta tanggal Hari Puncak, tidak bisa kita ubah sendiri.

**Misi koordinasi wajib.**
- **R-01 ke Biro Relasi & Hubungan Eksternal:** wajib menyepakati **2 Medpar** dan **1 surat undangan resmi ke LDK se-Surabaya**. Sepakati juga PIC tunggal, tenggat surat, dan siapa yang menghubungi pihak luar. (Bonus: 5 Medpar.) Yang bisa ditawarkan: draf surat dan daftar LDK sudah siap, data acara lengkap, dan kesediaan memakai jalur alumni atau mitra lama kalau jatah pintu eksternal mereka penuh. **Jangan:** menghubungi LDK atau media sendiri lewat jalur pribadi.
- **R-02 ke Biro Usaha Mandiri:** wajib menyepakati unit tersedia (**minimal 8 HT, 6 kabel roll, 1 proyektor, 3 standing banner**) untuk H-2 sampai H+1, **pinjam gratis (Rp0)** karena sesama biro JMMI, plus **jaminan perawatan**: berita acara serah terima dengan foto dan uji fungsi, satu PIC peminjam, dan tanggung jawab bila rusak atau hilang karena kelalaian. (Bonus: HT 12 dan proyektor kedua.) Yang bisa ditawarkan: alat kembali tepat waktu, cek fungsi bareng saat serah terima, dan promosi GoRent di materi acara. Stok dan booking klien luar mereka belum kita tahu. Gali dari mereka.

**Permintaan yang mungkin masuk (2 tiket masuk).**
- **R-09 dari Biro Amaliyah Yaumiyah** (protokol adab masjid, penugasan GDM, dan zonasi makan peserta): Kita bisa memasukkan **jeda salat Dzuhur (11.30–12.15) dan Ashar (15.00–15.45)** ke rundown dan memakai **petugas GDM** dari Biro Amaliyah Yaumiyah. Makan peserta dibagi **3 gelombang** di serambi bawah dan pelataran sisi barat (±250 orang per gelombang), dan karpet utama bebas makanan. Kita tidak bisa mengubah isi atau urutan kajian utama.
- **R-11 dari Biro Digital Production** (titik kamera, jalur listrik atau videotron, dan rundown dokumentasi untuk live streaming kajian akbar Maulid × Milad): Kita bisa memberi **1 titik kamera** di belakang area peserta Aula (bukan di jalur masuk), **1 jalur listrik** dari panel Aula, tempat videotron di sisi panggung, dan **rundown dokumentasi 1 halaman**. Survei lokasi hanya boleh **sebelum H-3 pukul 12.00** karena Aula lalu terkunci. Kita **tidak punya tenaga cadangan** untuk Hari Puncak, jadi operator kamera harus dari tim mereka.

**Batasan wewenang dan SOP.** Perubahan rundown inti, tanggal, atau format Hari Puncak → **Kadep Syi'ar → Waket I → BPI**. Perubahan karpet atau area masjid → **Kadep Pelayanan Masjid & Dakwah** (aturan masjid ada di tangan Takmir). Pinjam inventaris sekretariat (bukan GoRent) → lewat **Sekretaris Umum**.

### 5.2 Kasus 2 — Biro Pengabdian Masyarakat

| | |
|---|---|
| Departemen / Bidang | Syi'ar · Bidang 1 (Kadep Syi'ar → Waket I) |
| Proker Amanah | **JMMI Peduli** (donasi musibah) dan **JMMI Mengabdi** (desa mitra) |
| Tiket yang dimulai | **R-03** ke Biro Digital Production · **R-04** ke Biro Relasi & Hubungan Eksternal |
| Sumber deck | JMMI Peduli OKR 3: open donasi tiap bencana, poster donasi dan publikasi transparansi, 3 kandidat mitra penyalur, fiksasi 1 mitra, survei 1 kali, penyaluran 100% donasi; JMMI Mengabdi: pendampingan desa mitra, artikel media massa, after movie, sertifikat relawan |

**Latar belakang / trigger (sim).** Banjir bandang (sim) menerjang desa dekat mitra JMMI Mengabdi. BPI minta JMMI Peduli bergerak sekarang. Masalahnya, **poster open donasi harus jadi dalam 24 jam**, dan **mitra penyalur yang terverifikasi** harus jelas **sebelum donasi dibuka**. Di saat yang sama, data desa mitra kita masih belum rapi.

**Limitasi dan kapasitas.**
- Tim 4 orang (sim); relawan JMMI Mengabdi 25 orang (sim). Donasi ada dua jenis: dana tunai dan barang kebutuhan pokok.
- Tiga kandidat mitra penyalur (sim): **A** lembaga kemanusiaan nasional (verifikasi 4 hari), **B** komunitas relawan lokal (verifikasi 2 hari, tanpa MoU), **C** mitra JMMI Mengabdi yang sudah dikenal (verifikasi 1 hari, lokasi 30 km dari titik banjir).
- Kanal donasi resmi sudah disetujui Bendum. Data desa mitra (sim): baru sekitar 60% rapi.
- Jangan buka rekening atau kanal donasi sendiri. Rekening resmi dipegang Bendum.
- Uang donasi atau bagi hasil tidak boleh dipegang relawan.

**Misi koordinasi wajib.**
- **R-03 ke Biro Digital Production:** wajib menyepakati **poster open donasi banjir JMMI Peduli jadi paling lama 24 jam** sejak brief lengkap (jalur darurat kemanusiaan), memuat kanal resmi, penanggung jawab, dan jadwal laporan. (Bonus: template **poster transparansi** untuk laporan 7 hari setelah donasi dibuka, boleh menyusul.) Yang bisa ditawarkan: brief lengkap, teks final, foto lokasi, logo mitra, dan kanal donasi yang sudah disetujui Bendum. **Jangan:** minta memuat kanal yang belum disetujui Bendum. Aturan normal mereka butuh pengajuan 7 hari. Gali apakah ada jalur darurat.
- **R-04 ke Biro Relasi & Hubungan Eksternal:** wajib menyepakati **1 mitra penyalur resmi** yang terverifikasi sebelum donasi dibuka (verifikasi maksimal 2 hari). Sepakati syarat verifikasi, PIC, dan cara kerja samanya. Yang bisa ditawarkan: data kebutuhan donasi yang lengkap, dan kesediaan memakai mitra yang sudah dikenal supaya verifikasinya cepat.

**Permintaan yang mungkin masuk (2 tiket masuk).**
- **R-08 dari Biro Usaha Mandiri** (merchandise amal totebag dan stiker relawan JMMI Mengabdi, bagi hasil ke kas JMMI Peduli): Kita senang dapat tambahan dana, tapi **bagi hasil hanya boleh disetor lewat Bendum**, bukan lewat tangan relawan. Kita bisa menawarkan promosi ke 25 relawan dan desa mitra, serta izin memakai nama JMMI Mengabdi dengan syarat tampilan disetujui. Kita **tidak berwenang** menetapkan kebijakan penyaluran dana, itu urusan BPI.
- **R-14 dari Biro Media Analysis & Strategi** (data riil desa mitra untuk artikel rilis media massa kampus): Kita bisa memberi **jumlah penerima manfaat, 3 foto, dan 2 kutipan warga** setelah izin desa keluar, dalam **3 hari kerja**. **Data pribadi warga tidak diberikan.** Draf artikel kita baca dulu (maksimal 2 hari) sebelum terbit. Karena tim lagi sibuk banjir, data lain menyusul.

**Batasan wewenang dan SOP.** Buka rekening atau kanal donasi → **Bendum / BPI**. Ubah target donasi, kebijakan penyaluran, atau skema bagi hasil → **BPI**. Rebutan antrean desain dengan biro lain → **Kadep Media, Informasi & Digitalisasi**. Mitra yang belum pernah bekerja sama wajib lewat verifikasi Biro Relasi & Hubungan Eksternal.

### 5.3 Kasus 3 — Biro Kajian & Inovasi Dakwah

| | |
|---|---|
| Departemen / Bidang | Pelayanan Masjid & Dakwah · Bidang 1 (Kadep Pelayanan Masjid & Dakwah → Waket I) |
| Proker Amanah | **SaJi** (Sarapan & Ngaji), **KID Insight**, dan **Simposium Nalar** |
| Tiket yang dimulai | **R-05** ke Biro Usaha Mandiri · **R-06** ke Biro Amaliyah Yaumiyah |
| Sumber deck | SaJi: minimal 4 kali, rata-rata 75 peserta, vendor konsumsi 75 porsi, RSVP; KID Insight: 12 konten feed berbasis dalil dan data ilmiah, 12 tulisan final untuk didesain Biro Digital Production; Simposium Nalar: 2 kali, minimal 30 peserta, notulensi dan publikasi oleh Biro Media Analysis & Strategi. JMMI Academy tidak terlaksana di kepengurusan riil karena tumpang tindih Minion Class, sehingga tidak dipakai |

**Latar belakang / trigger (sim).** Kita lagi nyiapin **SaJi**, sarapan bareng sambil ngaji, dan sekarang **H-21**. Masalahnya: **paket sarapan** belum dipastikan, padahal RSVP baru 52 dari target rata-rata 75 (sim). Kita juga punya **kader da'i** dan **silabus kultum 10 menit** yang belum punya panggung tetap.

**Limitasi dan kapasitas.**
- SaJi 4 sesi, 50–75 porsi per sesi. Plafon konsumsi (sim): **Rp3.300.000** untuk 300 porsi, artinya rata-rata **Rp11.000 per porsi**.
- Kader da'i terlatih 6 orang dan silabus 8 tema kultum 10 menit (sim).
- Kurasi dalil (sim): maksimal **2 draf per minggu**, 2 hari kerja per draf. Antrean KID Insight lagi padat (12 konten).
- Materi yang mewakili JMMI ke pihak luar harus disetujui Kadep Pelayanan Masjid & Dakwah.
- Kas biro tidak boleh dipakai di luar plafon konsumsi.
- Pemateri atau pengisi acara kita hubungi sendiri, tanpa lewat Relasi.

**Misi koordinasi wajib.**
- **R-05 ke Biro Usaha Mandiri:** wajib menyepakati paket sarapan SaJi **50–75 porsi per sesi untuk 4 sesi**, harga rata-rata **tidak lebih dari Rp11.000 per porsi**, plus jadwal antar sebelum 06.30, standar menu halal, dan cara bayar. Yang bisa ditawarkan: komitmen 4 sesi, jumlah pasti dari RSVP 3 hari sebelumnya, dan promosi JMMI Commerce di materi SaJi. Kapasitas dapur dan harga mereka belum kita tahu. Gali dari mereka.
- **R-06 ke Biro Amaliyah Yaumiyah:** wajib menyepakati **penugasan kader da'i** (satu per sesi) dengan **silabus kultum 10 menit** untuk buka bersama KSSI (Senin dan Kamis, 8 sesi) dan **penutupan OWOJ**. Sepakati jam kultum supaya tidak menabrak azan Maghrib, dan siapa yang menyetujui silabus. Yang bisa ditawarkan: kader terlatih, silabus lengkap yang bisa dibaca dulu, dan latihan 1 kali sebelum sesi pertama. Rundown dan aturan KSSI mereka belum kita tahu. Gali dari mereka.

**Permintaan yang mungkin masuk (2 tiket masuk).**
- **R-13 dari Biro Media Analysis & Strategi** (kurasi dalil, hadits, dan sudut pandang syar'i untuk draf opini dan policy brief): Kita bisa memeriksa **dalil, hadits, dan sudut pandang syar'i** dengan batas 2 draf per minggu dan 2 hari kerja. Hasilnya berupa catatan (aman, perlu diperiksa, atau ganti), bukan menulis ulang. **Keputusan tayang tetap di Biro Media Analysis & Strategi.** Topik sensitif atau khilafiyah dibawa ke Kadep, bukan diputuskan sendiri.
- **R-16 dari Biro Relasi & Hubungan Eksternal** (rekomendasi database narasumber alumni dan ustadz jejaring luar untuk pemateri kajian): Kita bisa menyebut kriteria pemateri (keilmuan, bisa hadir di jam yang cocok) dan menerima **maksimal 5 nama rekomendasi**. Setelah Biro Relasi & Hubungan Eksternal memberi lampu hijau soal etiket, **kita hubungi sendiri** pematerinya. Kita tidak boleh menjanjikan honor tanpa persetujuan Kadep.

**Batasan wewenang dan SOP.** Materi untuk pihak luar, topik sensitif, atau honor pemateri → **Kadep Pelayanan Masjid & Dakwah**. Anggaran konsumsi melewati plafon → **Kadep Pelayanan Masjid & Dakwah dan Bendum**. Beda pendapat soal dalil dengan Biro Media Analysis & Strategi yang tidak selesai di meja → **Kadep Pelayanan Masjid & Dakwah dan Kadep Media, Informasi & Digitalisasi**.

### 5.4 Kasus 4 — Biro Usaha Mandiri

| | |
|---|---|
| Departemen / Bidang | Relasi Publik & Advokasi · Bidang 3 (Kadep Relasi Publik & Advokasi → Waket III) |
| Proker Amanah | **JMMI Store**, **JMMI Commerce**, dan **GoRent** |
| Tiket yang dimulai | **R-07** ke Biro Media Analysis & Strategi · **R-08** ke Biro Pengabdian Masyarakat |
| Sumber deck | JMMI Store: desain atribut dan merchandise JMMI (3 aset merchandise siap cetak), kolaborasi desain bersama Biro Digital Production; GoRent: penyewaan perlengkapan kerja (proyektor, layar, HT, kamera, tripod) dalam paket, KR 20 penyewa dan keuntungan minimal Rp 250.000, reinventaris dan perbaikan; JMMI Commerce: keuntungan ≥ Rp 150.000, papan transparansi harga. Peminjaman GoRent untuk biro internal JMMI gratis (cukup koordinasi jadwal, unit, dan berita acara jaminan perawatan) |

**Latar belakang / trigger (sim).** Kita lagi ngejar omzet **JMMI Store** dan **GoRent** menuju Hari Puncak. Dua hal yang kita butuhkan: **slot posting di Instagram JMMI** untuk katalog sewa alat dan pre-order merchandise, padahal slot Biro Media Analysis & Strategi terbatas, dan **mitra untuk merchandise amal**. Sambil itu, permintaan **pinjam alat GoRent** dan **paket sarapan** lagi masuk.

**Limitasi dan kapasitas.**
- **Merchandise amal (sim):** totebag modal Rp22.000, jual Rp35.000; stiker modal Rp4.000, jual Rp10.000. Rencana produksi **100 totebag dan 200 stiker**, desain sudah siap.
- **Konten promosi (sim):** katalog sewa GoRent (1 carousel 4 halaman) dan poster pre-order merchandise (1 feed), keduanya sudah final dengan caption.
- **Stok GoRent (sim):** HT 12, kabel roll 6, proyektor 2, standing banner 4. Mulai H-1 sampai Hari Puncak, **4 HT dan 1 proyektor sudah dibooking klien luar**, jadi yang tersisa **8 HT dan 1 proyektor**. Klien luar itu penting untuk target untung GoRent minimal Rp250.000.
- **JMMI Commerce (sim):** dapur 40 porsi per hari, modal Rp8.000, harga Rp11.000, diskon 5% (Rp10.450) kalau komit minimal 200 porsi. Porsi tambahan dari tenant mitra Rp12.000, bisa Rp11.000 kalau komit minimal 80 porsi. Target untung minimal Rp150.000.
- Pinjam GoRent untuk biro JMMI **gratis**, tapi wajib koordinasi jadwal, unit, dan berita acara jaminan perawatan.
- Jangan janjikan unit yang sudah dibooking, dan jangan lewati kapasitas dapur.

**Misi koordinasi wajib.**
- **R-07 ke Biro Media Analysis & Strategi:** wajib menyepakati **slot kalender konten dan jadwal tayang di Instagram JMMI** untuk katalog sewa GoRent dan pre-order merchandise JMMI Store: **minimal 2 slot** (boleh digabung dalam satu carousel), tanggal tayang pasti, dan tenggat file final tiap Kamis pukul 16.00. Yang bisa ditawarkan: konten sudah final (desain dan caption), mau digabung dalam satu carousel, dan mau mengalah kalau ada konten donasi atau kemanusiaan. **Jangan:** minta jalur kilat atau menyerobot antrean untuk promosi komersial. Jumlah slot dan kalender mereka belum kita tahu. Gali dari mereka.
- **R-08 ke Biro Pengabdian Masyarakat:** wajib menyepakati **kolaborasi merchandise amal** totebag dan stiker relawan JMMI Mengabdi: jumlah produksi, harga jual, **bagi hasil ke kas JMMI Peduli**, dan tata cara penyetoran. (Bonus: 100 totebag habis lewat pre-order.) Yang bisa ditawarkan: desain dan vendor siap, margin yang transparan (papan transparansi harga), dan nama JMMI Mengabdi di setiap produk. **Jangan:** menerima atau menitipkan uang bagi hasil lewat tangan relawan.

**Permintaan yang mungkin masuk (2 tiket masuk).**
- **R-02 dari Biro Manajemen Event** (pinjam alat GoRent (HT, kabel roll, proyektor, standing banner) H-2 sampai H+1): Layani sesuai stok: **8 HT, 1 proyektor, 6 kabel roll, 4 standing banner** pada H-1 sampai Hari Puncak. Empat HT dan proyektor kedua hanya tersedia di H-2 dan harus kembali sebelum H-1 pukul 08.00. **Gratis**, tapi wajib berita acara dengan foto dan uji fungsi, satu PIC, dan ganti rugi bila rusak atau hilang karena kelalaian (keausan wajar tidak dihitung). Booking klien luar tidak boleh dibatalkan.
- **R-05 dari Biro Kajian & Inovasi Dakwah** (paket sarapan SaJi 50–75 porsi per sesi dengan harga nego mahasiswa): Layani sesuai modal: dapur 40 porsi per hari, diskon sarapan **maksimal 5%** (komit minimal 200 porsi), dan harga di bawah modal bukan wewenang kita. Porsi lebih dari 40 harus dari tenant mitra.

**Batasan wewenang dan SOP.** Pembebasan jaminan perawatan atau ganti rugi di bawah 100%, pinjam untuk pihak di luar JMMI, diskon makanan lewat 5%, atau harga di bawah modal → **Kadep Relasi Publik & Advokasi**. Beli unit baru atau perbaikan besar → **Kadep Relasi Publik & Advokasi dan Bendum**. Uang bagi hasil dan penerimaan lain dipegang **Bendum**, kebijakan penyaluran dana → **BPI**. Tenant luar yang baru pertama kali bermitra → lewat **Biro Relasi & Hubungan Eksternal**.

### 5.5 Kasus 5 — Biro Amaliyah Yaumiyah

| | |
|---|---|
| Departemen / Bidang | Pelayanan Masjid & Dakwah · Bidang 1 (Kadep Pelayanan Masjid & Dakwah → Waket I) |
| Proker Amanah | **KSSI** (berbuka bersama Senin dan Kamis), **OWOJ**, **GDM**, **Q-TIME**, dan **RAPI** |
| Tiket yang dimulai | **R-09** ke Biro Manajemen Event · **R-10** ke Biro Media Analysis & Strategi |
| Sumber deck | KSSI: berbuka puasa Senin dan Kamis, konten dokumentasi bulanan, jadwal puasa sunnah via Google Calendar dan WA; OWOJ: khatmil Qur'an; GDM: penertiban jamaah saat azan Dzuhur dan Ashar; Q-TIME: murottal 17.00–17.30; RAPI: perawatan sarung, mukena, dan sajadah setiap Selasa. Dana takjil KSSI murni berasal dari Takmir melalui Bendahara Umum JMMI, tanpa jual-beli dengan Biro Usaha Mandiri |

**Latar belakang / trigger (sim).** Hari Puncak bakal ramai, dan kita khawatir **salat berjamaah** terganggu dan **karpet utama** kotor oleh makanan. Kita juga punya urusan lain: **dokumentasi KSSI bulan ini** belum tayang, dan jadwal puasa sunnah belum keluar.

**Limitasi dan kapasitas.**
- **Petugas GDM 12 orang** (sim), bergantian. GDM menertibkan jamaah saat azan Dzuhur dan Ashar.
- Dana takjil KSSI **berasal dari Takmir lewat Bendum**, bukan dari biro lain.
- Tim 5 orang (sim). Ruang yang boleh dipakai pihak lain (sim): **Senin, Rabu, Kamis pukul 15.30–16.55**. Selasa tidak tersedia.
- Acara kita pekan depan (sim): **khatmil Qur'an OWOJ**, Kamis H-9, ba'da Maghrib (±18.00–19.15).
- GDM menertibkan jamaah saat azan Dzuhur dan Ashar. Q-TIME murottal pukul 17.00–17.30 hari kerja.
- RAPI memakai serambi setiap Selasa untuk merawat sarung, mukena, dan sajadah.

**Misi koordinasi wajib.**
- **R-09 ke Biro Manajemen Event:** wajib menyepakati **protokol adab masjid** untuk Hari Puncak (alas kaki, suara, sampah), **jeda salat Dzuhur dan Ashar** di rundown, **zonasi makan di luar karpet utama**, dan **penugasan petugas GDM** (siapa, di mana, jam berapa). Yang bisa ditawarkan: petugas GDM terlatih, lembar adab satu halaman, dan bantuan pengumuman. Panitia mereka mandiri dan punya rundown sendiri. Gali bagian mana yang masih bisa disesuaikan.
- **R-10 ke Biro Media Analysis & Strategi:** wajib menyepakati **1 feed + 1 reels** dokumentasi bulanan KSSI (boleh dibundel) dengan tanggal tayang pasti, plus rilis kalender puasa sunnah di Instagram JMMI. Yang bisa ditawarkan: foto dan video mentah yang lengkap dan tepat waktu, draf caption, dan brief yang jelas.

**Permintaan yang mungkin masuk (2 tiket masuk).**
- **R-06 dari Biro Kajian & Inovasi Dakwah** (penugasan kader da'i dan silabus kultum 10 menit untuk buka bersama KSSI dan penutupan OWOJ): Kita bisa memberi slot **kultum 10 menit** di buka bersama KSSI (17.15–17.25, sebelum Maghrib 17.30) dan di penutupan OWOJ, maksimal **satu kader per sesi**. Silabus kita **baca dulu maksimal 2 hari** sebelum disetujui. Kultum tidak boleh menabrak azan dan buka puasa.
- **R-12 dari Biro Digital Production** (siaran langsung STREAMMI khatmil Qur'an OWOJ dan aftermovie): Boleh siaran langsung dengan syarat: **1 kamera** diam di belakang saf terakhir (kamera kedua dari sisi samping), tripod di depan saf dilarang, persiapan selesai sebelum **17.00**, uji coba 1 kali di H-1 setelah Ashar, izin pembaca dan pengisi, dan GDM mengamankan jalur. Izin resmi ruang tetap lewat surat peminjaman tempat dari Sekretaris Pelaksana.

**Batasan wewenang dan SOP.** Aturan dan area masjid ada di tangan **Takmir**. Kebutuhan di luar serambi dan jam di atas → **Kadep Pelayanan Masjid & Dakwah**. Dana takjil dan anggaran KSSI → **Bendum** (sumber dana Takmir). Kita tidak boleh mengurangi GDM atau Q-TIME demi kegiatan biro lain, dan tidak boleh menyerobot antrean media.

### 5.6 Kasus 6 — Biro Digital Production

| | |
|---|---|
| Departemen / Bidang | Media, Informasi & Digitalisasi · Bidang 3 (Kadep Media, Informasi & Digitalisasi → Waket III) |
| Proker Amanah | **STREAMMI** (live streaming dan videotron), **Requesta**, dan **POTRET JMMI** |
| Tiket yang dimulai | **R-11** ke Biro Manajemen Event · **R-12** ke Biro Amaliyah Yaumiyah |
| Sumber deck | STREAMMI: live streaming dan tayangan sinergi di videotron sesuai request; Requesta: merangkum semua permintaan luar departemen dan membaginya sesuai jobdesk dan kemampuan staf; POTRET JMMI: dokumentasi kegiatan |

**Latar belakang / trigger (sim).** Order masuk barengan, dan kita mau **STREAMMI** dan **POTRET JMMI** menyiarkan langsung **kajian akbar Maulid × Milad** di Hari Puncak serta khatmil Qur'an OWOJ tanpa mengganggu jamaah. Titik kamera, listrik, dan rundown belum ada, sementara kru akhir pekan tinggal satu orang.

**Limitasi dan kapasitas.**
- Kru (sim): 4 multimedia + 4 kreatif. **Akhir pekan cuma 1 orang** yang siaga, hanya untuk foto, tanpa video panjang.
- Requesta menerima **maksimal 4 order per minggu**, satu form untuk satu konten. Desain dan video pendek diajukan minimal **7 hari** sebelum dibutuhkan, video panjang **10 hari**. Revisi maksimal 2 kali.
- Hasil jadi per minggu: **6 aset** (sim).
- Pengecualian untuk order darurat kemanusiaan (sim): bisa dikejar ≤ 24 jam kalau brief lengkap dan **Kadep Media** setuju.
- Kita **berhak menolak atau menunda** order kalau brief tidak jelas, terlalu mepet, atau kapasitas penuh.
- Aturan dan jadwal masjid bukan wewenang kita, tanyakan ke Biro Amaliyah Yaumiyah atau Takmir.

**Misi koordinasi wajib.**
- **R-11 ke Biro Manajemen Event:** wajib menyepakati **fiksasi untuk live streaming kajian akbar Maulid × Milad**: titik kamera, jalur listrik atau kabel dan tempat videotron, **rundown dokumentasi** (momen penting, jam mulai, pembicara), dan jadwal survei lokasi. (Bonus: 2 kamera.) Yang bisa ditawarkan: kamera tidak menutupi pandangan peserta atau jalur masuk, kita bawa kabel dan penyangga sendiri, dan kru siap survei lokasi lebih dulu. Kru akhir pekan kita cuma 1 orang. Gali apakah panitia bisa membantu tenaga.
- **R-12 ke Biro Amaliyah Yaumiyah:** wajib menyepakati **izin siaran langsung STREAMMI khatmil Qur'an OWOJ**: minimal 1 kamera (posisi tripod, jam persiapan yang selesai sebelum Q-TIME, uji coba), PIC lokasi, izin pembaca, dan tidak mengganggu jamaah. (Bonus: 2 kamera dan **aftermovie 2 menit** dengan tenggat tayang.) Yang bisa ditawarkan: cara siaran yang menghormati kekhusyukan, misalnya kamera diam di belakang saf dan tidak ada yang berlalu-lalang, plus permintaan rundown dan daftar momen dari Biro Amaliyah Yaumiyah.

**Permintaan yang mungkin masuk (2 tiket masuk).**
- **R-03 dari Biro Pengabdian Masyarakat** (poster open donasi banjir JMMI Peduli jadi paling lama 24 jam): Poster **donasi kemanusiaan** boleh didahulukan walau melewati aturan 7 hari, **kalau brief lengkap** dan **Kadep Media setuju**. Konsekuensinya jatah order lain bergeser. Poster wajib memuat kanal resmi yang sudah disetujui Bendum.
- **R-15 dari Biro Relasi & Hubungan Eksternal** (1 fotografer dan desain e-invitation Jaulah LDK di akhir pekan): Akhir pekan kita hanya **1 orang, hanya foto**. Bisa kirim 1 fotografer untuk Jaulah hari Sabtu. **E-invitation** dikerjakan sebagai order biasa (pengajuan 7 hari, revisi maksimal 2 kali). Video recap menyusul hari Senin.

**Batasan wewenang dan SOP.** Dua biro beda departemen rebutan slot kita, atau pengecualian order darurat → **Kadep Media, Informasi & Digitalisasi** yang memutuskan. Aturan dan jadwal masjid → Biro Amaliyah Yaumiyah atau Takmir. Kontak luar hanya lewat Biro Relasi & Hubungan Eksternal. Konten sensitif atau kanal donasi hanya dibuat kalau sumber dan izinnya jelas (kanal donasi lewat Bendum).

### 5.7 Kasus 7 — Biro Media Analysis & Strategi

| | |
|---|---|
| Departemen / Bidang | Media, Informasi & Digitalisasi · Bidang 3 (Kadep Media, Informasi & Digitalisasi → Waket III) |
| Proker Amanah | **Publikasi Request**, **Analysis Media**, dan **IQRA X AKSI** (opini dan policy brief) |
| Tiket yang dimulai | **R-13** ke Biro Kajian & Inovasi Dakwah · **R-14** ke Biro Pengabdian Masyarakat |
| Sumber deck | Publikasi Req: kalender konten, hanya draf final dari Form Request yang diunggah; Analysis Media dan IQRA X AKSI: opini dan policy brief; Reels Insight; artikel rilis media massa. Forum diskusi NARASI tidak dipakai dalam simulasi ini |

**Latar belakang / trigger (sim).** Kita lagi menyiapkan **draf opini dan policy brief IQRA X AKSI** yang mau rilis pekan depan, plus **artikel rilis media massa kampus** tentang desa mitra. Dua hal bikin cemas: **dalil dan sudut pandang syar'i** belum ada yang mengecek, dan **data desa mitra** belum kita pegang. Di saat yang sama antrean posting lagi penuh.

**Limitasi dan kapasitas.**
- Tim 5 orang (sim), piket Senin–Kamis, **tanpa piket akhir pekan**. File final dari biro lain harus masuk **Kamis pukul 16.00**.
- **4 slot posting per minggu** untuk permintaan biro lain (sim). Satu carousel atau reels bisa memuat sampai 4 aset.
- Publikasi normal butuh 48 jam. Jalur kilat 24 jam hanya untuk kondisi kemanusiaan atau darurat dan harus disetujui Kadep Media.
- Hanya draf final dari form request yang kita unggah. Brief tidak lengkap, kita tolak.
- Draf opini: 2 per minggu (sim). Artikel media massa butuh 5 hari kerja sejak data lengkap (sim).
- Jangan hubungi pihak luar sendiri, semua lewat Biro Relasi & Hubungan Eksternal.
- Jangan menerbitkan tema yang berpotensi polemik tanpa persetujuan Kadep.

**Misi koordinasi wajib.**
- **R-13 ke Biro Kajian & Inovasi Dakwah:** wajib menyepakati **kurasi dalil, hadits, dan sudut pandang syar'i** untuk draf opini dan policy brief kita: alur kirim draf, waktu review (kita mengincar 2 hari kerja), siapa PIC, dan format catatan. (Bonus: nama Biro Kajian & Inovasi Dakwah dicantumkan sebagai pengkurasi.) Yang bisa ditawarkan: draf rapi dengan sumber yang jelas, jatah 2 draf per minggu, dan kredit untuk Biro Kajian & Inovasi Dakwah di setiap tulisan. **Jangan:** minta Biro Kajian & Inovasi Dakwah menulis ulang atau memutuskan boleh tayang atau tidak.
- **R-14 ke Biro Pengabdian Masyarakat:** wajib menyepakati **data riil desa mitra JMMI Mengabdi** (jumlah penerima manfaat, foto, kutipan warga yang sudah diizinkan, tanggal kegiatan) untuk artikel rilis media massa kampus: daftar data, tenggat kirim, PIC, dan Biro Pengabdian Masyarakat membaca draf sebelum terbit. Yang bisa ditawarkan: kita yang menulis dan menyunting artikel, hasilnya bisa dipakai Biro Pengabdian Masyarakat untuk laporan dan konversi KKN, dan tanpa membuka data pribadi warga. Tim Biro Pengabdian Masyarakat lagi sibuk banjir. Gali waktu yang realistis.

**Permintaan yang mungkin masuk (2 tiket masuk).**
- **R-10 dari Biro Amaliyah Yaumiyah** (publikasi dokumentasi KSSI bulanan dan rilis kalender puasa sunnah): Layani **1 slot bundling** (carousel atau reels) untuk dokumentasi bulanan KSSI, dan jadwal puasa sunnah lewat kanal WA atau Google Calendar (**tidak memakai slot**). Brief harus lengkap dan konten sudah final.
- **R-07 dari Biro Usaha Mandiri** (slot kalender konten untuk katalog sewa GoRent dan pre-order merchandise JMMI Store): Layani **maksimal 2 slot** (satu untuk katalog GoRent, satu untuk pre-order merchandise) kalau brief lengkap dan **file final masuk Kamis pukul 16.00**. Boleh digabung dalam satu carousel supaya hemat slot. Jatah total 4 slot, jadi dengan R-10 tinggal 1 slot sisa. Promosi komersial tidak boleh mengalahkan konten donasi atau kemanusiaan.

**Batasan wewenang dan SOP.** Rebutan prioritas lintas departemen, atau butuh publikasi kilat → **Kadep Media, Informasi & Digitalisasi**. Tema opini atau policy brief yang berpotensi memicu polemik → **Kadep Media, Informasi & Digitalisasi**. Beda pendapat dalil dengan Biro Kajian & Inovasi Dakwah yang buntu → **Kadep Pelayanan Masjid & Dakwah** juga dilibatkan. Kanal donasi atau konten yang belum disetujui pemiliknya atau Bendum jangan diunggah.

### 5.8 Kasus 8 — Biro Relasi & Hubungan Eksternal

| | |
|---|---|
| Departemen / Bidang | Relasi Publik & Advokasi · Bidang 3 (Kadep Relasi Publik & Advokasi → Waket III) |
| Proker Amanah | **Jaulah LDK** (JMMI sebagai tuan rumah), **Database Alumni**, dan pintu kerja sama eksternal |
| Tiket yang dimulai | **R-15** ke Biro Digital Production · **R-16** ke Biro Kajian & Inovasi Dakwah |
| Sumber deck | Jaulah LDK 1 dan 2: kolaborasi dengan 2–3 LDK, forum silaturahmi dan sharing kelembagaan, perwakilan tiap biro pada FGD; Rihlah Anjangsana: delegasi JMMI berkunjung ke LDK lain; Database Alumni 2020–2025; Silaturrahim Takmir dan Dosen Pembina; Gift Alumni W-133; Syukuran Alumni W-134; Media Eksternal; AMKI Muda. Jaulah berformat forum silaturahmi dan sharing kelembagaan, sehingga tidak membutuhkan pemateri atau ceramah |

**Latar belakang / trigger (sim).** Di **H-7 (hari Sabtu)** kita menerima **2 LDK mitra (sekitar 20 tamu)** di Ruang Audiovisual untuk **Jaulah**, yaitu forum silaturahmi dan sharing kelembagaan (bukan ceramah). Kita butuh **fotografer dan e-invitation**. Di sisi lain, **database alumni** kita belum nyambung dengan kebutuhan pemateri biro lain, dan banyak biro minta kontak luar lewat kita.

**Limitasi dan kapasitas.**
- Pintu eksternal ada **6** (sim). **2 terpakai** untuk 2 LDK Jaulah, jadi **sisa 4 slot** untuk kontak luar yang baru.
- Tim 3 orang (sim).
- Database alumni 2020–2025: sekitar 40 alumni berkontak lengkap (sim), plus jejaring ustadz luar. Untuk **pemateri**, biro pemilik acara menghubungi sendiri. Kita hanya memberi rekomendasi nama dan mencatat siapa yang sudah dihubungi, supaya satu alumni tidak diserbu banyak biro (maksimal 1 permintaan per alumni per bulan, sim).
- Mitra yang pernah bekerja sama **tidak memakai slot** dan hanya butuh verifikasi 1 hari.
- Setiap kontak luar baru wajib punya **surat resmi** (diajukan paling lambat 3 hari sebelum tenggat, diasistensi Pembina) dan persetujuan **Kadep Relasi Publik & Advokasi dan Waket III**.
- Jangan berkomitmen lisan atas nama JMMI ke pihak luar.

**Misi koordinasi wajib.**
- **R-15 ke Biro Digital Production:** wajib menyepakati dokumentasi Jaulah hari Sabtu, minimal **1 fotografer**, plus desain **e-invitation** untuk LDK dengan tenggat yang jelas. (Bonus: 1 videografer dan video recap 2 menit.) Yang bisa ditawarkan: form request dan brief lengkap, logo dan aset, akses lokasi, rencana publikasi. Video pendek diajukan minimal 7 hari sebelumnya. Kru akhir pekan mereka belum kita tahu. Gali dulu, siapkan alternatif.
- **R-16 ke Biro Kajian & Inovasi Dakwah:** wajib menyepakati **sinergi rekomendasi pemateri**: kriteria pemateri kajian Biro Kajian & Inovasi Dakwah, **5 nama rekomendasi** dari database alumni dan jejaring ustadz luar, dan alur etiket (Biro Kajian & Inovasi Dakwah menghubungi sendiri, kita mencatat supaya tidak tumpang tindih). Yang bisa ditawarkan: daftar nama lengkap dengan bidang dan kontak yang sudah terverifikasi, serta catatan siapa yang sudah dihubungi biro lain. **Jangan:** menghubungi pemateri atas nama Biro Kajian & Inovasi Dakwah atau menjanjikan jadwal mereka.

**Permintaan yang mungkin masuk (2 tiket masuk).**
- **R-01 dari Biro Manajemen Event** (Medpar dan undangan resmi LDK se-Surabaya untuk Maulid × Milad): Permintaan harus jelas: tujuan, nama pihak, tenggat, PIC, dan penandatangan surat. **Undangan LDK se-Surabaya** cukup **1 surat edaran lewat forum** (memakai 1 slot). **Setiap media baru** memakai 1 slot, sedangkan alumni atau media mitra lama **tanpa slot**. Total permintaan bisa melebihi 4 slot, jadi prioritas diputuskan bareng Kadep Relasi Publik & Advokasi.
- **R-04 dari Biro Pengabdian Masyarakat** (verifikasi 1 mitra penyalur resmi bantuan donasi bencana): Mitra penyalur yang sudah pernah bekerja sama (**mitra C**) tidak memakai slot dan hanya butuh verifikasi 1 hari. Mitra baru memakai slot dan butuh surat resmi.

**Batasan wewenang dan SOP.** Mau menambah slot di atas 4 → **Kadep Relasi Publik & Advokasi dan Waket III**. Kerja sama yang mengikat organisasi atau mengubah kebijakan → **BPI**. Kerja sama luar yang final bukan keputusan satu meja. Surat resmi lewat **Sekum atau Sekretaris Pelaksana**.

---

## 6. Matriks Koordinasi Delapan Biro (Ringkasan)

| Biro pengusung | Proker | Trigger masalah atau kebutuhan | Wajib koordinasi ke | Esensi yang harus disepakati |
|---|---|---|---|---|
| **Biro Manajemen Event** | **Maulid Nabi × Milad JMMI ke-37** (event Hari Puncak), plus peran konsultan teknis acara bagi biro lain | Kita lagi nyiapin Maulid Nabi × Milad JMMI ke-37, dan sekarang **H-21**. Panitia kita mandiri dan tupoksinya lengkap, tapi dua hal belum beres: belum ada **Medpar (media partner)** dan **undangan resmi ke LDK se-Surabaya**, dan **alat event** dari GoRent belum dipastikan. Kita tidak boleh menghubungi pihak luar sendiri. Di sisi lain, biro lain akan datang minta izin dan aturan main di venue Hari Puncak. | **Tujuan 1:** Biro Relasi & Hubungan Eksternal (R-01) | Medpar dan undangan resmi LDK se-Surabaya untuk Maulid × Milad lewat jalur Relasi: PIC tunggal, tenggat surat, prioritas bila kuota pintu eksternal terbatas |
| | | | **Tujuan 2:** Biro Usaha Mandiri (R-02) | Pinjam GoRent internal gratis (HT, kabel roll, proyektor, standing banner): ketersediaan unit terhadap booking klien luar, jadwal, PIC, dan jaminan perawatan lewat berita acara |
| **Biro Pengabdian Masyarakat** | **JMMI Peduli** (donasi musibah) dan **JMMI Mengabdi** (desa mitra) | Banjir bandang (sim) menerjang desa dekat mitra JMMI Mengabdi. BPI minta JMMI Peduli bergerak sekarang. Masalahnya, **poster open donasi harus jadi dalam 24 jam**, dan **mitra penyalur yang terverifikasi** harus jelas **sebelum donasi dibuka**. Di saat yang sama, data desa mitra kita masih belum rapi. | **Tujuan 1:** Biro Digital Production (R-03) | Poster darurat open donasi banjir JMMI Peduli ≤ 24 jam: jalur darurat terhadap aturan pengajuan 7 hari, isi wajib (kanal resmi, penanggung jawab, jadwal laporan) |
| | | | **Tujuan 2:** Biro Relasi & Hubungan Eksternal (R-04) | Pilihan 1 mitra penyalur resmi dari kandidat beserta syarat verifikasi, PIC, dan prosedur kerja sama lewat jalur khusus |
| **Biro Kajian & Inovasi Dakwah** | **SaJi** (Sarapan & Ngaji), **KID Insight**, dan **Simposium Nalar** | Kita lagi nyiapin **SaJi**, sarapan bareng sambil ngaji, dan sekarang **H-21**. Masalahnya: **paket sarapan** belum dipastikan, padahal RSVP baru 52 dari target rata-rata 75 (sim). Kita juga punya **kader da'i** dan **silabus kultum 10 menit** yang belum punya panggung tetap. | **Tujuan 1:** Biro Usaha Mandiri (R-05) | Paket sarapan SaJi 50–75 porsi per sesi lewat JMMI Commerce: harga rata-rata terhadap plafon, jadwal antar, standar menu, cara bayar |
| | | | **Tujuan 2:** Biro Amaliyah Yaumiyah (R-06) | Penugasan kader da'i dan silabus kultum 10 menit untuk buka bersama KSSI dan penutupan OWOJ: slot, jam kultum terhadap azan, persetujuan silabus |
| **Biro Usaha Mandiri** | **JMMI Store**, **JMMI Commerce**, dan **GoRent** | Kita lagi ngejar omzet **JMMI Store** dan **GoRent** menuju Hari Puncak. Dua hal yang kita butuhkan: **slot posting di Instagram JMMI** untuk katalog sewa alat dan pre-order merchandise, padahal slot Biro Media Analysis & Strategi terbatas, dan **mitra untuk merchandise amal**. Sambil itu, permintaan **pinjam alat GoRent** dan **paket sarapan** lagi masuk. | **Tujuan 1:** Biro Media Analysis & Strategi (R-07) | Slot kalender konten dan jadwal tayang di Instagram JMMI untuk katalog sewa GoRent dan pre-order merchandise JMMI Store: jumlah slot, bundling, tenggat file final, prioritas terhadap konten donasi |
| | | | **Tujuan 2:** Biro Pengabdian Masyarakat (R-08) | Merchandise amal totebag dan stiker relawan JMMI Mengabdi: jumlah produksi, harga, bagi hasil ke kas JMMI Peduli lewat Bendum, tenggat pre-order |
| **Biro Amaliyah Yaumiyah** | **KSSI** (berbuka bersama Senin dan Kamis), **OWOJ**, **GDM**, **Q-TIME**, dan **RAPI** | Hari Puncak bakal ramai, dan kita khawatir **salat berjamaah** terganggu dan **karpet utama** kotor oleh makanan. Kita juga punya urusan lain: **dokumentasi KSSI bulan ini** belum tayang, dan jadwal puasa sunnah belum keluar. | **Tujuan 1:** Biro Manajemen Event (R-09) | Protokol adab masjid, jeda salat di rundown, zonasi makan di luar karpet utama, dan penugasan petugas GDM pada Hari Puncak |
| | | | **Tujuan 2:** Biro Media Analysis & Strategi (R-10) | Slot dan kalender konten bulanan KSSI (feed, reels, rilis kalender puasa sunnah di Instagram JMMI): format, tenggat brief, jadwal tayang |
| **Biro Digital Production** | **STREAMMI** (live streaming dan videotron), **Requesta**, dan **POTRET JMMI** | Order masuk barengan, dan kita mau **STREAMMI** dan **POTRET JMMI** menyiarkan langsung **kajian akbar Maulid × Milad** di Hari Puncak serta khatmil Qur'an OWOJ tanpa mengganggu jamaah. Titik kamera, listrik, dan rundown belum ada, sementara kru akhir pekan tinggal satu orang. | **Tujuan 1:** Biro Manajemen Event (R-11) | Fiksasi live streaming kajian akbar Maulid × Milad: titik kamera, jalur listrik dan videotron, rundown dokumentasi, jadwal survei sebelum Aula terkunci, tenaga operator akhir pekan |
| | | | **Tujuan 2:** Biro Amaliyah Yaumiyah (R-12) | Teknis STREAMMI khatmil Qur'an OWOJ: posisi kamera dan tripod, jam persiapan sebelum Q-TIME, izin pembaca, PIC lokasi, aftermovie |
| **Biro Media Analysis & Strategi** | **Publikasi Request**, **Analysis Media**, dan **IQRA X AKSI** (opini dan policy brief) | Kita lagi menyiapkan **draf opini dan policy brief IQRA X AKSI** yang mau rilis pekan depan, plus **artikel rilis media massa kampus** tentang desa mitra. Dua hal bikin cemas: **dalil dan sudut pandang syar'i** belum ada yang mengecek, dan **data desa mitra** belum kita pegang. Di saat yang sama antrean posting lagi penuh. | **Tujuan 1:** Biro Kajian & Inovasi Dakwah (R-13) | Kurasi dalil, hadits, dan sudut pandang syar'i untuk draf opini dan policy brief: alur, waktu review, PIC, format catatan, batas wewenang |
| | | | **Tujuan 2:** Biro Pengabdian Masyarakat (R-14) | Data riil desa mitra JMMI Mengabdi untuk artikel rilis media massa kampus: daftar data, tenggat, izin desa, review draf oleh Pengmas |
| **Biro Relasi & Hubungan Eksternal** | **Jaulah LDK** (JMMI sebagai tuan rumah), **Database Alumni**, dan pintu kerja sama eksternal | Di **H-7 (hari Sabtu)** kita menerima **2 LDK mitra (sekitar 20 tamu)** di Ruang Audiovisual untuk **Jaulah**, yaitu forum silaturahmi dan sharing kelembagaan (bukan ceramah). Kita butuh **fotografer dan e-invitation**. Di sisi lain, **database alumni** kita belum nyambung dengan kebutuhan pemateri biro lain, dan banyak biro minta kontak luar lewat kita. | **Tujuan 1:** Biro Digital Production (R-15) | Dokumentasi (1 fotografer) dan e-invitation Jaulah LDK di akhir pekan: cakupan, tenaga akhir pekan, tenggat brief, batas revisi |
| | | | **Tujuan 2:** Biro Kajian & Inovasi Dakwah (R-16) | Sinergi rekomendasi narasumber alumni dan ustadz jejaring luar untuk pemateri kajian: kriteria, nama rekomendasi, etiket kontak langsung oleh biro pemilik acara |

---

## 7. Skenario Tiga Inject (Dimampatkan)

Inject dijalankan oleh **Pengendali Waktu / Master Inject** pada menit game yang ditentukan (versi 2.2: menit 8, 12, dan 16). Pengumuman dilakukan dengan suara jelas dan ditulis pada papan agar bisa dirujuk. Jarak antar-inject sengaja pendek agar tim tidak sempat nyaman.

| Inject | Menit | Nama | Efek singkat |
|---|---|---|---|
| A | **8** | Kapasitas Media Turun | Biro Digital Production turun dari 4 menjadi 3 order; Biro Media Analysis & Strategi turun dari 4 menjadi 3 slot |
| B | **12** | Instruksi Ganda | Fasilitator "Waket" memberi arahan lisan yang bertentangan kepada satu anggota |
| C | **16–21** | Pengambil Kendali Berhalangan | Anggota yang sedang memegang kendali ditarik 5 menit |

### 7.1 Inject A, Menit ke-8: "Kapasitas Media Turun"

| Unsur | Isi |
|---|---|
| **Trigger** | Master Inject mengumumkan: "Dua staf Digital Production dan satu staf Media Analysis & Strategi mendadak berhalangan." |
| **Efek mekanik** | **Biro Digital Production turun dari 4 menjadi 3 order** desain atau dokumentasi. **Biro Media Analysis & Strategi turun dari 4 menjadi 3 slot** posting untuk biro lain. Berlaku sampai akhir sesi |
| **Yang terdampak** | Pengirim ke Biro Digital Production: Biro Pengabdian Masyarakat (R-03, poster darurat donasi), Biro Relasi & Hubungan Eksternal (R-15, fotografer dan e-invitation). Pengirim ke Biro Media Analysis & Strategi: Biro Amaliyah Yaumiyah (R-10, 1 slot bundling), Biro Usaha Mandiri (R-07, katalog GoRent dan pre-order merchandise, sampai 2 slot) |
| **Yang diuji** | Prioritisasi, penolakan beradab, eskalasi ke Kadep Media, Informasi & Digitalisasi |
| **Perilaku ideal** | Meja yang terdampak berdiskusi cepat, memutuskan prioritas berdasarkan urgensi dan dampak (poster untuk sesi yang sudah terjadwal dan donasi kemanusiaan mendahului katalog atau promosi rutin), menjelaskan alasan kepada biro yang tertolak, dan melaporkan penolakan ke Kadep |
| **Perilaku bermasalah** | Menolak tanpa penjelasan, membagi rata tanpa dasar, melobi biro pengirim di luar jalur |
| **Peran fasilitator** | Kadep Media, Informasi & Digitalisasi menunggu eskalasi. Bila dua biro lintas departemen berebut slot dan buntu, Kadep memutuskan |

### 7.2 Inject B, Menit ke-12: "Instruksi Ganda"

| Unsur | Isi |
|---|---|
| **Trigger** | Fasilitator berperan sebagai **Waket** (Waket I untuk Biro Manajemen Event, Biro Pengabdian Masyarakat, Biro Kajian & Inovasi Dakwah, Biro Amaliyah Yaumiyah; Waket III untuk biro lainnya) mendatangi **satu anggota** di meja sasaran dan memberi arahan lisan yang bertentangan dengan keputusan tim atau aturan. Anggota dipilih fasilitator, sebaiknya yang sedang tidak memegang kendali tim |
| **Meja sasaran** | Dipilih fasilitator. Rekomendasi: Biro Usaha Mandiri atau Biro Pengabdian Masyarakat (lihat 7.2.1) |
| **Yang diuji** | Anggota tidak mengeksekusi sendiri; membawa arahan itu ke tim; tim mengonfirmasinya ke Kadep |
| **Perilaku ideal** | Anggota berkata sopan: "Siap, saya sampaikan ke tim dulu agar dikonfirmasi lewat Kadep." Tim mencatatnya di Tabel 3 dan melapor |
| **Perilaku bermasalah** | Langsung mengeksekusi, mengabaikan Waket, atau membahasnya di luar jalur |

#### 7.2.1 Pilihan Naskah Instruksi

| Meja sasaran | Naskah lisan "Waket" | Mengapa bermasalah |
|---|---|---|
| Biro Usaha Mandiri | "Gratiskan saja paket sarapan SaJi untuk KID, anggap dukungan sesama biro." | Harga di bawah modal dan diskon di atas 5% di luar kewenangan, harus lewat Kadep Relasi Publik & Advokasi (catatan: pinjam GoRent internal memang gratis, tetapi makanan tidak) |
| Biro Pengabdian Masyarakat | "Pakai saja rekening koordinator relawan supaya donasi cepat masuk." | Rekening resmi dikelola Bendum |
| Biro Manajemen Event | "Majukan Hari Puncak seminggu." | Perubahan tanggal Hari Puncak butuh Kadep → Waket → BPI |
| Biro Amaliyah Yaumiyah | "Hentikan Q-TIME pekan ini supaya aula dipakai kegiatan lain." | Mengubah komitmen rutin Biro Amaliyah Yaumiyah, perlu persetujuan Kadep Pelayanan Masjid & Dakwah |

### 7.3 Inject C, Menit ke-16: "Pengambil Kendali Berhalangan"

| Unsur | Isi |
|---|---|
| **Trigger** | Fasilitator menyerahkan kartu "kabar mendadak, harap keluar sebentar" kepada **anggota yang sedang paling banyak memegang kendali** di meja sasaran (ditentukan pengamat meja). Anggota itu meninggalkan meja selama **5 menit** (sampai menit ke-27) |
| **Meja sasaran** | Dipilih fasilitator, bukan meja yang sama dengan inject B. Rekomendasi: Biro Manajemen Event (menerima R-09 dan R-11 yang berbagi ruang) atau Biro Media Analysis & Strategi (menerima R-07 dan R-10 yang berebut slot), sehingga dampaknya terasa luas |
| **Yang diuji** | Perpindahan kepemimpinan, penunjukan pengganti sementara lewat Kadep, kontinuitas keputusan, dan siapa yang melangkah maju |
| **Perilaku ideal** | Tim berhenti sejenak, menyepakati siapa yang melanjutkan, menyampaikan kepada Kadep dan menuliskannya di Tabel 3, lalu menunda keputusan kritis atau mengambilnya dalam batas yang disepakati. Setelah anggota kembali, tim memaparkan keputusan yang dibuat |
| **Perilaku bermasalah** | Tim berhenti total, satu orang mengambil alih tanpa musyawarah, atau tiket yang sudah disepakati diubah tanpa sepengetahuan tim |
| **Nilai observasi** | Inject ini paling informatif untuk melihat kepemimpinan yang tumbuh: siapa yang melangkah maju saat pemimpin sementara hilang |

---

## 8. Struktur Google Sheets

**File:** `main/template_simulasi_taktis.xlsx` (11 tab, **Ultra-Lean Layout**). Berkas biner ini hanya disimpan lokal (diabaikan Git) dan dibangun oleh `python main/generate_template_simulasi.py`. Unggah ke Google Drive dan buka dengan Google Sheets, lalu pilih *File → Simpan sebagai Google Sheets*. Fase koordinasi aktif hanya 17 menit, sehingga peserta cukup mengisi sel kuning pada tiga tabel kecil dan sisanya bergerak langsung ke meja lain.

### 8.1 Daftar Tab

| Tab | Isi | Pengisi |
|---|---|---|
| `00_PETUNJUK` | Satu halaman: tujuan latihan, jadwal 30 menit, cara mengisi, tata krama antarmeja, aturan eskalasi, dan catatan pengamat | Dibaca peserta |
| Delapan tab biro, **berjudul sesuai nama biro** (`Manajemen Event`, `Pengabdian Masyarakat`, `Kajian & Inovasi Dakwah`, `Usaha Mandiri`, `Amaliyah Yaumiyah`, `Digital Production`, `Media Analysis & Strategi`, `Relasi & Hubungan Eksternal`) | Lembar kerja ringkas tiap biro, 19 baris | Meja biro |
| `PAPAN_JARING` | Matriks 8×8 status 16 tiket (Deal / Pending / Batal) yang membaca Tabel 1 tiap tab biro, kartu skor, dan rekap per meja | Otomatis |
| `SKOR_EVALUASI` | Satu tabel penilaian ringkas untuk pengamat Badan Personalia yang berkeliling | Penilai |

### 8.2 Tata Letak Tab Biro (19 Baris)

| Bagian | Baris | Isi |
|---|---|---|
| Header | 1–4 | Nama biro, departemen dan bidang (Kadep → Waket), sel kuning anggota meja, dan kalimat "Fokus negosiasi langsung antarmeja. Cukup isi sel kuning pada tabel di bawah." |
| **Tabel 1: Misi Koordinasi Keluar** | 7–9 | 2 tiket keluar. Kolom: ID Tiket, Biro Tujuan, Kebutuhan / Kasus Kita (terisi), **Hasil Kesepakatan / Deal** (kuning), **Status** (dropdown: Sepakat / Masih Negosiasi / Batal) |
| **Tabel 2: Koordinasi Masuk** | 12–14 | 2 tiket masuk. Kolom: ID Tiket, Biro Pengirim, Permintaan Mereka (terisi), **Respon & Syarat Balik Kita** (kuning), **Status** (dropdown: Diterima / Diterima Bersyarat / Ditolak) |
| **Tabel 3: Catatan Kebuntuan / Eskalasi ke Kadep** | 16–19 | Opsional, 2 baris cadangan. Kolom: No, Isu / Kebuntuan, Arahan & Solusi Kadep. Diisi hanya bila koordinasi macet total |

Kode warna: sel kuning = diisi peserta; sel abu-abu = terisi dan terkunci secara konvensi. Header berwarna menurut departemen (Syi'ar jingga, Pelayanan hijau, Medigi biru, Relasi Publik & Advokasi ungu). Tidak ada kolom jenis lintas, menit, atau borang Fakta–Opsi–Permintaan.

### 8.3 Formula Kunci

| Fungsi | Formula (contoh) |
|---|---|
| Status relasi (`PAPAN_JARING`) | `=IF('Manajemen Event'!E8="Sepakat","Deal",IF('Manajemen Event'!E8="Batal","Batal","Pending"))` untuk R-01. Tiap sel matriks menunjuk sel Status Tabel 1 pada tab biro pengusung; sel tanpa tiket berisi "—" |
| Kartu skor | `=COUNTIF(B5:I12,"Deal")`, dan serupa untuk "Pending" dan "Batal" |
| Rekap per meja | Keluar Deal `=COUNTIF('Manajemen Event'!E8:E9,"Sepakat")`; Masuk Diterima `=COUNTIF('Manajemen Event'!E13:E14,"Diterima*")`; Eskalasi `=COUNTA('Manajemen Event'!B18:B19)` |
| Total skor (`SKOR_EVALUASI`) | `=IF(COUNT(B5:E5)=0,"",ROUND(AVERAGE(B5:E5)*20,0))` |

**Validasi data:** dropdown Status Tabel 1 (Sepakat / Masih Negosiasi / Batal) dan Status Tabel 2 (Diterima / Diterima Bersyarat / Ditolak); skor evaluasi dibatasi bilangan bulat 1–5. Status Tabel 1 terisi awal "Masih Negosiasi" sehingga papan langsung menampilkan Pending.

### 8.4 Pengaturan Google Sheets Sebelum Hari-H

1. Unggah dan konversi file ke Google Sheets.
2. Atur **Protected range** manual: sel abu-abu pada tab biro terkunci, sel kuning terbuka untuk mejanya; `PAPAN_JARING` dan `SKOR_EVALUASI` hanya fasilitator (sebaiknya disembunyikan dari peserta). Proteksi lembar dari berkas xlsx tidak terbawa ke Google Sheets.
3. Buat salinan cadangan di Drive dan simpan tautan tab tiap biro dalam kode QR agar tiap meja langsung membuka tab yang benar. Meja gabungan menyimpan dua tautan.
4. Uji dengan 8 akun uji coba secara bersamaan.
5. Hapus data uji sebelum hari-H.

---

## 9. Rubrik Penilaian Kinerja Meja

Empat kriteria dengan bobot sama (**25% masing-masing**), dinilai satu pengamat Badan Personalia yang berkeliling pada `SKOR_EVALUASI`. Skala 1–5 per kriteria; total = rata-rata × 20 (0–100).

| Kriteria | Skor 5 | Skor 3 | Skor 2 | Skor 1 | Sumber data |
|---|---|---|---|---|---|
| **1. Keaktifan Negosiasi** | Meja langsung bergerak, mendatangi kedua tujuan, dan melayani kedua tamu | Bergerak, tetapi satu tiket tertinggal | Menunggu, baru bergerak setelah didorong | Tidak bergerak | Pengamatan pengamat meja |
| **2. Kualitas Deal Konkret** | Konkret (volume, waktu, PIC, syarat), seimbang, bisa dieksekusi di **kedua** tujuan | Ada, tetapi satu unsur samar | Umum atau sepihak | Tidak ada kesepakatan | Tabel 1 dan 2 tab biro dan `PAPAN_JARING` |
| **3. Ketepatan Eskalasi** | Tepat topik dan waktu, fakta–opsi–permintaan jelas | Tepat tetapi format kurang | Terlambat atau tidak perlu | Tidak mengeskalasi padahal wajib, atau memutuskan di luar wewenang | Tabel 3 tab biro dan respon Kadep |
| **4. Adab Kerjasama** | Santun, keputusan lahir dari musyawarah (semua didengar), batas wewenang dipatuhi, tolak dengan alasan dan alternatif | Satu pelanggaran ringan | Beberapa pelanggaran | Pelanggaran berat | Pengamatan pengamat meja |

**Predikat:** ≥ 85 Tangguh · 70–84 Cakap · 55–69 Berkembang · < 55 Perlu pendalaman.

**Catatan penting:** skor menilai **kinerja meja**, bukan individu, dan bukan alat peringkat sosial. Skor dipakai untuk presentasi dan ulasan serta bukti TUK (K6, K7, K8). Pola kontribusi individu dicatat terpisah (bagian 10).

---

## 10. Lembar Observasi Kepemimpinan Emergen (Badan Personalia)

### 10.1 Tujuan dan Batasan

- **Tujuan:** memperoleh gambaran objektif tentang pola kontribusi dan kepemimpinan yang tumbuh secara alami, sebagai **masukan pembinaan dan pemetaan pipeline**, melengkapi Form Minat Peran dan Ngopi Khidmah.
- **Bukan:** nilai lulus atau gagal, peringkat peserta, atau satu-satunya dasar seleksi peran. Keputusan seleksi tetap mengikuti mekanisme BPI.
- **Wadah:** formulir terpisah dengan **akses terbatas** (Badan Personalia, Waket II, Ketua Umum). Tidak ditaruh di berkas Google Sheets simulasi, karena berkas itu dibuka seluruh meja.

### 10.2 Prosedur

1. **Kalibrasi pengamat** pada technical meeting (11 November): membahas enam dimensi dan skala dengan contoh perilaku, serta bias yang perlu dihindari.
2. Setiap pengamat duduk di dekat satu meja dan **tidak ikut berbicara**. Pengamat mengenali peserta lewat kode pada name tag (bukan nama lengkap) dan menuliskan bukti perilaku singkat.
3. Pengamat mengisi lembar **segera setelah P4** (maksimal 10 menit), saat presentasi dimulai, selagi ingatan segar.
4. Satu pengamat per meja. Untuk meja gabungan, pengamat ditambah satu bila memungkinkan.

### 10.3 Dimensi Perilaku yang Diamati

| No | Dimensi | Contoh perilaku yang tampak |
|---|---|---|
| 1 | Inisiatif memulai | Membuka tiket lebih dulu, mengusulkan pembagian kerja, menggerakkan tim saat diam |
| 2 | Mengarahkan dan memutuskan | Merangkum pilihan, memutuskan saat buntu, menetapkan prioritas, menyatakan "kita ambil opsi ini" |
| 3 | Komunikasi dan negosiasi | Bahasa santun dan jelas, argumen konkret, mencari titik temu dengan meja lain |
| 4 | Mendengarkan dan melibatkan | Memberi ruang bicara, menengahi, menanyakan pendapat anggota pendiam, merangkum ulang |
| 5 | Ketepatan jalur dan ketenangan | Mengikuti aturan arah, mengeskalasi tepat, tetap tenang saat inject |
| 6 | Kontribusi pendukung | Mencatat rapi, menghitung kapasitas dan angka, memastikan tindak lanjut, menjaga waktu |

### 10.4 Skala dan Format

Setiap dimensi diberi skala **1–4**: 1 = belum tampak, 2 = muncul sesekali, 3 = konsisten, 4 = menonjol dan memengaruhi tim. Setiap skor wajib disertai **satu bukti perilaku** (kalimat atau tindakan nyata). Skor tanpa bukti tidak dipakai.

| Kolom formulir | Isi |
|---|---|
| Nama pengamat | Anggota Badan Personalia |
| Meja (biro) | Nama biro lengkap |
| Kode peserta | Dari name tag |
| Dimensi 1–6 | Skor 1–4 dan bukti singkat |
| Momen kunci | Perilaku saat Inject B dan Inject C |
| Catatan pendampingan | Hal yang bisa dibantu (opsional) |

### 10.5 Pemanfaatan dan Larangan

| Boleh | Dilarang |
|---|---|
| Menjadi bahan pembinaan dan percakapan pendampingan oleh Badan Personalia | Menyebut peringkat atau "juara kepemimpinan" |
| Melengkapi pemetaan pipeline di database kader | Menentukan seleksi peran hanya dari catatan ini |
| Menunjukkan peserta tenang dan suportif yang layak ditawari peran Staf Ahli atau peran pendukung | Membandingkan peserta di depan umum |
| Memberi umpan balik ke peserta yang meminta | Membagikan catatan ke pihak di luar akses terbatas |

Tata kelola data (akses, retensi, pelaporan agregat) mengikuti dokumen 04, bagian 5.2.

---

## 11. Panduan Fasilitator dan Game Master

### 11.1 Persiapan (H-13 sampai H-1)

| Waktu | Tugas | PIC |
|---|---|---|
| 2–6 November (H-13 s.d. H-9) | **Validasi kasus dan angka** dengan Kabiro yang bersangkutan (status proker OKR sekarang, kapasitas, tenggat). Kartu direvisi bila perlu | Sie Simulasi, Ketupel |
| 8 November (H-7) | Uji `template_simulasi_taktis.xlsx` dengan 8 akun. Daftar meja awal dari data RSVP | Sie Simulasi |
| 10 November (H-5) | Cetak 8 set Kartu Rahasia **dengan 2 salinan per meja** (+2 cadangan) setelah validasi selesai; masukkan ke amplop tersegel bertanda nama biro | Sie Perlengkapan |
| 11 November (H-4) | **Technical meeting:** latihan peran Kadep, Waket, Bendum; latihan inject; **kalibrasi pengamat** (bagian 10.2) | Sie Simulasi |
| 13 November (H-2) | **Keputusan penggabungan final** (biro dengan hadir < 3 orang) berdasarkan konfirmasi kehadiran | Sie Simulasi, Sie Registrasi |
| 14 November (H-1) | Siapkan tata letak meja, proyektor Papan Jaring, penghitung waktu, hotspot cadangan | Sie Perlengkapan |

### 11.2 Skrip Peran Kadep

1. **Terima eskalasi** dalam format *fakta → opsi → permintaan arahan*. Bila belum lengkap, kembalikan dengan pertanyaan pemandu ("Apa opsi lain?", "Apa dampaknya bagi biro lain?").
2. **Jangan menyelesaikan masalah.** Berikan arahan atau persetujuan, bukan solusi lengkap. Kadep tidak mengambil alih kewenangan operasional biro.
3. **Respons maksimal 3 menit.** Catat respons di kolom *Respon Kadep/Fasilitator*, bukan hanya lisan.
4. **Lintas departemen:** hubungi Kadep departemen lain atau eskalasikan ke Waket (peran fasilitator lain).
5. **Persetujuan P3:** periksa kesesuaian poin deal di Tabel 1 dan 2 dengan yang dilaporkan meja; minta revisi bila tidak sejalan dengan batas wewenang.
6. **Hak tolak:** Kadep boleh menolak komitmen di luar RAB atau kapasitas, dengan alasan tertulis.
7. **Jangan menunjuk pemimpin.** Bila anggota bertanya "siapa yang harus bicara dengan Kadep?", jawab: "Siapa pun yang mewakili tim." Biarkan tim memutuskan.

**Contoh respons:**
- "Opsi 1 dan 2 masuk akal. Saya setuju opsi 2, tetapi tolong informasikan ke Kadep Relasi Publik & Advokasi karena melibatkan departemen lain."
- "Belum cukup. Fakta kalian belum menyebut tenggat vendor. Lengkapi dan kembali."
- "Ini wilayah BPI. Saya eskalasikan ke Waket. Sementara, tahan komitmen tertulis."

### 11.3 Skrip Peran Waket / BPI / Bendum

- **Waket:** menerima eskalasi lintas departemen dalam satu bidang. Untuk Inject B, mendatangi anggota dengan naskah (lihat 7.2.1).
- **BPI:** menerima eskalasi kebijakan atau lintas bidang. Cenderung menanyakan dasar Tata Kelola dan dampak organisasi.
- **Bendum:** menjawab pertanyaan kanal donasi, bagi hasil merchandise amal, dana takjil KSSI, dan penerimaan uang. Jawaban baku: rekening resmi dikelola Bendum; kanal donasi harus disetujui sebelum disebar; dana takjil KSSI berasal dari Takmir lewat Bendum; bagi hasil merchandise amal dan pemasukan GoRent dari klien eksternal dicatat melalui mekanisme administrasi keuangan, bukan dipegang biro atau relawan secara pribadi.

### 11.4 Skrip Pengendali Waktu dan Master Inject (30 Menit)

| Menit | Aksi |
|---|---|
| 0 | Umumkan "P1 dimulai: baca kartu dan bergerak" |
| 4 | "P2 dimulai: buka tiket" |
| **8** | **Inject A** (Kapasitas Media Turun) |
| **12** | **Inject B** (Waket mendatangi satu anggota) |
| **16** | **Inject C** (kartu "kabar mendadak" kepada anggota yang memegang kendali) |
| 18 | Peringatan "3 menit lagi" |
| 19 | Anggota Inject C kembali |
| 20 | Peringatan "1 menit lagi, siapkan laporan ke Kadep" |
| 21 | "P3 dimulai: rapikan deal, lapor Kadep" |
| 23 | Peringatan "2 menit lagi" |
| 25 | "P4 dimulai: Papan Jaring" |
| 30 | Selesai. Foto Papan Jaring |

### 11.5 Titik Temu Kesepakatan (ZOPA) per Tiket

Bukan jawaban tunggal. Dipakai untuk menilai kualitas kesepakatan (rubrik 2).

| Tiket | Titik temu realistis | Jebakan dan catatan |
|---|---|---|
| R-01 Biro Manajemen Event → Biro Relasi & Hubungan Eksternal | **2 Medpar** lewat alumni atau media mitra lama (tanpa slot) dan **1 surat edaran undangan LDK se-Surabaya** lewat forum (1 slot); PIC tunggal; tenggat surat disepakati sesuai aturan pengajuan H-3 dan asistensi Pembina | Slot eksternal sisa 4 melawan permintaan masuk (Biro Manajemen Event sampai 6 pihak, Biro Pengabdian Masyarakat 1 mitra). Tanpa prioritisasi Kadep Relasi Publik & Advokasi, tiket macet. Target 5 Medpar tidak realistis |
| R-02 Biro Manajemen Event → Biro Usaha Mandiri | **8 HT, 1 proyektor, 6 kabel roll, 3–4 standing banner** untuk H-2 sampai H+1, **Rp0** (internal). HT tambahan dan proyektor kedua hanya H-2 dan kembali sebelum H-1 pukul 08.00. Jaminan perawatan: berita acara dengan foto dan uji fungsi, satu PIC, ganti rugi bila rusak karena kelalaian (biaya perbaikan) atau hilang (unit setara), keausan wajar dikecualikan, telat kembali menurunkan prioritas pinjam berikutnya (tanpa denda uang) | Klien luar sudah booking 4 HT dan 1 proyektor mulai H-1 dan tidak boleh dibatalkan (target untung GoRent Rp250.000). Pinjam untuk pihak di luar JMMI atau pembebasan jaminan perawatan butuh Kadep Relasi Publik & Advokasi |
| R-03 Biro Pengabdian Masyarakat → Biro Digital Production | Poster open donasi **≤ 24 jam** lewat pengecualian darurat (persetujuan Kadep Media, Informasi & Digitalisasi), memuat kanal resmi, penanggung jawab, dan jadwal laporan; template poster transparansi menyusul ≤ 7 hari | Aturan normal 7 hari. Kanal belum disetujui Bendum, sehingga wajib ditolak. Bila Inject A (kapasitas 3 order), donasi kemanusiaan mendahului promosi rutin dan order Biro Relasi & Hubungan Eksternal bergeser |
| R-04 Biro Pengabdian Masyarakat → Biro Relasi & Hubungan Eksternal | **Mitra C** (sudah ada, tanpa slot, verifikasi 1 hari) sebagai penyalur pertama; B opsional; A ditunda | Mitra A (4 hari) terlalu lambat. Mitra baru berebut slot Relasi dengan R-01. Kadep dan Waket III diinfokan |
| R-05 Biro Kajian & Inovasi Dakwah → Biro Usaha Mandiri | 4 sesi, dapur 40 porsi per hari @ **Rp10.450** (diskon 5%, komit ≥ 200 porsi). **Skema 50 porsi**: tambah 10 porsi tenant @ Rp12.000 (komit tenant 40 < 80) = Rp538.000 per sesi, total Rp2.152.000, rata-rata **Rp10.760**. **Skema 75 porsi**: tambah 35 porsi tenant @ Rp11.000 (komit tenant 140 ≥ 80) = Rp803.000 per sesi, total Rp3.212.000, rata-rata **Rp10.707**. Keduanya ≤ plafon Rp11.000. Antar sebelum 06.30, menu halal, bayar per sesi | Dapur maksimal 40 porsi per hari. Diskon di atas 5% atau harga di bawah modal Rp8.000 butuh Kadep Relasi Publik & Advokasi. Tenant baru lewat Relasi. RSVP baru 52 dari target 75, jadi jumlah pasti harus disepakati 3 hari sebelumnya |
| R-06 Biro Kajian & Inovasi Dakwah → Biro Amaliyah Yaumiyah | **8 sesi KSSI** (Senin dan Kamis) dan **1 penutupan OWOJ**, satu kader per sesi dari 6 kader (maksimal 2 sesi per kader); kultum **17.15–17.25** sebelum Maghrib 17.30; silabus dibaca Biro Amaliyah Yaumiyah maksimal 2 hari; 1 kali latihan | Kultum tidak boleh menabrak azan dan buka puasa. Penutupan OWOJ juga disiarkan STREAMMI (R-12), jadi kader tampil di siaran dan silabusnya harus disetujui sebelum itu |
| R-07 Biro Usaha Mandiri → Biro Media Analysis & Strategi | **2 slot** untuk Biro Usaha Mandiri (katalog sewa GoRent dan pre-order merchandise), idealnya **digabung dalam 1 carousel** (4 aset) sehingga hanya memakai 1 slot; file final **Kamis 16.00**; tanggal tayang pasti; caption dan desain sudah final | Jatah 4 slot: R-10 memakai 1, R-07 memakai 1–2, sisa 1–2. Bila Inject A (3 slot), tiket ini bersaing dengan R-10. Konten donasi atau kemanusiaan (R-03) boleh didahulukan, jalur kilat tidak untuk promosi komersial |
| R-08 Biro Usaha Mandiri → Biro Pengabdian Masyarakat | **100 totebag dan 200 stiker**; harga jual Rp35.000 dan Rp10.000. Margin total: 100 × Rp13.000 + 200 × Rp6.000 = Rp2.500.000. **Bagi hasil 20–30%** (Rp500.000–Rp750.000) ke kas JMMI Peduli **lewat Bendum**; pre-order dibuka dengan tenggat jelas; papan transparansi harga | Uang tidak boleh melewati tangan relawan. Persentase dan skema penyaluran di luar wewenang meja butuh BPI. Biro Pengabdian Masyarakat lagi sibuk banjir (R-03, R-04) |
| R-09 Biro Amaliyah Yaumiyah → Biro Manajemen Event | Jeda salat **Dzuhur 11.30–12.15** dan **Ashar 15.00–15.45** masuk rundown; makan **3 gelombang × ±250 orang** di serambi bawah dan pelataran sisi barat; karpet utama bebas makanan; petugas GDM bertugas di pintu Aula, jalur wudu, dan zona makan; lembar adab dibagikan | Konsumsi 750 orang butuh waktu, sementara Biro Manajemen Event tidak bisa menukar isi kajian utama. Serambi dan area Aula juga dipakai titik kamera dan jalur kabel STREAMMI (R-11). Mengubah karpet atau area masjid butuh Takmir lewat Kadep Pelayanan Masjid & Dakwah |
| R-10 Biro Amaliyah Yaumiyah → Biro Media Analysis & Strategi | **1 slot bundling** (carousel atau reels) bulanan; jadwal puasa lewat kanal WA atau Calendar (tidak memakai slot); tanggal tayang pasti | Slot sangat terbatas, bundling adalah kunci. Bila Inject A (3 slot), tiket ini bersaing dengan R-07 |
| R-11 Biro Digital Production → Biro Manajemen Event | **1 titik kamera** di belakang area peserta Aula (bukan jalur masuk), **1 jalur listrik** dari panel Aula, videotron di sisi panggung, **rundown dokumentasi 1 halaman**; survei lokasi **sebelum H-3 pukul 12.00**; operator kamera dari Biro Digital Production (1 kru akhir pekan), kamera ke-2 sebagai bonus hanya bila ada tenaga | Aula terkunci mulai H-3 pukul 12.00, jadi survei wajib lebih awal. Biro Manajemen Event tidak punya tenaga cadangan di Hari Puncak. Kru akhir pekan Biro Digital Production hanya 1 orang dan Jaulah (R-15) juga hari Sabtu, jadi kru bersaing. Titik kamera tidak boleh menabrak zonasi makan dan jalur GDM (R-09) |
| R-12 Biro Digital Production → Biro Amaliyah Yaumiyah | STREAMMI khatmil OWOJ (Kamis H-9): **1 kamera** di belakang saf terakhir (kamera ke-2 sisi samping sebagai bonus); persiapan selesai **< 17.00**, uji coba H-1 setelah Ashar; izin pembaca dan pengisi; GDM amankan jalur; aftermovie 2 menit dari rundown dan daftar momen Biro Amaliyah Yaumiyah | Tripod di depan saf dilarang. Persiapan tidak boleh menabrak Q-TIME 17.00–17.30. Aftermovie butuh pengajuan 10 hari. Kultum kader Biro Kajian & Inovasi Dakwah (R-06) ikut tersiarkan |
| R-13 Biro Media Analysis & Strategi → Biro Kajian & Inovasi Dakwah | Alur: draf masuk Biro Kajian & Inovasi Dakwah, catatan kembali dalam **2 hari kerja**, **maksimal 2 draf per minggu**; tiga penanda (aman, perlu diperiksa, ganti); keputusan tayang tetap di Biro Media Analysis & Strategi; PIC kedua pihak; kredit Biro Kajian & Inovasi Dakwah di tulisan | KID Insight sedang padat (12 konten). Kurasi bukan fatwa: topik sensitif atau khilafiyah ke Kadep Pelayanan Masjid & Dakwah dan Kadep Media, Informasi & Digitalisasi |
| R-14 Biro Media Analysis & Strategi → Biro Pengabdian Masyarakat | Data: jumlah penerima manfaat, 3 foto, 2 kutipan warga (izin desa), tanggal kegiatan, **dalam 3 hari kerja**; Biro Pengabdian Masyarakat membaca draf maksimal 2 hari; Biro Media Analysis & Strategi menulis 5 hari kerja; tanpa data pribadi warga | Data desa baru 60% rapi dan tim Biro Pengabdian Masyarakat sibuk banjir. Izin desa belum keluar. Rilis media kampus mengikuti tenggat redaksi, jadi jadwal harus mundur dari tanggal rilis |
| R-15 Biro Relasi & Hubungan Eksternal → Biro Digital Production | **1 fotografer** hari Sabtu; **e-invitation** sebagai order biasa (diajukan H-21, jadi tenggat ≥ 7 hari terpenuhi, revisi maksimal 2 kali); video recap dikerjakan Senin dari bahan sendiri | Akhir pekan hanya 1 orang, tanpa video panjang. Jaulah berformat silaturahmi dan sharing kelembagaan, tanpa pemateri. Bila Inject A, order Biro Relasi & Hubungan Eksternal bersaing dengan donasi kemanusiaan (R-03) |
| R-16 Biro Relasi & Hubungan Eksternal → Biro Kajian & Inovasi Dakwah | **5 nama rekomendasi** (alumni dan ustadz jejaring) sesuai kriteria pemateri Biro Kajian & Inovasi Dakwah; **Biro Kajian & Inovasi Dakwah menghubungi sendiri** setelah Biro Relasi & Hubungan Eksternal memberi lampu hijau etiket; Biro Relasi & Hubungan Eksternal mencatat kontak; maksimal 1 permintaan per alumni per bulan; honor lewat persetujuan Kadep Pelayanan Masjid & Dakwah | Biro Relasi & Hubungan Eksternal tidak boleh menghubungi pemateri atas nama Biro Kajian & Inovasi Dakwah. Alumni yang sudah dihubungi biro lain (misalnya untuk Maulid × Milad) perlu dicatat supaya tidak diserbu |

**Pemeriksaan matematis R-05:** dapur 40 porsi × Rp10.450 = Rp418.000 per sesi. Skema 50 porsi: tenant 10 × Rp12.000 = Rp120.000, total Rp538.000 per sesi, × 4 sesi = Rp2.152.000 untuk 200 porsi, rata-rata Rp10.760. Skema 75 porsi: tenant 35 × Rp11.000 = Rp385.000, total Rp803.000 per sesi, × 4 sesi = Rp3.212.000 untuk 300 porsi, rata-rata Rp10.707. Keduanya di bawah plafon Rp11.000 per porsi (Rp3.300.000 untuk 300 porsi).

**Pemeriksaan matematis R-08:** margin totebag Rp35.000 − Rp22.000 = Rp13.000 × 100 = Rp1.300.000; margin stiker Rp10.000 − Rp4.000 = Rp6.000 × 200 = Rp1.200.000; total Rp2.500.000. Bagi hasil 20–30% = Rp500.000 sampai Rp750.000 ke kas JMMI Peduli lewat Bendum.

### 11.6 Pemecahan Masalah Saat Berjalan

| Masalah | Penanganan |
|---|---|
| Tim tidak bergerak di P2 | Pengamat **tidak** mengarahkan; fasilitator lain boleh bertanya "Siapa tujuan pertama kalian?" tanpa memberi jawaban |
| Satu orang mendominasi, yang lain diam | Biarkan dinamika berjalan sampai presentasi dan ulasan; catat sebagai bahan pembelajaran. Jika tim jelas macet, Kadep dapat bertanya "Apa pendapat anggota lain?" |
| Dua tim saling memaksa | Kadep memanggil keduanya dan mengingatkan wewenang Kadep dan jalur eskalasi |
| Tim menghubungi biro di luar daftar | Tegur lembut, arahkan eskalasi ke Kadep. Pengamat mencatatnya untuk bahan ulasan |
| Wi-Fi bermasalah | Aktifkan hotspot cadangan. Bila gagal, tulis tiket pada kertas dan operator memasukkan sesudahnya |
| Google Sheets lambat | Minta tim mengisi hanya kolom Hasil Kesepakatan dan Status selama P2; Tabel 3 hanya bila macet |
| Kartu terlalu panjang dibaca dalam 5 menit | Sediakan 2 salinan per meja dan anjurkan membagi baca; tidak ada perpanjangan P1 |
| Inject membuat tim panik | Master Inject mengingatkan bahwa kekacauan adalah bagian dari pembelajaran |

### 11.7 Alur Presentasi dan Ulasan (30 Menit, 13.41–14.11)

Presentasi ini menggantikan debrief 25 menit pada versi 2.0. Kegiatan dilakukan di aula setelah Simulasi Taktis, dengan panitia, BPH, dan Kabiro yang hadir sebagai pembawa.

| Menit | Kegiatan | Pembawa |
|---|---|---|
| 0–5 | Tampilkan `PAPAN_JARING` dan rekap (Deal, Pending, Batal) | Operator |
| 5–12 | Presentasi singkat tiap biro (±1 menit per biro): satu kesepakatan terbaik dan satu tiket tersulit | Perwakilan meja |
| 12–20 | Ulasan: tiga pertanyaan ulasan (di bawah); 3–4 meja bicara | Fasilitator utama bersama BPH dan Kabiro yang hadir |
| 20–25 | **Pelajaran kepemimpinan organik:** bagaimana keputusan lahir di meja, bagaimana yang pendiam dilibatkan, apa yang terjadi saat pengambil kendali ditarik (Inject C). Tidak menyebut nama peserta | Fasilitator utama |
| 25–30 | Penutup: tiga pelajaran utama dan jembatan ke jeda Ashar dan Materi 4. Keterkaitan dengan prinsip koordinasi dan etika eskalasi (Materi 3) disebut singkat | Fasilitator utama |

**Tiga pertanyaan ulasan:**
1. Tiket mana yang paling alot dan mengapa? Apa yang akhirnya membuka kebuntuan?
2. Kapan kalian memilih eskalasi dan kapan menyelesaikan sendiri? Apa dasarnya, baik prinsip koordinasi maupun konvensi struktur saat ini?
3. Siapa yang menanggung dampak keputusan kalian di biro lain, dan apakah kalian mengetahuinya?

**Pertanyaan tambahan untuk bagian kepemimpinan organik:**
- Bagaimana tim memutuskan siapa yang bicara dengan Kadep?
- Apa yang dilakukan tim saat satu anggota harus keluar mendadak?
- Peran apa yang paling membantu tim hari ini selain yang paling vokal?

**Kalimat jembatan ke Materi 4:** "Tadi kalian merasakan betapa beratnya memikul amanah di tengah keterbatasan, dan betapa pentingnya orang-orang yang mau melangkah maju. Setelah Ashar kita bicara tentang mengapa orang tetap mau memikulnya."

### 11.8 Temuan untuk Badan Keorganisasian

Penilai mencatat **titik ambigu Tata Kelola** yang muncul saat simulasi (misalnya kapan "diketahui" cukup, atau aturan peminjaman internal GoRent dan jaminan perawatannya). Catatan ini diserahkan ke Badan Keorganisasian sebagai masukan revisi Tata Kelola, digabung dengan masukan anonim peserta yang dijaring pada Materi 3. Dengan begitu simulasi menghasilkan dua manfaat: pelatihan peserta dan evaluasi dokumen.

---

## 12. Kontrol Kualitas

| Pemeriksaan | Metode | Hasil terakhir |
|---|---|---|
| Graf: 16 tiket, 2 keluar dan 2 masuk per biro, tanpa loop diri, **tanpa pasangan timbal-balik** | Skrip generator (assert pada daftar `TIKET` di `generate_template_simulasi.py`) | Lulus |
| Daftar `TIKET` skrip sama dengan tabel 3.2 (ID, pengusung, tujuan) | Skrip pembanding | 16 dari 16 sama |
| Tujuan dan pengirim pada kartu sama dengan tabel 3.2 | Skrip penyusun dokumen (assert) | 8 dari 8 sama |
| Formula `PAPAN_JARING`, rekap per meja, dan total skor dengan nama biro lengkap | Dihitung dengan pustaka `formulas` pada data uji (R-01 dan R-03 Sepakat, R-02 Batal, satu tiket masuk Diterima Bersyarat, satu eskalasi, skor 4 dan 5) | Sesuai: 2 Deal, 13 Pending, 1 Batal; rekap meja dan skor 90 benar |
| Tampilan di Excel dan Google Sheets | **Belum diuji** | Perlu pemeriksaan visual setelah unggah |

**Regenerasi file:** `python main/generate_template_simulasi.py`. Sumber kebenaran graf adalah daftar `TIKET` di skrip, yang **sinkron penuh** dengan tabel 3.2 dan lolos uji di atas. Bila relasi diubah, perbarui `kartu_skenario_simulasi.md` dan dokumen ini. Skrip dilacak Git; berkas xlsx hasilnya tidak.

---

## 13. Asumsi dan Keterbatasan

1. Angka bertanda (sim) adalah fiktif dan belum divalidasi Kabiro terkait. Validasi dilakukan pada 2–6 November (H-13 s.d. H-9), sebelum kartu dicetak pada 10 November.
2. Seluruh deck berasal dari **OKR 1 (Musyker 4 April 2026)**. Proker OKR 2 dan 3 mungkin berbeda.
3. **Interpretasi penggabungan:** meja gabungan memegang dua kartu dan dua tab agar seluruh 16 relasi tetap hidup. Bila Ketua menghendaki biro kecil sekadar "menumpang" pada biro partner tanpa kartu sendiri, graf menjadi tujuh simpul dan relasi yang menyentuh biro itu harus dirancang ulang.
4. **Jumlah pengamat dan fasilitator** (±17–19) belum dikonfirmasi ketersediaannya di Badan Personalia dan panitia.
5. **Observasi kepemimpinan** bergantung pada kalibrasi pengamat dan transparansi kepada peserta (naskah 4.1). Tanpa itu, risiko bias dan hilangnya kepercayaan meningkat.
6. Proteksi sel tidak terbawa ke Google Sheets, sehingga perlu diatur manual.
7. Kapasitas Aula atau Ruang Audiovisual untuk 8 meja plus pengamat dan fasilitator belum terverifikasi (lihat dokumen 01, bagian 4.3).
8. Distribusi jumlah Staf Muda per biro belum diketahui. Contoh pada 2.2 bersifat ilustratif.
