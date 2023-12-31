import altair as alt
from vega_datasets import data

def make_chart(well_df):
    # Read in polygons from topojson
    states = alt.topo_feature(data.us_10m.url, feature='states')

    # US states background
    background = alt.Chart(states).mark_geoshape(
        fill='lightgray',
        stroke='white',
        tooltip=None
    ).properties(
        width=500,
        height=300
    ).project('albersUsa')

    well_chart = alt.Chart(well_df).mark_circle()\
                    .encode(latitude='latitude:Q', longitude='longitude:Q', 
                            color=alt.Color('gradient:Q', scale=alt.Scale(scheme='yelloworangered')),
                            tooltip=[alt.Tooltip('depth:Q', title='Depth (m)'),
                                     alt.Tooltip('gradient:Q', title='Gradient (°C / m)', format='0.3f')]
                           )\
                    .properties(title='Well locations')

    return background + well_chart
