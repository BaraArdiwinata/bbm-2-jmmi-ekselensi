"""Generate main/template_simulasi_taktis.xlsx: Ultra-Lean Template Simulasi Taktis BBM 2 (30 menit, topologi 2 keluar 2 masuk).

Jalankan:  python main/generate_template_simulasi.py
Sumber kebenaran graf = TIKET di bawah; kartu_skenario_simulasi.md dan blueprint 03 harus selaras dengan tabel ini.
Tab: 00_PETUNJUK, 8 tab biro (4 baris kerja), PAPAN_JARING (otomatis), SKOR_EVALUASI.
"""
from pathlib import Path

from openpyxl import Workbook
from openpyxl.formatting.rule import FormulaRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.worksheet.properties import PageSetupProperties

OUT = Path(__file__).with_name("template_simulasi_taktis.xlsx")

# ---------------------------------------------------------------- data
DEPT = {  # dept -> (warna, kadep, bidang, waket)
    "Syi'ar": ("C46A12", "Kadep Syi'ar", "Bidang 1", "Waket I"),
    "Pelayanan Masjid & Dakwah": ("1E7B5A", "Kadep Pelayanan Masjid & Dakwah", "Bidang 1", "Waket I"),
    "Media, Informasi & Digitalisasi": ("2E6FBA", "Kadep Media, Informasi & Digitalisasi", "Bidang 3", "Waket III"),
    "Relasi Publik & Advokasi": ("6B4FA0", "Kadep Relasi Publik & Advokasi", "Bidang 3", "Waket III"),
}
BIRO = {  # kode internal -> (nama = judul tab, dept)
    "E": ("Manajemen Event", "Syi'ar"),
    "P": ("Pengabdian Masyarakat", "Syi'ar"),
    "K": ("Kajian & Inovasi Dakwah", "Pelayanan Masjid & Dakwah"),
    "U": ("Usaha Mandiri", "Relasi Publik & Advokasi"),
    "A": ("Amaliyah Yaumiyah", "Pelayanan Masjid & Dakwah"),
    "D": ("Digital Production", "Media, Informasi & Digitalisasi"),
    "M": ("Media Analysis & Strategi", "Media, Informasi & Digitalisasi"),
    "R": ("Relasi & Hubungan Eksternal", "Relasi Publik & Advokasi"),
}
ORDER = list(BIRO)
NAME = {k: v[0] for k, v in BIRO.items()}

# (id, pengusung, tujuan, kebutuhan kita [tabel keluar], permintaan mereka [tabel masuk])
TIKET = [
    ("R-01", "E", "R", "Butuh 2 Medpar dan 1 surat undangan resmi LDK se-Surabaya untuk Maulid × Milad, tapi pihak luar harus lewat Relasi.",
     "Manajemen Event minta Medpar eksternal dan undangan resmi LDK se-Surabaya untuk Maulid × Milad."),
    ("R-02", "E", "U", "Butuh pinjam alat GoRent (HT, kabel roll, proyektor, standing banner) H-2 sampai H+1, gratis Rp0, dengan jaminan perawatan.",
     "Manajemen Event minta pinjam inventaris GoRent internal (gratis Rp0) beserta jaminan perawatan."),
    ("R-03", "P", "D", "Butuh poster darurat open donasi banjir JMMI Peduli jadi paling lama 24 jam, plus template poster transparansi.",
     "Pengabdian Masyarakat minta poster darurat open donasi banjir ≤ 24 jam dan template transparansi."),
    ("R-04", "P", "R", "Butuh fiksasi 1 mitra penyalur bantuan banjir yang cepat terverifikasi sebelum donasi dibuka.",
     "Pengabdian Masyarakat minta fiksasi 1 mitra penyalur bantuan banjir yang terverifikasi di lokasi."),
    ("R-05", "K", "U", "Butuh paket sarapan SaJi (Sarapan & Ngaji) 50–75 porsi per sesi lewat JMMI Commerce dengan harga nego mahasiswa.",
     "Kajian & Inovasi Dakwah minta paket sarapan SaJi 50–75 porsi lewat JMMI Commerce dengan harga nego mahasiswa."),
    ("R-06", "K", "A", "Menawarkan kader da'i dan silabus kultum 10 menit untuk buka puasa KSSI dan penutupan OWOJ.",
     "Kajian & Inovasi Dakwah menawarkan penugasan da'i dan silabus kultum 10 menit untuk KSSI dan OWOJ."),
    ("R-07", "U", "E", "Butuh izin lapak bazaar resmi untuk merchandise JMMI Store dan snack Commerce di venue Maulid.",
     "Usaha Mandiri minta izin buka lapak bazaar resmi (merchandise JMMI Store dan snack Commerce) di venue Maulid."),
    ("R-08", "U", "P", "Ajak kolaborasi merchandise amal totebag dan stiker relawan, dengan bagi hasil ke kas JMMI Peduli lewat Bendum.",
     "Usaha Mandiri ajak kolaborasi merchandise amal relawan, bagi hasil disalurkan ke kas JMMI Peduli via Bendum."),
    ("R-09", "A", "E", "Butuh protokol adab masjid untuk Hari Puncak: salat tepat waktu dikawal petugas GDM, makan peserta di luar karpet utama.",
     "Amaliyah Yaumiyah minta protokol adab masjid, petugas GDM, dan zonasi makan di luar karpet utama pada Hari Puncak."),
    ("R-10", "A", "M", "Butuh publikasi dokumentasi KSSI bulanan dan rilis infografis jadwal puasa sunnah di Instagram.",
     "Amaliyah Yaumiyah minta publikasi dokumentasi KSSI dan infografis jadwal puasa sunnah di Instagram."),
    ("R-11", "D", "M", "Mau serah-terima file final desain tiap Kamis 16.00 dengan jatah minimal 2 slot posting per minggu.",
     "Digital Production minta file final diterima tiap Kamis 16.00 dan jatah minimal 2 slot posting per minggu."),
    ("R-12", "D", "A", "Mau live streaming khatmil Qur'an OWOJ (STREAMMI) tanpa mengganggu jamaah dan siap sebelum Q-TIME.",
     "Digital Production minta izin STREAMMI live streaming khatmil Qur'an OWOJ sebelum waktu Q-TIME."),
    ("R-13", "M", "K", "Butuh telaah dan kurasi syar'i atas draf opini dan policy brief supaya dalil tidak keliru.",
     "Media Analysis & Strategi minta kurasi dalil dan sudut pandang syar'i atas draf opini dan policy brief."),
    ("R-14", "M", "P", "Butuh data riil desa mitra JMMI Mengabdi untuk menulis rilis berita media massa kampus.",
     "Media Analysis & Strategi minta data riil desa mitra JMMI Mengabdi untuk rilis media massa kampus."),
    ("R-15", "R", "D", "Butuh 1 fotografer dokumentasi dan desain e-invitation untuk Jaulah LDK di akhir pekan.",
     "Relasi & Hubungan Eksternal minta 1 fotografer dan desain e-invitation Jaulah LDK di akhir pekan."),
    ("R-16", "R", "K", "Mau merekomendasikan database narasumber alumni dan ustadz jejaring luar untuk pemateri kajian rutin KID.",
     "Relasi & Hubungan Eksternal merekomendasikan narasumber alumni dan ustadz jejaring luar untuk pemateri kajian."),
]
OUTGOING = {k: [t for t in TIKET if t[1] == k] for k in ORDER}
INCOMING = {k: [t for t in TIKET if t[2] == k] for k in ORDER}

# self-check graf: 16 tiket, tiap biro 2 keluar dan 2 masuk, tanpa loop diri
assert len(TIKET) == 16 and len({t[0] for t in TIKET}) == 16
assert all(len(OUTGOING[k]) == 2 and len(INCOMING[k]) == 2 for k in ORDER)
assert all(t[1] != t[2] for t in TIKET) and len({(t[1], t[2]) for t in TIKET}) == 16
assert max(len(n) for n in NAME.values()) <= 31  # batas judul tab Excel

# ---------------------------------------------------------------- style
THIN = Side(style="thin", color="9E9E9E")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
INPUT, LOCK = "FFF8DC", "ECEFF1"
STATUS_OUT = "Sepakat,Masih Negosiasi,Batal"
STATUS_IN = "Diterima,Diterima Bersyarat,Ditolak"
R_OUT = (8, 9)    # baris tabel 1 (keluar)
R_IN = (13, 14)   # baris tabel 2 (masuk)
R_ESK = (18, 19)  # baris tabel 3 (eskalasi)


def fill(c):
    return PatternFill("solid", start_color=c, end_color=c)


def tint(c, k=0.82):
    r, g, b = (int(c[i:i + 2], 16) for i in (0, 2, 4))
    return "".join(f"{int(v + (255 - v) * k):02X}" for v in (r, g, b))


def put(ws, ref, v, bold=False, color="000000", bg=None, size=11, h="left", italic=False, border=True):
    c = ws[ref]
    c.value = v
    c.font = Font(name="Calibri", size=size, bold=bold, italic=italic, color=color)
    c.alignment = Alignment(horizontal=h, vertical="center", wrap_text=True)
    if bg:
        c.fill = fill(bg)
    if border:
        c.border = BORDER
    return c


def mput(ws, rng, v, **kw):
    ws.merge_cells(rng)
    put(ws, rng.split(":")[0], v, **kw)
    for row in ws[rng]:
        for c in row:
            if kw.get("border", True):
                c.border = BORDER
            if kw.get("bg"):
                c.fill = fill(kw["bg"])


def page(ws, color):
    ws.sheet_properties.tabColor = color
    ws.page_setup.orientation = "landscape"
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    ws.sheet_properties.pageSetUpPr = PageSetupProperties(fitToPage=True)
    ws.sheet_view.showGridLines = False


def widths(ws, d):
    for col, w in d.items():
        ws.column_dimensions[col].width = w


def q(name):  # nama tab untuk rujukan formula
    return "'" + name.replace("'", "''") + "'"


# ---------------------------------------------------------------- 00_PETUNJUK
def sheet_petunjuk(wb):
    ws = wb.active
    ws.title = "00_PETUNJUK"
    page(ws, "424242")
    widths(ws, {"A": 26, "B": 90})
    mput(ws, "A1:B1", "SIMULASI TAKTIS BBM 2 · Petunjuk 1 Halaman", bold=True, size=16, color="FFFFFF", bg="263238", border=False)
    ws.row_dimensions[1].height = 30
    rows = [
        ("Tujuan latihan", "Melatih komunikasi langsung antarbiro dan eskalasi yang tepat. Fokusnya bergerak dan tatap muka dengan meja lain, bukan mengisi borang. Kartu Rahasia berisi modal dan batasan mejamu."),
        ("Jadwal 30 menit", "P1 Persiapan 4' (baca kartu, tentukan tiket yang dibuka lebih dulu) · P2 Gerak aktif 17' (negosiasi, inject di menit 8, 12, 16) · P3 Fiksasi 4' (rapikan hasil, lapor Kadep) · P4 Penutup 5' (papan jaring ditampilkan, tiap biro menyebut satu deal terbaik dan satu kompromi tersulit)."),
        ("Cara mengisi", "Tab biromu hanya punya 3 tabel kecil. Isi **sel kuning** saja: (1) Hasil Kesepakatan dan Status untuk 2 misi keluar, (2) Respon dan Status untuk 2 tamu yang datang, (3) Catatan Kebuntuan bila macet total. Tulis poin konkret: jumlah, kuota, harga, tenggat, PIC."),
        ("Arah koordinasi", "Kamu memulai 2 tiket keluar dan menerima 2 tiket masuk (tertulis di tabel). Butuh sesuatu di luar itu? Naikkan ke Kadep. Tiket yang diterima dijawab di tiket yang sama."),
        ("Status", "Keluar: Sepakat / Masih Negosiasi / Batal. Masuk: Diterima / Diterima Bersyarat / Ditolak. Papan jaring panitia membaca status tabel keluar."),
        ("Tata krama antarmeja", "Datangi meja tujuan secara langsung dan sopan. Dengarkan kebutuhan mereka dulu. Tawar dengan modalmu, jangan mengancam atau melampaui batas wewenang. Tolak dengan alasan dan tawarkan alternatif. Catat apa yang disepakati sebelum berpisah."),
        ("Eskalasi ke Kadep", "Pakai tabel 3 hanya jika koordinasi macet total atau di luar wewenang mejamu. Ceritakan fakta singkat: apa yang buntu, opsi yang sudah dicoba, dan arahan yang kamu minta. Kadep menjawab maksimal 3 menit."),
        ("Pengamat", "Satu pengamat Badan Personalia berkeliling mencatat pola kontribusi untuk pembinaan, bukan nilai lulus atau gagal. Tidak ada jabatan yang ditunjuk; semua setara."),
    ]
    r = 3
    for k, v in rows:
        put(ws, f"A{r}", k, bold=True, bg="CFD8DC")
        put(ws, f"B{r}", v)
        ws.row_dimensions[r].height = max(34, 17 * (len(v) // 88 + 1))
        r += 1
    mput(ws, f"A{r + 1}:B{r + 1}", "Rahasia: kartu skenario hanya dibaca mejamu sendiri. Hapus data uji sebelum hari-H.", italic=True, border=False)


# ---------------------------------------------------------------- tab biro
def sheet_biro(wb, k):
    nama, dept = BIRO[k]
    color, kadep, bidang, waket = DEPT[dept]
    ws = wb.create_sheet(nama)
    page(ws, color)
    widths(ws, {"A": 11, "B": 26, "C": 52, "D": 52, "E": 20})
    mput(ws, "A1:E1", f"Biro {nama}", bold=True, size=16, color="FFFFFF", bg=color, border=False)
    ws.row_dimensions[1].height = 30
    mput(ws, "A2:E2", f"Departemen {dept} · {bidang} · {kadep} → {waket}", bg=tint(color), bold=True)
    put(ws, "A3", "Anggota meja", bold=True, bg=tint(color))
    mput(ws, "B3:E3", "", bg=INPUT)
    mput(ws, "A4:E4", "Fokus negosiasi langsung antarmeja. Cukup isi sel kuning pada tabel di bawah.", italic=True, border=False)

    def header(row, title, cols):
        mput(ws, f"A{row - 1}:E{row - 1}", title, bold=True, color="FFFFFF", bg=color)
        for col, text in zip("ABCDE", cols):
            put(ws, f"{col}{row}", text, bold=True, bg=tint(color, 0.6), h="center")

    header(7, "TABEL 1 · MISI KOORDINASI KELUAR (2 tiket yang kita mulai)",
           ["ID Tiket", "Biro Tujuan", "Kebutuhan / Kasus Kita", "Hasil Kesepakatan / Deal", "Status"])
    for row, t in zip(range(R_OUT[0], R_OUT[1] + 1), OUTGOING[k]):
        put(ws, f"A{row}", t[0], bold=True, bg=LOCK, h="center")
        put(ws, f"B{row}", "Biro " + NAME[t[2]], bg=LOCK)
        put(ws, f"C{row}", t[3], bg=LOCK)
        put(ws, f"D{row}", None, bg=INPUT)
        put(ws, f"E{row}", "Masih Negosiasi", bg=INPUT, h="center")
        ws.row_dimensions[row].height = 64
    header(12, "TABEL 2 · KOORDINASI MASUK (2 tamu di meja kita)",
           ["ID Tiket", "Biro Pengirim", "Permintaan Mereka", "Respon & Syarat Balik Kita", "Status"])
    for row, t in zip(range(R_IN[0], R_IN[1] + 1), INCOMING[k]):
        put(ws, f"A{row}", t[0], bold=True, bg=LOCK, h="center")
        put(ws, f"B{row}", "Biro " + NAME[t[1]], bg=LOCK)
        put(ws, f"C{row}", t[4], bg=LOCK)
        put(ws, f"D{row}", None, bg=INPUT)
        put(ws, f"E{row}", None, bg=INPUT, h="center")
        ws.row_dimensions[row].height = 64
    mput(ws, "A16:E16", "TABEL 3 · CATATAN KEBUNTUAN / ESKALASI KE KADEP (opsional, isi hanya jika macet total)", bold=True, color="FFFFFF", bg=color)
    put(ws, "A17", "No", bold=True, bg=tint(color, 0.6), h="center")
    mput(ws, "B17:C17", "Isu / Kebuntuan", bold=True, bg=tint(color, 0.6), h="center")
    mput(ws, "D17:E17", "Arahan & Solusi Kadep", bold=True, bg=tint(color, 0.6), h="center")
    for i, row in enumerate(range(R_ESK[0], R_ESK[1] + 1), 1):
        put(ws, f"A{row}", i, bg=LOCK, h="center")
        mput(ws, f"B{row}:C{row}", None, bg=INPUT)
        mput(ws, f"D{row}:E{row}", None, bg=INPUT)
        ws.row_dimensions[row].height = 44

    dv1 = DataValidation(type="list", formula1=f'"{STATUS_OUT}"', allow_blank=True)
    dv2 = DataValidation(type="list", formula1=f'"{STATUS_IN}"', allow_blank=True)
    dv1.add(f"E{R_OUT[0]}:E{R_OUT[1]}")
    dv2.add(f"E{R_IN[0]}:E{R_IN[1]}")
    ws.add_data_validation(dv1)
    ws.add_data_validation(dv2)
    rng = f"E{R_OUT[0]}:E{R_IN[1]}"
    for text, c in (("Sepakat", "C8E6C9"), ("Diterima", "C8E6C9"), ("Diterima Bersyarat", "FFE0B2"),
                    ("Masih Negosiasi", "FFF59D"), ("Batal", "FFCDD2"), ("Ditolak", "FFCDD2")):
        ws.conditional_formatting.add(rng, FormulaRule(formula=[f'E{R_OUT[0]}="{text}"'], fill=fill(c), stopIfTrue=False))
    ws.freeze_panes = "A5"


# ---------------------------------------------------------------- PAPAN_JARING
def sheet_papan(wb):
    ws = wb.create_sheet("PAPAN_JARING")
    page(ws, "00796B")
    widths(ws, {"A": 30, **{c: 14 for c in "BCDEFGHI"}, "J": 3, "K": 16, "L": 16, "M": 16})
    mput(ws, "A1:I1", "PAPAN JARING · Status 16 Tiket (otomatis dari Tabel 1 tiap biro)", bold=True, size=16, color="FFFFFF", bg="00796B", border=False)
    ws.row_dimensions[1].height = 30
    mput(ws, "A2:I2", "Baris = biro pengusung, kolom = biro tujuan. Deal = Sepakat, Pending = Masih Negosiasi atau kosong, Batal = Batal.", italic=True, border=False)
    put(ws, "A4", "Pengusung ↓ / Tujuan →", bold=True, bg="CFD8DC", h="center")
    for j, k in enumerate(ORDER):
        put(ws, f"{'BCDEFGHI'[j]}4", NAME[k], bold=True, bg="CFD8DC", h="center", size=9)
    ws.row_dimensions[4].height = 44
    for i, a in enumerate(ORDER):
        row = 5 + i
        put(ws, f"A{row}", NAME[a], bold=True, bg="CFD8DC")
        ws.row_dimensions[row].height = 30
        for j, b in enumerate(ORDER):
            col = "BCDEFGHI"[j]
            t = next((x for x in TIKET if x[1] == a and x[2] == b), None)
            if a == b:
                put(ws, f"{col}{row}", "■", bg="9E9E9E", h="center", color="9E9E9E")
            elif t is None:
                put(ws, f"{col}{row}", "—", bg=LOCK, h="center", color="9E9E9E")
            else:
                r = R_OUT[0] + OUTGOING[a].index(t)
                ref = f"{q(NAME[a])}!E{r}"
                put(ws, f"{col}{row}", f'=IF({ref}="Sepakat","Deal",IF({ref}="Batal","Batal","Pending"))', bold=True, h="center")
    grid = "B5:I12"
    for text, c in (("Deal", "A5D6A7"), ("Pending", "FFF59D"), ("Batal", "EF9A9A")):
        ws.conditional_formatting.add(grid, FormulaRule(formula=[f'B5="{text}"'], fill=fill(c)))
    put(ws, "K4", "Kartu Skor", bold=True, bg="263238", color="FFFFFF", h="center")
    put(ws, "L4", "Jumlah", bold=True, bg="263238", color="FFFFFF", h="center")
    put(ws, "M4", "dari 16", bold=True, bg="263238", color="FFFFFF", h="center")
    for i, (lab, c) in enumerate((("Total Deal", "A5D6A7"), ("Pending", "FFF59D"), ("Batal", "EF9A9A"))):
        row = 5 + i
        put(ws, f"K{row}", lab, bold=True, bg=c, h="center")
        put(ws, f"L{row}", f'=COUNTIF({grid},"{lab.replace("Total ", "")}")', bold=True, size=16, h="center")
        put(ws, f"M{row}", 16, h="center", bg=LOCK)
    mput(ws, "A14:I14", "Rekap per meja", bold=True, color="FFFFFF", bg="455A64")
    for col, text in zip("ABCD", ("Biro", "Keluar Deal (dari 2)", "Masuk Diterima (dari 2)", "Eskalasi ke Kadep")):
        put(ws, f"{col}15", text, bold=True, bg="CFD8DC", h="center", size=10)
    ws.row_dimensions[15].height = 32
    for i, k in enumerate(ORDER):
        row = 16 + i
        t = q(NAME[k])
        put(ws, f"A{row}", NAME[k], bold=True, bg="CFD8DC")
        put(ws, f"B{row}", f'=COUNTIF({t}!E{R_OUT[0]}:E{R_OUT[1]},"Sepakat")', h="center")
        put(ws, f"C{row}", f'=COUNTIF({t}!E{R_IN[0]}:E{R_IN[1]},"Diterima*")', h="center")
        put(ws, f"D{row}", f"=COUNTA({t}!B{R_ESK[0]}:B{R_ESK[1]})", h="center")
    ws.freeze_panes = "B5"


# ---------------------------------------------------------------- SKOR_EVALUASI
def sheet_skor(wb):
    ws = wb.create_sheet("SKOR_EVALUASI")
    page(ws, "6D4C41")
    widths(ws, {"A": 30, "B": 17, "C": 17, "D": 17, "E": 17, "F": 12, "G": 44})
    mput(ws, "A1:G1", "SKOR EVALUASI · Lembar Pengamat Badan Personalia", bold=True, size=16, color="FFFFFF", bg="6D4C41", border=False)
    ws.row_dimensions[1].height = 30
    mput(ws, "A2:G2", "Skala 1–5 per kriteria. Untuk pembinaan, bukan nilai lulus atau gagal. Total = rata-rata kriteria × 20.", italic=True, border=False)
    heads = ["Meja / Biro", "Keaktifan Negosiasi", "Kualitas Deal Konkret", "Ketepatan Eskalasi", "Adab Kerjasama", "Total (0–100)", "Catatan Pengamat"]
    for col, text in zip("ABCDEFG", heads):
        put(ws, f"{col}4", text, bold=True, bg="D7CCC8", h="center")
    ws.row_dimensions[4].height = 34
    for i, k in enumerate(ORDER):
        row = 5 + i
        put(ws, f"A{row}", NAME[k], bold=True, bg="D7CCC8")
        for col in "BCDE":
            put(ws, f"{col}{row}", None, bg=INPUT, h="center")
        put(ws, f"F{row}", f'=IF(COUNT(B{row}:E{row})=0,"",ROUND(AVERAGE(B{row}:E{row})*20,0))', bold=True, h="center")
        put(ws, f"G{row}", None, bg=INPUT)
        ws.row_dimensions[row].height = 30
    dv = DataValidation(type="whole", operator="between", formula1="1", formula2="5", allow_blank=True,
                        showErrorMessage=True, errorTitle="Skala 1–5", error="Isi angka 1 sampai 5.")
    dv.add("B5:E12")
    ws.add_data_validation(dv)


def main():
    wb = Workbook()
    sheet_petunjuk(wb)
    for k in ORDER:
        sheet_biro(wb, k)
    sheet_papan(wb)
    sheet_skor(wb)
    wb.save(OUT)
    print("OK:", OUT, "| tab:", ", ".join(wb.sheetnames))


if __name__ == "__main__":
    main()
