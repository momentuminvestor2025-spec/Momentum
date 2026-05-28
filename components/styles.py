.heatmap-title {
    font-size: 0.90rem;
    font-weight: 800;
    letter-spacing: 0.03em;
    text-transform: uppercase;
    color: #eef5fe;
    margin-bottom: 8px;
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
