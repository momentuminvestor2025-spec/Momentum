import streamlit as st
from datetime import date, timedelta
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

    filter_col1, filter_col2, filter_col3 = st.columns([1.2, 1.3, 4], gap="small")

    with filter_col1:
        as_of = st.selectbox(
            "Mode",
            ["Current Snapshot", "Historical Performance"],
            index=1,
            key="heatmap_mode",
        )

    today = date.today()
    default_start = today - timedelta(days=30)
    default_range = (default_start, today)

    with filter_col2:
        selected_range = st.date_input(
            "Date Range",
            value=default_range,
            max_value=today,
            key="heatmap_date_range",
        )

    if isinstance(selected_range, (list, tuple)) and len(selected_range) == 2:
        start_date, end_date = selected_range
    else:
        start_date, end_date = default_range

    with filter_col3:
        st.markdown(
            f"""
            <div class="panel filter-summary-panel">
                <div class="filter-summary-title">Historical Performance Analysis</div>
                <div class="filter-summary-text">
                    Selected window: {start_date.strftime('%d %b %Y')} → {end_date.strftime('%d %b %Y')}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "Broad Market Indices",
            "Sectoral Indices",
            "Thematic Indices",
            "Strategy Indices",
        ]
    )

    with tab1:
        render_heatmap_page("broad", start_date, end_date, as_of)

    with tab2:
        render_heatmap_page("sectoral", start_date, end_date, as_of)

    with tab3:
        render_heatmap_page("thematic", start_date, end_date, as_of)

    with tab4:
        render_heatmap_page("strategy", start_date, end_date, as_of)
