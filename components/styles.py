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
        padding-bottom: 0.75rem;
    }

    [data-testid="stHeader"] { display: none; }
    [data-testid="stSidebar"] { display: none; }

    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background: transparent;
        margin-bottom: 10px;
    }

    .stTabs [data-baseweb="tab"] {
        height: 40px;
        padding: 0 16px;
        border-radius: 12px;
        background: rgba(16, 24, 42, 0.90);
        border: 1px solid rgba(123, 150, 188, 0.12);
        color: #95a8c2;
        font-size: 0.80rem;
        font-weight: 700;
    }

    .stTabs [aria-selected="true"] {
        background: linear-gradient(180deg, rgba(42,109,255,0.18), rgba(25,67,168,0.12));
        color: #eaf2fb;
        border-color: rgba(75, 127, 255, 0.22);
        box-shadow: inset 0 -2px 0 rgba(255, 89, 107, 0.90);
    }

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
        margin-bottom: 12px;
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

    .heatmap-widget-title {
        padding: 12px 14px;
        margin-bottom: 10px;
    }

    .widget-title-text {
        font-size: 0.88rem;
        font-weight: 800;
        letter-spacing: 0.03em;
        text-transform: uppercase;
        color: #eef5fe;
        position: relative;
        z-index: 1;
    }

    .heatmap-page {
        padding: 12px;
        min-height: 720px;
    }

    .section-head {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 8px;
        margin-bottom: 12px;
        position: relative;
        z-index: 1;
    }

    .section-title {
        font-size: 0.78rem;
        text-transform: uppercase;
        letter-spacing: 0.04em;
        font-weight: 800;
        color: #eef5fe;
    }

    .controls-row {
        display: flex;
        align-items: center;
        gap: 8px;
        flex-wrap: wrap;
        margin-bottom: 12px;
        position: relative;
        z-index: 1;
    }

    .mini-pill {
        font-size: 0.69rem;
        color: rgba(221,231,243,0.78);
        background: rgba(18,26,45,0.84);
        border: 1px solid rgba(123,150,188,0.10);
        border-radius: 10px;
        padding: 6px 11px;
        white-space: nowrap;
    }

    .heatmap-grid {
        display: grid;
        grid-template-columns: repeat(6, minmax(0, 1fr));
        gap: 4px;
        border-radius: 14px;
        overflow: hidden;
        background: rgba(255,255,255,0.03);
        position: relative;
        z-index: 1;
    }

    .heat-tile {
        min-height: 126px;
        padding: 14px 10px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
    }

    .heat-name {
        font-size: 0.84rem;
        font-weight: 700;
        color: #f8fbff;
        margin-bottom: 10px;
        line-height: 1.15;
        max-width: 92%;
    }

    .heat-score {
        font-size: 1.48rem;
        font-weight: 800;
        color: white;
        margin-bottom: 8px;
        line-height: 1;
    }

    .heat-change {
        font-size: 0.87rem;
        font-weight: 700;
    }

    .heat-green-5 { background: linear-gradient(180deg, #125238 0%, #0f4430 100%); }
    .heat-green-4 { background: linear-gradient(180deg, #10472f 0%, #0d3a28 100%); }
    .heat-green-3 { background: linear-gradient(180deg, #0d3d29 0%, #0a3121 100%); }
    .heat-green-2 { background: linear-gradient(180deg, #0a3322 0%, #08291b 100%); }
    .heat-green-1 { background: linear-gradient(180deg, #08281c 0%, #071f16 100%); }
    .heat-red-1 { background: linear-gradient(180deg, #2a1218 0%, #210d13 100%); }
    .heat-red-2 { background: linear-gradient(180deg, #351118 0%, #280d13 100%); }
    .heat-red-3 { background: linear-gradient(180deg, #401118 0%, #300d13 100%); }
    .heat-red-4 { background: linear-gradient(180deg, #4b1118 0%, #370d13 100%); }
    .heat-red-5 { background: linear-gradient(180deg, #571118 0%, #3f0d13 100%); }
    .heat-neutral { background: linear-gradient(180deg, #121d33 0%, #0e1727 100%); }

    .legend-row {
        display: flex;
        justify-content: center;
        gap: 8px;
        margin-top: 14px;
        flex-wrap: wrap;
        position: relative;
        z-index: 1;
    }

    .legend-pill {
        min-width: 94px;
        text-align: center;
        padding: 6px 10px;
        border-radius: 8px;
        color: #edf5ff;
        font-size: 0.69rem;
        font-weight: 700;
    }

    .legend-red-3 { background: #4a1019; }
    .legend-red-2 { background: #391118; }
    .legend-red-1 { background: #2a1217; }
    .legend-green-1 { background: #133427; }
    .legend-green-2 { background: #0f4630; }
    .legend-green-3 { background: #0f5a3d; }

    @media (max-width: 1200px) {
        .top-header-grid { grid-template-columns: 1fr; }
        .breadth-grid { grid-template-columns: repeat(2, 1fr); }
        .kpi-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
        .heatmap-grid { grid-template-columns: repeat(3, minmax(0, 1fr)); }
    }

    @media (max-width: 760px) {
        .kpi-grid { grid-template-columns: 1fr; }
        .heatmap-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
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
        <div class="panel kpi-card"><div class="kpi-inner"><div><div class="kpi-label">Universe</div><div class="kpi-value" style="font-size:1.55rem">NIFTY 500</div><div class="kpi-delta" style="color:#8fa1bb">Heatmap view</div></div></div></div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)


def render_heatmap_widget_header():
    st.markdown("""
    <div class="panel heatmap-widget-title">
        <div class="widget-title-text">Heatmap</div>
    </div>
    """, unsafe_allow_html=True)


def render_heatmap_page(mode="broad"):
    titles = {
        "broad": "Broad Market Indices",
        "sectoral": "Sectoral Indices",
        "thematic": "Thematic Indices",
        "strategy": "Strategy Indices",
    }

    data = {
        "broad": [
            ("NIFTY 50", "1.24%", "+1.24%", "heat-green-4", "green"),
            ("NIFTY NEXT 50", "1.08%", "+1.08%", "heat-green-3", "green"),
            ("NIFTY 100", "0.96%", "+0.96%", "heat-green-3", "green"),
            ("NIFTY 200", "0.88%", "+0.88%", "heat-green-2", "green"),
            ("NIFTY 500", "0.82%", "+0.82%", "heat-green-2", "green"),
            ("NIFTY MIDCAP 50", "1.41%", "+1.41%", "heat-green-5", "green"),
            ("NIFTY MIDCAP 100", "1.28%", "+1.28%", "heat-green-4", "green"),
            ("NIFTY SMALLCAP 100", "1.62%", "+1.62%", "heat-green-5", "green"),
            ("NIFTY SMALLCAP 250", "1.74%", "+1.74%", "heat-green-5", "green"),
            ("NIFTY MICROCAP 250", "1.11%", "+1.11%", "heat-green-3", "green"),
            ("NIFTY LARGEMIDCAP 250", "0.77%", "+0.77%", "heat-green-2", "green"),
            ("INDIA VIX", "-1.92%", "-1.92%", "heat-red-3", "red"),
        ],
        "sectoral": [
            ("NIFTY BANK", "0.42%", "+0.42%", "heat-green-1", "green"),
            ("NIFTY FIN SERVICE", "0.36%", "+0.36%", "heat-green-1", "green"),
            ("NIFTY IT", "-0.54%", "-0.54%", "heat-red-2", "red"),
            ("NIFTY AUTO", "1.31%", "+1.31%", "heat-green-4", "green"),
            ("NIFTY FMCG", "-0.48%", "-0.48%", "heat-red-2", "red"),
            ("NIFTY PHARMA", "-0.22%", "-0.22%", "heat-red-1", "red"),
            ("NIFTY METAL", "1.58%", "+1.58%", "heat-green-5", "green"),
            ("NIFTY REALTY", "-0.84%", "-0.84%", "heat-red-3", "red"),
            ("NIFTY MEDIA", "-1.14%", "-1.14%", "heat-red-4", "red"),
            ("NIFTY PSU BANK", "0.92%", "+0.92%", "heat-green-2", "green"),
            ("NIFTY OIL & GAS", "0.74%", "+0.74%", "heat-green-2", "green"),
            ("NIFTY CONSUMER DURABLES", "1.18%", "+1.18%", "heat-green-3", "green"),
        ],
        "thematic": [
            ("NIFTY INDIA DEFENCE", "1.84%", "+1.84%", "heat-green-5", "green"),
            ("NIFTY INDIA DIGITAL", "1.26%", "+1.26%", "heat-green-4", "green"),
            ("NIFTY ENERGY", "0.81%", "+0.81%", "heat-green-2", "green"),
            ("NIFTY INFRASTRUCTURE", "1.12%", "+1.12%", "heat-green-3", "green"),
            ("NIFTY COMMODITIES", "0.94%", "+0.94%", "heat-green-2", "green"),
            ("NIFTY MNC", "-0.21%", "-0.21%", "heat-red-1", "red"),
            ("NIFTY PSE", "0.62%", "+0.62%", "heat-green-1", "green"),
            ("NIFTY HOUSING", "-0.42%", "-0.42%", "heat-red-2", "red"),
            ("NIFTY RURAL", "0.37%", "+0.37%", "heat-green-1", "green"),
            ("NIFTY CONSUMPTION", "-0.35%", "-0.35%", "heat-red-1", "red"),
            ("NIFTY MANUFACTURING", "1.47%", "+1.47%", "heat-green-4", "green"),
            ("NIFTY TRANSPORTATION", "1.03%", "+1.03%", "heat-green-3", "green"),
        ],
        "strategy": [
            ("NIFTY ALPHA 50", "1.66%", "+1.66%", "heat-green-5", "green"),
            ("NIFTY QUALITY LOW VOL 30", "0.74%", "+0.74%", "heat-green-2", "green"),
            ("NIFTY LOW VOLATILITY 50", "0.28%", "+0.28%", "heat-green-1", "green"),
            ("NIFTY MOMENTUM 30", "1.58%", "+1.58%", "heat-green-5", "green"),
            ("NIFTY VALUE 20", "-0.16%", "-0.16%", "heat-red-1", "red"),
            ("NIFTY GROWTH SECTORS 15", "1.12%", "+1.12%", "heat-green-3", "green"),
            ("NIFTY100 QUALITY 30", "0.64%", "+0.64%", "heat-green-2", "green"),
            ("NIFTY200 MOMENTUM 30", "1.44%", "+1.44%", "heat-green-4", "green"),
            ("NIFTY MIDCAP150 MOMENTUM 50", "1.88%", "+1.88%", "heat-green-5", "green"),
            ("NIFTY SMALLCAP250 MOMENTUM QUALITY 100", "1.97%", "+1.97%", "heat-green-5", "green"),
            ("NIFTY50 VALUE 20", "-0.38%", "-0.38%", "heat-red-1", "red"),
            ("NIFTY100 ALPHA 30", "1.21%", "+1.21%", "heat-green-3", "green"),
        ],
    }

    rows = data[mode]

    html = f"""
    <div class="panel heatmap-page">
        <div class="section-head">
            <div class="section-title">{titles[mode]}</div>
            <div class="mini-pill">NSE Indices</div>
        </div>

        <div class="controls-row">
            <div class="mini-pill">1D Change</div>
            <div class="mini-pill">Sorted by Performance</div>
            <div class="mini-pill">Index Universe</div>
            <div class="mini-pill">Heat Scale</div>
        </div>

        <div class="heatmap-grid">
    """

    for name, score, change, bg, txt in rows:
        html += f"""
        <div class="heat-tile {bg}">
            <div class="heat-name">{name}</div>
            <div class="heat-score">{score}</div>
            <div class="heat-change {txt}">{change}</div>
        </div>
        """

    html += """
        </div>

        <div class="legend-row">
            <div class="legend-pill legend-red-3">Deep Red</div>
            <div class="legend-pill legend-red-2">Red</div>
            <div class="legend-pill legend-red-1">Soft Red</div>
            <div class="legend-pill legend-green-1">Soft Green</div>
            <div class="legend-pill legend-green-2">Green</div>
            <div class="legend-pill legend-green-3">Deep Green</div>
        </div>
    </div>
    """

    st.markdown(html, unsafe_allow_html=True)
