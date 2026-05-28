import streamlit as st


def inject_global_styles():
    st.markdown("""
    <style>
    :root {
        --bg: #050b16;
        --panel: #081120;
        --panel-2: #0b1628;
        --panel-3: #0d1930;
        --border: rgba(123, 150, 188, 0.14);
        --text: #eaf2fb;
        --muted: #8fa1bb;
        --faint: #607089;
        --green: #20e38b;
        --red: #ff5f6d;
        --orange: #f2aa3b;
        --purple: #7f56ff;
        --cyan: #1ad6ff;
        --blue: #2d8cff;
    }

    .stApp {
        background:
            radial-gradient(circle at top left, rgba(24, 94, 255, 0.08), transparent 16%),
            radial-gradient(circle at 80% 0%, rgba(0, 255, 170, 0.05), transparent 12%),
            linear-gradient(180deg, #040915 0%, #050b16 100%);
        color: var(--text);
    }

    .block-container {
        max-width: 100%;
        padding-top: 0.35rem;
        padding-left: 0.45rem;
        padding-right: 0.45rem;
        padding-bottom: 0.6rem;
    }

    [data-testid="stHeader"] { display: none; }
    [data-testid="stSidebar"] { display: none; }

    .panel {
        position: relative;
        overflow: hidden;
        border-radius: 16px;
        background:
            linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01)),
            linear-gradient(180deg, #07101d 0%, #091422 100%);
        border: 1px solid var(--border);
        box-shadow:
            0 12px 28px rgba(0,0,0,0.22),
            inset 0 1px 0 rgba(255,255,255,0.03);
    }

    .panel::after {
        content: "";
        position: absolute;
        inset: 0;
        pointer-events: none;
        background: linear-gradient(180deg, rgba(255,255,255,0.02), transparent 18%);
    }

    .nav-rail {
        width: 100%;
        border-radius: 18px;
        background:
            linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01)),
            linear-gradient(180deg, #081120 0%, #091423 100%);
        border: 1px solid var(--border);
        box-shadow:
            0 12px 30px rgba(0,0,0,0.24),
            inset 0 1px 0 rgba(255,255,255,0.03);
        padding: 8px 6px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: space-between;
        min-height: calc(100vh - 1rem);
        position: sticky;
        top: 0.5rem;
    }

    .nav-group {
        display: flex;
        flex-direction: column;
        gap: 8px;
        width: 100%;
        align-items: center;
    }

    .brand-orb {
        width: 30px;
        height: 30px;
        border-radius: 50%;
        background:
            radial-gradient(circle at 30% 30%, rgba(78,255,168,0.55), rgba(20,173,101,0.10) 55%),
            linear-gradient(180deg, #0d3225, #0a261d);
        border: 1px solid rgba(32,227,139,0.28);
        box-shadow: 0 0 0 3px rgba(32,227,139,0.05);
        display: flex;
        align-items: center;
        justify-content: center;
        color: #9cffcb;
        font-size: 0.92rem;
        font-weight: 800;
    }

    .nav-btn {
        width: 34px;
        height: 34px;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: rgba(255,255,255,0.02);
        border: 1px solid transparent;
        color: #7084a0;
        font-size: 0.95rem;
    }

    .nav-btn.active {
        background: linear-gradient(180deg, rgba(34,111,255,0.22), rgba(22,72,170,0.18));
        color: #79b0ff;
        border-color: rgba(78,132,255,0.18);
    }

    .nav-badge {
        width: 28px;
        height: 28px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 0.66rem;
        font-weight: 800;
        color: #d8e5f7;
        border: 1px solid var(--border);
        background: rgba(255,255,255,0.03);
    }

    .nav-badge.pro {
        color: #ffcf67;
        border-color: rgba(242,170,59,0.22);
        background: rgba(242,170,59,0.08);
    }

    .top-header {
        padding: 10px 14px;
        margin-bottom: 10px;
    }

    .top-header-grid {
        display: grid;
        grid-template-columns: 1.3fr 1fr auto;
        gap: 12px;
        align-items: center;
    }

    .brand-title {
        font-size: 1.06rem;
        font-weight: 800;
        line-height: 1.05;
        color: #f6fbff;
        letter-spacing: -0.02em;
    }

    .brand-title .accent {
        color: var(--green);
    }

    .brand-sub {
        color: rgba(205, 218, 235, 0.68);
        font-size: 0.74rem;
    }

    .search-bar {
        height: 42px;
        border-radius: 12px;
        padding: 0 12px;
        display: flex;
        align-items: center;
        gap: 8px;
        background: rgba(16, 24, 42, 0.88);
        border: 1px solid rgba(123, 150, 188, 0.12);
        color: #d8e6f8;
    }

    .search-text {
        flex: 1;
        color: rgba(205, 218, 235, 0.50);
        font-size: 0.80rem;
    }

    .kbd {
        font-size: 0.69rem;
        color: rgba(205,218,235,0.48);
        padding: 2px 7px;
        border-radius: 7px;
        background: rgba(255,255,255,0.03);
        border: 1px solid rgba(255,255,255,0.04);
        font-weight: 700;
    }

    .header-actions {
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .pill-btn {
        height: 42px;
        border-radius: 12px;
        padding: 0 14px;
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(16, 24, 42, 0.92);
        border: 1px solid rgba(123, 150, 188, 0.12);
        color: #edf4ff;
        font-size: 0.80rem;
        font-weight: 600;
        white-space: nowrap;
    }

    .square-btn {
        width: 42px;
        justify-content: center;
        padding: 0;
    }

    .market-time {
        text-align: right;
        margin-left: 6px;
        white-space: nowrap;
    }

    .market-status {
        color: #ff6d76;
        font-size: 0.78rem;
        font-weight: 700;
    }

    .market-date {
        margin-top: 3px;
        color: rgba(205,218,235,0.66);
        font-size: 0.74rem;
    }

    .breadth-strip {
        padding: 12px 10px;
        margin-bottom: 10px;
    }

    .breadth-grid {
        display: grid;
        grid-template-columns: 1.2fr repeat(8, 1fr);
    }

    .breadth-item {
        min-height: 54px;
        padding: 0 12px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        border-right: 1px solid rgba(123,150,188,0.10);
    }

    .breadth-item:last-child { border-right: none; }

    .breadth-label {
        font-size: 0.69rem;
        color: rgba(205,218,235,0.68);
        margin-bottom: 5px;
        font-weight: 600;
    }

    .breadth-value {
        font-size: 0.98rem;
        font-weight: 800;
        line-height: 1;
        color: #f6fbff;
    }

    .breadth-sub {
        margin-top: 4px;
        font-size: 0.73rem;
        color: rgba(205,218,235,0.75);
    }

    .green { color: var(--green) !important; }
    .red { color: var(--red) !important; }

    .kpi-grid {
        display: grid;
        grid-template-columns: repeat(5, minmax(0, 1fr));
        gap: 10px;
        margin-bottom: 10px;
    }

    .kpi-card {
        padding: 12px;
        min-height: 86px;
    }

    .kpi-inner {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 8px;
        position: relative;
        z-index: 1;
    }

    .kpi-left {
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .kpi-icon {
        width: 34px;
        height: 34px;
        border-radius: 50%;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        background: rgba(255,255,255,0.02);
        font-size: 0.92rem;
        font-weight: 700;
        flex: 0 0 auto;
    }

    .kpi-label {
        font-size: 0.61rem;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        color: rgba(215, 225, 240, 0.72);
        font-weight: 700;
        margin-bottom: 7px;
        white-space: nowrap;
    }

    .kpi-value {
        font-size: 1.85rem;
        line-height: 1;
        font-weight: 800;
        color: #f7fbff;
        letter-spacing: -0.03em;
        margin-bottom: 7px;
    }

    .kpi-delta {
        font-size: 0.73rem;
        font-weight: 600;
    }

    .sparkline {
        width: 52px;
        height: 20px;
    }

    .section-panel {
        padding: 10px;
        margin-bottom: 12px;
    }

    .section-head {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 8px;
        margin-bottom: 10px;
        position: relative;
        z-index: 1;
    }

    .section-title {
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.04em;
        font-weight: 800;
        color: #eef5fe;
    }

    .mini-pill {
        font-size: 0.68rem;
        color: rgba(221,231,243,0.70);
        background: rgba(18,26,45,0.84);
        border: 1px solid rgba(123,150,188,0.10);
        border-radius: 10px;
        padding: 5px 10px;
        white-space: nowrap;
    }

    .chip-board {
        display: grid;
        grid-template-columns: repeat(9, minmax(0, 1fr));
        gap: 8px;
    }

    .rs-chip {
        border-radius: 12px;
        background: rgba(11, 20, 37, 0.85);
        border: 1px solid rgba(123,150,188,0.10);
        padding: 10px 10px 12px 10px;
        min-height: 52px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }

    .rs-chip-symbol {
        font-size: 0.72rem;
        color: #dfe9f7;
        font-weight: 700;
        margin-bottom: 6px;
    }

    .rs-chip-value {
        font-size: 0.96rem;
        color: #ffffff;
        font-weight: 800;
        line-height: 1;
    }

    .table-panel { padding: 10px; }
    .table-wrap { overflow-x: auto; }

    table.ms-table {
        width: 100%;
        border-collapse: collapse;
        font-size: 0.72rem;
        color: #dce7f6;
    }

    .ms-table thead th {
        text-align: left;
        font-size: 0.64rem;
        color: #8398b5;
        padding: 10px 8px;
        border-bottom: 1px solid rgba(123,150,188,0.12);
        font-weight: 700;
        white-space: nowrap;
    }

    .ms-table tbody td {
        padding: 11px 8px;
        border-bottom: 1px solid rgba(123,150,188,0.08);
        white-space: nowrap;
    }

    .detail-top, .summary-panel, .qualification-panel {
        padding: 10px;
        margin-bottom: 10px;
    }

    @media (max-width: 1200px) {
        .top-header-grid { grid-template-columns: 1fr; }
        .breadth-grid { grid-template-columns: repeat(2, 1fr); }
        .kpi-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
        .chip-board { grid-template-columns: repeat(4, minmax(0, 1fr)); }
    }

    @media (max-width: 760px) {
        .kpi-grid { grid-template-columns: 1fr; }
        .chip-board { grid-template-columns: repeat(2, minmax(0, 1fr)); }
        .nav-rail { min-height: auto; }
    }
    </style>
    """, unsafe_allow_html=True)


def render_sidebar_nav():
    st.markdown("""
    <div class="nav-rail">
        <div class="nav-group">
            <div class="brand-orb">✦</div>
        </div>
        <div class="nav-group">
            <div class="nav-btn active">⌂</div>
            <div class="nav-btn">↗</div>
            <div class="nav-btn">◎</div>
            <div class="nav-btn">▦</div>
            <div class="nav-btn">⌘</div>
            <div class="nav-btn">🔔</div>
        </div>
        <div class="nav-group">
            <div class="nav-badge pro">Pro</div>
            <div class="nav-badge">RM</div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_top_header():
    st.markdown("""
    <div class="panel top-header">
        <div class="top-header-grid">
            <div>
                <div class="brand-title">Nifty500 <span class="accent">Momentum Radar</span></div>
                <div class="brand-sub">Momentum. Relative Strength. Institutional Edge.</div>
            </div>
            <div class="search-bar">
                <div>⌕</div>
                <div class="search-text">Search by symbol or company</div>
                <div class="kbd">⌘ K</div>
            </div>
            <div class="header-actions">
                <div class="pill-btn">☆ Watchlist</div>
                <div class="pill-btn square-btn">⚙</div>
                <div class="market-time">
                    <div class="market-status">● Market Closed</div>
                    <div class="market-date">16 May 2025, 03:30 PM IST</div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_breadth_strip():
    st.markdown("""
    <div class="panel breadth-strip">
        <div class="breadth-grid">
            <div class="breadth-item"><div class="breadth-label">MARKET BREADTH</div><div class="breadth-sub">NIFTY 500</div></div>
            <div class="breadth-item"><div class="breadth-label green">Advancing</div><div class="breadth-value green">314</div><div class="breadth-sub">(62.8%)</div></div>
            <div class="breadth-item"><div class="breadth-label red">Declining</div><div class="breadth-value red">172</div><div class="breadth-sub">(34.4%)</div></div>
            <div class="breadth-item"><div class="breadth-label">Unchanged</div><div class="breadth-value">14</div><div class="breadth-sub">(2.8%)</div></div>
            <div class="breadth-item"><div class="breadth-label green">New 52W High</div><div class="breadth-value green">128</div></div>
            <div class="breadth-item"><div class="breadth-label red">New 52W Low</div><div class="breadth-value red">12</div></div>
            <div class="breadth-item"><div class="breadth-label">Above 20 DMA</div><div class="breadth-value green">286</div><div class="breadth-sub">(57.2%)</div></div>
            <div class="breadth-item"><div class="breadth-label">Above 50 DMA</div><div class="breadth-value green">272</div><div class="breadth-sub">(54.4%)</div></div>
            <div class="breadth-item"><div class="breadth-label">Above 200 DMA</div><div class="breadth-value green">245</div><div class="breadth-sub">(49.0%)</div></div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def _sparkline_svg(color):
    return f'''<svg class="sparkline" viewBox="0 0 100 32" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M3 23 C9 21, 16 24, 22 18 C27 14, 34 16, 40 12 C47 7, 55 12, 61 14 C67 16, 73 13, 80 7 C86 3, 92 6, 98 2" stroke="{color}" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'''


def render_kpi_cards():
    html = f"""
    <div class="kpi-grid">
        <div class="panel kpi-card"><div class="kpi-inner"><div class="kpi-left"><div class="kpi-icon" style="color:#20e38b;border:1px solid rgba(32,227,139,.42)">↗</div><div><div class="kpi-label">Momentum Leaders</div><div class="kpi-value">98</div><div class="kpi-delta" style="color:#20e38b">+ 18.1% vs yesterday</div></div></div><div>{_sparkline_svg("#20e38b")}</div></div></div>
        <div class="panel kpi-card"><div class="kpi-inner"><div class="kpi-left"><div class="kpi-icon" style="color:#1ad6ff;border:1px solid rgba(26,214,255,.42)">⌁</div><div><div class="kpi-label">Strong Relative Strength</div><div class="kpi-value">156</div><div class="kpi-delta" style="color:#1ad6ff">+ 22.7% vs yesterday</div></div></div><div>{_sparkline_svg("#1ad6ff")}</div></div></div>
        <div class="panel kpi-card"><div class="kpi-inner"><div class="kpi-left"><div class="kpi-icon" style="color:#f2aa3b;border:1px solid rgba(242,170,59,.42)">♛</div><div><div class="kpi-label">QMO Qualified</div><div class="kpi-value">74</div><div class="kpi-delta" style="color:#f2aa3b">+ 12.1% vs yesterday</div></div></div><div>{_sparkline_svg("#f2aa3b")}</div></div></div>
        <div class="panel kpi-card"><div class="kpi-inner"><div class="kpi-left"><div class="kpi-icon" style="color:#7f56ff;border:1px solid rgba(127,86,255,.42)">◔</div><div><div class="kpi-label">Average RS (Nifty500)</div><div class="kpi-value">0.86</div><div class="kpi-delta" style="color:#7f56ff">+ 0.04 vs yesterday</div></div></div><div>{_sparkline_svg("#7f56ff")}</div></div></div>
        <div class="panel kpi-card"><div class="kpi-inner"><div><div class="kpi-label">NIFTY 500</div><div class="kpi-value" style="font-size:1.55rem">DIXON</div><div class="kpi-delta" style="color:#8fa1bb">Dixon Technologies (India) Ltd.</div></div></div></div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)


def render_rs_leaderboard():
    chips = [
        ("DIXON", "2.56"),
        ("COFORGE", "2.31"),
        ("KALYANKJIL", "2.21"),
        ("ASTRAL", "2.08"),
        ("LTF", "1.98"),
        ("HAL", "1.93"),
        ("DEEPAKNTR", "1.87"),
        ("CGPOWER", "1.82"),
        ("JINDALSTEL", "1.78"),
    ]

    html = """
    <div class="panel section-panel">
        <div class="section-head">
            <div class="section-title">Relative Strength Leaderboard</div>
            <div class="mini-pill">View All</div>
        </div>
        <div class="chip-board">
    """
    for sym, val in chips:
        html += f"""
        <div class="rs-chip">
            <div class="rs-chip-symbol">{sym}</div>
            <div class="rs-chip-value">{val}</div>
        </div>
        """
    html += "</div></div>"
    st.markdown(html, unsafe_allow_html=True)


def render_scanner_table():
    st.markdown("""
    <div class="panel table-panel">
        <div class="section-head">
            <div class="section-title">Momentum Scanner (NIFTY 500)</div>
            <div class="mini-pill">302 Results</div>
        </div>
        <div class="table-wrap">
            <table class="ms-table">
                <thead>
                    <tr><th>#</th><th>Symbol</th><th>Company</th><th>Price</th><th>Daily %</th><th>Weekly %</th><th>RS</th><th>ATR RS</th><th>Dist. 52W High</th></tr>
                </thead>
                <tbody>
                    <tr><td>1</td><td>DIXON</td><td>Dixon Technologies (India) Ltd.</td><td>15,642.50</td><td class="green">+3.24%</td><td class="green">+8.91%</td><td>2.56</td><td>1.42</td><td class="red">-8.33%</td></tr>
                    <tr><td>2</td><td>COFORGE</td><td>Coforge Ltd.</td><td>8,144.30</td><td class="green">+2.87%</td><td class="green">+7.32%</td><td>2.31</td><td>1.28</td><td class="red">-12.41%</td></tr>
                    <tr><td>3</td><td>KALYANKJIL</td><td>Kalyan Jewellers India Ltd.</td><td>714.80</td><td class="green">+4.12%</td><td class="green">+10.27%</td><td>2.21</td><td>1.67</td><td class="red">-6.17%</td></tr>
                </tbody>
            </table>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_right_detail_panel():
    st.markdown("""
    <div class="panel detail-top">
        <div class="section-title">NIFTY 500 / DIXON</div>
        <div style="font-size:1.35rem;font-weight:800;margin-top:6px;">DIXON</div>
        <div style="font-size:0.72rem;color:#8ea1bb;margin-top:4px;">Dixon Technologies (India) Ltd.<br>Consumer Electronics · Small Cap</div>
        <div style="font-size:2rem;font-weight:800;margin-top:12px;">15,642.50</div>
        <div class="green" style="font-size:0.84rem;font-weight:700;margin-top:4px;">▲ 3.24% (490.40)</div>
    </div>

    <div class="panel summary-panel">
        <div class="section-head"><div class="section-title">Earnings Summary</div></div>
        <div style="font-size:0.75rem;color:#dce7f7;line-height:1.9;">
            Next Earnings: 29 May 2025<br>
            EPS (TTM): 132.45<br>
            EPS Growth (YoY): <span class="green">+78.6%</span><br>
            Surprise (Last): <span class="green">+12.3%</span>
        </div>
    </div>

    <div class="panel qualification-panel">
        <div class="section-head"><div class="section-title">Scanner Qualification</div></div>
        <div style="font-size:0.72rem;color:#dce7f7;line-height:2;">
            Price above 10W MA — <span class="green">Pass</span><br>
            Price above 20W MA — <span class="green">Pass</span><br>
            Price above 50W MA — <span class="green">Pass</span><br>
            Price above 200W MA — <span class="green">Pass</span><br>
            RS vs NIFTY500 &gt; 1.0 — <span class="green">Pass</span><br>
            Positive Weekly % — <span class="green">Pass</span><br>
            Positive Daily % — <span class="green">Pass</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
