import streamlit as st
from components.styles import (
    inject_global_styles,
    render_app_shell_open,
    render_sidebar_nav,
    render_main_shell_open,
    render_top_header,
    render_breadth_strip,
    render_kpi_cards,
    render_heatmap_panel,
    render_rs_leaderboard,
    render_scanner_table,
    render_right_detail_panel,
    render_main_shell_close,
    render_app_shell_close,
)

st.set_page_config(page_title="Momentum Scanner", layout="wide")

inject_global_styles()

render_app_shell_open()
render_sidebar_nav()
render_main_shell_open()

render_top_header()
render_breadth_strip()
render_kpi_cards()

left, right = st.columns([2.15, 1.0], gap="medium")

with left:
    render_heatmap_panel()
    render_rs_leaderboard()
    render_scanner_table()

with right:
    render_right_detail_panel()

render_main_shell_close()
render_app_shell_close()
