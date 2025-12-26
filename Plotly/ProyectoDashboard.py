from os import name
from turtle import title
from dash.html import Figure
import pandas as pd
from pandas.io.formats import style
import dash
import dash_bootstrap_components as dbc
import plotly.express as px 


data = pd.read_csv('./csv/StudentsPerformance.csv')
df = pd.DataFrame(data)

#function score selector by mean
def Score_Selector(value): 
    if value  >= 90: 
        return 'A'
    elif value >= 80: 
        return 'B'
    elif value >= 70: 
        return 'C'
    elif value >= 60: 
        return 'D'
    else: 
        return 'F'

df['promedio'] = df[['math score', 'reading score', 'writing score']].mean(axis=1).round(2)
# print(df['promedio'])
# print(df.head())
#aplicando un score selector por nivel
df['nivel'] = df['promedio'].apply(Score_Selector)
pct_value = df['nivel'].value_counts(normalize=True) * 100
# Creating the app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

#navbar simple 
navbar = dbc.NavbarSimple(
    brand="Student Performance Dashboard",
    children=[
        dash.html.A(
            'Data reference link', 
            href="https://www.kaggle.com/datasets/spscientist/students-performance-in-exams",
            target="_blank", #jump to a new page
            style={'color': 'white'}
        )
    ],
    fluid=True, # this makes sure all changes are aplied correctly
)
#menu 
menu = dash.html.Div(
    dash.dcc.Dropdown(
        id = 'Menu', 
        options= [
            {
                'label': 'All students',
                'value': 'Students'
            },
            {
                'label': 'All Woman',
                'value': 'Woman'
            }, 
            {
                'label': 'All Man',
                'value': 'Man'
            }
        ],
        value='Students',
        clearable=False,
        searchable= False,
        style={
            'width': '60%',
            'marginTop': '5px',
        }, 

    ), 
    style={
        'margin': '20px',
        'display': 'flex', 
        'justifyContent': 'center',
    }
)
#Ahora crearemos cartas en donde se alojaran los datos en mi dashboard
cards = dbc.Row([
    dbc.Col(
        dbc.Card(
        [ dash.html.H4('Math'), dash.html.H5(id = 'meanMath')
        ], body=True, id = 'Card_math') 
    ),
    dbc.Col(
        dbc.Card(
        [ dash.html.H4('Reading'), dash.html.H5(id = 'meanReading')
        ], body=True, id = 'Card_reading') 
    ), 
    dbc.Col(
        dbc.Card(
        [ dash.html.H4('Writing'), dash.html.H5(id = 'meanWriting')
        ], body=True, id = 'Card_writing') 
    )
], style={
    'marginTop': '20px',
    'marginLeft': '20px',
    'marginRight': '20px',
})

#creating the first bar graph
graph = dash.html.Div(dash.dcc.Graph(id = 'graph'))

#GRAFICOS STATICOS Correlation graph
graph1 = dash.html.Div([
    dbc.Row([
        dbc.Col([
            dash.dcc.Graph(id = 'statter_plot', figure= px.scatter_matrix(df,
            dimensions=['math score', 'reading score', 'writing score'],
            color='gender', title = 'Scores Correlation'))
        ])
    ])
])

#GRAFICOS STATICOS pastel graph
graph2 = dash.html.Div([
    dbc.Row([
        dbc.Col([
            dash.dcc.Graph(id = 'pastel_plot', figure= px.pie(names= pct_value.index, values= pct_value.values, title='Distribution of Student Levels'))
        ])
    ])
])



#aniadir los callbacks esto nos ayudara a traer la informacion de manera dinamic atravez del menu

@app.callback(
    dash.Output('meanMath', 'children'),
    dash.Output('meanReading', 'children'),
    dash.Output('meanWriting', 'children'),
    dash.Output('graph', 'figure'),
    dash.Output('statter_plot', 'figure'),
    dash.Output('pastel_plot', 'figure'),
    dash.Input('Menu', 'value'),

)
#function to use when call back execute
def update_cards(value):
    if value == 'Students':
        df_filtered = df
    elif value == 'Woman':
        df_filtered = df[df['gender'] == 'female']
    elif value == 'Man':
        df_filtered = df[df['gender'] == 'male']
    else:
        df_filtered = df
    meanMath = df_filtered['math score'].mean().round(2)
    meanReading = df_filtered['reading score'].mean().round(2)
    meanWriting = df_filtered['writing score'].mean().round(2)
    
    meanLevelEducation = df_filtered.groupby('parental level of education',as_index=False)[['math score', 'reading score', 'writing score']].mean().round(2)
    meanLevelEducation['GeneralMean'] = meanLevelEducation[['math score', 'reading score', 
    'writing score']].mean(axis=1).round(2)

    graph = px.bar(meanLevelEducation, x='parental level of education', y='GeneralMean', 
    color='GeneralMean', color_continuous_scale='Viridis', title='General Mean by Parental Level of Education', 
    labels = {
        'parental level of education': 'Parental Level of Education',
        'GeneralMean': 'General Mean',
    })
    graph1 = px.scatter_matrix(df_filtered,
            dimensions=['math score', 'reading score', 'writing score'],
            color='gender', title = 'Scores Correlation')

    # Pie chart update
    pct_value = df_filtered['nivel'].value_counts(normalize=True) * 100
    graph2 = px.pie(names= pct_value.index, values= pct_value.values, title='Distribution of Student Levels')

    return meanMath, meanReading, meanWriting, graph, graph1, graph2






app.layout = dash.html.Div([
    dbc.Row(navbar), 
    dbc.Row(menu),
    dbc.Row(cards),
    dbc.Row(graph),
    dbc.Row(graph1), 
    dbc.Row(graph2)
])

if __name__ == '__main__':
    app.run(debug=True, port = 8000)