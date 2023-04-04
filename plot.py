# imports
import pandas as pd
import plotly.graph_objects as go

# df = pd.read_csv('data/IP_locs.csv')

def plot_trace(df):
    # plot of region
    fig = go.Figure(go.Scattergeo(
            lon = df['longitude'],
            lat = df['latitude'],
            text = df['city'],
            mode = 'lines+markers',
            marker = dict(
            color = df.index,
            colorscale = "greys",
            size = 18,
            ),
            line = dict(
            color = "pink",
            )
            # textfont = dict(color="Black", size = 48),
        )
    )

    # style plot
    fig.update_layout(
        paper_bgcolor = "White",
        plot_bgcolor = "White",
        geo = dict(
            scope = 'world',
            showland = True,
            landcolor = "White",
            showsubunits = True,
            subunitcolor = "Black",
            # lataxis_showgrid=True,
            # lonaxis_showgrid=True,
        )
    )

    # fig.update_layout(margin=dict(t=50), height = 720, width = 1280)

    fig.show()

# plot_trace(df)