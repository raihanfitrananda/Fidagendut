/* ─── Import Fonts ─────────────────────────────────────────────────────────── */
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=DM+Sans:wght@300;400;500;600;700&family=Playfair+Display:wght@700&display=swap');
 
/* ─── Root Variables ────────────────────────────────────────────────────────── */
:root {
    --bg: #0b0f1a;
    --surface: #111827;
    --surface2: #1a2236;
    --border: #1e2d45;
    --accent: #00d4ff;
    --accent2: #7c3aed;
    --accent3: #10b981;
    --text: #e2e8f0;
    --text-muted: #64748b;
    --danger: #ef4444;
    --warn: #f59e0b;
    --success: #22c55e;
    --font-body: 'DM Sans', sans-serif;
    --font-mono: 'Space Mono', monospace;
    --font-display: 'Playfair Display', serif;
    --radius: 12px;
    --glow: 0 0 20px rgba(0, 212, 255, 0.15);
}
 
/* ─── Global Reset ──────────────────────────────────────────────────────────── */
html, body, [class*="css"] {
    font-family: var(--font-body) !important;
    color: var(--text) !important;
}
 
.stApp {
    background: var(--bg) !important;
    background-image:
        radial-gradient(ellipse at 20% 0%, rgba(124, 58, 237, 0.08) 0%, transparent 50%),
        radial-gradient(ellipse at 80% 100%, rgba(0, 212, 255, 0.06) 0%, transparent 50%);
    min-height: 100vh;
}
 
/* ─── Hide Streamlit Branding ───────────────────────────────────────────────── */
#MainMenu, footer, header {visibility: hidden;}
.stDeployButton {display: none;}
 
/* ─── Scrollbar ─────────────────────────────────────────────────────────────── */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: var(--bg); }
::-webkit-scrollbar-thumb { background: var(--accent2); border-radius: 3px; }
 
/* ─── Landing Hero ──────────────────────────────────────────────────────────── */
.landing-hero {
    text-align: center;
    padding: 4rem 2rem 3rem;
    position: relative;
}
 
.hero-badge {
    display: inline-block;
    font-family: var(--font-mono);
    font-size: 0.75rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: var(--accent);
    border: 1px solid rgba(0, 212, 255, 0.3);
    padding: 0.4rem 1.2rem;
    border-radius: 999px;
    margin-bottom: 1.5rem;
    background: rgba(0, 212, 255, 0.05);
    animation: fadeInDown 0.6s ease;
}
 
.hero-title {
    font-family: var(--font-display) !important;
    font-size: clamp(2.2rem, 5vw, 3.5rem) !important;
    font-weight: 700 !important;
    line-height: 1.15 !important;
    color: var(--text) !important;
    margin-bottom: 0.5rem !important;
    animation: fadeInUp 0.7s ease 0.1s both;
}
 
.hero-accent {
    background: linear-gradient(135deg, var(--accent), var(--accent2));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
 
.hero-desc {
    font-size: 1.05rem;
    color: var(--text-muted);
    max-width: 600px;
    margin: 0 auto 2.5rem;
    line-height: 1.7;
    animation: fadeInUp 0.7s ease 0.2s both;
}
 
/* ─── Feature Grid ──────────────────────────────────────────────────────────── */
.feature-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 1.2rem;
    margin-top: 3rem;
    animation: fadeInUp 0.8s ease 0.4s both;
}
 
.feature-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 1.6rem;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}
 
.feature-card::before {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(135deg, rgba(0, 212, 255, 0.03), rgba(124, 58, 237, 0.03));
    opacity: 0;
    transition: opacity 0.3s;
}
 
.feature-card:hover { 
    border-color: rgba(0, 212, 255, 0.3);
    transform: translateY(-3px);
    box-shadow: var(--glow);
}
 
.feature-card:hover::before { opacity: 1; }
 
.feature-icon {
    font-size: 2rem;
    margin-bottom: 0.8rem;
}
 
.feature-card h3 {
    font-size: 0.95rem !important;
    font-weight: 600 !important;
    color: var(--text) !important;
    margin-bottom: 0.5rem !important;
}
 
.feature-card p {
    font-size: 0.83rem;
    color: var(--text-muted);
    line-height: 1.6;
    margin: 0;
}
 
/* ─── Page Titles ───────────────────────────────────────────────────────────── */
.page-title {
    font-family: var(--font-display) !important;
    font-size: 2rem !important;
    color: var(--text) !important;
    margin-bottom: 0.3rem !important;
}
 
.page-sub {
    color: var(--text-muted);
    font-size: 0.95rem;
    margin-bottom: 1.5rem;
}
 
/* ─── Card ──────────────────────────────────────────────────────────────────── */
.card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 2rem;
    margin-bottom: 1.5rem;
}
 
/* ─── Buttons ───────────────────────────────────────────────────────────────── */
.stButton > button {
    background: var(--surface2) !important;
    border: 1px solid var(--border) !important;
    color: var(--text) !important;
    border-radius: 8px !important;
    font-family: var(--font-body) !important;
    font-size: 0.9rem !important;
    font-weight: 500 !important;
    padding: 0.55rem 1.2rem !important;
    transition: all 0.2s ease !important;
    cursor: pointer !important;
}
 
.stButton > button:hover {
    border-color: var(--accent) !important;
    box-shadow: 0 0 12px rgba(0, 212, 255, 0.2) !important;
    transform: translateY(-1px) !important;
}
 
.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, var(--accent2), #5b21b6) !important;
    border-color: transparent !important;
    color: white !important;
}
 
.stButton > button[kind="primary"]:hover {
    box-shadow: 0 0 20px rgba(124, 58, 237, 0.4) !important;
}
 
/* ─── Radio ─────────────────────────────────────────────────────────────────── */
.stRadio > label {
    color: var(--text) !important;
    font-weight: 500 !important;
    font-size: 0.9rem !important;
}
 
.stRadio [role="radiogroup"] label {
    background: var(--surface2) !important;
    border: 1px solid var(--border) !important;
    border-radius: 8px !important;
    padding: 0.4rem 1rem !important;
    transition: all 0.2s !important;
}
 
.stRadio [role="radiogroup"] label:hover {
    border-color: var(--accent) !important;
}
 
/* ─── Select / Text Input ────────────────────────────────────────────────────── */
.stSelectbox > div > div, .stTextInput > div > div > input {
    background: var(--surface2) !important;
    border: 1px solid var(--border) !important;
    color: var(--text) !important;
    border-radius: 8px !important;
}
 
/* ─── Expander ──────────────────────────────────────────────────────────────── */
.streamlit-expanderHeader {
    background: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: 8px !important;
    color: var(--text) !important;
    font-weight: 600 !important;
    font-size: 0.95rem !important;
}
 
.streamlit-expanderContent {
    background: var(--surface2) !important;
    border: 1px solid var(--border) !important;
    border-top: none !important;
    border-radius: 0 0 8px 8px !important;
}
 
/* ─── Divider ───────────────────────────────────────────────────────────────── */
hr {
    border-color: var(--border) !important;
    margin: 1.5rem 0 !important;
}
 
/* ─── Result Box ────────────────────────────────────────────────────────────── */
.result-box {
    background: linear-gradient(135deg, rgba(124, 58, 237, 0.1), rgba(0, 212, 255, 0.05));
    border: 1px solid rgba(124, 58, 237, 0.3);
    border-radius: var(--radius);
    padding: 1.8rem;
    margin-top: 1.5rem;
}
 
.result-item {
    background: var(--surface);
    border-radius: 8px;
    padding: 1rem 1.2rem;
    margin-bottom: 0.8rem;
    border-left: 3px solid var(--accent3);
}
 
.result-golongan {
    font-family: var(--font-mono);
    font-size: 1rem;
    font-weight: 700;
    color: var(--accent3);
    margin-bottom: 0.3rem;
}
 
.result-alasan {
    font-size: 0.85rem;
    color: var(--text-muted);
    line-height: 1.5;
}
 
/* ─── Tag ───────────────────────────────────────────────────────────────────── */
.tag {
    display: inline-block;
    background: rgba(0, 212, 255, 0.1);
    border: 1px solid rgba(0, 212, 255, 0.25);
    color: var(--accent);
    font-size: 0.78rem;
    padding: 0.25rem 0.7rem;
    border-radius: 999px;
    font-family: var(--font-mono);
    margin: 0.2rem;
}
 
/* ─── Simulation Result ─────────────────────────────────────────────────────── */
.sim-result {
    border-radius: var(--radius);
    padding: 1.8rem;
    margin-top: 1rem;
    border: 1px solid;
}
 
.sim-positif {
    background: rgba(34, 197, 94, 0.08);
    border-color: rgba(34, 197, 94, 0.3);
}
 
.sim-negatif {
    background: rgba(239, 68, 68, 0.08);
    border-color: rgba(239, 68, 68, 0.3);
}
 
.sim-header {
    display: flex;
    gap: 1rem;
    align-items: center;
    margin-bottom: 1rem;
    font-family: var(--font-mono);
    font-size: 0.85rem;
    color: var(--text-muted);
}
 
.sim-sampel { color: var(--accent); font-weight: 700; }
.sim-uji { color: var(--accent2); }
 
.sim-hasil {
    font-size: 1.4rem;
    font-weight: 700;
    margin-bottom: 0.7rem;
    color: var(--text);
}
 
.sim-penjelasan {
    font-size: 0.9rem;
    color: var(--text-muted);
    line-height: 1.6;
    margin-bottom: 1rem;
}
 
.sim-kesimpulan {
    font-size: 0.88rem;
    background: rgba(255,255,255,0.04);
    border-radius: 8px;
    padding: 0.8rem 1rem;
    border-left: 3px solid var(--accent);
}
 
/* ─── Quiz ──────────────────────────────────────────────────────────────────── */
.kuis-soal-box {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 2rem;
    margin-bottom: 1.5rem;
    position: relative;
}
 
.kuis-nomor {
    font-family: var(--font-mono);
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: var(--accent);
    margin-bottom: 0.8rem;
}
 
.kuis-pertanyaan {
    font-size: 1.05rem;
    font-weight: 500;
    line-height: 1.6;
    color: var(--text);
}
 
/* ─── Score Card ────────────────────────────────────────────────────────────── */
.score-card {
    text-align: center;
    background: linear-gradient(135deg, rgba(124, 58, 237, 0.15), rgba(0, 212, 255, 0.08));
    border: 1px solid rgba(124, 58, 237, 0.3);
    border-radius: 16px;
    padding: 3rem 2rem;
    margin: 1rem 0 2rem;
}
 
.score-grade {
    font-size: 1.5rem;
    font-weight: 700;
    margin-bottom: 1rem;
}
 
.score-number {
    font-family: var(--font-display);
    font-size: 4rem;
    font-weight: 700;
    background: linear-gradient(135deg, var(--accent), var(--accent2));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1;
    margin-bottom: 0.5rem;
}
 
.score-pct {
    font-size: 1.2rem;
    color: var(--text-muted);
    font-family: var(--font-mono);
}
 
/* ─── Count Badge ───────────────────────────────────────────────────────────── */
.count-badge {
    font-family: var(--font-mono);
    font-size: 0.78rem;
    color: var(--text-muted);
    margin-bottom: 0.8rem;
}
 
/* ─── Dataframe ─────────────────────────────────────────────────────────────── */
.stDataFrame {
    border: 1px solid var(--border) !important;
    border-radius: var(--radius) !important;
    overflow: hidden !important;
}
 
.stDataFrame table {
    background: var(--surface) !important;
}
 
.stDataFrame th {
    background: var(--surface2) !important;
    color: var(--accent) !important;
    font-family: var(--font-mono) !important;
    font-size: 0.75rem !important;
    text-transform: uppercase !important;
    letter-spacing: 0.08em !important;
    padding: 0.8rem 1rem !important;
    border-bottom: 1px solid var(--border) !important;
}
 
.stDataFrame td {
    background: var(--surface) !important;
    color: var(--text) !important;
    font-size: 0.88rem !important;
    padding: 0.7rem 1rem !important;
    border-bottom: 1px solid var(--border) !important;
}
 
.stDataFrame tr:hover td {
    background: var(--surface2) !important;
}
 
/* ─── Info / Alert ──────────────────────────────────────────────────────────── */
.stInfo, .stAlert {
    background: rgba(0, 212, 255, 0.06) !important;
    border: 1px solid rgba(0, 212, 255, 0.2) !important;
    border-radius: 8px !important;
    color: var(--text) !important;
}
 
/* ─── Progress ──────────────────────────────────────────────────────────────── */
.stProgress > div > div > div > div {
    background: linear-gradient(90deg, var(--accent2), var(--accent)) !important;
}
 
/* ─── Code Block ────────────────────────────────────────────────────────────── */
.stCode, code, pre {
    background: #0d1117 !important;
    border: 1px solid var(--border) !important;
    border-radius: 6px !important;
    font-family: var(--font-mono) !important;
    font-size: 0.82rem !important;
    color: #a5f3fc !important;
}
 
/* ─── Tabs ──────────────────────────────────────────────────────────────────── */
.stTabs [data-baseweb="tab-list"] {
    background: var(--surface) !important;
    border-radius: 10px !important;
    padding: 4px !important;
    border: 1px solid var(--border) !important;
}
 
.stTabs [data-baseweb="tab"] {
    color: var(--text-muted) !important;
    font-weight: 500 !important;
    border-radius: 8px !important;
    transition: all 0.2s !important;
}
 
.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, var(--accent2), #5b21b6) !important;
    color: white !important;
}
 
/* ─── Animations ────────────────────────────────────────────────────────────── */
@keyframes fadeInDown {
    from { opacity: 0; transform: translateY(-15px); }
    to { opacity: 1; transform: translateY(0); }
}
 
@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(15px); }
    to { opacity: 1; transform: translateY(0); }
}
 
@keyframes glow {
    0%, 100% { box-shadow: 0 0 10px rgba(0, 212, 255, 0.2); }
    50% { box-shadow: 0 0 25px rgba(0, 212, 255, 0.4); }
}
 
