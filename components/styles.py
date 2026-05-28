import streamlit as st


def inject_global_styles():
    st.markdown("""
    <style>
    :root {
        --bg: #050b16;
        --panel: #081120;
        --border: rgba(123, 150, 188, 0.14);
        --text: #eaf2fb;
        --muted: #8fa1bb;
        --green: #20e38b;
        --red: #ff5f6d;
        --cyan: #1ad6ff;
        --orange: #f2aa3b;
        --purple: #7f56ff;
    }

    .stApp {
        background: linear-gradient(180deg, #040915 0%, #050b16 100%);
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

    .heatmap-title {
        font-size: 0.90rem;
        font-weight: 800;
        letter-spacing: 0.03em;
        text-transform: uppercase;
        color: #eef5fe;
        margin-bottom: 8px;
    }

    div[data-testid="stSegmentedControl"] {
        margin-bottom: 12px;
    }

    div[data-testid="stSegmentedControl"] > label {
        display: none;
    }

    div[data-testid="stSegmentedControl"] [role="radiogroup"] {
        display: grid !important;
        grid-template-columns: repeat(4, minmax(0, 1fr));
        gap: 0px;
        background: rgba(255,255,255,0.02) !important;
        border-radius: 10px !important;
        overflow: hidden;
        width: fit-content;
    }

    div[data-testid="stSegmentedControl"] [role="radio"] {
        min-height: 38px;
        border-radius: 0 !important;
        background: rgba(255,255,255,0.92) !important;
        border-top: 1px solid rgba(123,150,188,0.12) !important;
        border-bottom: 1px solid rgba(123,150,188,0.12) !important;
        border-left: 1px solid rgba(123,150,188,0.12) !important;
        border-right: none !important;
        color: #cfd7e3 !important;
        font-size: 0.76rem !important;
        font-weight: 700 !important;
        box-shadow: none !important;
        padding: 0 18px !important;
    }

    div[data-testid="stSegmentedControl"] [role="radio"]:last-child {
        border-right: 1px solid rgba(123,150,188,0.12) !important;
    }

    div[data-testid="stSegmentedControl"] [role="radio"][aria-checked="true"] {
        background: rgba(53, 16, 18, 0.18) !important;
        color: #ff6a63 !important;
        border: 1px solid rgba(255, 95, 90, 0.88) !important;
        position: relative;
        z-index: 2;
    }

    .heatmap-widget {
        border-radius: 14px;
        overflow: hidden;
        background: rgba(255,255,255,0.02);
        border: 1px solid rgba(123,150,188,0.10);
    }

    .heatmap-grid {
        display: grid;
        grid-template-columns: repeat(6, minmax(0, 1fr));
        gap: 3px;
        background: rgba(255,255,255,0.03);
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

    @media (max-width: 1200px) {
        .top-header-grid { grid-template-columns: 1fr; }
        .breadth-grid { grid-template-columns: repeat(2, 1fr); }
        .kpi-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
        .heatmap-grid { grid-template-columns: repeat(3, minmax(0, 1fr)); }
        div[data-testid="stSegmentedControl"] [role="radiogroup"] {
            grid-template-columns: repeat(2, minmax(0, 1fr));
            width: 100%;
        }
    }

    @media (max-width: 760px) {
        .kpi-grid { grid-template-columns: 1fr; }
        .heatmap-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
        .nav-rail { min-height: auto; }
        div[data-testid="stSegmentedControl"] [role="radiogroup"] {
            grid-template-columns: 1fr;
            width: 100%;
        }
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


def _get_heatmap_data():
    return {
        "Broad Market Indices": [
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
        "Sectoral Indices": [
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
        "Thematic Indices": [
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
        "Strategy Indices": [
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


def render_heatmap_widget():
    st.markdown('<div class="heatmap-title">HEATMAP</div>', unsafe_allow_html=True)

    selected = st.segmented_control(
        "",
        ["Broad Market Indices", "Sectoral Indices", "Thematic Indices", "Strategy Indices"],
        default="Broad Market Indices",
        selection_mode="single",
        key="heatmap_selector",
    )

    if not selected:
        selected = "Broad Market Indices"

    data = _get_heatmap_data()[selected]

    html = '<div class="heatmap-widget"><div class="heatmap-grid">'
    for name, score, change, bg, txt in data:
        html += f"""
        <div class="heat-tile {bg}">
            <div class="heat-name">{name}</div>
            <div class="heat-score">{score}</div>
            <div class="heat-change {txt}">{change}</div>
        </div>
        """
    html += '</div></div>'

    st.markdown(html, unsafe_allow_html=True)
