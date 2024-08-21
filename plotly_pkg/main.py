from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

# Incorporate data
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv")

# Initialize the app
app = Dash()

# App layout
app.layout = [
    html.Div(children="Simple plot"),
    html.Hr(),
    dcc.RadioItems(options=["pop", "lifeExpert", "gdpPercap"], value="lifeExp", id="controls-and-radio-item"),
    dash_table.DataTable(data=df.to_dict("records"), page_size=10),
    dcc.Graph(figure=px.histogram(df, x="continent", y="lifeExp", histfunc="avg"))
]

# Add controls to build the interaction (@decorator)
@callback(
    Output(component_id="controls-and-graph", component_property="figure"),
    Input(component_id="controls-and-radio-item", component_property="value")
)
def update_graph(col_chosen):
    fig = px.histogram(df, x="continetal", y=col_chosen, histfunv="avg")
    return fig

# Run the app
if __name__ == "__main__":
    app.run(debug=True)

