# 03 — Petunjuk Pelaksanaan Simulasi Taktis

**Nama sesi:** Simulasi Taktis (Live Cross-Bureau Coordination Game)
**Waktu:** Minggu, 15 November 2026, briefing 13.10–13.20, permainan 13.20–14.40 (80 menit), debrief 15.10–15.25
**Peserta:** Staf Muda angkatan 2025, ±50–70 orang, dibagi ke 8 tim biro
**Fasilitator:** Badan Personalia (Bidang 2)
**Medium:** Google Sheets (`main/template_simulasi_taktis.xlsx`) dan Kartu Rahasia (`main/kartu_skenario_simulasi.md`)
**Versi:** 1.0, 8 Oktober 2026

---

## 1. Konsep Game

### 1.1 Gambaran Umum

Simulasi Taktis adalah **satu ronde terpadu** berdurasi 80 menit. Delapan biro, yaitu **ME, PM, KI, UM, AM, DG, MS, RL**, menjalankan proker amanahnya secara bersamaan menuju sebuah **Hari Puncak (HP)** yang fiktif. Kondisi awal adalah **H-21**. Semua kesepakatan lintas biro harus tuntas dalam satu sesi, yang dianggap sebagai pekan perencanaan.

Keunikan desainnya: ketergantungan antar-biro bersifat **asimetris dan searah** (directed graph). Setiap biro hanya boleh **memulai** koordinasi ke **dua** biro tujuan dan tidak boleh memulai balik kepada biro yang telah meminta kepadanya. Dengan begitu, seluruh delapan biro bergerak secara serentak membentuk satu jaring kerja, bukan sekadar dua biro saling bertukar kepentingan.

### 1.2 Tujuan Belajar

1. Memilih jalur yang tepat: komando, koordinasi langsung, atau eskalasi (Tata Kelola 5.5.1).
2. Bernegosiasi lintas biro dengan kapasitas terbatas dan menghasilkan kesepakatan yang konkret.
3. Mengambil keputusan sebagai Kabiro di bawah tekanan tanpa melampaui wewenang.
4. Melapor dan meminta arahan Kadep dengan format *fakta → opsi → permintaan arahan*.
5. Merasakan beban peran struktural dengan aman sehingga keraguan bisa dibicarakan jujur pada M4 dan KPP.

### 1.3 Mengapa Satu Ronde Terpadu

| Pertimbangan | Penjelasan |
|---|---|
| Ketergantungan nyata | Pada organisasi nyata, banyak biro bergerak bersamaan. Satu ronde terpadu meniru kondisi itu |
| Efisiensi waktu | 80 menit cukup untuk P1–P4 dan tiga inject |
| Keterlibatan | Seluruh biro aktif, tidak ada yang menunggu giliran |
| Pembelajaran tentang dampak | Keputusan satu biro memengaruhi biro lain secara berantai |

---

## 2. Parameter dan Skala

### 2.1 Komposisi Tim untuk 50–70 Peserta

Desain awal mensyaratkan minimal 3 orang per biro (24 peserta). Dengan 50–70 peserta, rata-rata tim berisi 6–9 orang. Peran internal diperluas sebagai berikut.

| Peran | Tugas | Wewenang |
|---|---|---|
| **Kabiro** (1 orang) | Memimpin, memutuskan kesepakatan dan keputusan final, mewakili biro ke Kadep dan biro lain | Memutuskan dalam batas wewenang |
| **Staf Ahli** (1–2 orang) | Memberi pertimbangan, menganalisis kapasitas dan risiko, ikut negosiasi atas penugasan Kabiro | Tidak memutuskan atas nama biro |
| **Staf Muda — Komunikator Keluar** (1–2 orang) | Menjalankan koordinasi ke Target 1 dan Target 2 | Tidak membuat komitmen tanpa persetujuan Kabiro |
| **Staf Muda — Penerima Masuk** (1 orang) | Menerima, mencatat, dan merespons permintaan masuk | Merekomendasikan, Kabiro memutuskan |
| **Staf Muda — Pencatat Sheet** (1 orang) | Mengisi Blok B–E di tab biro | Mencatat, tidak memutuskan |
| **Staf Muda — Pelapor Kadep** (1 orang) | Menyusun dan menyampaikan eskalasi (Blok B) | Menyampaikan, tidak memutuskan |

**Contoh pembagian per ukuran tim:**

| Ukuran | Kabiro | Staf Ahli | Komunikator Keluar | Penerima Masuk | Pencatat | Pelapor Kadep |
|---|---|---|---|---|---|---|
| 6 | 1 | 1 | 1 | 1 | 1 | 1 |
| 7 | 1 | 1 | 2 | 1 | 1 | 1 |
| 8 | 1 | 2 | 2 | 1 | 1 | 1 |
| 9 | 1 | 2 | 2 | 2 | 1 | 1 |

**Contoh sebaran jumlah peserta:**
- 50 peserta: 2 tim berisi 7 orang dan 6 tim berisi 6 orang.
- 60 peserta: 4 tim berisi 8 orang dan 4 tim berisi 7 orang.
- 70 peserta: 2 tim berisi 8 orang dan 6 tim berisi 9 orang.

### 2.2 Pembentukan Tim (Usulan)

1. Tim dibentuk **acak lintas biro asal**. Tidak lebih dari satu anggota yang berasal dari biro yang dimainkan timnya. Alasannya: peserta belajar memahami biro lain dan tidak mengandalkan pengetahuan biro asalnya.
2. Peran Kabiro ditentukan secara acak oleh fasilitator, bukan dengan sukarela, agar semua orang punya peluang merasakan beban pengambilan keputusan.
3. Panitia menyiapkan daftar tim dan peran sebelum hari-H (berdasarkan daftar peserta dengan kode peserta). Pengumuman tim dilakukan pada briefing (13.10).
4. Name tag peserta dilengkapi **warna biro asal** dan **kode peserta**; stiker tambahan ditempel saat tim diumumkan: kode biro simulasi dan peran.

### 2.3 Kebutuhan Fasilitator dan Peran Pendukung

| Peran | Jumlah | Tugas |
|---|---|---|
| Kadep Pelayanan Masjid & Dakwah | 1 | Menerima eskalasi dari KI dan AM |
| Kadep Syi'ar | 1 | Menerima eskalasi dari ME dan PM |
| Kadep Media, Informasi & Digitalisasi | 1 | Menerima eskalasi dari DG dan MS, menyetujui publikasi kilat |
| Kadep Relasi Publik & Advokasi | 1 | Menerima eskalasi dari RL dan UM |
| Waket (I dan III) / BPI | 1–2 | Menerima eskalasi lintas dept atau lintas bidang, menjalankan peran inject B |
| Bendum | 1 | Menjawab pertanyaan kanal donasi (kasus PM) serta deposit, denda, dan penerimaan uang sewa (kasus ME dan UM) |
| Sekum | 0–1 | Opsional: menjawab pertanyaan surat resmi dan SOP |
| Pengendali waktu dan Master Inject | 1 | Menjalankan jam, mengumumkan inject |
| Operator Papan Jaring | 1 | Menampilkan `PAPAN_JARING` dan memantau Sheets |
| Penilai | 4 | Setiap penilai mengamati 2 biro dan mengisi `SKOR_EVALUASI` |
| **Total minimum** | **±12–14** | |

Peran Kadep sebaiknya dimainkan oleh anggota Badan Personalia atau pengurus yang memahami wewenang Kadep. Pemateri yang masih hadir boleh mengisi peran, tetapi tidak wajib.

---

## 3. Aturan Main dan Directed Graph

### 3.1 Delapan Aturan Rantai Koordinasi Asimetris

| No | Aturan | Dasar |
|---|---|---|
| 1 | Setiap biro hanya boleh **menginisiasi** koordinasi ke **2 Biro Tujuan** di kartunya (terkunci). Menerima permintaan dari biro mana pun diperbolehkan. | Desain simulasi |
| 2 | **Dilarang menginisiasi balik** ke biro yang telah meminta kepadamu. Boleh membalas, menawar, atau memberi syarat di tiket yang sama, tetapi tidak boleh membuka tiket baru ke pengirim. | Desain simulasi |
| 3 | Butuh sesuatu di luar 2 target? **Eskalasi ke Kadep.** Kadep menentukan jalurnya. | 5.5.2.7 (eskalasi) |
| 4 | Koordinasi lintas departemen atau bidang wajib **diinfokan** ke Kadep masing-masing. | 5.5.1 ("diketahui koordinator masing-masing") |
| 5 | Request ke DG atau MS wajib lewat form singkat dan lead time. DG dan MS **berhak menolak atau menunda** bila brief tidak jelas, terlalu mepet, atau kapasitas penuh. Kontak ke pihak eksternal **hanya** lewat Biro Relasi. | 6.4.12, 5.5.2.7 |
| 6 | Satu tiket = satu kebutuhan = satu ID dengan format `PENGUSUNG>TUJUAN-nn` (contoh `KI>PM-01`). Biro penerima mencatat ID yang sama di Blok D. | Desain simulasi |
| 7 | Peran dikunci: **Kabiro memutuskan**, Staf Ahli mempertimbangkan, Staf Muda menjalankan komunikasi dan mengisi sheet. | 5.6.9, 5.6.10, 5.6.11 |
| 8 | Kesepakatan yang menyangkut anggaran di luar RAB, perubahan kebijakan, atau program lintas bidang tidak diputuskan sendiri: Kadep → Waket → BPI. | 5.5.2.7 penutup |

**Pelanggaran arah** (menginisiasi balik atau menghubungi biro di luar daftar) ditandai otomatis di kolom *Flag Arah* pada Blok C dan mengurangi skor jalur 25 poin per pelanggaran. Biro yang melanggar tidak dihukum secara verbal. Pelanggaran dibahas pada debrief.

### 3.2 Enam Belas Relasi Resmi (Directed Graph)

Arah panah: **pengusung → tujuan** (pengusung adalah pihak yang boleh memulai).

| No | Pengusung | Tujuan | Jenis lintas | Esensi target kesepakatan |
|---|---|---|---|---|
| 1 | ME | RL | [B] | PIC tunggal dan jalur resmi ke pihak eksternal (mitra donor darah, pemateri tamu, sponsor funrun); tenggat surat; prioritas bila kuota pintu eksternal Relasi terbatas |
| 2 | ME | UM | [B] | Layanan GoRent: ketersediaan unit (HT, sound portable, frame backdrop atau standing banner, kabel roll, proyektor cadangan), paket harga sewa internal ormawa, durasi sewa, serta klausul ganti rugi dan denda bila alat rusak atau hilang |
| 3 | PM | MS | [B] | Prioritas dan lead time publikasi donasi kilat; isi wajib (kanal resmi, penanggung jawab, jadwal laporan transparansi); jumlah slot posting |
| 4 | PM | RL | [B] | Pilihan mitra penyaluran (dari kandidat) beserta syarat verifikasi, PIC, dan prosedur kerja sama lewat jalur khusus |
| 5 | KI | PM | [D] | Pengadaan pengajar Academy: berbagi pool volunteer atau rekrutmen dan pelatihan pengajar tanpa rebutan; hari tersedia dan syarat |
| 6 | KI | AM | [=] | Slot hari dan jam kelas Academy yang tidak bentrok dengan GDM, Q-TIME, dan RAPI; jumlah kelas paralel; aturan kebisingan |
| 7 | UM | KI | [B] | Segmentasi Minion Class vs Academy (mata kuliah, level, jadwal), aturan promosi saling tidak merugikan, pembagian pengajar bila beririsan |
| 8 | UM | DG | [D] | Antrean dan tenggat desain (poster Minion Class dan poster atau katalog paket GoRent), kelengkapan brief sesuai SOP 6.4 (pengajuan H-7), batas revisi |
| 9 | AM | UM | [B] | Pasokan takjil KSSI: volume rata-rata, jadwal, harga per porsi, standar kualitas, skema komitmen |
| 10 | AM | MS | [B] | Slot dan kalender konten bulanan KSSI (feed, reels, pengumuman jadwal), format, tenggat brief, jadwal tayang |
| 11 | DG | MS | [=] | Hand-off produksi → publikasi: format dan tenggat file final, bundling aset, kalender tayang, siapa yang mengunggah |
| 12 | DG | AM | [B] | Izin dan jadwal siaran langsung Q-TIME, posisi kamera dan tripod yang tidak mengganggu jamaah dan GDM, jumlah hari siaran |
| 13 | MS | RL | [D] | Narasumber dan media partner eksternal untuk NARASI lewat jalur Relasi: siapa menghubungi, kapan, sumber alternatif (jaringan alumni) |
| 14 | MS | ME | [B] | Dukungan manajemen acara NARASI (ruang, tanggal, tenaga, rundown) tanpa mengambil alih konten; kompromi dengan jadwal acara besar |
| 15 | RL | DG | [D] | Dokumentasi dan publikasi Jaulah LDK: cakupan (foto, video), tenaga akhir pekan, tenggat brief, batas revisi |
| 16 | RL | KI | [B] | Materi paparan inovasi dakwah dan moderator FGD: durasi, persetujuan materi, penyediaan template, jadwal bebas bentrok |

Legenda: **[=]** satu departemen · **[D]** lintas departemen dalam satu bidang · **[B]** lintas bidang. Hitungan: 2 × [=], 4 × [D], 10 × [B].

### 3.3 Sifat Graf (Telah Diverifikasi Program)

| Properti | Hasil |
|---|---|
| Jumlah relasi | 16 |
| Out-degree tiap biro | Tepat 2 |
| Pasangan timbal-balik | 0 (tidak ada A→B bersama B→A) |
| Loop diri | 0 |
| Konektivitas | Terhubung kuat: dari tiap biro dapat dicapai tiap biro lain lewat arah panah |

| Biro | Menginisiasi ke | In-degree (menerima dari) |
|---|---|---|
| ME | RL, UM | 1 (MS) |
| PM | MS, RL | 1 (KI) |
| KI | PM, AM | 2 (UM, RL) |
| UM | KI, DG | 2 (ME, AM) |
| AM | UM, MS | 2 (KI, DG) |
| DG | MS, AM | 2 (UM, RL) |
| MS | RL, ME | 3 (PM, AM, DG) |
| RL | DG, KI | 3 (ME, PM, MS) |

**Simpul padat:** MS dan RL menerima paling banyak permintaan (masing-masing 3). Ini disengaja karena Tata Kelola memosisikan Biro Relasi sebagai pintu kerja sama eksternal dan Medsist sebagai penayang publikasi.

**Loop koordinasi alami** (sengaja dipasang agar kapasitas tiap biro saling memengaruhi):
- UM → KI → AM → UM
- DG → AM → UM → DG
- RL → DG → MS → RL
- ME → RL → KI → PM → MS → ME
- AM → MS → ME → UM → KI → AM

**Rantai dampak (cascade):**
1. **GoRent:** ME>UM bersaing dengan klien eksternal UM untuk unit HT dan proyektor pada H-1 sampai HP. Tarif dan klausul memengaruhi anggaran sewa ME sekaligus target keuntungan UM, dan SOP 6.3 tidak mengatur tarif atau denda sehingga kesepakatan harus dicatat dan diinfokan ke Kadep RnA.
2. **Slot eksternal RL:** ME, PM, dan MS bersaing untuk sisa 4 slot.
3. **Antrean DG dan MS:** UM, RL → DG; PM, AM, DG → MS. Inject A menurunkan kapasitas keduanya.
4. **Hari pengajar:** KI>PM (relawan hanya tersedia Rabu dan Kamis) menentukan KI>AM (hari kelas).
5. **Aula:** NARASI milik MS berbenturan dengan penguncian Aula oleh ME.

---

## 4. Alur 80 Menit

### 4.1 Briefing (13.10–13.20, 10 menit)

| Menit | Kegiatan | Penyampai |
|---|---|---|
| 0–2 | Tujuan dan gambaran game; kondisi H-21 | Fasilitator utama |
| 2–5 | Aturan arah, eskalasi, dan larangan menginisiasi balik | Fasilitator utama |
| 5–8 | Pengumuman tim dan peran, pembagian klaster dan amplop Kartu Rahasia | Sie Simulasi |
| 8–10 | Pengenalan tab Google Sheets (Blok A–E, flag arah) dan tanya jawab kilat | Operator Papan Jaring |

### 4.2 Fase Permainan

| Fase | Menit game | Aktivitas | Output | Yang dilakukan fasilitator |
|---|---|---|---|---|
| **P1 Persiapan** | 0–10 | Baca Kartu Rahasia, isi Blok A (nama peran), susun prioritas, rencanakan 2 tiket keluar. Briefing awal ke Kadep (opsional, Blok B) | Blok A lengkap; rencana 2 tiket | Keliling memastikan semua tim membaca kartu dan membuka tab biro yang benar |
| **P2 Koordinasi Live** | 10–50 | Buka tiket ke 2 target; layani permintaan masuk; negosiasi; eskalasi ke Kadep bila perlu; tiga inject berjalan | Blok C dan D terisi; status tiap tiket | Umumkan inject pada menit 15, 25, 35; pantau Papan Jaring; Kadep menjawab eskalasi |
| **P3 Finalisasi** | 50–70 | Rapat dengan Kadep: laporkan hasil dan minta persetujuan; Kabiro mengisi Blok E | Blok E lengkap; persetujuan Kadep | Kadep memeriksa konsistensi keputusan dengan hasil tiket; penilai menyelesaikan penilaian awal |
| **P4 Papan Jaring** | 70–80 | Layar menampilkan `PAPAN_JARING`; tiap biro menyebut satu kesepakatan terbaik dan satu kompromi tersulit (30 detik per biro) | Papan final | Operator menampilkan papan; pengendali waktu menjaga 30 detik per biro |

**Catatan:** transisi antar fase diberi sinyal suara. Waktu P2 mencakup tiga inject. Penutupan P3 tepat pada menit 70 agar Ashar tidak terlambat.

### 4.3 Tiket Koordinasi

- Setiap biro membuka **minimal 2 tiket** (satu per target). Baris pertama dan kedua Blok C sudah terisi ID dan tujuan.
- Setiap tiket memuat: kebutuhan, tawaran, hasil kesepakatan (isi, volume, waktu, PIC), syarat, status, dan perlunya eskalasi.
- Status: `Pending`, `Negosiasi`, `Sepakat`, `Ditolak`, `Batal`. Pada `PAPAN_JARING` ditampilkan sebagai *Pending / Deal / Reject / Batal*.
- Komunikasi boleh lisan antar-meja untuk kecepatan. **Hasilnya wajib dicatat** pada Blok C (pengirim) dan Blok D (penerima).

---

## 5. Katalog Delapan Kasus Biro

> **Catatan penanda angka:** angka **tanpa tanda** bersumber dari paparan Musyker OKR 1. Angka bertanda **(sim)** adalah angka simulasi. Seluruhnya bersifat fiktif dan dapat disesuaikan fasilitator setelah divalidasi Kabiro terkait.
> **Kondisi dunia simulasi:** sekarang H-21 menuju HP. Waktu masjid (sim): Ashar 15.00; Maghrib 17.30; Q-TIME 17.00–17.30 pada hari kerja.

### 5.1 Kasus 1 — ME, Biro Manajemen Event (Maven)

| | |
|---|---|
| Departemen / Bidang | Syi'ar, Bidang 1 (Kadep Syi'ar → Waket I) |
| Proker Amanah | **Maulid Nabi × Milad JMMI** (kajian, funrun, donor darah) |
| Target terkunci | **RL** dan **UM** |
| Sumber deck | Maulid Nabi × Milad JMMI, 5 April–10 September 2026; tujuan memperkuat nilai spiritual, kebersamaan, dan identitas JMMI; kegiatan kajian, funrun, donor darah |

**Latar belakang / trigger.** H-21 menuju HP. Tiga hal belum beres: (1) belum ada mitra penyelenggara donor darah resmi; (2) belum ada pemateri tamu kajian dan sponsor funrun; (3) peralatan event belum tersedia: panitia butuh HT, sound portable, frame backdrop atau standing banner, kabel roll, dan proyektor cadangan untuk kajian, funrun, dan donor darah, sementara anggaran sewa terbatas.

**Limitasi dan kapasitas.**
- Panitia 55 orang (sim); target funrun 300 pelari (sim); target donor 100 kantong (sim).
- Aula MMI **terkunci** untuk pasang-bongkar mulai **H-3 pukul 12.00 sampai HP**. Sebelum itu Aula bebas. Ruang Audiovisual (kapasitas 60, sim) bebas kapan saja.
- Tim cadangan tanpa tugas panitia: 4 Staf Muda (sim).
- **Kebutuhan alat (sim):** HT 12 unit (minimal 8), sound portable 2 set, frame backdrop atau standing banner 3 set, kabel roll 6, proyektor cadangan 1. Dipakai **H-2 sampai H+1 (4 hari)**.
- **Anggaran sewa alat maksimal Rp 1.000.000** (sim) untuk seluruh paket. Dana panitia baru cair setelah proposal disetujui, sehingga **deposit** yang sanggup disetor saat pengambilan **maksimal 20%** dari nilai sewa.
- ME tidak ingin menanggung **keausan wajar**, tetapi bersedia bertanggung jawab atas kerusakan atau kehilangan akibat kelalaian panitia.
- Hanya 1 PIC eksternal (Staf Ahli ME) untuk semua kontak ke luar.

**Misi koordinasi wajib.**
- **Target 1 (RL):** wajib menyepakati (a) 1 mitra donor darah resmi, (b) 1 pemateri tamu kajian. Diinginkan: 1 sponsor funrun. Harus memuat PIC tunggal, tenggat surat, dan siapa yang menghubungi pihak luar. Dilarang menghubungi pihak eksternal sendiri.
- **Target 2 (UM), layanan GoRent:** wajib menyepakati (1) **ketersediaan unit**: minimal 8 HT, 2 sound portable, 3 frame backdrop atau standing banner, dan 1 proyektor cadangan; (2) **paket harga sewa internal ormawa** dengan total ≤ Rp 1.000.000; (3) **durasi sewa** H-2 sampai H+1; (4) **klausul ganti rugi dan denda** bila alat rusak atau hilang, termasuk besaran deposit. Diinginkan: HT 12 unit dan kabel roll 6. Yang bisa ditawarkan: pengembalian tepat waktu, satu PIC peminjam (Staf Ahli ME), pengecekan fungsi bersama saat serah terima, dan promosi GoRent di materi acara. ME belum tahu stok, tarif, dan aturan UM, dan harus menggalinya.

**Permintaan yang mungkin masuk.** Dukungan acara (ruang dan tenaga). Boleh memberi maksimal 4 Staf Muda cadangan, 1 hari kerja, tidak untuk H-3 sampai HP; Aula bebas sebelum H-3 pukul 12.00; Ruang Audiovisual kapan saja.

**Batasan wewenang dan SOP.** Kontak eksternal hanya lewat RL. Biaya sewa > Rp 1.000.000, deposit > 20%, atau klausul ganti rugi yang menambah beban di luar RAB diusulkan ke Kadep Syi'ar. Peminjaman inventaris sekretariat JMMI (bukan GoRent) mengikuti SOP 6.3 melalui Sekretaris Umum. Perubahan tanggal HP atau format acara: Kadep → Waket I → BPI. Tidak boleh meminjamkan Aula pada rentang terkunci. Staf Ahli tidak berkomitmen atas nama biro.

### 5.2 Kasus 2 — PM, Biro Pengabdian Masyarakat

| | |
|---|---|
| Departemen / Bidang | Syi'ar, Bidang 1 |
| Proker Amanah | **JMMI Peduli** (donasi musibah dan bantuan mitra pengabdian) |
| Target terkunci | **MS** dan **RL** |
| Sumber deck | JMMI Peduli: Oktober 2026 dan insidental; penggalangan dana untuk korban bencana dan bantuan mitra kegiatan pengabdian JMMI; KR: konsep pengumpulan dan penyaluran donasi, 2 jenis donasi, 3 kandidat mitra |

**Latar belakang / trigger (sim).** Banjir bandang melanda desa dekat lokasi mitra JMMI Mengabdi. BPI meminta JMMI Peduli bergerak: donasi harus **tayang** dan penyaluran ke mitra terverifikasi harus jelas **sebelum donasi dibuka**.

**Limitasi dan kapasitas.**
- Dua jenis donasi: dana tunai dan barang kebutuhan pokok.
- Tim Peduli: 1 Staf Ahli dan 3 Staf Muda (sim).
- Tiga kandidat mitra (sim): **A** lembaga kemanusiaan nasional (verifikasi 4 hari); **B** komunitas relawan lokal (verifikasi 2 hari, tanpa MoU); **C** mitra JMMI Mengabdi yang sudah dikenal (verifikasi 1 hari, lokasi 30 km dari titik banjir).
- Pool volunteer pengajar JMMI Mengajar: 8 orang terlatih (sim). 6 terikat sesi, **2 cadangan**. Dua cadangan dipakai untuk sortir dan packing donasi Senin–Selasa, bebas **Rabu–Kamis**.
- Standar pengajar: 1× open recruitment dan 2 sesi pelatihan (sesi pelatihan sim: H-17 dan H-14).
- Rekening resmi donasi dikelola **Bendum**.

**Misi koordinasi wajib.**
- **Target 1 (MS):** wajib menyepakati 2 posting: (a) pengumuman donasi tayang ≤ 24 jam sejak brief, (b) laporan transparansi 7 hari setelah donasi dibuka. Harus memuat kanal resmi, penanggung jawab, dan jadwal laporan. Dilarang meminta MS memuat kanal yang belum disetujui Bendum.
- **Target 2 (RL):** wajib menyepakati 1 mitra penyaluran terverifikasi sebelum donasi dibuka (maksimal 2 hari), beserta syarat verifikasi, PIC, dan prosedur kerja sama.

**Permintaan yang mungkin masuk.** Peminjaman volunteer atau penggabungan rekrutmen pengajar. Boleh meminjamkan 2 cadangan **hanya Rabu–Kamis**, bila (1) tidak bentrok sesi JMMI Mengajar, (2) relawan ikut 2 sesi pelatihan standar, (3) jadwal tertulis. Rekrutmen satu pintu boleh.

**Batasan wewenang dan SOP.** Dilarang membuka rekening atau kanal donasi sendiri (Bendum/BPI). Perubahan target donasi dan kebijakan penyaluran → BPI. Kontak eksternal hanya via RL. Prioritas antrean media → Kadep Media.

### 5.3 Kasus 3 — KI, Biro Kajian dan Inovasi Dakwah (KID)

| | |
|---|---|
| Departemen / Bidang | Pelayanan Masjid dan Dakwah, Bidang 1 |
| Proker Amanah | **JMMI Academy** |
| Target terkunci | **PM** dan **AM** |
| Sumber deck | JMMI Academy: minimal 4 kelas, minimal 20 peserta per kelas, minimal 1 pengajar per kelas, menjelang ETS dan EAS; konsep, rekrutmen pengajar, poster, pelaksanaan |

**Latar belakang / trigger (sim).** H-21. Kelas dijadwalkan Senin–Kamis pada H-12 sampai H-9. Pengajar baru 2, pendaftar baru 38 dari target 80, dan terdengar ada kegiatan bimbel lain untuk mahasiswa yang sama.

**Limitasi dan kapasitas.**
- 4 kelas (sim): Kalkulus, Fisika Dasar, Kimia Dasar, Pengantar Pemrograman. Durasi ideal 105 menit, minimal 75 menit; mulai ideal 15.30.
- Pengajar internal 2 (Kalkulus dan Fisika Dasar), **kurang 2** (Kimia Dasar dan Pemrograman).
- Pendaftar 38 (sim) dari target 80.
- Maksimal 2 ruang paralel (sim). Tim: 2 Staf Ahli dan 3 Staf Muda.
- Materi yang mewakili JMMI ke pihak luar harus disetujui **Kadep Pelayanan**.

**Misi koordinasi wajib.**
- **Target 1 (PM):** wajib menyepakati 2 pengajar tambahan siap mengajar H-12 sampai H-9 dengan pelatihan minimal 1 sesi. Diinginkan: rekrutmen satu pintu. Yang bisa ditawarkan: template materi ajar, sertifikat atau jam terbang, bantuan promosi.
- **Target 2 (AM):** wajib menyepakati 4 kelas dalam 4 hari kerja, selesai ≤ 17.00, bebas bentrok kegiatan masjid. Diinginkan: durasi ≥ 90 menit, 2 kelas paralel dalam satu hari. KI belum tahu hari dan jam tersedia dan harus menggalinya.

**Permintaan yang mungkin masuk.**
- Sinkronisasi bimbel lain (segmen, jadwal, promosi): boleh bernegosiasi. Syarat KI: Academy fokus konsep dasar bagi mahasiswa baru, nama dan logo Academy tidak dipakai program lain, promosi tidak saling menjatuhkan. KI tidak berwenang meminta program biro lain dibatalkan.
- Permintaan materi atau moderator untuk tamu eksternal: 1 moderator (Staf Muda yang bebas hanya hari Sabtu) dan 1 materi 15 menit (butuh persiapan 3 hari dan template dari pemohon).

**Batasan wewenang dan SOP.** Materi untuk pihak eksternal → persetujuan Kadep Pelayanan. Penambahan atau pengurangan kelas di luar rencana atau anggaran → Kadep Pelayanan. Kerja sama pihak luar hanya via RL. Konflik segmen yang tidak selesai → Kadep kedua belah pihak.

### 5.4 Kasus 4 — UM, Biro Usaha Mandiri

| | |
|---|---|
| Departemen / Bidang | Relasi Publik dan Advokasi, Bidang 3 (Kadep RnA → Waket III) |
| Proker Amanah | **Minion Class** (layanan: GoRent, JMMI Commerce) |
| Target terkunci | **KI** dan **DG** |
| Sumber deck | Minion Class: bimbingan belajar mingguan offline, KR 4 kali pelaksanaan, pendataan partisipan dan net income; GoRent: penyewaan perlengkapan kerja (proyektor, layar, HT, kamera, tripod) dalam paket, KR 20 penyewa dan keuntungan minimal Rp 250.000, reinventaris, perbaikan, dan pengadaan unit bila perlu, poster penyewaan bersama Digipro; JMMI Commerce: keuntungan ≥ Rp 150.000, papan transparansi harga |

**Latar belakang / trigger (sim).** UM ingin menjalankan 2 sesi Minion Class pada H-12 sampai H-9, tetapi mata kuliah, peserta, dan pengajarnya mirip dengan program kelas milik biro lain, dan promosi belum ada. Pada saat yang sama UM menerima banyak permintaan sewa alat GoRent (termasuk dari klien eksternal untuk Hari Puncak) dan takjil.

**Limitasi dan kapasitas.**
- Minion Class (sim): 2 sesi, target 20 peserta per sesi, biaya Rp 15.000 per peserta, honor tutor Rp 150.000 per sesi, 3 tutor internal.
- **Inventaris GoRent (sim):** HT 12 unit; sound portable 2 set; frame backdrop atau standing banner 4 set; kabel roll 6; proyektor 2 unit. Pada **H-1 sampai HP**, **4 HT dan 1 proyektor** sudah dibooking klien eksternal, sehingga yang tersedia pada hari puncak hanya **8 HT dan 1 proyektor**.
- **Tarif umum per hari (sim):** HT Rp 10.000 per unit; sound portable Rp 100.000 per set; frame backdrop Rp 30.000 per set; kabel roll Rp 5.000 per unit; proyektor Rp 100.000 per unit.
- **Harga internal ormawa JMMI (sim):** diskon **30%** dari tarif umum. Untuk sewa **3 hari atau lebih**, hari ke-3 dan seterusnya dihitung **50% dari tarif internal**. Nilai satu peminjaman besar tidak boleh di bawah **Rp 800.000** (biaya perawatan dan target keuntungan).
- **Klausul standar GoRent (sim):** deposit 30% dari nilai sewa (dikembalikan); denda terlambat 25% dari tarif harian per hari; kerusakan = biaya perbaikan sesuai nota; hilang atau rusak berat = ganti unit setara atau 100% harga pengadaan; wajib berita acara serah terima (foto kondisi dan uji fungsi) saat ambil dan kembali.
- **Catatan SOP:** SOP 6.3 hanya mengatur peminjaman inventaris sekretariat lewat Sekretaris Umum, dan kewajiban menjaga barang sesuai keadaan saat pengambilan. **SOP tidak mengatur tarif sewa, deposit, atau denda.** Klausul itu dirumuskan UM dalam batas wewenangnya dan dicatat sebagai temuan untuk Badan Keorganisasian.
- JMMI Commerce (sim): dapur 40 porsi per hari; HPP Rp 8.000; harga Rp 11.000; diskon 5% (Rp 10.450) bila komitmen ≥ 400 porsi (8 sesi). Porsi tambahan dari tenant mitra Rp 12.000, bisa Rp 11.000 bila komitmen ≥ 80 porsi.
- Target keuntungan (deck): minimal Rp 150.000.

**Misi koordinasi wajib.**
- **Target 1 (KI):** wajib menyepakati pembagian segmen (mata kuliah, level, jadwal) agar Minion Class dan kelas KI tidak bentrok dan tidak saling mematikan; 2 sesi Minion Class punya jadwal pasti. Diinginkan: promosi silang atau pembagian pengajar. Tawaran: Minion Class fokus latihan soal intensif. Dilarang meminta KI membatalkan atau mengurangi programnya.
- **Target 2 (DG):** wajib menyepakati poster Minion Class siap ≤ H-16 (batas terima ≤ H-14) dan poster atau katalog paket GoRent ≤ H-12. Harus memuat tenggat, kelengkapan brief, batas revisi. Siapkan brief lengkap sebelum meminta. Ingat SOP media: desain diajukan minimal H-7 sebelum hasil dibutuhkan, dan pengajuan lebih mepet tidak menjamin selesai.

**Permintaan yang mungkin masuk.** Penyewaan alat GoRent dan pemesanan takjil. Layani sesuai batas. Tidak boleh menjanjikan unit yang sudah dibooking atau melewati kapasitas dapur. Diskon sewa > 30%, sewa gratis, atau pembebasan deposit atau denda di luar kewenangan. Diskon takjil > 5% atau harga di bawah HPP juga di luar kewenangan.

**Batasan wewenang dan SOP.** Diskon sewa > 30%, sewa gratis, pembebasan deposit atau denda, atau ganti rugi di bawah 100% harga pengadaan → Kadep RnA. Diskon takjil > 5% atau harga di bawah HPP → Kadep RnA. Pengadaan unit baru atau perbaikan besar → Kadep RnA dan Bendum. Tenant eksternal baru → lewat RL. Penerimaan uang (sewa, deposit, denda) → Bendum. Prioritas permintaan boleh diputuskan Kabiro UM, penolakan dikomunikasikan sopan dan diinfokan ke Kadep RnA.

> **Catatan analisis.** Tumpang tindih Minion Class dan JMMI Academy adalah **temuan penyusun** dari dua deck, yaitu sama-sama membidik mata kuliah dasar menjelang ETS dan EAS. Kasus ini dipakai sebagai bahan latihan negosiasi dan bukan tuduhan terhadap salah satu biro.

### 5.5 Kasus 5 — AM, Biro Amaliyah Yaumiyah

| | |
|---|---|
| Departemen / Bidang | Pelayanan Masjid dan Dakwah, Bidang 1 |
| Proker Amanah | **KSSI** (Komunitas Shaum Sunnah ITS) |
| Target terkunci | **UM** dan **MS** |
| Sumber deck | KSSI: berbuka puasa Senin dan Kamis, rata-rata minimal 50 porsi, konten dokumentasi bulanan, jadwal puasa sunnah via Google Calendar dan WA; Q-TIME: murottal 30 menit sebelum azan Magrib hari kerja; GDM: 40 kali penertiban saat azan Dzuhur dan Ashar; RAPI: perawatan sarung, mukena, sajadah (setiap minggu ke-3) |

**Latar belakang / trigger (sim).** Donasi takjil dari jamaah menurun padahal 8 sesi (4 pekan) butuh pasokan stabil, dan konten dokumentasi bulan ini belum keluar.

**Limitasi dan kapasitas.**
- Target KSSI (deck): rata-rata minimal 50 porsi per sesi, 8 sesi sama dengan 400 porsi.
- Plafon konsumsi KSSI (sim): **Rp 4.250.000** untuk 8 sesi, rata-rata **Rp 10.625** per porsi.
- Komitmen rutin yang membatasi pihak lain: GDM (azan Dzuhur dan Ashar), Q-TIME (17.00–17.30), RAPI (setiap **Selasa** area serambi).
- **Slot ruang untuk pihak lain (sim):** Senin, Rabu, Kamis pukul 15.30–16.55; Selasa tidak; maksimal 1 kelas paralel per hari, kecuali Rabu boleh 2 area. Aktivitas berhenti 16.55 dan bersuara pelan.
- **Siaran langsung Q-TIME (sim):** hanya Rabu dan Kamis, 1 kamera, tripod di **belakang saf terakhir**, wajib izin pelantun, GDM mengamankan jalur.
- Tim AM 5 orang (sim).

**Misi koordinasi wajib.**
- **Target 1 (UM):** wajib menyepakati pasokan takjil rata-rata ≥ 50 porsi per sesi untuk 8 sesi (40–60 per sesi boleh selama rata-rata ≥ 50), harga rata-rata ≤ Rp 10.625 per porsi, jadwal pengiriman, standar kualitas. Tawaran: komitmen 8 sesi (400 porsi), pembayaran mingguan, promosi UM di konten KSSI.
- **Target 2 (MS):** wajib menyepakati 1 feed dan 1 reels dokumentasi bulanan (boleh dibundel) dengan tanggal tayang pasti, plus pengumuman jadwal puasa sunnah. Tawaran: materi mentah lengkap dan tepat waktu, draf caption, brief jelas.

**Permintaan yang mungkin masuk.** Slot ruang atau izin siaran langsung Q-TIME. Jawab hanya dalam batas di atas. Izin resmi ruang masjid mengikuti surat peminjaman tempat dan fasilitas oleh Sekretaris Pelaksana.

**Batasan wewenang dan SOP.** Aturan dan area masjid ada di tangan Takmir; di luar serambi dan jam di atas → Kadep Pelayanan. Anggaran konsumsi di atas plafon → Kadep Pelayanan. Tidak boleh mengurangi GDM atau Q-TIME demi kegiatan biro lain. Permintaan media mengikuti SOP media.

### 5.6 Kasus 6 — DG, Biro Digital Production (Digipro)

| | |
|---|---|
| Departemen / Bidang | Media, Informasi, dan Digitalisasi (Medigi), Bidang 3 |
| Proker Amanah | **STREAMMI** (live streaming dan videotron) dan **Requesta** |
| Target terkunci | **MS** dan **AM** |
| Sumber deck | STREAMMI: live streaming dan tayangan sinergi di videotron sesuai request; Requesta: merangkum semua permintaan luar departemen dan membaginya sesuai jobdesk dan kemampuan staf |

**Latar belakang / trigger (sim).** Permintaan masuk bersamaan, DG ingin memperluas siaran Q-TIME, dan hasil produksi menumpuk karena jalur publikasi lambat.

**Limitasi dan kapasitas.**
- Kru (sim): 4 multimedia dan 4 kreatif; **akhir pekan hanya 1 orang** siaga (hanya foto, tanpa video panjang).
- **Requesta (SOP 6.4):** maksimal **4 order desain atau dokumentasi per minggu** (sim). Satu form hanya untuk satu konten. Batas pengajuan dihitung dari tanggal hasil dibutuhkan: desain kreatif dan motion graphic **H-7**, video atau konten kurang dari 3 menit **H-7**, video atau konten lebih dari 3 menit **H-10**. Estimasi desain 4–5 hari kerja ditambah 1–2 hari revisi minor; revisi maksimal 2 kali. Pengajuan yang lebih mepet tidak menjamin selesai tepat waktu.
- Output final DG per minggu: 6 aset (sim); satu carousel atau reels memuat hingga 4 aset.
- Target siaran: Q-TIME 5 hari per minggu dengan 2 kamera.
- Berhak menolak atau menunda bila brief tidak jelas, terlalu mepet, atau kapasitas penuh (6.4.12).

**Misi koordinasi wajib.**
- **Target 1 (MS):** wajib menyepakati hand-off produksi ke publikasi: format file, tenggat file final (DG mengincar **Jumat 20.00**), siapa yang mengunggah, kalender tayang, dan minimal 2 slot tayang per minggu (boleh dibundel). Tawaran: aset siap tayang, draf caption, standar penamaan file.
- **Target 2 (AM):** wajib menyepakati izin siaran langsung Q-TIME minimal 2 hari per minggu dengan minimal 1 kamera, tanpa mengganggu jamaah. Diinginkan: 2 kamera dan 5 hari. Murottal menuntut kekhusyukan; tawaran harus menghormatinya.

**Permintaan yang mungkin masuk.** Order desain atau dokumentasi dari biro lain. Layani dalam batas 4 order per minggu. Order yang terkait tenggat acara atau kegiatan yang sudah terjadwal lebih kritis dari promosi rutin. Akhir pekan hanya foto. Penolakan disampaikan sopan lewat PIC dengan alasan SOP.

**Batasan wewenang dan SOP.** Prioritas ketika dua biro lintas dept berebut slot → Kadep Media. Aturan masjid dan jadwal ada pada AM atau Takmir. Kontak eksternal via RL. Konten sensitif atau kanal donasi hanya diproduksi bila sumber dan izinnya jelas.

### 5.7 Kasus 7 — MS, Biro Media Analysis dan Strategi (Medsist)

| | |
|---|---|
| Departemen / Bidang | Media, Informasi, dan Digitalisasi, Bidang 3 |
| Proker Amanah | **NARASI** (diskusi publik atau FGD isu keumatan) |
| Target terkunci | **RL** dan **ME** |
| Sumber deck | NARASI: forum diskusi publik/FGD isu sosial dan keumatan; KPI Instagram: 250 ribu tayangan, 3 ribu interaksi, 300 pengikut baru; menerima draf final dari Form Request; Medpar dengan SOP |

**Latar belakang / trigger (sim).** NARASI direncanakan **H-2 pukul 19.30 di Aula**, 80 peserta. Belum ada narasumber, media partner, maupun tim teknis acara. Antrean publikasi juga penuh.

**Limitasi dan kapasitas.**
- Kalender konten (sim): sisa **5 slot posting** untuk 14 hari ke depan. 1 slot untuk promosi NARASI, sehingga **4 slot** untuk permintaan biro lain.
- Lead time standar 48 jam. **Kilat 24 jam** hanya dengan persetujuan Kadep Media untuk kondisi kemanusiaan atau darurat.
- Hanya draf final dari Form Request yang diunggah; brief tidak lengkap ditolak.
- Tim: 2 Staf Ahli dan 3 Staf Muda, piket Senin–Kamis, **tanpa piket akhir pekan**, sehingga tenggat file final hand-off **Kamis 16.00**.
- Kebutuhan NARASI: 2 narasumber (1 akademisi, 1 praktisi), 1 media partner, 80 peserta.

**Misi koordinasi wajib.**
- **Target 1 (RL):** wajib menyepakati 2 narasumber dan 1 Medpar lewat jalur resmi Relasi (siapa menghubungi, kapan, siapa PIC). Boleh mempertimbangkan jaringan alumni. Dilarang menghubungi pihak luar sendiri.
- **Target 2 (ME):** wajib menyepakati tempat dan tanggal pasti serta dukungan 4 panitia (MC, registrasi, rundown, dokumentasi). Diinginkan: Aula untuk 80 orang pada H-2. Tawaran: konten dan moderator disiapkan MS sendiri, ME hanya mengurus manajemen acara; materi promosi siap.

**Permintaan yang mungkin masuk.** Slot posting atau hand-off produksi. Layani hanya dengan brief lengkap dan konten final dalam batas 4 slot (bisa turun). Konten kemanusiaan boleh didahulukan dengan persetujuan Kadep Media. Boleh menawarkan bundling.

**Batasan wewenang dan SOP.** Prioritas antar permintaan lintas dept dan publikasi kilat → Kadep Media. Kontak eksternal via RL. Kanal donasi atau konten yang belum disetujui pemilik atau Bendum tidak diunggah. Tema sensitif NARASI → Kadep Media.

### 5.8 Kasus 8 — RL, Biro Relasi dan Hubungan Eksternal

| | |
|---|---|
| Departemen / Bidang | Relasi Publik dan Advokasi, Bidang 3 |
| Proker Amanah | **Benchmarking / Jaulah LDK** |
| Target terkunci | **DG** dan **KI** |
| Sumber deck | Benchmarking: kolaborasi dengan 2–3 LDK, forum diskusi dan sharing session, perwakilan tiap biro pada FGD, laporan dan evaluasi; Database Alumni (2020–2025); Gift Alumni W-133; AMKI Muda; kedirjenan internal |

**Latar belakang / trigger (sim).** **H-7 (Sabtu)** RL menerima **2 LDK mitra (±20 tamu)** di **Ruang Audiovisual**. Di waktu yang sama beberapa biro mengajukan kontak ke pihak luar lewat RL.

**Limitasi dan kapasitas.**
- Pintu eksternal (sim): **6 total**. 2 terpakai (2 LDK), **sisa 4 slot** untuk kontak eksternal baru.
- Setiap kontak eksternal baru wajib memiliki **surat resmi** (SOP: diajukan paling lambat H-3 sebelum tenggat, diasistensi Pembina) dan **persetujuan Kadep RnA dan Waket III** (jalur khusus).
- Tim: 1 Staf Ahli (PIC eksternal) dan 2 Staf Muda (sim).
- Database Alumni 2020–2025: ±40 alumni berkontak lengkap (sim). Menghubungi alumni **tidak memakai slot**, tetapi tetap lewat RL.
- Mitra yang sudah pernah bekerja sama tidak memakai slot dan hanya butuh **verifikasi 1 hari**.
- Hari-H Jaulah: sharing 15 menit dan FGD, perlu dokumentasi.

**Misi koordinasi wajib.**
- **Target 1 (DG):** wajib menyepakati dokumentasi Jaulah H-7 (Sabtu): 1 fotografer dan 1 videografer, 1 desain undangan LDK, 1 video recap 2 menit. Siapkan tawaran: form request dan brief lengkap sesuai SOP (video kurang dari 3 menit diajukan minimal H-7), aset logo, akses lokasi, rencana publikasi. RL belum tahu kru DG pada akhir pekan, jadi harus menggali dan menyiapkan alternatif.
- **Target 2 (KI):** wajib menyepakati 1 moderator FGD dan 1 materi 15 menit "Inovasi Dakwah JMMI". Diinginkan: 3 perwakilan KID. Tawaran: template slide, naskah, jam latihan. Materi untuk tamu eksternal perlu persetujuan Kadep Pelayanan.

**Permintaan yang mungkin masuk.** Kontak eksternal dari biro lain, kemungkinan **melebihi 4 slot**. Aturan jawaban: setiap permintaan harus memuat tujuan, nama pihak, tenggat, PIC, dan penandatangan surat; yang tidak lengkap boleh ditunda. Boleh menawarkan alternatif (alumni, mitra yang sudah ada) yang tidak memakai slot. Prioritas diputuskan bersama Kadep RnA.

**Batasan wewenang dan SOP.** Menambah slot di atas 4 → Kadep RnA dan Waket III. Kerja sama yang mengikat organisasi atau mengubah kebijakan → BPI. Surat resmi lewat Sekum atau Sekretaris Pelaksana; tidak boleh berkomitmen lisan atas nama JMMI. Kerja sama eksternal final: Kadep RnA dan Waket III.

---

## 6. Matriks Koordinasi 8 Biro (Ringkasan)

| Biro pengusung | Proker | Trigger masalah / kebutuhan | Wajib koordinasi ke | Esensi yang harus disepakati |
|---|---|---|---|---|
| **ME** | Maulid Nabi × Milad JMMI | Tiga minggu sebelum hari-H: perlu mitra donor darah dan narasumber atau sponsor luar. Panitia juga perlu menyewa alat event (HT, sound portable, frame backdrop, kabel roll, proyektor cadangan) dengan anggaran terbatas | **T1: RL** [B] | PIC tunggal ke eksternal dan tenggat surat lewat jalur resmi |
| | | | **T2: UM** [B] | Ketersediaan unit GoRent, paket harga sewa internal, durasi sewa, dan klausul ganti rugi atau denda |
| **PM** | JMMI Peduli | Musibah mendadak: donasi harus tayang cepat dan disalurkan ke mitra terverifikasi | **T1: MS** [B] | Prioritas antrean publikasi kilat, isi konten verifikasi dan transparansi donasi |
| | | | **T2: RL** [B] | Pilihan mitra penyaluran, syarat verifikasi, dan prosedur kerja sama |
| **KI** | JMMI Academy | Pengajar terbatas. Kelas di area masjid beririsan dengan waktu salat | **T1: PM** [D] | Berbagi pool volunteer pengajar dan pelatihan tanpa rebutan |
| | | | **T2: AM** [=] | Slot kelas tidak bentrok dengan GDM, Q-TIME, dan RAPI |
| **UM** | Minion Class | Segmen, periode, dan pengajar tumpang tindih dengan Academy. Perlu materi promosi | **T1: KI** [B] | Pembagian segmen, mata kuliah, jadwal, dan aturan promosi agar tidak saling mematikan |
| | | | **T2: DG** [D] | Antrean desain poster, kelengkapan brief, lead time |
| **AM** | KSSI | Berbuka rutin Senin dan Kamis ≥ 50 porsi dan konten dokumentasi bulanan | **T1: UM** [B] | Pasokan takjil: harga, jumlah, jadwal, standar kualitas |
| | | | **T2: MS** [B] | Kalender konten bulanan, format, jadwal posting |
| **DG** | STREAMMI | Live streaming Q-TIME dan kajian, hasil produksi harus naik tepat waktu | **T1: MS** [=] | Hand-off ke publikasi: format file, tenggat, siapa yang mengunggah |
| | | | **T2: AM** [B] | Izin siaran dan jadwal Q-TIME, posisi kamera tidak mengganggu jamaah |
| **MS** | NARASI | Butuh narasumber dan media partner luar, plus dukungan teknis acara | **T1: RL** [D] | Narasumber dan Medpar eksternal lewat jalur Relasi |
| | | | **T2: ME** [B] | Dukungan manajemen acara tanpa mengambil alih konten |
| **RL** | Benchmarking / Jaulah LDK | Tamu 2–3 LDK hari-H: butuh dokumentasi dan materi atau PIC FGD | **T1: DG** [D] | Tim dokumentasi, batas request, publikasi hasil |
| | | | **T2: KI** [B] | Materi paparan inovasi dakwah dan PIC FGD |

---

## 7. Skenario Tiga Inject

Inject dijalankan oleh **Pengendali Waktu / Master Inject** pada menit game yang ditentukan. Pengumuman dilakukan dengan suara jelas dan ditulis pada papan agar bisa dirujuk.

### 7.1 Inject A, Menit ke-15: "Kapasitas Media Turun"

| Unsur | Isi |
|---|---|
| **Trigger** | Master Inject mengumumkan: "Dua staf Digipro dan satu staf Medsist mendadak berhalangan." |
| **Efek mekanik** | **DG turun dari 4 menjadi 3 order** desain atau dokumentasi. **MS turun dari 4 menjadi 3 slot** posting untuk biro lain. Berlaku sampai akhir sesi |
| **Yang terdampak** | Pengirim ke DG: UM (2 order), RL (2 order). Pengirim ke MS: PM (2 slot), AM (1–2 slot), DG (hand-off) |
| **Yang diuji** | Prioritisasi, penolakan beradab, eskalasi ke Kadep Medigi |
| **Perilaku ideal** | Kabiro DG dan MS memutuskan prioritas berdasarkan urgensi dan dampak (poster untuk sesi yang sudah terjadwal dan donasi kemanusiaan mendahului katalog atau promosi rutin), menjelaskan alasan kepada biro yang tertolak, dan melaporkan penolakan ke Kadep Medigi |
| **Perilaku bermasalah** | Menolak tanpa penjelasan, membagi rata tanpa dasar, melobi biro pengirim di luar jalur |
| **Peran fasilitator** | Kadep Media menunggu eskalasi. Bila dua biro lintas dept berebut slot dan buntu, Kadep Media memutuskan |

### 7.2 Inject B, Menit ke-25: "Instruksi Ganda"

| Unsur | Isi |
|---|---|
| **Trigger** | Fasilitator berperan sebagai **Waket** (Waket I untuk ME, PM, KI, AM; Waket III untuk DG, MS, RL, UM) mendatangi **satu Staf Muda** di biro sasaran dan memberi arahan lisan yang bertentangan dengan keputusan Kabiro atau aturan |
| **Biro sasaran** | Dipilih fasilitator. Rekomendasi: UM atau PM (lihat 7.2.1) |
| **Yang diuji** | Staf Muda tidak mengeksekusi langsung, melapor ke Kabiro, Kabiro mengonfirmasi ke Kadep |
| **Perilaku ideal** | Staf Muda berkata sopan: "Siap, saya sampaikan ke Kabiro dahulu agar dikonfirmasi lewat Kadep." Kabiro mencatat di Blok B dan melapor ke Kadep |
| **Perilaku bermasalah** | Langsung mengeksekusi, mengabaikan Waket, atau membahas di luar jalur |

#### 7.2.1 Pilihan Naskah Instruksi

| Biro | Naskah lisan "Waket" | Mengapa bermasalah |
|---|---|---|
| UM | "Gratiskan saja sewa alat untuk panitia Maulid, tidak usah pakai deposit dan denda." | Sewa gratis dan pembebasan deposit atau denda di luar kewenangan, harus lewat Kadep RnA |
| PM | "Pakai saja rekening koordinator relawan supaya donasi cepat masuk." | Rekening resmi dikelola Bendum |
| ME | "Majukan Hari Puncak seminggu." | Perubahan tanggal HP butuh Kadep → Waket → BPI |
| AM | "Hentikan Q-TIME pekan ini supaya aula dipakai kegiatan lain." | Mengubah komitmen rutin AM, perlu persetujuan Kadep Pelayanan |

### 7.3 Inject C, Menit ke-35: "Kabiro Berhalangan"

| Unsur | Isi |
|---|---|
| **Trigger** | Fasilitator menyerahkan kartu "Kabiro sakit mendadak" kepada Kabiro biro sasaran. Kabiro meninggalkan meja selama **10 menit** (sampai menit ke-45). Staf Ahli **tidak otomatis** memegang wewenang |
| **Biro sasaran** | Dipilih fasilitator, bukan biro yang sama dengan inject B. Rekomendasi: **RL** atau **MS** (simpul padat sehingga dampaknya terasa luas) |
| **Yang diuji** | Delegasi, eskalasi ke Kadep untuk penunjukan Plt, kontinuitas |
| **Perilaku ideal** | Staf Ahli menyampaikan ke Kadep, Kadep menunjuk Plt Kabiro secara tertulis (Blok B), keputusan kritis ditunda atau dibuat berdasarkan batas yang disetujui. Setelah Kabiro kembali, ia meninjau keputusan |
| **Perilaku bermasalah** | Staf Ahli memutuskan sendiri, tim berhenti total, atau tiket yang sudah disepakati diubah tanpa sepengetahuan Kabiro |

---

## 8. Struktur Google Sheets

**File:** `main/template_simulasi_taktis.xlsx` (12 tab, 406 formula). Unggah ke Google Drive dan buka dengan Google Sheets, lalu pilih *File → Simpan sebagai Google Sheets*.

### 8.1 Daftar Tab

| Tab | Isi | Pengisi |
|---|---|---|
| `00_PETUNJUK` | Gambaran umum, aturan, alur, inject, peran, SOP eskalasi, peta Kadep, kode biro, cara pakai | Dibaca peserta |
| `ALLOWED_EDGES` | 16 relasi resmi dengan jenis lintas, esensi, dan Kadep yang diinfokan. Kolom E berisi kunci `PENGUSUNG\|TUJUAN` untuk formula | Fasilitator |
| `BIRO_ME`, `BIRO_PM`, `BIRO_KI`, `BIRO_UM`, `BIRO_AM`, `BIRO_DG`, `BIRO_MS`, `BIRO_RL` | Lembar kendali tiap biro (Blok A–E) | Tim biro |
| `PAPAN_JARING` | Matriks 8×8 status 16 relasi, rekap, dan papan eskalasi serta keputusan | Otomatis |
| `SKOR_EVALUASI` | Rubrik dan rekap nilai | Otomatis dan fasilitator |

### 8.2 Tata Letak Tab Biro

| Blok | Baris | Isi |
|---|---|---|
| Banner dan petunjuk | 1–2 | Judul biro (warna departemen) |
| **A. Identitas, Proker Amanah, Susunan Tim** | 4–11 | Kode, nama, departemen, bidang, proker, **2 target terkunci**; nama Kabiro, Staf Ahli, 3 Staf Muda; Kadep dan Waket |
| **B. Log Laporan dan Eskalasi ke Kadep** | 13–22 (data 15–22) | No, Menit ke-, Jenis, Urgensi, Jalur sudah dicoba?, Topik, Fakta, Opsi, Permintaan Arahan, Respon Kadep/Fasilitator, Tindak Lanjut, Status Respon |
| **C. Log Koordinasi Keluar** | 24–35 (data 26–35) | ID Tiket, Menit ke-, Biro Tujuan, Jenis Lintas (otomatis), Kadep diinfokan?, Kebutuhan, Tawaran, Hasil Kesepakatan, Syarat, Status, Perlu Eskalasi?, Flag Arah (otomatis) |
| **D. Log Koordinasi Masuk** | 37–48 (data 39–48) | ID Tiket, Menit ke-, Biro Pengirim, Respons, Kadep diinfokan?, Isi Permintaan, Dampak Internal, Keputusan Kabiro, Syarat Balik, Alasan atau Dasar SOP, Sudah dibalas?, Cek Jalur Pengirim (otomatis) |
| **E. Keputusan Final Eksekusi** | 50–61 | Status keputusan (Go / Go Bersyarat / Tunda), Scope final, Komitmen keluar (otomatis), Komitmen masuk (otomatis), Risiko tersisa, Mitigasi, Jobdesc Kabiro, Staf Ahli, Staf Muda, Persetujuan Kadep (Ya / Belum / Revisi), Refleksi |

Kode warna: sel kuning = diisi peserta; sel abu-abu = otomatis atau terkunci secara konvensi. Header berwarna menurut departemen (Syi'ar jingga, Pelayanan hijau, Medigi biru, RnA ungu).

### 8.3 Formula Kunci

| Fungsi | Formula (contoh baris 26 tab BIRO_ME) |
|---|---|
| Jenis lintas otomatis | `=IF(C26="","",IFERROR(INDEX(ALLOWED_EDGES!$C$6:$C$21,MATCH($C$5&"\|"&C26,ALLOWED_EDGES!$E$6:$E$21,0)),"—"))` |
| Flag arah (Blok C) | `=IF(C26="","",IF(COUNTIF(ALLOWED_EDGES!$E$6:$E$21,C26&"\|"&$C$5)>0,"⛔ ARAH BALIK — dilarang",IF(COUNTIF(ALLOWED_EDGES!$E$6:$E$21,$C$5&"\|"&C26)=0,"⛔ DI LUAR JALUR — eskalasi ke Kadep","✔ sesuai jalur")))` |
| Cek jalur pengirim (Blok D) | `=IF(C39="","",IF(COUNTIF(ALLOWED_EDGES!$E$6:$E$21,C39&"\|"&$C$5)>0,"✔ pengirim di jalur resmi","⚠ pengirim di luar jalur — catat & lapor Kadep"))` |
| Status relasi (`PAPAN_JARING`) | `=IF(COUNTIFS('BIRO_ME'!$C$26:$C$35,"RL",'BIRO_ME'!$J$26:$J$35,"Sepakat")>0,"Deal",IF(COUNTIFS(…,"Ditolak")>0,"Reject",IF(COUNTIFS(…,"Batal")>0,"Batal","Pending")))` |
| Skor jalur otomatis | `=MAX(0,100-25*C13)` dengan `C13 = COUNTIF('BIRO_ME'!$L$26:$L$35,"⛔*")` |
| Total skor | `=ROUND(G13*0.3+N(H13)*0.3+N(I13)*0.15+N(J13)*0.15+N(K13)*0.1,1)` |

**Validasi data:** dropdown pada Jenis (Briefing / Minta Arahan / Eskalasi / Laporan), Urgensi, Jalur dicoba, Status Respon; pada Biro Tujuan (hanya 2 target); pada Respons masuk (Terima / Terima Bersyarat / Tolak / Tunda); pada Status tiket (Pending / Negosiasi / Sepakat / Ditolak / Batal); dan pada Status Keputusan dan Persetujuan Kadep. Skor evaluasi dibatasi angka 0–100.

**Format bersyarat:** flag arah merah/kuning/hijau; status tiket (Sepakat hijau, Ditolak merah, Negosiasi kuning, Batal abu); Papan Jaring (Deal hijau, Reject merah, Pending kuning, Batal abu).

### 8.4 Pengaturan Google Sheets Sebelum Hari-H

1. Unggah dan konversi file ke Google Sheets.
2. Atur **Protected range** manual: tiap tab `BIRO_xx` hanya untuk tim tersebut; kolom *Respon Kadep/Fasilitator* (Blok B) hanya fasilitator; `ALLOWED_EDGES`, `PAPAN_JARING`, `SKOR_EVALUASI` hanya fasilitator. Proteksi lembar dari berkas xlsx tidak terbawa ke Google Sheets.
3. Buat salinan cadangan di Drive dan simpan tautan tab per biro dalam QR agar tiap tim langsung membuka tab yang benar.
4. Uji dengan 8 akun uji coba secara bersamaan.
5. Hapus data uji sebelum hari-H.

---

## 9. Rubrik Penilaian

Bobot: Ketepatan Jalur **30%**, Kualitas Kesepakatan **30%**, Ketepatan Eskalasi **15%**, Keputusan Final **15%**, Adab/SOP **10%**.

| Kriteria | Skor 100 | Skor 70 | Skor 40 | Skor 0 | Sumber data |
|---|---|---|---|---|---|
| **1. Ketepatan Jalur (30%)** | Tanpa pelanggaran arah atau jalur | — | — | — | **Otomatis:** 100 − 25 × pelanggaran, minimum 0 |
| **2. Kualitas Kesepakatan (30%)** | Konkret (volume, waktu, PIC, syarat), seimbang, bisa dieksekusi di **kedua** target | Ada, tetapi satu unsur samar | Umum atau sepihak | Tidak ada kesepakatan | Penilai membaca Blok C dan Papan Jaring |
| **3. Ketepatan Eskalasi (15%)** | Tepat topik dan waktu, format fakta–opsi–permintaan jelas | Tepat tetapi format kurang | Terlambat atau tidak perlu | Tidak mengeskalasi padahal wajib atau memutuskan di luar wewenang | Blok B dan respon Kadep |
| **4. Keputusan Final (15%)** | Konsisten dengan hasil tiket, risiko dan mitigasi realistis, jobdesc jelas | Ada satu bagian lemah | Tidak konsisten | Kosong | Blok E dan persetujuan Kadep |
| **5. Adab/SOP (10%)** | Santun, patuh peran (Kabiro memutuskan, Staf Ahli mempertimbangkan), SOP media dan eksternal dipatuhi, catatan rapi | Satu pelanggaran ringan | Beberapa pelanggaran | Pelanggaran berat | Pengamatan penilai P2–P3 |

**Predikat:** ≥ 85 Tangguh · 70–84 Cakap · 55–69 Berkembang · < 55 Perlu pendalaman.

**Catatan penting:** skor bukan alat peringkat sosial peserta. Skor dipakai untuk debrief dan untuk bukti TUK (K6, K7, K8). Skor tim tidak dikaitkan dengan penilaian individu dalam seleksi peran.

---

## 10. Panduan Fasilitator dan Game Master

### 10.1 Persiapan (H-7 sampai H-1)

| Waktu | Tugas | PIC |
|---|---|---|
| H-13 s.d. H-9 (2–6 November) | **Validasi kasus dan angka** dengan Kabiro terkait (status proker OKR sekarang, kapasitas, tenggat). Kartu direvisi bila perlu | Sie Simulasi, Ketupel |
| H-7 (8 November) | Final daftar tim, peran, dan kode peserta; uji `template_simulasi_taktis.xlsx` dengan 8 akun | Sie Simulasi |
| H-5 (10 November) | Cetak 8 set Kartu Rahasia (+2 cadangan) **setelah validasi selesai**, masukkan ke amplop tersegel bertanda kode biro | Sie Perlengkapan |
| H-4 (11 November) | **Technical meeting fasilitator:** latihan peran Kadep, Waket, Bendum; latihan inject; pembagian penilai | Sie Simulasi |
| H-1 (14 November) | Siapkan tata letak klaster, proyektor Papan Jaring, penghitung waktu, hotspot cadangan | Sie Perlengkapan |

### 10.2 Skrip Peran Kadep

Kadep adalah pemegang peran paling menentukan. Pedomannya:

1. **Terima eskalasi** dalam format *fakta → opsi → permintaan arahan*. Bila belum lengkap, kembalikan dengan pertanyaan pemandu ("Apa opsi lain?", "Apa dampaknya bagi biro lain?").
2. **Jangan menyelesaikan masalah.** Berikan arahan atau persetujuan, bukan solusi lengkap. Kadep tidak mengambil alih kewenangan operasional biro.
3. **Respons maksimal 5 menit.** Catat respons di kolom *Respon Kadep/Fasilitator*, bukan hanya lisan.
4. **Lintas dept:** bila masalah melibatkan dept lain, hubungi Kadep dept tersebut atau eskalasikan ke Waket (peran fasilitator lain).
5. **Persetujuan P3:** periksa konsistensi Blok E dengan Blok C dan D; minta revisi bila keputusan tidak sejalan dengan tiket.
6. **Hak tolak:** Kadep boleh menolak komitmen di luar RAB atau kapasitas, dengan alasan tertulis.

**Contoh respons:**
- "Opsi 1 dan 2 masuk akal. Saya setuju opsi 2, tetapi tolong informasikan ke Kadep RnA karena melibatkan departemen lain."
- "Belum cukup. Fakta Anda belum menyebut tenggat vendor. Lengkapi dan kembali."
- "Ini wilayah BPI. Saya eskalasikan ke Waket. Sementara, tahan komitmen tertulis."

### 10.3 Skrip Peran Waket / BPI / Bendum

- **Waket:** menerima eskalasi lintas dept dalam satu bidang. Memberi keputusan taktis. Untuk inject B, mendatangi Staf Muda dengan naskah (lihat 7.2.1).
- **BPI:** menerima eskalasi kebijakan atau lintas bidang. Cenderung menanyakan dasar Tata Kelola dan dampak organisasi.
- **Bendum:** menjawab pertanyaan kanal donasi serta deposit, denda, dan penerimaan uang sewa. Jawaban baku: rekening resmi dikelola Bendum; kanal donasi harus disetujui sebelum disebar; pemasukan sewa, deposit, dan denda dicatat melalui mekanisme administrasi keuangan, bukan dipegang biro secara pribadi.
- **Sekum (bila ada):** menjawab pertanyaan surat resmi, batas H-3, dan asistensi.

### 10.4 Skrip Pengendali Waktu dan Master Inject

| Menit | Aksi |
|---|---|
| 0 | Umumkan "P1 dimulai" |
| 10 | Umumkan "P2 dimulai, buka tiket" |
| 15 | **Inject A** |
| 25 | **Inject B** (fasilitator Waket bergerak) |
| 35 | **Inject C** (kartu Kabiro sakit) |
| 45 | Kabiro sasaran inject C kembali |
| 48 | Peringatan 2 menit sebelum P3 |
| 50 | "P3 dimulai, kabiro lapor ke Kadep" |
| 68 | Peringatan 2 menit sebelum P4 |
| 70 | "P4 dimulai, papan jaring" |
| 80 | Penutupan, Papan Jaring difoto |

### 10.5 Titik Temu Kesepakatan (ZOPA) per Tiket

Bukan jawaban tunggal. Dipakai untuk menilai kualitas kesepakatan (rubrik 2).

| Tiket | Titik temu realistis | Jebakan dan catatan |
|---|---|---|
| ME>RL | PMI dan pemateri **dari jaringan alumni** (tanpa slot); sponsor funrun dilepas atau ditunda; PIC tunggal adalah Staf Ahli RL | Slot RL 4 vs permintaan masuk 7. Tanpa prioritisasi Kadep RnA semua tiket RL macet |
| ME>UM | **Paket 4 hari (H-2 s.d. H+1)**: 8 HT, 2 sound portable, 3 frame backdrop, 1 proyektor. **Jalur A:** tanpa kabel roll (ME memakai milik sendiri atau meminjam inventaris sekretariat lewat Sekum, SOP 6.3), tarif internal 30% dan hari ke-3 dan ke-4 50% = **Rp 987.000**. **Jalur B:** paket penuh dengan kabel roll, diskon 35% (di atas wewenang UM, butuh Kadep RnA) = **Rp 975.000**. Klausul: deposit 20–25% saat pengambilan, denda terlambat 25% tarif harian per hari, ganti rugi hanya untuk kelalaian (keausan wajar dikecualikan), berita acara serah terima dengan foto dan uji fungsi | HT hanya 8 unit pada H-1 s.d. HP (ME meminta 12). Paket penuh 4 hari dengan diskon 30% = Rp 1.050.000 dan 5 hari = Rp 1.225.000, keduanya melampaui anggaran Rp 1.000.000. SOP 6.3 tidak mengatur tarif atau denda, sehingga klausul wajib dicatat dan dilaporkan ke Kadep RnA |
| PM>MS | 2 slot: 1 kilat ≤ 24 jam (persetujuan Kadep Media) dan 1 laporan transparansi; kanal sudah disetujui Bendum | Kanal belum disetujui Bendum, sehingga MS wajib menolak |
| PM>RL | **Mitra C** (sudah ada, tanpa slot, verifikasi 1 hari) sebagai penyalur pertama; B opsional; A ditunda | Mitra A (4 hari) terlalu lambat. Kadep RnA dan Waket III diinfokan |
| KI>PM | **2 relawan cadangan hanya Rabu–Kamis**, setelah 2 sesi pelatihan (H-17, H-14) | PM butuh cadangan itu untuk packing Senin–Selasa |
| KI>AM | **Senin 1 kelas, Rabu 2 kelas, Kamis 1 kelas**, 15.30–16.55 (85 menit) | Selasa tidak tersedia. Hari ini harus cocok dengan hari PM (Rabu–Kamis) |
| UM>KI | Segmentasi: Academy konsep dasar (mahasiswa baru); Minion Class latihan soal intensif **di luar** Senin–Kamis 15.30–17.00; promosi tidak saling menjatuhkan | KI tidak boleh diminta membatalkan kelas |
| UM>DG | Prioritas 1 **poster Minion Class ≤ H-14** (batas yang dijamin SOP 6.4.3 bila diajukan H-21); prioritas 2 **poster atau katalog paket GoRent ≤ H-12** | Permintaan ≤ H-16 tidak dijamin SOP. Bila inject A: DG mengorbankan katalog GoRent atau dokumentasi RL |
| AM>UM | **8 sesi 400 porsi**: UM 40 per hari @ **Rp 10.450** + 10 per hari tenant @ **Rp 11.000** (komit ≥ 80) → rata-rata **Rp 10.560 ≤ plafon Rp 10.625** | UM maksimal 40 per hari; tanpa porsi tenant rata-rata < 50 |
| AM>MS | **1 slot bundling** (carousel atau reels) bulanan; jadwal puasa lewat kanal WA atau Calendar (tidak memakai slot) | Slot MS sangat terbatas, bundling adalah kunci |
| DG>MS | File final **Kamis 16.00**; bundling 4 aset per carousel; ≥ 2 slot per minggu; DG menyediakan caption draft | MS tanpa piket akhir pekan; DG mengincar Jumat 20.00 |
| DG>AM | Live Q-TIME **Rabu dan Kamis, 1 kamera**, tripod di belakang saf; izin pelantun; GDM amankan jalur | Tripod di depan saf dilarang |
| MS>RL | 1 narasumber akademisi via **alumni** (tanpa slot) dan 1 praktisi via slot eksternal; Medpar bila slot tersisa | Berebut slot dengan ME dan PM |
| MS>ME | NARASI di **Ruang Audiovisual H-2 (60 orang)** atau **Aula H-4 (80 orang)**; 4 panitia cadangan, 1 hari | Aula terkunci mulai H-3 pukul 12.00, sehingga rencana awal H-2 di Aula mustahil |
| RL>DG | Foto (1 orang, Sabtu) dan klip 60 detik dari bahan RL; desain undangan sebagai order; video recap dikerjakan Senin | DG akhir pekan hanya 1 orang, tanpa video panjang |
| RL>KI | Moderator (Staf Muda KI yang bebas Sabtu) dan materi 15 menit memakai template RL; materi disetujui Kadep Pelayanan paling lambat H-10 | Eskalasi ke Kadep Pelayanan wajib |

**Pemeriksaan matematis kasus AM>UM:** UM 40 porsi × 8 sesi = 320 porsi × Rp 10.450 = Rp 3.344.000; tenant 10 porsi × 8 sesi = 80 porsi × Rp 11.000 = Rp 880.000; total Rp 4.224.000 untuk 400 porsi atau rata-rata Rp 10.560, di bawah plafon AM Rp 10.625. Keuntungan UM dari porsi sendiri: 320 × (Rp 10.450 − Rp 8.000) = Rp 784.000, melampaui target Rp 150.000.

### 10.6 Pemecahan Masalah Saat Berjalan

| Masalah | Penanganan |
|---|---|
| Tim tidak bergerak di P2 | Penilai mendatangi tim dan bertanya "Siapa target pertama Anda?" tanpa memberi jawaban |
| Dua tim saling memaksa | Kadep memanggil keduanya dan mengingatkan wewenang Kadep dan jalur eskalasi |
| Tim menghubungi biro di luar daftar | Tegur lembut, arahkan eskalasi ke Kadep. Flag arah otomatis mencatat |
| Wi-Fi bermasalah | Aktifkan hotspot cadangan. Bila gagal, tulis tiket pada kertas dan operator memasukkan sesudahnya |
| Google Sheets lambat | Minta tim mengisi hanya Blok C dan D selama P2, Blok B dan E pada P3 |
| Peserta bingung peran | Fasilitator menunjuk Kartu Rahasia dan tabel peran |
| Inject membuat tim panik | Master Inject mengingatkan bahwa kekacauan adalah bagian dari pembelajaran |

### 10.7 Alur Debrief (15 menit, 15.10–15.25)

| Menit | Kegiatan | Pembawa |
|---|---|---|
| 0–2 | Tampilkan `PAPAN_JARING` dan rekap (Deal, Reject, Batal, Pending) | Operator |
| 2–7 | Tiga pertanyaan debrief (di bawah). Beri kesempatan 3–4 tim bicara | Fasilitator utama |
| 7–12 | Kaitkan temuan dengan pasal: Ketua Badan Keorg dan Waket III menyoroti dua atau tiga pelanggaran atau praktik baik tanpa menyebut nama | Ketua Keorg, Waket III |
| 12–15 | Penutup: tiga pelajaran utama dan jembatan ke M4 | Fasilitator utama |

**Tiga pertanyaan debrief:**
1. Tiket mana yang paling alot dan mengapa? Apa yang akhirnya membuka kebuntuan?
2. Kapan kalian memilih eskalasi dan kapan menyelesaikan sendiri? Apa dasarnya di Tata Kelola?
3. Siapa yang menanggung dampak keputusan kalian di biro lain, dan apakah kalian mengetahuinya?

**Kalimat jembatan ke M4:** "Tadi kalian merasakan betapa beratnya memikul amanah di tengah keterbatasan. Setelah ini kita bicara tentang mengapa orang tetap mau memikulnya."

### 10.8 Temuan untuk Badan Keorganisasian

Penilai mencatat **titik ambigu Tata Kelola** yang muncul saat simulasi (misalnya kapan "diketahui" cukup, atau siapa Sekretaris Pelaksana biro). Catatan ini diserahkan ke Badan Keorganisasian sebagai masukan revisi Tata Kelola. Dengan begitu simulasi menghasilkan dua manfaat: pelatihan peserta dan evaluasi dokumen.

---

## 11. Kontrol Kualitas

| Pemeriksaan | Metode | Hasil terakhir |
|---|---|---|
| Graf: 16 relasi, out-degree 2, tanpa pasangan timbal-balik, terhubung kuat | Skrip Python (assert pada `generate_template_simulasi.py`) | Lulus |
| Target kartu sama dengan `ALLOWED_EDGES` | Skrip pembanding | 8 dari 8 sama |
| Formula (jenis lintas, flag arah, status Papan Jaring, skor) | Dihitung dengan pustaka `formulas` pada data uji | Sesuai dugaan: 2 Deal, 1 Reject, 13 Pending dari 16 relasi; skor jalur 75 untuk satu pelanggaran |
| Tampilan di Excel dan Google Sheets | **Belum diuji** | Perlu pemeriksaan visual setelah unggah |

**Regenerasi file:** `python main/generate_template_simulasi.py`. Sumber kebenaran graf adalah daftar `EDGES` di skrip. Bila relasi diubah, perbarui `kartu_skenario_simulasi.md` dan dokumen ini.

---

## 12. Asumsi dan Keterbatasan

1. Angka bertanda (sim) adalah fiktif dan belum divalidasi Kabiro terkait. Validasi dilakukan pada 2–6 November (H-13 s.d. H-9), sebelum kartu dicetak pada 10 November.
2. Seluruh deck berasal dari **OKR 1 (Musyker 4 April 2026)**. Proker OKR 2 dan 3 mungkin berbeda.
3. Tim yang dibentuk acak lintas biro adalah usulan dan perlu disetujui.
4. Jumlah fasilitator ±12–14 belum dikonfirmasi ketersediaannya.
5. Proteksi sel tidak terbawa ke Google Sheets, sehingga perlu diatur manual.
6. Kapasitas Aula atau Ruang Audiovisual untuk 8 klaster belum terverifikasi (lihat dokumen 01, butir 4.3).
