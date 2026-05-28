import streamlit as st
from components.styles import (
    inject_global_styles,
    render_sidebar_nav,
    render_top_header,
    render_breadth_strip,
    render_kpi_cards,
    render_rs_leaderboard,
    render_scanner_table,
    render_right_detail_panel,
)

st.set_page_config(page_title="Nifty500 Momentum Radar", layout="wide")
inject_global_styles()

shell_left, shell_main = st.columns([0.065, 0.935], gap="small")

with shell_left:
    render_sidebar_nav()

with shell_main:
    render_top_header()
    render_breadth_strip()
    render_kpi_cards()

    left, right = st.columns([2.15, 1.0], gap="medium")

    with left:
        render_rs_leaderboard()
        render_scanner_table()

    with right:
        render_right_detail_panel()
