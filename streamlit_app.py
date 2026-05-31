import streamlit as st
import pandas as pd
import random
 
# ─── Page Config ────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="ChemOrg ID — Identifikasi Senyawa Organik",
    page_icon="⚗️",
    layout="wide",
    initial_sidebar_state="collapsed",
)
 
# ─── Load CSS ────────────────────────────────────────────────────────────────
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
 
# ─── Data ────────────────────────────────────────────────────────────────────
 
SENYAWA_DB = [
    {"Nama": "Etanol", "Rumus": "C₂H₅OH", "Golongan": "Alkohol", "Uji Positif": "Esterifikasi, Iodoform", "CAS": "64-17-5"},
    {"Nama": "Metanol", "Rumus": "CH₃OH", "Golongan": "Alkohol", "Uji Positif": "Esterifikasi", "CAS": "67-56-1"},
    {"Nama": "Aseton", "Rumus": "CH₃COCH₃", "Golongan": "Keton", "Uji Positif": "2,4-DNPH", "CAS": "67-64-1"},
    {"Nama": "Formaldehid", "Rumus": "HCHO", "Golongan": "Aldehid", "Uji Positif": "Tollens, Fehling", "CAS": "50-00-0"},
    {"Nama": "Asetaldehid", "Rumus": "CH₃CHO", "Golongan": "Aldehid", "Uji Positif": "Tollens, Fehling, Iodoform", "CAS": "75-07-0"},
    {"Nama": "Asam Asetat", "Rumus": "CH₃COOH", "Golongan": "Asam Karboksilat", "Uji Positif": "Lakmus, Esterifikasi", "CAS": "64-19-7"},
    {"Nama": "Asam Format", "Rumus": "HCOOH", "Golongan": "Asam Karboksilat", "Uji Positif": "Tollens, Lakmus", "CAS": "64-18-6"},
    {"Nama": "Etil Asetat", "Rumus": "CH₃COOC₂H₅", "Golongan": "Ester", "Uji Positif": "Hidrolisis", "CAS": "141-78-6"},
    {"Nama": "Fenol", "Rumus": "C₆H₅OH", "Golongan": "Fenol", "Uji Positif": "FeCl₃ (ungu)", "CAS": "108-95-2"},
    {"Nama": "Etilena", "Rumus": "CH₂=CH₂", "Golongan": "Alkena", "Uji Positif": "Bromin, Baeyer", "CAS": "74-85-1"},
    {"Nama": "Benzena", "Rumus": "C₆H₆", "Golongan": "Aromatik", "Uji Positif": "Nitrasi", "CAS": "71-43-2"},
    {"Nama": "Glukosa", "Rumus": "C₆H₁₂O₆", "Golongan": "Karbohidrat", "Uji Positif": "Tollens, Fehling, Benedict", "CAS": "50-99-7"},
    {"Nama": "Sukrosa", "Rumus": "C₁₂H₂₂O₁₁", "Golongan": "Karbohidrat", "Uji Positif": "Molisch", "CAS": "57-50-1"},
    {"Nama": "Albumin", "Rumus": "Protein", "Golongan": "Protein", "Uji Positif": "Biuret, Ninhidrin", "CAS": "—"},
    {"Nama": "Anilin", "Rumus": "C₆H₅NH₂", "Golongan": "Amina", "Uji Positif": "Reaksi diazonium", "CAS": "62-53-3"},
]
 
MATERI_UJI = {
    "🟡 Uji Bromin": {
        "tujuan": "Mendeteksi ikatan rangkap (C=C) pada senyawa tak jenuh.",
        "pereaksi": "Larutan Br₂ dalam CCl₄ atau air.",
        "prinsip": "Bromin bereaksi adisi dengan ikatan rangkap. Warna coklat-merah bromin akan hilang (dekolorisasi) bila bereaksi dengan alkena atau alkuna.",
        "reaksi": "Alkena + Br₂ → Dibromoalkana (tak berwarna)",
        "positif": "Warna bromin (coklat-merah) hilang menjadi bening.",
        "negatif": "Warna bromin tetap / tidak berubah.",
        "contoh_positif": ["Etilena", "Propena", "Butadiena"],
        "emoji": "🟡",
    },
    "🟣 Uji Baeyer": {
        "tujuan": "Mendeteksi ketidakjenuhan (ikatan rangkap) dan gugus yang mudah dioksidasi.",
        "pereaksi": "KMnO₄ encer (0,1%) dalam suasana netral/basa.",
        "prinsip": "KMnO₄ mengoksidasi ikatan rangkap atau gugus aldehid. Mn⁷⁺ (ungu) tereduksi menjadi MnO₂ (coklat).",
        "reaksi": "3 R-CH=CH-R' + 2 KMnO₄ + 4H₂O → 3 R-CHOH-CHOH-R' + 2 MnO₂ + 2 KOH",
        "positif": "Warna ungu hilang, terbentuk endapan coklat MnO₂.",
        "negatif": "Warna ungu tetap.",
        "contoh_positif": ["Alkena", "Alkuna", "Aldehid", "Alkohol primer"],
        "emoji": "🟣",
    },
    "⚪ Uji Tollens": {
        "tujuan": "Identifikasi spesifik gugus aldehid (−CHO).",
        "pereaksi": "Pereaksi Tollens: [Ag(NH₃)₂]⁺ (larutan perak-amonia).",
        "prinsip": "Aldehid mereduksi ion perak (Ag⁺) menjadi logam perak (Ag⁰) yang mengendap di dinding tabung membentuk cermin perak.",
        "reaksi": "R-CHO + 2[Ag(NH₃)₂]⁺ + 2OH⁻ → R-COO⁻ + 2Ag↓ + 4NH₃ + H₂O",
        "positif": "Terbentuk cermin perak (silver mirror) di dinding tabung.",
        "negatif": "Tidak ada perubahan / larutan tetap bening.",
        "contoh_positif": ["Formaldehid", "Asetaldehid", "Glukosa", "Asam Format"],
        "emoji": "⚪",
    },
    "🔵 Uji Fehling": {
        "tujuan": "Membedakan aldehid alifatik dari keton.",
        "pereaksi": "Fehling A (CuSO₄) + Fehling B (NaOH + Na-Kalium tartrat).",
        "prinsip": "Cu²⁺ (biru) dalam kompleks tartrat direduksi oleh aldehid menjadi Cu⁺ (merah bata Cu₂O).",
        "reaksi": "R-CHO + 2Cu²⁺ + 5OH⁻ → R-COO⁻ + Cu₂O↓ + 3H₂O",
        "positif": "Endapan merah bata (Cu₂O).",
        "negatif": "Larutan tetap biru.",
        "contoh_positif": ["Formaldehid", "Glukosa", "Maltosa"],
        "emoji": "🔵",
    },
    "🟤 Uji Iodoform": {
        "tujuan": "Mendeteksi gugus metil keton (CH₃CO−) atau alkohol sekunder dengan gugus metil (CH₃CHOH−).",
        "pereaksi": "I₂ dalam NaOH (KI/I₂ + NaOH).",
        "prinsip": "Metil keton bereaksi dengan I₂/NaOH membentuk iodoform (CHI₃) yang berwarna kuning dengan bau khas.",
        "reaksi": "CH₃COR + 3I₂ + 3NaOH → CHI₃↓ + RCOONa + 3NaI + 3H₂O",
        "positif": "Endapan kuning CHI₃ berbau antiseptik.",
        "negatif": "Tidak ada endapan kuning.",
        "contoh_positif": ["Aseton", "Etanol", "Asetaldehid", "2-Propanol"],
        "emoji": "🟤",
    },
    "🟢 Uji FeCl₃": {
        "tujuan": "Mendeteksi senyawa fenol (gugus −OH aromatik).",
        "pereaksi": "FeCl₃ 1% dalam air.",
        "prinsip": "Ion Fe³⁺ membentuk kompleks berwarna dengan gugus fenolat.",
        "reaksi": "3 ArOH + FeCl₃ → [Fe(OAr)₃] + 3 HCl",
        "positif": "Terbentuk warna ungu, biru, atau hijau tergantung senyawa.",
        "negatif": "Tidak ada perubahan warna.",
        "contoh_positif": ["Fenol", "Resorsinol", "Katekin"],
        "emoji": "🟢",
    },
    "🔴 Uji Biuret": {
        "tujuan": "Mendeteksi protein (ikatan peptida −CO−NH−).",
        "pereaksi": "NaOH + CuSO₄ encer.",
        "prinsip": "Ion Cu²⁺ membentuk kompleks dengan dua atau lebih ikatan peptida menghasilkan warna ungu-violet.",
        "reaksi": "Cu²⁺ + ikatan peptida → Kompleks ungu",
        "positif": "Warna ungu-violet muncul.",
        "negatif": "Larutan tetap biru muda.",
        "contoh_positif": ["Albumin", "Kasein", "Gelatin"],
        "emoji": "🔴",
    },
    "🟠 Uji Molisch": {
        "tujuan": "Uji umum keberadaan karbohidrat.",
        "pereaksi": "α-naftol dalam etanol + H₂SO₄ pekat.",
        "prinsip": "H₂SO₄ mendehidrasi karbohidrat menjadi furfural yang bereaksi dengan α-naftol membentuk cincin berwarna.",
        "reaksi": "Karbohidrat →(H₂SO₄) Furfural + α-naftol → Kompleks ungu-merah",
        "positif": "Cincin ungu-merah di batas dua lapisan cairan.",
        "negatif": "Tidak ada cincin berwarna.",
        "contoh_positif": ["Glukosa", "Sukrosa", "Amilum", "Selulosa"],
        "emoji": "🟠",
    },
}
 
SIMULASI_DATA = {
    "Formaldehid (HCHO)": {
        "Uji Bromin": {"hasil": "❌ Negatif", "penjelasan": "Warna bromin tetap. Formaldehid tidak memiliki ikatan C=C.", "positif": False},
        "Uji Baeyer": {"hasil": "✅ Positif", "penjelasan": "Warna ungu KMnO₄ hilang. Gugus aldehid teroksidasi.", "positif": True},
        "Uji Tollens": {"hasil": "✅ Positif", "penjelasan": "Terbentuk cermin perak! Formaldehid adalah aldehid kuat.", "positif": True},
        "Uji Fehling": {"hasil": "✅ Positif", "penjelasan": "Endapan merah bata Cu₂O terbentuk.", "positif": True},
        "Uji Iodoform": {"hasil": "❌ Negatif", "penjelasan": "Tidak ada endapan kuning. Formaldehid bukan metil keton.", "positif": False},
        "Uji FeCl₃": {"hasil": "❌ Negatif", "penjelasan": "Tidak ada warna. Tidak ada gugus fenol.", "positif": False},
        "Uji Biuret": {"hasil": "❌ Negatif", "penjelasan": "Tidak ada warna ungu. Bukan protein.", "positif": False},
        "Uji Molisch": {"hasil": "❌ Negatif", "penjelasan": "Tidak ada cincin warna. Bukan karbohidrat.", "positif": False},
        "kesimpulan": "Aldehid",
    },
    "Etanol (C₂H₅OH)": {
        "Uji Bromin": {"hasil": "❌ Negatif", "penjelasan": "Warna bromin tetap. Etanol jenuh, tidak ada C=C.", "positif": False},
        "Uji Baeyer": {"hasil": "❌ Negatif", "penjelasan": "Warna ungu tetap. Alkohol sekunder tidak dioksidasi KMnO₄ encer dengan mudah.", "positif": False},
        "Uji Tollens": {"hasil": "❌ Negatif", "penjelasan": "Tidak ada cermin perak. Etanol bukan aldehid.", "positif": False},
        "Uji Fehling": {"hasil": "❌ Negatif", "penjelasan": "Tidak ada endapan merah bata.", "positif": False},
        "Uji Iodoform": {"hasil": "✅ Positif", "penjelasan": "Endapan kuning CHI₃ terbentuk! Etanol memiliki gugus CH₃CH(OH)−.", "positif": True},
        "Uji FeCl₃": {"hasil": "❌ Negatif", "penjelasan": "Tidak ada perubahan warna bermakna.", "positif": False},
        "Uji Biuret": {"hasil": "❌ Negatif", "penjelasan": "Tidak ada warna ungu.", "positif": False},
        "Uji Molisch": {"hasil": "❌ Negatif", "penjelasan": "Tidak ada cincin warna.", "positif": False},
        "kesimpulan": "Alkohol",
    },
    "Fenol (C₆H₅OH)": {
        "Uji Bromin": {"hasil": "✅ Positif", "penjelasan": "Warna bromin hilang dan terbentuk endapan putih (2,4,6-tribromofenol).", "positif": True},
        "Uji Baeyer": {"hasil": "❌ Negatif", "penjelasan": "Warna ungu tetap. Fenol tidak memiliki ikatan alkena biasa.", "positif": False},
        "Uji Tollens": {"hasil": "❌ Negatif", "penjelasan": "Tidak ada cermin perak.", "positif": False},
        "Uji Fehling": {"hasil": "❌ Negatif", "penjelasan": "Tidak ada endapan merah bata.", "positif": False},
        "Uji Iodoform": {"hasil": "❌ Negatif", "penjelasan": "Tidak ada endapan kuning.", "positif": False},
        "Uji FeCl₃": {"hasil": "✅ Positif", "penjelasan": "Warna ungu terbentuk! Karakteristik kuat gugus fenol.", "positif": True},
        "Uji Biuret": {"hasil": "❌ Negatif", "penjelasan": "Tidak ada warna ungu.", "positif": False},
        "Uji Molisch": {"hasil": "❌ Negatif", "penjelasan": "Tidak ada cincin warna.", "positif": False},
        "kesimpulan": "Fenol",
    },
    "Glukosa (C₆H₁₂O₆)": {
        "Uji Bromin": {"hasil": "❌ Negatif", "penjelasan": "Tidak ada ikatan C=C pada glukosa.", "positif": False},
        "Uji Baeyer": {"hasil": "✅ Positif", "penjelasan": "Warna ungu hilang karena gugus aldehid glukosa teroksidasi.", "positif": True},
        "Uji Tollens": {"hasil": "✅ Positif", "penjelasan": "Cermin perak terbentuk! Glukosa adalah aldosa (aldehid gula).", "positif": True},
        "Uji Fehling": {"hasil": "✅ Positif", "penjelasan": "Endapan merah bata terbentuk. Glukosa adalah gula pereduksi.", "positif": True},
        "Uji Iodoform": {"hasil": "❌ Negatif", "penjelasan": "Tidak ada endapan kuning.", "positif": False},
        "Uji FeCl₃": {"hasil": "❌ Negatif", "penjelasan": "Tidak ada warna ungu bermakna.", "positif": False},
        "Uji Biuret": {"hasil": "❌ Negatif", "penjelasan": "Tidak ada warna ungu. Bukan protein.", "positif": False},
        "Uji Molisch": {"hasil": "✅ Positif", "penjelasan": "Cincin ungu-merah terbentuk! Glukosa adalah karbohidrat.", "positif": True},
        "kesimpulan": "Karbohidrat (Aldosa / Gula Pereduksi)",
    },
    "Aseton (CH₃COCH₃)": {
        "Uji Bromin": {"hasil": "❌ Negatif", "penjelasan": "Tidak ada ikatan rangkap C=C.", "positif": False},
        "Uji Baeyer": {"hasil": "❌ Negatif", "penjelasan": "Keton tidak mudah dioksidasi oleh KMnO₄ encer.", "positif": False},
        "Uji Tollens": {"hasil": "❌ Negatif", "penjelasan": "Keton tidak dapat mereduksi pereaksi Tollens.", "positif": False},
        "Uji Fehling": {"hasil": "❌ Negatif", "penjelasan": "Tidak ada endapan. Keton tidak mereduksi Fehling.", "positif": False},
        "Uji Iodoform": {"hasil": "✅ Positif", "penjelasan": "Endapan kuning CHI₃ terbentuk! Aseton adalah metil keton.", "positif": True},
        "Uji FeCl₃": {"hasil": "❌ Negatif", "penjelasan": "Tidak ada perubahan warna bermakna.", "positif": False},
        "Uji Biuret": {"hasil": "❌ Negatif", "penjelasan": "Tidak ada warna ungu.", "positif": False},
        "Uji Molisch": {"hasil": "❌ Negatif", "penjelasan": "Tidak ada cincin warna.", "positif": False},
        "kesimpulan": "Keton",
    },
    "Albumin (Protein)": {
        "Uji Bromin": {"hasil": "❌ Negatif", "penjelasan": "Tidak spesifik untuk protein.", "positif": False},
        "Uji Baeyer": {"hasil": "❌ Negatif", "penjelasan": "Tidak relevan untuk protein.", "positif": False},
        "Uji Tollens": {"hasil": "❌ Negatif", "penjelasan": "Tidak ada cermin perak.", "positif": False},
        "Uji Fehling": {"hasil": "❌ Negatif", "penjelasan": "Tidak ada endapan merah bata.", "positif": False},
        "Uji Iodoform": {"hasil": "❌ Negatif", "penjelasan": "Tidak ada endapan kuning.", "positif": False},
        "Uji FeCl₃": {"hasil": "❌ Negatif", "penjelasan": "Tidak ada warna ungu bermakna.", "positif": False},
        "Uji Biuret": {"hasil": "✅ Positif", "penjelasan": "Warna ungu-violet muncul! Ikatan peptida terdeteksi.", "positif": True},
        "Uji Molisch": {"hasil": "❌ Negatif", "penjelasan": "Tidak ada cincin warna.", "positif": False},
        "kesimpulan": "Protein",
    },
}
 
KUIS_SOAL = [
    {
        "soal": "Suatu senyawa memberikan hasil positif pada uji Tollens tetapi negatif pada uji Iodoform. Golongan senyawa tersebut adalah?",
        "pilihan": ["Alkohol", "Aldehid (non-metil)", "Keton", "Fenol"],
        "jawaban": 1,
        "penjelasan": "Tollens positif → ada gugus aldehid. Iodoform negatif → bukan metil keton dan bukan CH₃CHO. Jadi aldehid selain asetaldehid.",
    },
    {
        "soal": "Senyawa X larut dalam air, bereaksi positif dengan uji Fehling dan Tollens, serta positif pada uji Molisch. Kemungkinan besar senyawa X adalah?",
        "pilihan": ["Fenol", "Aldehid aromatik", "Glukosa", "Aseton"],
        "jawaban": 2,
        "penjelasan": "Fehling & Tollens positif → gula pereduksi (aldosa). Molisch positif → karbohidrat. Glukosa adalah aldosa yang memenuhi semua kriteria.",
    },
    {
        "soal": "Manakah pereaksi yang digunakan untuk mendeteksi ikatan rangkap C=C?",
        "pilihan": ["Pereaksi Tollens", "FeCl₃", "KMnO₄ encer (Baeyer)", "Biuret"],
        "jawaban": 2,
        "penjelasan": "Uji Baeyer menggunakan KMnO₄ encer yang bereaksi dengan ikatan rangkap. Warna ungu hilang dan endapan MnO₂ coklat terbentuk.",
    },
    {
        "soal": "Endapan kuning pada uji Iodoform menunjukkan adanya?",
        "pilihan": ["Gugus fenol", "Gugus metil keton atau etanol", "Ikatan peptida", "Gugus aldehid"],
        "jawaban": 1,
        "penjelasan": "Iodoform (CHI₃) kuning terbentuk dari gugus CH₃CO− (metil keton) atau CH₃CHOH− (seperti etanol dan 2-propanol).",
    },
    {
        "soal": "Warna ungu pada uji FeCl₃ menandakan adanya?",
        "pilihan": ["Karbohidrat", "Protein", "Fenol", "Aldehid"],
        "jawaban": 2,
        "penjelasan": "FeCl₃ bereaksi dengan gugus fenol (−OH aromatik) membentuk kompleks berwarna ungu, biru, atau hijau.",
    },
    {
        "soal": "Pereaksi Tollens mengandung ion apa sebagai agen pengoksidasi?",
        "pilihan": ["Cu²⁺", "Ag⁺", "Mn⁷⁺", "Fe³⁺"],
        "jawaban": 1,
        "penjelasan": "[Ag(NH₃)₂]⁺ adalah kompleks perak-amonia. Ion Ag⁺ direduksi oleh aldehid menjadi Ag⁰ (logam perak).",
    },
    {
        "soal": "Uji Molisch digunakan untuk mendeteksi golongan senyawa apa?",
        "pilihan": ["Protein", "Alkohol", "Karbohidrat", "Alkena"],
        "jawaban": 2,
        "penjelasan": "Uji Molisch (α-naftol + H₂SO₄) adalah uji umum untuk semua karbohidrat. Cincin ungu-merah terbentuk di batas dua lapisan.",
    },
    {
        "soal": "Senyawa manakah yang memberikan hasil NEGATIF pada uji Tollens?",
        "pilihan": ["Formaldehid", "Aseton", "Glukosa", "Asetaldehid"],
        "jawaban": 1,
        "penjelasan": "Aseton adalah keton yang tidak dapat mereduksi pereaksi Tollens. Hanya aldehid dan beberapa gula pereduksi yang memberi hasil positif.",
    },
]
 
# ─── Logic Identifikasi ───────────────────────────────────────────────────────
 
def identifikasi_senyawa(jawaban: dict) -> list:
    kandidat = []
    
    larut = jawaban.get("larut")
    bromin = jawaban.get("bromin")
    baeyer = jawaban.get("baeyer")
    tollens = jawaban.get("tollens")
    fehling = jawaban.get("fehling")
    iodoform = jawaban.get("iodoform")
    fecl3 = jawaban.get("fecl3")
    biuret = jawaban.get("biuret")
    molisch = jawaban.get("molisch")
    asam = jawaban.get("asam")
 
    if tollens == "Ya" and fehling == "Ya":
        if molisch == "Ya":
            kandidat.append(("Karbohidrat (Gula Pereduksi)", "Tollens ✅ + Fehling ✅ + Molisch ✅ → Aldosa seperti Glukosa, Maltosa"))
        else:
            kandidat.append(("Aldehid", "Tollens ✅ + Fehling ✅ → Aldehid alifatik (Formaldehid, Asetaldehid)"))
    elif tollens == "Ya" and fehling == "Tidak":
        kandidat.append(("Aldehid Aromatik / Asam Format", "Tollens ✅ + Fehling ❌ → Kemungkinan benzaldehid atau asam format"))
 
    if iodoform == "Ya" and tollens == "Tidak":
        kandidat.append(("Keton (Metil Keton)", "Iodoform ✅ + Tollens ❌ → Metil keton seperti Aseton"))
    elif iodoform == "Ya" and tollens == "Ya":
        kandidat.append(("Asetaldehid", "Iodoform ✅ + Tollens ✅ → Kemungkinan besar Asetaldehid (CH₃CHO)"))
 
    if fecl3 == "Ya":
        kandidat.append(("Fenol", "FeCl₃ ✅ → Gugus fenol terdeteksi (warna ungu/biru/hijau)"))
 
    if bromin == "Ya" and baeyer == "Ya" and tollens == "Tidak" and fecl3 == "Tidak":
        kandidat.append(("Alkena / Alkuna", "Bromin ✅ + Baeyer ✅ + Tollens ❌ → Senyawa tak jenuh"))
 
    if iodoform == "Ya" and tollens == "Tidak" and fecl3 == "Tidak" and bromin == "Tidak":
        kandidat.append(("Alkohol (Etanol / 2-Propanol)", "Iodoform ✅ + Tollens ❌ + Bromin ❌ → Alkohol dengan gugus CH₃CHOH−"))
 
    if asam == "Ya" and tollens == "Tidak" and fehling == "Tidak":
        kandidat.append(("Asam Karboksilat", "Sifat asam ✅ + Tollens ❌ → Kemungkinan asam karboksilat"))
 
    if biuret == "Ya":
        kandidat.append(("Protein", "Biuret ✅ → Ikatan peptida terdeteksi. Kemungkinan protein"))
 
    if molisch == "Ya" and tollens == "Tidak" and fehling == "Tidak":
        kandidat.append(("Karbohidrat (Non-Pereduksi)", "Molisch ✅ + Tollens ❌ → Karbohidrat non-pereduksi seperti Sukrosa, Amilum"))
 
    if not kandidat:
        kandidat.append(("Tidak Teridentifikasi", "Kombinasi hasil uji tidak cocok dengan pola yang ada. Coba periksa kembali hasil uji Anda."))
 
    return kandidat
 
 
# ─── Session State Init ───────────────────────────────────────────────────────
if "halaman" not in st.session_state:
    st.session_state.halaman = "landing"
if "kuis_soal_idx" not in st.session_state:
    st.session_state.kuis_soal_idx = 0
if "kuis_skor" not in st.session_state:
    st.session_state.kuis_skor = 0
if "kuis_jawaban" not in st.session_state:
    st.session_state.kuis_jawaban = {}
if "kuis_selesai" not in st.session_state:
    st.session_state.kuis_selesai = False
if "kuis_soal_list" not in st.session_state:
    st.session_state.kuis_soal_list = random.sample(KUIS_SOAL, len(KUIS_SOAL))
 
# ─── Navigation Helper ────────────────────────────────────────────────────────
def nav(page):
    st.session_state.halaman = page
    st.rerun()
 
 
# ════════════════════════════════════════════════════════════════════════════════
#  LANDING PAGE
# ════════════════════════════════════════════════════════════════════════════════
if st.session_state.halaman == "landing":
    st.markdown("""
    <div class="landing-hero">
        <div class="hero-badge">⚗️ Kimia Organik Kualitatif</div>
        <h1 class="hero-title">Sistem Identifikasi<br><span class="hero-accent">Senyawa Organik</span></h1>
        <p class="hero-desc">
            Platform edukasi interaktif untuk mengidentifikasi golongan senyawa organik 
            berdasarkan hasil pengujian laboratorium — uji kelarutan, bromin, Baeyer, 
            Tollens, Fehling, dan lebih banyak lagi.
        </p>
    </div>
    """, unsafe_allow_html=True)
 
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("🔬 Mulai Identifikasi", use_container_width=True, type="primary"):
            nav("identifikasi")
    with col2:
        if st.button("📚 Materi Uji Organik", use_container_width=True):
            nav("materi")
    with col3:
        if st.button("🗄️ Database Senyawa", use_container_width=True):
            nav("database")
    with col4:
        if st.button("🧪 Simulasi & Kuis", use_container_width=True):
            nav("simulasi")
 
    st.markdown("""
    <div class="feature-grid">
        <div class="feature-card">
            <div class="feature-icon">🔬</div>
            <h3>Identifikasi Senyawa</h3>
            <p>Jawab pertanyaan berdasarkan hasil praktikum dan dapatkan identifikasi golongan senyawa secara otomatis.</p>
        </div>
        <div class="feature-card">
            <div class="feature-icon">📚</div>
            <h3>Materi Lengkap</h3>
            <p>Pelajari teori, prinsip, pereaksi, dan interpretasi 8 jenis uji kualitatif organik.</p>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🗄️</div>
            <h3>Database Senyawa</h3>
            <p>Akses database 15+ senyawa organik dengan rumus, golongan, dan uji positifnya.</p>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🎮</div>
            <h3>Simulasi & Kuis</h3>
            <p>Simulasikan pengujian di lab virtual dan uji pemahaman dengan kuis interaktif.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
 
 
# ════════════════════════════════════════════════════════════════════════════════
#  IDENTIFIKASI
# ════════════════════════════════════════════════════════════════════════════════
elif st.session_state.halaman == "identifikasi":
    if st.button("← Kembali"):
        nav("landing")
 
    st.markdown('<h2 class="page-title">🔬 Identifikasi Senyawa Organik</h2>', unsafe_allow_html=True)
    st.markdown('<p class="page-sub">Jawab pertanyaan berikut berdasarkan hasil pengujian di laboratorium Anda.</p>', unsafe_allow_html=True)
 
    st.markdown('<div class="card">', unsafe_allow_html=True)
 
    jawaban = {}
 
    st.markdown("#### 💧 Kelarutan")
    jawaban["larut"] = st.radio("Apakah sampel larut dalam air?", ["Ya", "Tidak", "Sebagian"], horizontal=True, key="q_larut")
 
    st.divider()
    st.markdown("#### 🧪 Uji Ikatan Rangkap")
    col1, col2 = st.columns(2)
    with col1:
        jawaban["bromin"] = st.radio("Warna bromin hilang (Uji Bromin)?", ["Ya", "Tidak"], horizontal=True, key="q_bromin")
    with col2:
        jawaban["baeyer"] = st.radio("Warna ungu hilang (Uji Baeyer)?", ["Ya", "Tidak"], horizontal=True, key="q_baeyer")
 
    st.divider()
    st.markdown("#### ⚗️ Uji Oksidasi-Reduksi")
    col1, col2 = st.columns(2)
    with col1:
        jawaban["tollens"] = st.radio("Terbentuk cermin perak (Uji Tollens)?", ["Ya", "Tidak"], horizontal=True, key="q_tollens")
    with col2:
        jawaban["fehling"] = st.radio("Endapan merah bata (Uji Fehling)?", ["Ya", "Tidak"], horizontal=True, key="q_fehling")
 
    st.divider()
    st.markdown("#### 🔍 Uji Spesifik Gugus Fungsi")
    col1, col2, col3 = st.columns(3)
    with col1:
        jawaban["iodoform"] = st.radio("Endapan kuning (Uji Iodoform)?", ["Ya", "Tidak"], horizontal=True, key="q_iodoform")
    with col2:
        jawaban["fecl3"] = st.radio("Warna ungu/biru (Uji FeCl₃)?", ["Ya", "Tidak"], horizontal=True, key="q_fecl3")
    with col3:
        jawaban["asam"] = st.radio("Mengubah lakmus merah (bersifat asam)?", ["Ya", "Tidak"], horizontal=True, key="q_asam")
 
    st.divider()
    st.markdown("#### 🧬 Uji Biomolekul")
    col1, col2 = st.columns(2)
    with col1:
        jawaban["biuret"] = st.radio("Warna ungu-violet (Uji Biuret)?", ["Ya", "Tidak"], horizontal=True, key="q_biuret")
    with col2:
        jawaban["molisch"] = st.radio("Cincin ungu-merah (Uji Molisch)?", ["Ya", "Tidak"], horizontal=True, key="q_molisch")
 
    st.markdown('</div>', unsafe_allow_html=True)
 
    if st.button("🔎 Identifikasi Sekarang!", type="primary", use_container_width=True):
        hasil = identifikasi_senyawa(jawaban)
        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.markdown("### 📊 Hasil Identifikasi")
        for golongan, alasan in hasil:
            st.markdown(f"""
            <div class="result-item">
                <div class="result-golongan">✅ {golongan}</div>
                <div class="result-alasan">{alasan}</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
 
        if len(hasil) > 1:
            st.info("💡 **Catatan:** Beberapa golongan terdeteksi. Pertimbangkan konteks sampel dan uji tambahan untuk konfirmasi.")
 
 
# ════════════════════════════════════════════════════════════════════════════════
#  MATERI
# ════════════════════════════════════════════════════════════════════════════════
elif st.session_state.halaman == "materi":
    if st.button("← Kembali"):
        nav("landing")
 
    st.markdown('<h2 class="page-title">📚 Materi Uji Kualitatif Organik</h2>', unsafe_allow_html=True)
    st.markdown('<p class="page-sub">Teori lengkap setiap metode pengujian beserta pereaksi, prinsip, dan interpretasi hasil.</p>', unsafe_allow_html=True)
 
    for nama_uji, data in MATERI_UJI.items():
        with st.expander(f"{nama_uji}", expanded=False):
            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown(f"**🎯 Tujuan:**\n{data['tujuan']}")
                st.markdown(f"**🧪 Pereaksi:**\n{data['pereaksi']}")
                st.markdown(f"**⚙️ Prinsip:**\n{data['prinsip']}")
            with col2:
                st.markdown(f"**🔬 Reaksi:**")
                st.code(data["reaksi"], language=None)
                st.markdown(f"**✅ Hasil Positif:** {data['positif']}")
                st.markdown(f"**❌ Hasil Negatif:** {data['negatif']}")
            
            st.markdown("**🔬 Contoh Senyawa Positif:**")
            cols = st.columns(len(data["contoh_positif"]))
            for i, senyawa in enumerate(data["contoh_positif"]):
                cols[i].markdown(f'<span class="tag">{senyawa}</span>', unsafe_allow_html=True)
 
 
# ════════════════════════════════════════════════════════════════════════════════
#  DATABASE
# ════════════════════════════════════════════════════════════════════════════════
elif st.session_state.halaman == "database":
    if st.button("← Kembali"):
        nav("landing")
 
    st.markdown('<h2 class="page-title">🗄️ Database Senyawa Organik</h2>', unsafe_allow_html=True)
    st.markdown('<p class="page-sub">Cari dan telusuri senyawa organik beserta golongan dan uji positifnya.</p>', unsafe_allow_html=True)
 
    col1, col2 = st.columns([2, 1])
    with col1:
        cari = st.text_input("🔍 Cari senyawa...", placeholder="Contoh: etanol, aldehid, glukosa...")
    with col2:
        filter_golongan = st.selectbox("Filter Golongan", 
            ["Semua"] + sorted(list(set(s["Golongan"] for s in SENYAWA_DB))))
 
    df = pd.DataFrame(SENYAWA_DB)
    if cari:
        mask = (df["Nama"].str.contains(cari, case=False) | 
                df["Golongan"].str.contains(cari, case=False) |
                df["Uji Positif"].str.contains(cari, case=False))
        df = df[mask]
    if filter_golongan != "Semua":
        df = df[df["Golongan"] == filter_golongan]
 
    st.markdown(f'<p class="count-badge">Menampilkan {len(df)} dari {len(SENYAWA_DB)} senyawa</p>', unsafe_allow_html=True)
    st.dataframe(df, use_container_width=True, hide_index=True,
        column_config={
            "Nama": st.column_config.TextColumn("Nama Senyawa", width="medium"),
            "Rumus": st.column_config.TextColumn("Rumus Kimia", width="small"),
            "Golongan": st.column_config.TextColumn("Golongan", width="medium"),
            "Uji Positif": st.column_config.TextColumn("Uji Positif", width="large"),
            "CAS": st.column_config.TextColumn("CAS No.", width="small"),
        }
    )
 
 
# ════════════════════════════════════════════════════════════════════════════════
#  SIMULASI & KUIS
# ════════════════════════════════════════════════════════════════════════════════
elif st.session_state.halaman == "simulasi":
    if st.button("← Kembali"):
        nav("landing")
 
    tab1, tab2 = st.tabs(["🧪 Simulasi Praktikum", "📝 Kuis Interaktif"])
 
    # ── Simulasi ──
    with tab1:
        st.markdown('<h2 class="page-title">🧪 Simulasi Praktikum Virtual</h2>', unsafe_allow_html=True)
        st.markdown('<p class="page-sub">Pilih sampel dan uji, lalu lihat hasil simulasi laboratorium.</p>', unsafe_allow_html=True)
 
        col1, col2 = st.columns(2)
        with col1:
            sampel = st.selectbox("🧫 Pilih Sampel:", list(SIMULASI_DATA.keys()))
        with col2:
            uji = st.selectbox("🔬 Pilih Uji:", list(MATERI_UJI.keys()))
 
        uji_key = " ".join(uji.split()[1:])
 
        if st.button("▶️ Jalankan Simulasi", type="primary", use_container_width=True):
            hasil_sim = SIMULASI_DATA[sampel].get(uji_key)
            if hasil_sim:
                warna = "sim-positif" if hasil_sim["positif"] else "sim-negatif"
                st.markdown(f"""
                <div class="sim-result {warna}">
                    <div class="sim-header">
                        <span class="sim-sampel">🧫 {sampel}</span>
                        <span class="sim-uji">+ {uji}</span>
                    </div>
                    <div class="sim-hasil">{hasil_sim['hasil']}</div>
                    <div class="sim-penjelasan">{hasil_sim['penjelasan']}</div>
                    <div class="sim-kesimpulan">
                        <strong>Kesimpulan:</strong> Sampel kemungkinan termasuk golongan 
                        <strong>{SIMULASI_DATA[sampel]['kesimpulan']}</strong>
                    </div>
                </div>
                """, unsafe_allow_html=True)
 
        st.markdown("---")
        st.markdown("#### 📊 Tabel Lengkap Semua Uji untuk Sampel Terpilih")
        data_table = []
        for uji_name, hasil_data in SIMULASI_DATA[sampel].items():
            if uji_name != "kesimpulan":
                data_table.append({
                    "Uji": uji_name,
                    "Hasil": hasil_data["hasil"],
                    "Keterangan": hasil_data["penjelasan"]
                })
        st.dataframe(pd.DataFrame(data_table), use_container_width=True, hide_index=True)
 
    # ── Kuis ──
    with tab2:
        st.markdown('<h2 class="page-title">📝 Kuis Identifikasi</h2>', unsafe_allow_html=True)
 
        if st.session_state.kuis_selesai:
            skor = st.session_state.kuis_skor
            total = len(st.session_state.kuis_soal_list)
            pct = int(skor / total * 100)
            grade = "🏆 Luar Biasa!" if pct >= 80 else "👍 Cukup Baik!" if pct >= 60 else "📖 Perlu Belajar Lagi"
 
            st.markdown(f"""
            <div class="score-card">
                <div class="score-grade">{grade}</div>
                <div class="score-number">{skor} / {total}</div>
                <div class="score-pct">{pct}% Benar</div>
            </div>
            """, unsafe_allow_html=True)
 
            st.markdown("#### 📋 Review Jawaban")
            for i, soal in enumerate(st.session_state.kuis_soal_list):
                jawaban_user = st.session_state.kuis_jawaban.get(i)
                benar = jawaban_user == soal["jawaban"]
                ikon = "✅" if benar else "❌"
                with st.expander(f"{ikon} Soal {i+1}: {soal['soal'][:60]}..."):
                    st.write(f"**Soal:** {soal['soal']}")
                    st.write(f"**Jawaban Anda:** {soal['pilihan'][jawaban_user] if jawaban_user is not None else '—'}")
                    st.write(f"**Jawaban Benar:** {soal['pilihan'][soal['jawaban']]}")
                    st.info(f"💡 {soal['penjelasan']}")
 
            if st.button("🔄 Ulangi Kuis", type="primary"):
                st.session_state.kuis_soal_idx = 0
                st.session_state.kuis_skor = 0
                st.session_state.kuis_jawaban = {}
                st.session_state.kuis_selesai = False
                st.session_state.kuis_soal_list = random.sample(KUIS_SOAL, len(KUIS_SOAL))
                st.rerun()
        else:
            idx = st.session_state.kuis_soal_idx
            soal_list = st.session_state.kuis_soal_list
            soal = soal_list[idx]
            total = len(soal_list)
 
            progress = (idx) / total
            st.progress(progress, text=f"Soal {idx + 1} dari {total}")
 
            st.markdown(f"""
            <div class="kuis-soal-box">
                <div class="kuis-nomor">Soal {idx + 1}</div>
                <div class="kuis-pertanyaan">{soal['soal']}</div>
            </div>
            """, unsafe_allow_html=True)
 
            pilihan_key = f"kuis_{idx}"
            pilihan = st.radio("Pilih jawaban:", soal["pilihan"], key=pilihan_key, index=None)
 
            col1, col2 = st.columns(2)
            with col1:
                if idx > 0:
                    if st.button("← Sebelumnya"):
                        st.session_state.kuis_soal_idx -= 1
                        st.rerun()
 
            with col2:
                if pilihan is not None:
                    idx_pilihan = soal["pilihan"].index(pilihan)
                    st.session_state.kuis_jawaban[idx] = idx_pilihan
                    if idx < total - 1:
                        if st.button("Berikutnya →", type="primary"):
                            st.session_state.kuis_soal_idx += 1
                            st.rerun()
                    else:
                        if st.button("✅ Selesai & Lihat Nilai", type="primary"):
                            skor = 0
                            for i, s in enumerate(soal_list):
                                if st.session_state.kuis_jawaban.get(i) == s["jawaban"]:
                                    skor += 1
                            st.session_state.kuis_skor = skor
                            st.session_state.kuis_selesai = True
                            st.rerun()
 
