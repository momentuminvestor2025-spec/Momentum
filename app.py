import streamlit as st
from components.styles import (
    inject_global_styles,
    render_sidebar_nav,
    render_top_header,
    render_breadth_strip,
    render_kpi_cards,
    render_heatmap_widget_header,
    render_heatmap_page,
)

st.set_page_config(page_title="Nifty500 Momentum Radar", layout="wide")
inject_global_styles()

rail, main = st.columns([0.065, 0.935], gap="small")

with rail:
    render_sidebar_nav()

with main:
    render_top_header()
    render_breadth_strip()
    render_kpi_cards()

    render_heatmap_widget_header()

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "Broad Market Indices",
            "Sectoral Indices",
            "Thematic Indices",
            "Strategy Indices",
        ]
    )

    with tab1:
        render_heatmap_page("broad")

    with tab2:
        render_heatmap_page("sectoral")

    with tab3:
        render_heatmap_page("thematic")

    with tab4:
        render_heatmap_page("strategy")
