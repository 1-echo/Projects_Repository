import pandas as pd
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Reading the dataframe

initial_df = pd.read_csv('Total11.csv')
initial_df.drop(columns=['Unnamed: 0'],inplace=True)
numeric = initial_df.select_dtypes(include=['int64','float64'])
categorical = initial_df.select_dtypes(include=['object'])
ar_codes = {
    "ZW":"Air Wisconsin",
    "AS":"Alaska Airlines",
    "G4":"Allegiant Air LLC ",
    "AA":"American Airlines",
    "C5":"Champlain Air",
    "CP":"Compass Airlines",
    "DL":"Delta Air Lines, Inc.",
    "EM":"Empire Airline",
    "9E":"Endeavor Air", 
    "MQ":"Envoy Air",
    "EV":"ExpressJet Airlines", 
    "F9":"Frontier Airlines, Inc.", 
    "G7":"GoJet Airlines",
    "HA":"Hawaiian Airlines Inc.",
    "QX":"Horizon Air",
    "B6":"Jetblue Airways Corporation",
    "OH":"Jetstream Intl",
    "YV":"Mesa Airlines, Inc.",
    "KS":"Penair",
    "PT":"Piedmont Airlines",
    "YX":"Republic Airlines",
    "OO":"Skywest Airlines",
    "WN":"Southwest Airlines",
    "NK":"Spirit Airlines, Inc.",
    "AX":"Trans State",
    "UA":"United Airlines, Inc."
}

#### Plotting Graphs ####

def bar_q():
    df = numeric.groupby('QUARTER')['FLIGHTS'].sum().to_frame().reset_index().astype('int')
    df.QUARTER = df.QUARTER.replace([1,2,3,4],["Q1","Q2","Q3","Q4"])
    fig = px.bar(df,"QUARTER","FLIGHTS", color_discrete_sequence=["#81d8d0"])
    fig.update_layout(
        title="Total Flights Per Quarter in US (2022)",
        xaxis_title="QUARTER",
        yaxis_title="NUMBER OF FLIGHTS")    
    return fig
def bar_m():
    df = numeric.groupby('MONTH')['FLIGHTS'].sum().to_frame().reset_index().astype('int')
    Months = ['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December']
    df.MONTH = df['MONTH'].replace(list(range(1,13)),Months)
    fig = px.bar(df,"MONTH","FLIGHTS", color_discrete_sequence=["#81d8d0"])
    fig.update_layout(
        title="Total Flights Per Quarter in US (2022)",
        xaxis_title="MONTH",
        yaxis_title="NUMBER OF FLIGHTS")     
    return fig
def bar_can():
    df = numeric.groupby('QUARTER')[['CANCELLED','DIVERTED']].sum().reset_index().astype('int')
    df.QUARTER = df.QUARTER.replace([1,2,3,4],["Q1","Q2","Q3","Q4"])
    fig = px.bar(df,"QUARTER","CANCELLED", color_discrete_sequence=["#81d8d0"])
    fig.update_layout(
        title="Total Cancelled Flights in US (2022)",
        xaxis_title="QUARTER",
        yaxis_title="CANCELLED FLIGHTS")    
    return fig
def bar_div():
    df = numeric.groupby('QUARTER')[['CANCELLED','DIVERTED']].sum().reset_index().astype('int')
    df.QUARTER = df.QUARTER.replace([1,2,3,4],["Q1","Q2","Q3","Q4"])
    fig = px.bar(df,"QUARTER","DIVERTED", color_discrete_sequence=["#81d8d0"])
    fig.update_layout(
        title="Total Diverted Flights in US (2022)",
        xaxis_title="QUARTER",
        yaxis_title="DIVERTED FLIGHTS")    
    return fig
def bar_carr():
    df = categorical.groupby('OP_UNIQUE_CARRIER')['OP_UNIQUE_CARRIER'].count().reset_index(name='Counts')
    df.OP_UNIQUE_CARRIER = df.OP_UNIQUE_CARRIER.replace(list(ar_codes.keys()),list(ar_codes.values()))
    fig = px.bar(df,"OP_UNIQUE_CARRIER","Counts", color_discrete_sequence=["#81d8d0"])
    fig.update_layout(
        title="Total Flights per Carrier in US (2022)",
        xaxis_title="CARRIER",
        yaxis_title="FLIGHTS")
    return fig
def carr_can():
    df = initial_df[['YEAR','QUARTER','MONTH','OP_UNIQUE_CARRIER','CANCELLED','DIVERTED']]
    df = df.groupby(['OP_UNIQUE_CARRIER','MONTH'])[["CANCELLED",'DIVERTED']].sum().reset_index()
    df.OP_UNIQUE_CARRIER = df.OP_UNIQUE_CARRIER.replace(list(ar_codes.keys()),list(ar_codes.values()))
    df = df.groupby('OP_UNIQUE_CARRIER')[["CANCELLED",'DIVERTED']].sum().reset_index()
    fig = px.bar(df,"OP_UNIQUE_CARRIER","CANCELLED", color_discrete_sequence=["#81d8d0"])
    fig.update_layout(
        title="Total Cancelled Flights per Carrier in US (2022)",
        xaxis_title="CARRIER",
        yaxis_title="FLIGHTS")
    return fig
def carr_div():
    df = initial_df[['YEAR','QUARTER','MONTH','OP_UNIQUE_CARRIER','CANCELLED','DIVERTED']]
    df = df.groupby(['OP_UNIQUE_CARRIER','MONTH'])[["CANCELLED",'DIVERTED']].sum().reset_index()
    df.OP_UNIQUE_CARRIER = df.OP_UNIQUE_CARRIER.replace(list(ar_codes.keys()),list(ar_codes.values()))
    df = df.groupby('OP_UNIQUE_CARRIER')[["CANCELLED",'DIVERTED']].sum().reset_index()
    fig = px.bar(df,"OP_UNIQUE_CARRIER","DIVERTED", color_discrete_sequence=["#81d8d0"])
    fig.update_layout(
        title="Total Diverted Flights per Carrier in US (2022)",
        xaxis_title="CARRIER",
        yaxis_title="FLIGHTS")
    return fig


# Initializing Dash APP
app = dash.Dash(__name__)

# Layout

app.layout = html.Div(children=[

    # Setting Title
    html.H1("US Air Traffic Analysis",
            style={
                "textAlign":"center",
                "color":'#503D36',
                "font-size":40
            }),

    # Setting first group of graphs
    html.H2("Analysis by Quarters and Month"),
    html.Div(children=[dcc.Graph(id="bar-quarter", figure=bar_q()),
                       dcc.Graph(id="bar-month", figure=bar_m())]),
    html.Br(),

    # Setting second group of graphs
    html.H2("Analysis of July"),
        dcc.RangeSlider(
        id="day_slider",
        min=1,
        max=31,
        step=1,
        marks={
            1:"1",
            5:"5",
            10:"10",
            15:"15",
            20:"20",
            25:"25",
            31:"31"
            },
        value=[0,31]
    ),
    html.Div(children=[dcc.Graph(id="bar-july"),dcc.Graph(id="line-july")]),
    html.Br(),

    # Setting third group of graphics
    html.H2("Analysis of Cancelled and Diverted Flights"),
    html.Div(children=[dcc.Graph(id="bar-can", figure=bar_can()), dcc.Graph(id="bar-div", figure=bar_div())]),
    html.Br(),

    # Setting fourth group ( Categorical )
    html.H2("Analysis per Carrier"),
    html.Div(children=[dcc.Graph(id="bar_carr", figure=bar_carr())]),
    html.Div(children=[dcc.Graph(id="carr_can", figure=carr_can()),dcc.Graph(id="carr_div", figure=carr_div())]),
    html.Br(),

    ])


#### Setting react graphics

@app.callback( Output( component_id='bar-july', component_property='figure' ),
                Input( component_id="day_slider", component_property="value" ))
def july_b(day):
    df = numeric.groupby(['MONTH','DAY_OF_MONTH'])['FLIGHTS'].sum().to_frame().reset_index().astype('int')
    Months = ['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December']
    df.MONTH = df['MONTH'].replace(list(range(1,13)),Months)
    df = df[df['MONTH']=='July']
    df = df[(df["DAY_OF_MONTH"]>=day[0]) & (df["DAY_OF_MONTH"]<=day[1])]
    fig = px.bar(df,"DAY_OF_MONTH","FLIGHTS", color_discrete_sequence=["#81d8d0"], title='Total Flights July in US (2022)')
    fig.update_layout(xaxis = dict(
        tickmode = 'linear',
        tick0 = 0,
        dtick = 1),
        title="Total Flights July in US (2022)",
        xaxis_title="DAY OF MONTH",
        yaxis_title="NUMBER OF FLIGHTS")
    return fig

@app.callback( Output( component_id='line-july', component_property='figure' ),
                Input( component_id="day_slider", component_property="value" ))
def july_b(day):
    df = numeric.groupby(['MONTH','DAY_OF_MONTH'])['FLIGHTS'].sum().to_frame().reset_index().astype('int')
    Months = ['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December']
    df.MONTH = df['MONTH'].replace(list(range(1,13)),Months)
    df = df[df['MONTH']=='July']
    df = df[(df["DAY_OF_MONTH"]>=day[0]) & (df["DAY_OF_MONTH"]<=day[1])]
    fig = px.line(df,"DAY_OF_MONTH","FLIGHTS", color_discrete_sequence=["#81d8d0"])
    fig.update_layout(xaxis = dict(
        tickmode = 'linear',
        tick0 = 0,
        dtick = 1),
        title="Total Flights July in US (2022)",
        xaxis_title="DAY OF MONTH",
        yaxis_title="NUMBER OF FLIGHTS")
    return fig


if __name__ == '__main__':
    app.run_server()
