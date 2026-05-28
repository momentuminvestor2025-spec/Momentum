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
        --green-2: #10c972;
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
        padding-top: 0.4rem;
        padding-left: 0.5rem;
        padding-right: 0.5rem;
        padding-bottom: 0.6rem;
    }

    [data-testid="stHeader"] { display: none; }
    [data-testid="stToolbar"] { right: 0.5rem; top: 0.25rem; }
    [data-testid="stSidebar"] { display: none; }

    .app-shell {
        display: flex;
        gap: 12px;
        align-items: stretch;
        min-height: calc(100vh - 1rem);
    }

    .nav-rail {
        width: 52px;
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
        box-shadow: inset 0 1px 0 rgba(255,255,255,0.04);
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

    .main-shell {
        flex: 1;
        min-width: 0;
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

    .brand-wrap {
        display: flex;
        flex-direction: column;
        gap: 2px;
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
        gap: 0;
    }

    .breadth-item {
        min-height: 54px;
        padding: 0 12px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        border-right: 1px solid rgba(123,150,188,0.10);
    }

    .breadth-item:last-child {
        border-right: none;
    }

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
    .orange { color: var(--orange) !important; }
    .purple { color: var(--purple) !important; }
    .cyan { color: var(--cyan) !important; }

    .kpi-grid {
        display: grid;
        grid-template-columns: repeat(5, minmax(0, 1fr));
        gap: 10px;
        margin-bottom: 10px;
    }

    .kpi-card {
        padding: 12px 12px 10px 12px;
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
        min-width: 0;
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

    .kpi-copy {
        min-width: 0;
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

    .kpi-right {
        min-width: 52px;
        display: flex;
        align-items: flex-end;
        justify-content: flex-end;
    }

    .sparkline {
        width: 52px;
        height: 20px;
        opacity: 0.95;
    }

    .kpi-green .kpi-icon { color: var(--green); border: 1px solid rgba(32,227,139,0.42); }
    .kpi-cyan .kpi-icon { color: var(--cyan); border: 1px solid rgba(26,214,255,0.42); }
    .kpi-gold .kpi-icon { color: var(--orange); border: 1px solid rgba(242,170,59,0.42); }
    .kpi-purple .kpi-icon { color: var(--purple); border: 1px solid rgba(127,86,255,0.42); }

    .section-panel {
        padding: 10px 10px 10px 10px;
        margin-bottom: 10px;
    }

    .section-head {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 8px;
        margin-bottom: 8px;
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

    .section-title .muted {
        color: rgba(205,218,235,0.45);
        margin-left: 4px;
    }

    .section-actions {
        display: flex;
        align-items: center;
        gap: 6px;
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

    .heatmap-grid {
        display: grid;
        grid-template-columns: repeat(6, minmax(0, 1fr));
        gap: 2px;
        border-radius: 12px;
        overflow: hidden;
        background: rgba(255,255,255,0.03);
        position: relative;
        z-index: 1;
    }

    .heat-tile {
        min-height: 76px;
        padding: 10px 8px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
    }

    .heat-name {
        font-size: 0.74rem;
        font-weight: 700;
        color: #f8fbff;
        margin-bottom: 7px;
        line-height: 1.1;
    }

    .heat-score {
        font-size: 1.20rem;
        font-weight: 800;
        color: white;
        margin-bottom: 6px;
        line-height: 1;
    }

    .heat-change {
        font-size: 0.76rem;
        font-weight: 700;
    }

    .heat-green-5 { background: linear-gradient(180deg, #104d35 0%, #0e412e 100%); }
    .heat-green-4 { background: linear-gradient(180deg, #0d432f 0%, #0c3728 100%); }
    .heat-green-3 { background: linear-gradient(180deg, #0b3928 0%, #092f21 100%); }
    .heat-green-2 { background: linear-gradient(180deg, #092f22 0%, #08261c 100%); }
    .heat-green-1 { background: linear-gradient(180deg, #08251b 0%, #071d15 100%); }

    .heat-red-1 { background: linear-gradient(180deg, #281119 0%, #1f0d13 100%); }
    .heat-red-2 { background: linear-gradient(180deg, #331119 0%, #270d13 100%); }
    .heat-red-3 { background: linear-gradient(180deg, #3e1119 0%, #2f0d13 100%); }
    .heat-red-4 { background: linear-gradient(180deg, #481119 0%, #360d13 100%); }
    .heat-red-5 { background: linear-gradient(180deg, #531119 0%, #3c0d13 100%); }
    .heat-neutral { background: linear-gradient(180deg, #101a2f 0%, #0d1525 100%); }

    .legend-row {
        display: flex;
        justify-content: center;
        gap: 6px;
        margin-top: 9px;
        flex-wrap: wrap;
        position: relative;
        z-index: 1;
    }

    .legend-pill {
        min-width: 84px;
        text-align: center;
        padding: 4px 8px;
        border-radius: 7px;
        color: #edf5ff;
        font-size: 0.67rem;
        font-weight: 700;
    }

    .legend-red-3 { background: #4a1019; }
    .legend-red-2 { background: #3a1118; }
    .legend-red-1 { background: #2b1217; }
    .legend-green-1 { background: #123326; }
    .legend-green-2 { background: #0f4630; }
    .legend-green-3 { background: #0e5a3d; }

    .chip-board {
        display: grid;
        grid-template-columns: repeat(9, minmax(0, 1fr));
        gap: 8px;
        position: relative;
        z-index: 1;
    }

    .rs-chip {
        border-radius: 12px;
        background: rgba(11, 20, 37, 0.85);
        border: 1px solid rgba(123,150,188,0.10);
        padding: 7px 8px;
        min-height: 42px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }

    .rs-chip-top {
        display: flex;
        align-items: center;
        gap: 6px;
        margin-bottom: 4px;
    }

    .rs-chip-dot {
        width: 10px;
        height: 10px;
        border-radius: 50%;
        background: linear-gradient(180deg, #8bd1ff, #4f88ff);
        flex: 0 0 auto;
    }

    .rs-chip-symbol {
        font-size: 0.62rem;
        color: #dfe9f7;
        font-weight: 700;
    }

    .rs-chip-value {
        font-size: 0.84rem;
        color: #ffffff;
        font-weight: 800;
        line-height: 1;
    }

    .table-panel {
        padding: 10px;
    }

    .table-toolbar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 8px;
        margin-bottom: 8px;
        position: relative;
        z-index: 1;
    }

    .toolbar-left, .toolbar-right {
        display: flex;
        align-items: center;
        gap: 6px;
        flex-wrap: wrap;
    }

    .toolbar-chip {
        font-size: 0.68rem;
        color: #dce7f6;
        background: rgba(18, 26, 45, 0.84);
        border: 1px solid rgba(123,150,188,0.10);
        border-radius: 10px;
        padding: 5px 9px;
    }

    .table-wrap {
        overflow-x: auto;
        position: relative;
        z-index: 1;
    }

    table.ms-table {
        width: 100%;
        border-collapse: collapse;
        font-size: 0.72rem;
        color: #dce7f6;
    }

    .ms-table thead th {
        text-align: left;
        font-size: 0.64rem;
        text-transform: none;
        color: #8398b5;
        padding: 8px 8px;
        border-bottom: 1px solid rgba(123,150,188,0.12);
        font-weight: 700;
        white-space: nowrap;
    }

    .ms-table tbody td {
        padding: 8px 8px;
        border-bottom: 1px solid rgba(123,150,188,0.08);
        white-space: nowrap;
        vertical-align: middle;
    }

    .ms-table tbody tr:hover {
        background: rgba(255,255,255,0.015);
    }

    .rank {
        color: #91a4be;
        width: 20px;
    }

    .stock-cell {
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .stock-avatar {
        width: 18px;
        height: 18px;
        border-radius: 50%;
        background: linear-gradient(180deg, #f8fbff, #a7b5cc);
        color: #0b1120;
        font-size: 0.50rem;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        font-weight: 800;
    }

    .company-muted {
        color: #8093af;
        font-size: 0.66rem;
    }

    .metric-good {
        color: var(--green);
        font-weight: 700;
    }

    .metric-bad {
        color: var(--red);
        font-weight: 700;
    }

    .check-dot {
        width: 14px;
        height: 14px;
        border-radius: 50%;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        font-size: 0.55rem;
        font-weight: 800;
        color: #07101d;
    }

    .check-green {
        background: linear-gradient(180deg, #53ea93, #2fbc6b);
    }

    .check-yellow {
        background: linear-gradient(180deg, #f5c65a, #dfa22b);
    }

    .table-footer {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 8px;
        padding-top: 8px;
        color: #8297b3;
        font-size: 0.68rem;
        position: relative;
        z-index: 1;
    }

    .pagination {
        display: flex;
        align-items: center;
        gap: 6px;
    }

    .page-btn {
        min-width: 24px;
        height: 22px;
        border-radius: 7px;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        background: rgba(255,255,255,0.02);
        border: 1px solid rgba(123,150,188,0.10);
        color: #9bb0c9;
        font-size: 0.67rem;
    }

    .page-btn.active {
        background: rgba(45,140,255,0.16);
        color: #9fcbff;
        border-color: rgba(45,140,255,0.18);
    }

    .detail-top {
        padding: 10px 10px 12px;
        margin-bottom: 10px;
    }

    .detail-head {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 8px;
        margin-bottom: 10px;
        position: relative;
        z-index: 1;
    }

    .tiny-label {
        font-size: 0.61rem;
        color: #7e92ae;
        text-transform: uppercase;
        letter-spacing: 0.04em;
        font-weight: 700;
    }

    .detail-title {
        font-size: 1.35rem;
        color: #f8fbff;
        font-weight: 800;
        line-height: 1.05;
        margin-top: 4px;
    }

    .detail-sub {
        font-size: 0.72rem;
        color: #8ea1bb;
        margin-top: 4px;
    }

    .price-box {
        margin-top: 10px;
        position: relative;
        z-index: 1;
    }

    .price-main {
        font-size: 2.1rem;
        font-weight: 800;
        color: #f9fbff;
        letter-spacing: -0.03em;
        line-height: 1;
    }

    .price-change {
        font-size: 0.84rem;
        font-weight: 700;
        margin-top: 5px;
        color: var(--green);
    }

    .mini-stats {
        display: grid;
        grid-template-columns: repeat(4, minmax(0, 1fr));
        gap: 8px;
        margin-top: 12px;
        position: relative;
        z-index: 1;
    }

    .mini-stat {
        min-width: 0;
    }

    .mini-stat-label {
        font-size: 0.60rem;
        color: #7c90ad;
        margin-bottom: 4px;
    }

    .mini-stat-value {
        font-size: 0.76rem;
        color: #e8f0fa;
        font-weight: 700;
    }

    .time-tabs {
        display: flex;
        gap: 5px;
        margin-top: 10px;
        flex-wrap: wrap;
        position: relative;
        z-index: 1;
    }

    .time-pill {
        font-size: 0.62rem;
        color: #9cb0c9;
        background: rgba(255,255,255,0.02);
        border: 1px solid rgba(123,150,188,0.10);
        border-radius: 7px;
        padding: 4px 7px;
    }

    .time-pill.active {
        color: #9fcaff;
        background: rgba(45,140,255,0.16);
        border-color: rgba(45,140,255,0.18);
    }

    .chart-box {
        margin-top: 10px;
        height: 270px;
        border-radius: 14px;
        background:
            linear-gradient(180deg, rgba(8,16,32,0.55), rgba(6,12,24,0.82)),
            linear-gradient(180deg, #07101d 0%, #07101b 100%);
        border: 1px solid rgba(123,150,188,0.10);
        position: relative;
        overflow: hidden;
    }

    .chart-grid {
        position: absolute;
        inset: 0;
        background-image:
            linear-gradient(to right, rgba(255,255,255,0.045) 1px, transparent 1px),
            linear-gradient(to bottom, rgba(255,255,255,0.045) 1px, transparent 1px);
        background-size: 46px 46px;
        opacity: 0.40;
    }

    .chart-svg {
        position: absolute;
        inset: 0;
        width: 100%;
        height: 100%;
    }

    .summary-panel, .qualification-panel {
        padding: 10px;
        margin-bottom: 10px;
    }

    .summary-grid {
        display: grid;
        grid-template-columns: repeat(4, minmax(0, 1fr));
        gap: 8px;
        position: relative;
        z-index: 1;
    }

    .summary-card {
        border-radius: 12px;
        padding: 9px 8px;
        background: rgba(11, 20, 37, 0.84);
        border: 1px solid rgba(123,150,188,0.10);
    }

    .summary-card .label {
        font-size: 0.60rem;
        color: #7d91ad;
        margin-bottom: 6px;
    }

    .summary-card .value {
        font-size: 0.82rem;
        color: #f8fbff;
        font-weight: 800;
        line-height: 1;
    }

    .summary-card .value.good {
        color: var(--green);
    }

    .qual-row {
        display: grid;
        grid-template-columns: 1.7fr 1fr auto;
        gap: 8px;
        align-items: center;
        padding: 7px 0;
        border-bottom: 1px solid rgba(123,150,188,0.08);
        position: relative;
        z-index: 1;
    }

    .qual-row:last-child {
        border-bottom: none;
    }

    .qual-label {
        font-size: 0.69rem;
        color: #dce7f7;
    }

    .qual-value {
        font-size: 0.70rem;
        color: #8ea2bc;
        text-align: right;
    }

    .qual-status {
        font-size: 0.70rem;
        font-weight: 800;
        color: var(--green);
    }

    .tag-row {
        display: flex;
        gap: 6px;
        flex-wrap: wrap;
        margin-top: 10px;
        position: relative;
        z-index: 1;
    }

    .qual-tag {
        padding: 4px 10px;
        border-radius: 999px;
        font-size: 0.64rem;
        font-weight: 800;
        border: 1px solid rgba(123,150,188,0.14);
        background: rgba(255,255,255,0.02);
    }

    .tag-green { color: var(--green); border-color: rgba(32,227,139,0.18); }
    .tag-orange { color: var(--orange); border-color: rgba(242,170,59,0.18); }
    .tag-purple { color: var(--purple); border-color: rgba(127,86,255,0.18); }

    .data-note {
        margin-top: 10px;
        font-size: 0.62rem;
        color: #70839f;
        position: relative;
        z-index: 1;
    }

    .floating-chat {
        position: fixed;
        right: 12px;
        bottom: 12px;
        width: 42px;
        height: 42px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        background: linear-gradient(180deg, #2b86ff, #1558d6);
        color: white;
        font-size: 1rem;
        box-shadow: 0 14px 24px rgba(14, 74, 196, 0.32);
        z-index: 999;
    }

    @media (max-width: 1400px) {
        .kpi-grid { grid-template-columns: repeat(3, minmax(0, 1fr)); }
        .chip-board { grid-template-columns: repeat(6, minmax(0, 1fr)); }
    }

    @media (max-width: 1200px) {
        .top-header-grid { grid-template-columns: 1fr; }
        .header-actions { flex-wrap: wrap; }
        .breadth-grid { grid-template-columns: repeat(2, 1fr); }
        .breadth-item {
            border-right: none;
            border-bottom: 1px solid rgba(123,150,188,0.08);
            padding-top: 9px;
            padding-bottom: 9px;
        }
        .kpi-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
        .heatmap-grid { grid-template-columns: repeat(3, minmax(0, 1fr)); }
        .chip-board { grid-template-columns: repeat(4, minmax(0, 1fr)); }
        .summary-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
    }

    @media (max-width: 900px) {
        .app-shell {
            flex-direction: column;
        }
        .nav-rail {
            width: 100%;
            min-height: auto;
            position: relative;
            top: auto;
            flex-direction: row;
            justify-content: space-between;
            padding: 8px;
        }
        .nav-group {
            flex-direction: row;
            width: auto;
        }
    }

    @media (max-width: 760px) {
        .kpi-grid { grid-template-columns: 1fr; }
        .heatmap-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
        .chip-board { grid-template-columns: repeat(2, minmax(0, 1fr)); }
        .mini-stats { grid-template-columns: repeat(2, minmax(0, 1fr)); }
        .qual-row { grid-template-columns: 1fr; }
    }
    </style>
    """, unsafe_allow_html=True)


def render_app_shell_open():
    st.markdown('<div class="app-shell">', unsafe_allow_html=True)


def render_app_shell_close():
    st.markdown('<div class="floating-chat">💬</div></div>', unsafe_allow_html=True)


def render_main_shell_open():
    st.markdown('<div class="main-shell">', unsafe_allow_html=True)


def render_main_shell_close():
    st.markdown('</div>', unsafe_allow_html=True)


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
            <div class="brand-wrap">
                <div class="brand-title">Nifty500 <span class="accent">Momentum Radar</span></div>
                <div class="brand-sub">Momentum. Relative Strength. Institutional Edge.</div>
            </div>

            <div class="search-bar">
                <div>⌕</div>
                <div class="search-text">Search by symbol or company</div>
                <div class="kbd">⌘ K</div>
            </div>

            <div class="header-actions">
                <div class="pill-btn">☆ <span>Watchlist</span></div>
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
            <div class="breadth-item">
                <div class="breadth-label">MARKET BREADTH</div>
                <div class="breadth-sub">NIFTY 500</div>
            </div>

            <div class="breadth-item">
                <div class="breadth-label green">Advancing</div>
                <div class="breadth-value green">314</div>
                <div class="breadth-sub">(62.8%)</div>
            </div>

            <div class="breadth-item">
                <div class="breadth-label red">Declining</div>
                <div class="breadth-value red">172</div>
                <div class="breadth-sub">(34.4%)</div>
            </div>

            <div class="breadth-item">
                <div class="breadth-label">Unchanged</div>
                <div class="breadth-value">14</div>
                <div class="breadth-sub">(2.8%)</div>
            </div>

            <div class="breadth-item">
                <div class="breadth-label green">New 52W High</div>
                <div class="breadth-value green">128</div>
            </div>

            <div class="breadth-item">
                <div class="breadth-label red">New 52W Low</div>
                <div class="breadth-value red">12</div>
            </div>

            <div class="breadth-item">
                <div class="breadth-label">Above 20 DMA</div>
                <div class="breadth-value green">286</div>
                <div class="breadth-sub">(57.2%)</div>
            </div>

            <div class="breadth-item">
                <div class="breadth-label">Above 50 DMA</div>
                <div class="breadth-value green">272</div>
                <div class="breadth-sub">(54.4%)</div>
            </div>

            <div class="breadth-item">
                <div class="breadth-label">Above 200 DMA</div>
                <div class="breadth-value green">245</div>
                <div class="breadth-sub">(49.0%)</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def _sparkline_svg(color):
    return f"""
    <svg class="sparkline" viewBox="0 0 100 32" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M3 23 C9 21, 16 24, 22 18 C27 14, 34 16, 40 12 C47 7, 55 12, 61 14 C67 16, 73 13, 80 7 C86 3, 92 6, 98 2"
            stroke="{color}" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
    """


def render_kpi_cards():
    cards = [
        ("kpi-green", "↗", "Momentum Leaders", "98", "+ 18.1% vs yesterday", "#20e38b"),
        ("kpi-cyan", "⌁", "Strong Relative Strength", "156", "+ 22.7% vs yesterday", "#1ad6ff"),
        ("kpi-gold", "♛", "QMO Qualified", "74", "+ 12.1% vs yesterday", "#f2aa3b"),
        ("kpi-purple", "◔", "Average RS (Nifty500)", "0.86", "+ 0.04 vs yesterday", "#7f56ff"),
        ("", "", "Nifty 500", "DIXON", "Dixon Technologies (India) Ltd.", None),
    ]

    html = '<div class="kpi-grid">'
    for cls, icon, label, value, delta, color in cards:
        if label == "Nifty 500":
            html += f"""
            <div class="panel kpi-card">
                <div class="kpi-inner">
                    <div class="kpi-copy" style="width:100%;">
                        <div class="kpi-label">NIFTY 500 <span style="float:right;color:#7f93ad;">DIXON</span></div>
                        <div style="font-size:1.7rem;font-weight:800;color:#f8fbff;line-height:1;">DIXON</div>
                        <div style="margin-top:5px;font-size:0.68rem;color:#8fa1bb;">Dixon Technologies (India) Ltd.</div>
                    </div>
                </div>
            </div>
            """
        else:
            html += f"""
            <div class="panel kpi-card {cls}">
                <div class="kpi-inner">
                    <div class="kpi-left">
                        <div class="kpi-icon">{icon}</div>
                        <div class="kpi-copy">
                            <div class="kpi-label">{label}</div>
                            <div class="kpi-value">{value}</div>
                            <div class="kpi-delta" style="color:{color};">{delta}</div>
                        </div>
                    </div>
                    <div class="kpi-right">{_sparkline_svg(color)}</div>
                </div>
            </div>
            """
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)


def render_heatmap_panel():
    sectors = [
        ("Capital Goods", "1.67", "+2.45%", "heat-green-5", "green"),
        ("Metals", "1.54", "+2.18%", "heat-green-4", "green"),
        ("Auto", "1.32", "+1.72%", "heat-green-3", "green"),
        ("Construction", "1.21", "+1.35%", "heat-green-3", "green"),
        ("Chemicals", "1.15", "+1.08%", "heat-green-2", "green"),
        ("Consumer Durables", "1.07", "+0.98%", "heat-green-2", "green"),
        ("Oil & Gas", "1.03", "+0.71%", "heat-green-2", "green"),
        ("Power", "0.98", "+0.32%", "heat-green-1", "green"),
        ("Telecom", "0.94", "+0.12%", "heat-green-1", "green"),
        ("IT Services", "0.89", "-0.18%", "heat-neutral", "red"),
        ("Healthcare", "0.86", "-0.34%", "heat-red-1", "red"),
        ("FMCG", "0.82", "-0.56%", "heat-red-2", "red"),
        ("Services", "0.79", "-0.67%", "heat-red-2", "red"),
        ("Financials", "0.76", "-0.98%", "heat-red-3", "red"),
        ("Realty", "0.68", "-1.21%", "heat-red-3", "red"),
        ("Retail", "0.62", "-1.56%", "heat-red-4", "red"),
        ("Media", "0.58", "-1.87%", "heat-red-4", "red"),
        ("Textiles", "0.48", "-2.34%", "heat-red-5", "red"),
    ]

    html = """
    <div class="panel section-panel">
        <div class="section-head">
            <div class="section-title">Sector Strength Heatmap <span class="muted">ⓘ</span></div>
            <div class="section-actions">
                <div class="mini-pill">vs</div>
                <div class="mini-pill">NIFTY 500 ▾</div>
            </div>
        </div>
        <div class="heatmap-grid">
    """

    for name, score, change, tile, txt in sectors:
        html += f"""
        <div class="heat-tile {tile}">
            <div class="heat-name">{name}</div>
            <div class="heat-score">{score}</div>
            <div class="heat-change {txt}">{change}</div>
        </div>
        """

    html += """
        </div>
        <div class="legend-row">
            <div class="legend-pill legend-red-3">&lt; 0.60</div>
            <div class="legend-pill legend-red-2">0.60 - 0.80</div>
            <div class="legend-pill legend-red-1">0.80 - 1.10</div>
            <div class="legend-pill legend-green-1">1.10 - 1.30</div>
            <div class="legend-pill legend-green-2">1.30 - 1.60</div>
            <div class="legend-pill legend-green-3">&gt; 1.60</div>
        </div>
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
        ("KPIT", "1.74"),
    ]

    html = """
    <div class="panel section-panel">
        <div class="section-head">
            <div class="section-title">Relative Strength Leaderboard <span class="muted">ⓘ</span></div>
            <div class="section-actions">
                <div class="mini-pill">View All</div>
            </div>
        </div>
        <div class="chip-board">
    """
    for sym, val in chips:
        html += f"""
        <div class="rs-chip">
            <div class="rs-chip-top">
                <div class="rs-chip-dot"></div>
                <div class="rs-chip-symbol">{sym}</div>
            </div>
            <div class="rs-chip-value">{val}</div>
        </div>
        """
    html += "</div></div>"
    st.markdown(html, unsafe_allow_html=True)


def render_scanner_table():
    rows = [
        ("1", "DIXON", "Dixon Technologies (India) Ltd.", "15,642.50", "+3.24%", "+8.91%", "2.56", "1.42", "-8.33%", "green", "green", "green"),
        ("2", "COFORGE", "Coforge Ltd.", "8,144.30", "+2.87%", "+7.32%", "2.31", "1.28", "-12.41%", "green", "green", "yellow"),
        ("3", "KALYANKJIL", "Kalyan Jewellers India Ltd.", "714.80", "+4.12%", "+10.27%", "2.21", "1.67", "-6.17%", "green", "green", "green"),
        ("4", "ASTRAL", "Astral Ltd.", "1,803.25", "+2.61%", "+6.18%", "2.08", "1.35", "-9.72%", "green", "green", "yellow"),
        ("5", "LTF", "L&T Finance Ltd.", "162.45", "+2.34%", "+5.96%", "1.98", "1.18", "-15.38%", "green", "green", "yellow"),
        ("6", "HAL", "Hindustan Aeronautics Ltd.", "4,512.60", "+1.96%", "+5.47%", "1.93", "1.24", "-11.05%", "green", "green", "yellow"),
        ("7", "DEEPAKNTR", "Deepak Nitrite Ltd.", "2,681.90", "+2.78%", "+6.83%", "1.87", "1.31", "-13.42%", "green", "green", "yellow"),
        ("8", "CGPOWER", "CG Power and Industrial Ltd.", "679.15", "+1.78%", "+4.76%", "1.82", "1.16", "-17.91%", "green", "green", "yellow"),
        ("9", "JINDALSTEL", "Jindal Steel & Power Ltd.", "834.10", "+2.05%", "+5.11%", "1.78", "1.09", "-23.14%", "green", "green", "yellow"),
        ("10", "KPIT", "KP IT Solutions Ltd.", "1,367.40", "+1.62%", "+4.12%", "1.74", "1.07", "-18.76%", "green", "green", "yellow"),
    ]

    html = """
    <div class="panel table-panel">
        <div class="table-toolbar">
            <div class="toolbar-left">
                <div class="section-title" style="margin:0;">Momentum Scanner (NIFTY 500) <span class="muted">ⓘ</span></div>
            </div>
            <div class="toolbar-right">
                <div class="toolbar-chip">⚲ Filters</div>
                <div class="toolbar-chip">⟳ Reset</div>
                <div class="toolbar-chip">↻</div>
                <div class="toolbar-chip">302 Results</div>
            </div>
        </div>

        <div class="table-wrap">
            <table class="ms-table">
                <thead>
                    <tr>
                        <th></th>
                        <th>Symbol</th>
                        <th>Company</th>
                        <th>Price (₹)</th>
                        <th>Daily %</th>
                        <th>Weekly %</th>
                        <th>RS</th>
                        <th>ATR RS</th>
                        <th>Dist. from 52W High</th>
                        <th>QMO</th>
                        <th>QM</th>
                        <th>MO</th>
                    </tr>
                </thead>
                <tbody>
    """
    for rank, sym, comp, price, daily, weekly, rs, atr, dist, qmo, qm, mo in rows:
        html += f"""
        <tr>
            <td class="rank">{rank}</td>
            <td>
                <div class="stock-cell">
                    <div class="stock-avatar">{sym[:2]}</div>
                    <div>{sym}</div>
                </div>
            </td>
            <td>
                <div>{comp}</div>
            </td>
            <td>{price}</td>
            <td class="metric-good">{daily}</td>
            <td class="metric-good">{weekly}</td>
            <td>{rs}</td>
            <td>{atr}</td>
            <td class="metric-bad">{dist}</td>
            <td><span class="check-dot {'check-green' if qmo=='green' else 'check-yellow'}">✓</span></td>
            <td><span class="check-dot {'check-green' if qm=='green' else 'check-yellow'}">✓</span></td>
            <td><span class="check-dot {'check-green' if mo=='green' else 'check-yellow'}">✓</span></td>
        </tr>
        """
    html += """
                </tbody>
            </table>
        </div>

        <div class="table-footer">
            <div>Showing 1 to 50 of 500 results</div>
            <div class="pagination">
                <div class="page-btn">‹</div>
                <div class="page-btn active">1</div>
                <div class="page-btn">2</div>
                <div class="page-btn">3</div>
                <div class="page-btn">…</div>
                <div class="page-btn">10</div>
                <div class="page-btn">›</div>
                <div class="page-btn">50</div>
                <div class="page-btn">50 / page</div>
            </div>
        </div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)


def _chart_svg():
    return """
    <svg class="chart-svg" viewBox="0 0 420 270" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M30 225 C60 205, 80 215, 105 185 C130 155, 145 170, 165 145 C180 125, 205 135, 225 105 C240 84, 255 95, 272 80 C294 61, 310 64, 332 48 C350 36, 366 30, 388 18"
            stroke="#20e38b" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
      <path d="M30 205 C70 195, 105 188, 150 170 C190 156, 235 144, 280 133 C320 124, 352 116, 388 110"
            stroke="#f2aa3b" stroke-width="2.2" stroke-linecap="round"/>
      <path d="M30 219 C76 214, 120 210, 162 198 C205 187, 240 175, 284 164 C323 155, 355 148, 388 142"
            stroke="#3b8dff" stroke-width="2.2" stroke-linecap="round"/>
      <path d="M30 236 C78 233, 118 229, 166 220 C208 212, 250 202, 295 193 C330 187, 360 181, 388 176"
            stroke="#7f56ff" stroke-width="2.2" stroke-linecap="round"/>
    </svg>
    """


def render_right_detail_panel():
    st.markdown(f"""
    <div class="panel detail-top">
        <div class="detail-head">
            <div>
                <div class="tiny-label">NIFTY 500 / DIXON</div>
                <div class="detail-title">DIXON</div>
                <div class="detail-sub">Dixon Technologies (India) Ltd.<br>Consumer Electronics · Small Cap</div>
            </div>
            <div style="color:#8ea2bd;">☆</div>
        </div>

        <div class="price-box">
            <div class="price-main">15,642.50</div>
            <div class="price-change">▲ 3.24% (490.40)</div>
        </div>

        <div class="mini-stats">
            <div class="mini-stat">
                <div class="mini-stat-label">High</div>
                <div class="mini-stat-value">15,715.00</div>
            </div>
            <div class="mini-stat">
                <div class="mini-stat-label">Low</div>
                <div class="mini-stat-value">15,100.20</div>
            </div>
            <div class="mini-stat">
                <div class="mini-stat-label">Volume</div>
                <div class="mini-stat-value">12.45M</div>
            </div>
            <div class="mini-stat">
                <div class="mini-stat-label">Market Cap</div>
                <div class="mini-stat-value">₹93,512 Cr</div>
            </div>
        </div>

        <div class="time-tabs">
            <div class="time-pill active">1D</div>
            <div class="time-pill">5D</div>
            <div class="time-pill">1M</div>
            <div class="time-pill">3M</div>
            <div class="time-pill">6M</div>
            <div class="time-pill">YTD</div>
            <div class="time-pill">1Y</div>
            <div class="time-pill">5Y</div>
            <div class="time-pill">All</div>
        </div>

        <div class="chart-box">
            <div class="chart-grid"></div>
            {_chart_svg()}
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="panel summary-panel">
        <div class="section-head">
            <div class="section-title">Earnings Summary</div>
            <div class="section-actions">
                <div class="mini-pill">View More</div>
            </div>
        </div>
        <div class="summary-grid">
            <div class="summary-card">
                <div class="label">Next Earnings</div>
                <div class="value">29 May 2025</div>
            </div>
            <div class="summary-card">
                <div class="label">EPS (TTM)</div>
                <div class="value">132.45</div>
            </div>
            <div class="summary-card">
                <div class="label">EPS Growth (YoY)</div>
                <div class="value good">+78.6%</div>
            </div>
            <div class="summary-card">
                <div class="label">Surprise (Last)</div>
                <div class="value good">+12.3%</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="panel qualification-panel">
        <div class="section-head">
            <div class="section-title">Scanner Qualification</div>
            <div class="section-actions">
                <div class="mini-pill">View Rules</div>
            </div>
        </div>

        <div class="qual-row">
            <div class="qual-label">Price above 10W MA</div>
            <div class="qual-value">15,642.50 &gt; 13,920.30</div>
            <div class="qual-status">Pass</div>
        </div>
        <div class="qual-row">
            <div class="qual-label">Price above 20W MA</div>
            <div class="qual-value">15,642.50 &gt; 14,215.35</div>
            <div class="qual-status">Pass</div>
        </div>
        <div class="qual-row">
            <div class="qual-label">Price above 50W MA</div>
            <div class="qual-value">15,642.50 &gt; 13,102.80</div>
            <div class="qual-status">Pass</div>
        </div>
        <div class="qual-row">
            <div class="qual-label">Price above 200W MA</div>
            <div class="qual-value">15,642.50 &gt; 11,524.65</div>
            <div class="qual-status">Pass</div>
        </div>
        <div class="qual-row">
            <div class="qual-label">RS vs NIFTY500 &gt; 1.0</div>
            <div class="qual-value">2.56</div>
            <div class="qual-status">Pass</div>
        </div>
        <div class="qual-row">
            <div class="qual-label">RS Making New High</div>
            <div class="qual-value">2.58 (20D High)</div>
            <div class="qual-status">Pass</div>
        </div>
        <div class="qual-row">
            <div class="qual-label">Price within 25% of 52W High</div>
            <div class="qual-value">-8.33%</div>
            <div class="qual-status">Pass</div>
        </div>
        <div class="qual-row">
            <div class="qual-label">Positive Weekly %</div>
            <div class="qual-value metric-good">+8.91%</div>
            <div class="qual-status">Pass</div>
        </div>
        <div class="qual-row">
            <div class="qual-label">Positive Daily %</div>
            <div class="qual-value metric-good">+3.24%</div>
            <div class="qual-status">Pass</div>
        </div>

        <div class="tag-row">
            <div class="qual-tag tag-green">QMO</div>
            <div class="qual-tag tag-orange">QM</div>
            <div class="qual-tag tag-purple">MO</div>
        </div>

        <div class="data-note">
            Data as of 16 May 2025, 03:30 PM IST<br>
            Source: NSE, Trendlyne, Internal Calculations
        </div>
    </div>
    """, unsafe_allow_html=True)
