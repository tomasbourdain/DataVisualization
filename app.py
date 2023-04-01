import dash
from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

image_path = '/images/whr.jpg'
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


df_2015= pd.read_csv('data/2015.csv')
df_2016= pd.read_csv('data/2016.csv')
df_2017= pd.read_csv('data/2017.csv')
df_2018= pd.read_csv('data/2018.csv')
df_2019= pd.read_csv('data/2019.csv')
df_2020= pd.read_csv('data/2020.csv')
df_2021= pd.read_csv('data/2021.csv')
df_2022= pd.read_csv('data/2022.csv')
df_2023 = pd.read_csv('data/WHR2023.csv')


df_population = pd.read_csv('data/world_population.csv')
df_population = df_population.loc[:, ['CCA3', 'Country/Territory', '2022 Population', 'Area (km²)', 'Density (per km²)', 'Growth Rate', 'World Population Percentage']]

df_countryCode = pd.read_csv('data/2015_with_country_code.csv')
df_countryCode = df_countryCode.loc[:, ['Country', 'Code']]


#2015
df_2015 = df_2015.merge(df_countryCode, how='left', left_on='Country', right_on='Country')
df_2015 = df_2015.merge(df_population[['Country/Territory','2022 Population', 'Area (km²)', 'Density (per km²)', 'Growth Rate', 'World Population Percentage']], how='left', left_on='Country', right_on='Country/Territory')
df_2015.drop('Country/Territory', axis=1, inplace=True)
df_2015.dropna(subset=['Code','2022 Population' ], inplace=True)

#2016
#df_2016 drop 'Lower Confidence Interval', 'Upper Confidence Interval'
df_2016.drop(['Lower Confidence Interval', 'Upper Confidence Interval'],axis=1, inplace=True)
df_2016 = df_2016.merge(df_countryCode, how='left', left_on='Country', right_on='Country')
df_2016 = df_2016.merge(df_population[['Country/Territory','2022 Population', 'Area (km²)', 'Density (per km²)', 'Growth Rate', 'World Population Percentage']], how='left', left_on='Country', right_on='Country/Territory')
df_2016.drop('Country/Territory', axis=1, inplace=True)
df_2016.dropna(subset=['Code','2022 Population' ], inplace=True)

#2017 
#df_2017 ADD Region, CHANGE 'Happiness.Rank', 'Happiness.Score', 'Economy..GDP.per.Capita.', 'Health..Life.Expectancy.', 'Trust..Government.Corruption.', 'Dystopia.Residual', DROP 'Whisker.high', 'Whisker.low'
df_2017.rename(columns={
                        'Happiness.Rank': 'Happiness Rank',
                        'Happiness.Score': 'Happiness Score',
                        'Economy..GDP.per.Capita.': 'Economy (GDP per Capita)',
                        'Health..Life.Expectancy.': 'Health (Life Expectancy)',
                        'Trust..Government.Corruption.': 'Trust (Government Corruption)',
                        'Dystopia.Residual': 'Dystopia Residual'
                        } ,inplace=True)
df_2017 = df_2017.merge(df_2015[['Country', 'Region']], how='left', left_on='Country', right_on='Country')
df_2017 = df_2017.merge(df_countryCode, how='left', left_on='Country', right_on='Country')
df_2017 = df_2017.merge(df_population[['Country/Territory','2022 Population', 'Area (km²)', 'Density (per km²)', 'Growth Rate', 'World Population Percentage']], how='left', left_on='Country', right_on='Country/Territory')
df_2017.drop(['Country/Territory', 'Whisker.high', 'Whisker.low'], axis=1, inplace=True)
df_2017.dropna(subset=['Region','Code','2022 Population' ], inplace=True)


#2018
#df_2018 ADD Region, CHANGE 'Overall rank', 'Country or region', 'Score', 'GDP per capita', 'Social support', 'Healthy life expectancy', 'Freedom to make life choices', 'Perceptions of corruption'
df_2018.rename(columns={'Country or region': 'Country',
                        'Overall rank': 'Happiness Rank',
                        'Score': 'Happiness Score',
                        'GDP per capita': 'Economy (GDP per Capita)',
                        'Social support': 'Family',
                        'Healthy life expectancy': 'Health (Life Expectancy)',
                        'Freedom to make life choices': 'Freedom',
                        'Perceptions of corruption': 'Trust (Government Corruption)',
                        'Generosity': 'Generosity',
                        } ,inplace=True)
df_2018 = df_2018.merge(df_2015[['Country', 'Region']], how='left', left_on='Country', right_on='Country')
df_2018 = df_2018.merge(df_countryCode, how='left', left_on='Country', right_on='Country')
df_2018 = df_2018.merge(df_population[['Country/Territory','2022 Population', 'Area (km²)', 'Density (per km²)', 'Growth Rate', 'World Population Percentage']], how='left', left_on='Country', right_on='Country/Territory')
df_2018.drop(['Country/Territory'], axis=1, inplace=True)
df_2018.dropna(subset=['Region','Trust (Government Corruption)'], inplace=True)


#2019
#df_2019 ADD Region, CHANGE 'Overall rank', 'Country or region', 'Score', 'GDP per capita', 'Social support', 'Healthy life expectancy', 'Freedom to make life choices', 'Perceptions of corruption'
df_2019.rename(columns={'Country or region': 'Country',
                        'Overall rank': 'Happiness Rank',
                        'Score': 'Happiness Score',
                        'GDP per capita': 'Economy (GDP per Capita)',
                        'Social support': 'Family',
                        'Healthy life expectancy': 'Health (Life Expectancy)',
                        'Freedom to make life choices': 'Freedom',
                        'Perceptions of corruption': 'Trust (Government Corruption)',
                        'Generosity': 'Generosity',
                        } ,inplace=True)
df_2019 = df_2019.merge(df_2015[['Country', 'Region']], how='left', left_on='Country', right_on='Country')
df_2019 = df_2019.merge(df_countryCode, how='left', left_on='Country', right_on='Country')
df_2019 = df_2019.merge(df_population[['Country/Territory','2022 Population', 'Area (km²)', 'Density (per km²)', 'Growth Rate', 'World Population Percentage']], how='left', left_on='Country', right_on='Country/Territory')
df_2019.drop(['Country/Territory'], axis=1, inplace=True)
df_2019.dropna(subset=['Region','Trust (Government Corruption)'], inplace=True)

#2020
#df_2020 ADD Happiness Rank, CHANGE Country name', 'Regional indicator', 'Ladder score', 'Logged GDP per capita', 'Social support', 'Healthy life expectancy', 'Freedom to make life choices', 'Perceptions of corruption', 
#DROP 'Standard error of ladder score', 'upperwhisker', 'lowerwhisker', 'Logged GDP per capita', 'Social support', 'Healthy life expectancy', 'Dystopia + residual' 'Freedom to make life choices', 'Generosity', 'Perceptions of corruption',
# 'Ladder score in Dystopia'
df_2020.rename(columns={'Country name': 'Country',
                        'Regional indicator': 'Region',
                        'Ladder score': 'Happiness Score',
                        'Explained by: Log GDP per capita': 'Economy (GDP per Capita)',
                        'Explained by: Social support': 'Family',
                        'Explained by: Healthy life expectancy': 'Health (Life Expectancy)',
                        'Explained by: Freedom to make life choices': 'Freedom',
                        'Explained by: Perceptions of corruption': 'Trust (Government Corruption)',
                        'Explained by: Generosity': 'Generosity',
                        'Dystopia + residual': 'Dystopia Residual'
                        },inplace=True)
df_2020['Happiness Rank'] = range(1, len(df_2020)+1)
df_2020 = df_2020.merge(df_countryCode, how='left', left_on='Country', right_on='Country')
df_2020 = df_2020.merge(df_population[['Country/Territory','2022 Population', 'Area (km²)', 'Density (per km²)', 'Growth Rate', 'World Population Percentage']], how='left', left_on='Country', right_on='Country/Territory')
df_2020.drop(['Country/Territory', 'Standard error of ladder score', 'upperwhisker', 'lowerwhisker',
                'Logged GDP per capita', 'Social support', 'Healthy life expectancy',
                'Freedom to make life choices', 'Generosity',
                'Perceptions of corruption', 'Ladder score in Dystopia'], axis=1, inplace=True)
df_2020.dropna(subset=['Code', '2022 Population'], inplace=True)
df_2020.loc[df_2020['Country'].isin(['United States', 'Canada']), 'Region'] = 'North America'
df_2020.loc[df_2020['Country'].isin(['Australia', 'New Zealand']), 'Region'] = 'Australia and New Zealand'
df_2020['Region'] = df_2020['Region'].replace({
    'Middle East and North Africa': 'Middle East and Northern Africa',
    'Southeast Asia': 'Southeastern Asia',
    'Commonwealth of Independent States': 'Central and Eastern Europe',
    'East Asia': 'Eastern Asia',
    'South Asia': 'Southern Asia'
})



#2021
#df_2021 ADD Happiness Rank, CHANGE Country name', 'Regional indicator', 'Ladder score', 'Logged GDP per capita', 'Social support', 'Healthy life expectancy', 'Freedom to make life choices', 'Perceptions of corruption', 
#DROP 'Standard error of ladder score', 'upperwhisker', 'lowerwhisker', 'Logged GDP per capita', 'Social support', 'Healthy life expectancy', 'Dystopia + residual' 'Freedom to make life choices', 'Generosity', 'Perceptions of corruption',
# 'Ladder score in Dystopia'
df_2021.rename(columns={'Country name': 'Country',
                        'Regional indicator': 'Region',
                        'Ladder score': 'Happiness Score',
                        'Explained by: Log GDP per capita': 'Economy (GDP per Capita)',
                        'Explained by: Social support': 'Family',
                        'Explained by: Healthy life expectancy': 'Health (Life Expectancy)',
                        'Explained by: Freedom to make life choices': 'Freedom',
                        'Explained by: Perceptions of corruption': 'Trust (Government Corruption)',
                        'Explained by: Generosity': 'Generosity',
                        'Dystopia + residual': 'Dystopia Residual'
                        },inplace=True)
df_2021['Happiness Rank'] = range(1, len(df_2021)+1)
df_2021 = df_2021.merge(df_countryCode, how='left', left_on='Country', right_on='Country')
df_2021 = df_2021.merge(df_population[['Country/Territory','2022 Population', 'Area (km²)', 'Density (per km²)', 'Growth Rate', 'World Population Percentage']], how='left', left_on='Country', right_on='Country/Territory')
df_2021.drop(['Country/Territory', 'Standard error of ladder score', 'upperwhisker', 'lowerwhisker',
                'Logged GDP per capita', 'Social support', 'Healthy life expectancy',
                'Freedom to make life choices', 'Generosity',
                'Perceptions of corruption', 'Ladder score in Dystopia'], axis=1, inplace=True)
df_2021.dropna(subset=['Code', '2022 Population'], inplace=True)
df_2021.loc[df_2021['Country'].isin(['United States', 'Canada']), 'Region'] = 'North America'
df_2021.loc[df_2021['Country'].isin(['Australia', 'New Zealand']), 'Region'] = 'Australia and New Zealand'
df_2021['Region'] = df_2021['Region'].replace({
    'Middle East and North Africa': 'Middle East and Northern Africa',
    'Southeast Asia': 'Southeastern Asia',
    'Commonwealth of Independent States': 'Central and Eastern Europe',
    'East Asia': 'Eastern Asia',
    'South Asia': 'Southern Asia'
})

#2022
#df_2022 ADD Region, CHANGE 'RANK', 'Happiness score', 'Explained by: GDP per capita', 'Explained by: Social support', 'Explained by: Healthy life expectancy', 'Explained by: Freedom to make life choices', 'Explained by: Generosity', 'Explained by: Perceptions of corruption'
df_2022.rename(columns={
                        'RANK': 'Happiness Rank',
                        'Happiness score': 'Happiness Score',
                        'Explained by: GDP per capita': 'Economy (GDP per Capita)',
                        'Explained by: Social support': 'Family',
                        'Explained by: Healthy life expectancy': 'Health (Life Expectancy)',
                        'Explained by: Freedom to make life choices': 'Freedom',
                        'Explained by: Perceptions of corruption': 'Trust (Government Corruption)',
                        'Explained by: Generosity': 'Generosity',
                        'Dystopia (1.83) + residual': 'Dystopia Residual'
                        },inplace=True)
df_2022 = df_2022.merge(df_2015[['Country', 'Region']], how='left', left_on='Country', right_on='Country')
df_2022 = df_2022.merge(df_countryCode, how='left', left_on='Country', right_on='Country')
df_2022 = df_2022.merge(df_population[['Country/Territory','2022 Population', 'Area (km²)', 'Density (per km²)', 'Growth Rate', 'World Population Percentage']], how='left', left_on='Country', right_on='Country/Territory')
df_2022.drop(['Country/Territory', 'Whisker-high', 'Whisker-low'], axis=1, inplace=True)
df_2022.dropna(subset=['Region','Trust (Government Corruption)'], inplace=True)
df_2022 = df_2022.applymap(lambda x: x.replace(',', '.') if isinstance(x, str) else x)
df_2022['Happiness Score'] = df_2022['Happiness Score'].astype(float)
df_2022['Economy (GDP per Capita)'] = df_2022['Economy (GDP per Capita)'].astype(float)
df_2022['Family'] = df_2022['Family'].astype(float)
df_2022['Health (Life Expectancy)'] = df_2022['Health (Life Expectancy)'].astype(float)
df_2022['Trust (Government Corruption)'] = df_2022['Trust (Government Corruption)'].astype(float)
df_2022['Generosity'] = df_2022['Generosity'].astype(float)
df_2022['Dystopia Residual'] = df_2022['Dystopia Residual'].astype(float)

#2023
#df_2023 ADD Happiness Rank, CHANGE Country name', 'Regional indicator', 'Ladder score', 'Logged GDP per capita', 'Social support', 'Healthy life expectancy', 'Freedom to make life choices', 'Perceptions of corruption', 
#DROP 'Standard error of ladder score', 'upperwhisker', 'lowerwhisker', 'Logged GDP per capita', 'Social support', 'Healthy life expectancy', 'Dystopia + residual' 'Freedom to make life choices', 'Generosity', 'Perceptions of corruption',
# 'Ladder score in Dystopia'
df_2023.rename(columns={'Country name': 'Country',
                        'Regional indicator': 'Region',
                        'Ladder score': 'Happiness Score',
                        'Explained by: Log GDP per capita': 'Economy (GDP per Capita)',
                        'Explained by: Social support': 'Family',
                        'Explained by: Healthy life expectancy': 'Health (Life Expectancy)',
                        'Explained by: Freedom to make life choices': 'Freedom',
                        'Explained by: Perceptions of corruption': 'Trust (Government Corruption)',
                        'Explained by: Generosity': 'Generosity',
                        'Dystopia + residual': 'Dystopia Residual'
                        },inplace=True)
df_2023['Happiness Rank'] = range(1, len(df_2023)+1)
df_2023 = df_2023.merge(df_2015[['Country', 'Region']], how='left', left_on='Country', right_on='Country')
df_2023 = df_2023.merge(df_countryCode, how='left', left_on='Country', right_on='Country')
df_2023 = df_2023.merge(df_population[['Country/Territory','2022 Population', 'Area (km²)', 'Density (per km²)', 'Growth Rate', 'World Population Percentage']], how='left', left_on='Country', right_on='Country/Territory')
df_2023.drop(['Country/Territory', 'Standard error of ladder score', 'upperwhisker', 'lowerwhisker',
                'Logged GDP per capita', 'Social support', 'Healthy life expectancy',
                'Freedom to make life choices', 'Generosity',
                'Perceptions of corruption', 'Ladder score in Dystopia'], axis=1, inplace=True)
df_2023.dropna(subset=['Code', '2022 Population', 'Region'], inplace=True)

df = df_2015

df_unemployment = pd.read_csv('data/unemployment analysis.csv')
df_unemployment = df_unemployment[['Country Name', 'Country Code', '2015', '2016', '2017', '2018', '2019', '2020', '2021']]

df_inflation = pd.read_csv("data/Global Dataset of Inflation.csv",  encoding='iso-8859-1')
df_inflation = df_inflation[['Country', 'Country Code', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', 'Note']]
df_inflation = df_inflation[df_inflation['Note'] == 'Annual average inflation']
df_inflation.drop('Note', axis=1, inplace=True)

df_coords = pd.read_csv('data\world_country_and_usa_states_latitude_and_longitude_values.csv')
df_coords = df_coords[['country', 'country_code','latitude','longitude']]

app = Dash(__name__, external_stylesheets=external_stylesheets, assets_folder='assets', assets_url_path='assets')



# MAP
fig = px.choropleth(df, locations='Code', color='Happiness Score', 
                    hover_data={'Country':True,
                                'Code': False,
                                'Happiness Rank': True, 
                                'Happiness Score': ':.2f'},
                    scope='world', projection='equirectangular',
                    color_continuous_scale='Viridis',
                    range_color=[df['Happiness Score'].min(), df['Happiness Score'].max()],
                    template='plotly_dark',
                    height=650)

fig.update_layout(
    title_text='World Happiness Map', # Set the map title     
    polar=dict(
        radialaxis=dict(
            visible=True, # Show radial axis
            range=[df['Happiness Score'].min(), df['Happiness Score'].max()] # Set range of radial axis
        )
    )
)

fig.layout.geo.showframe = False
fig.layout.geo.showcountries = True
fig.layout.geo.projection.type == 'natural earth'
fig.layout.geo.lataxis.range = [-53, 76]
fig.layout.geo.lonaxis.range = [-167, 188]
fig.layout.geo.countrycolor = 'gray'
fig.layout.geo.coastlinecolor = 'gray'

# DROPDOWNS
options = [{'label': country, 'value': country} for country in df['Country'].unique()]

region_options = [{'label': region, 'value': region} for region in df['Region'].unique()]

# Define dropdown options
dropdown_options = [{'label': 'Happiness Score', 'value': 'Happiness Score'},
                    {'label': 'Economy (GDP per Capita)', 'value': 'Economy (GDP per Capita)'},
                    {'label': 'Health (Life Expectancy)', 'value': 'Health (Life Expectancy)'},
                    {'label': 'Freedom', 'value': 'Freedom'},
                    {'label': 'Trust (Government Corruption)', 'value': 'Trust (Government Corruption)'},
                    {'label': 'Family', 'value': 'Family'}]

# INDICATOR
indicator = go.Figure(go.Indicator(
    mode="number",
    value=df['Happiness Score'].mean(),
    title={"text": "Happiness Score"},
))

indicator_regions = go.Figure(go.Indicator(
    mode="number",
    value=len(df['Region'].unique()),
    title = {"text": "Number of Regions"}
))

indicator_countries = go.Figure(go.Indicator(
    mode="number",
    value=len(df['Country'].unique()),
    title = {"text": "Number of Countries"}
))


# SCATTER
fig_scatter_health = px.scatter(df, x="Economy (GDP per Capita)", y="Health (Life Expectancy)",
                 size='2022 Population', color="Region", hover_name="Country",
                 log_x=True, size_max=60,
                 template='plotly_dark')

fig_scatter_score = px.scatter(df, x="Economy (GDP per Capita)", y="Happiness Score",
                 size='2022 Population', color="Region", hover_name="Country",
                 log_x=True, size_max=60,
                 template='plotly_dark')

# BAR 
# Define the list of regions and corresponding colors
regions = ['Western Europe', 'North America', 'Australia and New Zealand',
           'Middle East and Northern Africa', 'Latin America and Caribbean',
           'Southeastern Asia', 'Central and Eastern Europe', 'Eastern Asia',
           'Sub-Saharan Africa', 'Southern Asia']
colors = ['blue', 'green', 'red', 'orange', 'purple', 'yellow', 'pink', 'brown', 'gray', 'cyan']

# Group data by region and calculate the mean happiness score
grouped_data = df.groupby(['Region'])['Happiness Score'].mean().loc[regions]

# Create a horizontal bar chart
fig_bar = go.Figure(go.Bar(
            x=grouped_data.values,  # mean happiness score as x-axis
            y=grouped_data.index,  # region as y-axis
            orientation='h',  # horizontal orientation
            marker_color=colors,  # set the bar color based on region
            opacity=0.8  # set the bar opacity
))

# TABLE
# sort the data by happiness score and select the top 5
top_5 = df.sort_values("Happiness Score", ascending=False).head(5)

# create the table
table = go.Figure(data=[go.Table(
    header=dict(values=["Rank", "Country", "Happiness Score"],
                fill_color="grey",
                align="left"),
    cells=dict(values=[top_5["Happiness Rank"], top_5["Country"], top_5["Happiness Score"]],
               fill_color="lavender",
               align="left"))
])

table.update_layout(title='Top 5 Happiest Countries')

# Set chart title and axis labels
fig_bar.update_layout(
    title='Mean Happiness Score by Region',
    xaxis_title='Mean Happiness Score',
    yaxis_title='Region'
)

#LINE CHART
years = [2015,2016,2017,2018,2019,2020,2021,2022,2023]
# calculate the average happiness score for each year
averages = []
for year in years:
    df = globals().get('df_{}'.format(year))
    avg_score = df['Happiness Score'].mean()
    averages.append({'Year': year, 'Happiness Score': avg_score})
df_avg = pd.DataFrame(averages)

# create the bar graph using Plotly Express
line = px.line(df_avg, x="Year", y="Happiness Score", title='Average Happiness Score by Year', template='plotly_dark')


image_filename = '/assets/whr.jpg'


app.layout = html.Div([
    html.Div([
        html.Img(
            id="logo-image",
            src=image_filename,
            style={'textAlign': 'center', 'width': '25%', 'margin': 'auto'}
        ),
        html.H2(children='World Happiness Report',
            style={'textAlign': 'center'}),
        html.H4(children='''
            Happiness In The World
            An Analysis Of Socio-Economic Factors    ''',
            style={'textAlign': 'center'}),
        html.P(children='''
            The World Happiness Report ranks countries based on various measures of 
            happiness and well-being, such as income, social support,
            life expectancy, and freedom to make life choices. 
            The Dashboard aims to provide insight 
            into the factors that contribute to people's happiness and 
            inform policy decisions to improve the well-being of 
            citizens around the world.    ''',
            style={'textAlign': 'justify', 'margin': '10px'}),
        html.Div([
            html.H6(children='''
            Region''',
            style={'textAlign': 'center'}),
            dcc.Dropdown(
                id='region-dropdown',
                options=region_options,
                #value='Western Europe',
                style={'width': '100%', 'marginTop': '5px'}
            ),
            html.H6(children='''
            Country''',
            style={'textAlign': 'center'}),
            dcc.Dropdown(
                id='country-dropdown',
                options=options,
                #value='Switzerland',
                style={'width': '100%', 'marginTop': '5px'}
            ),
            dcc.Graph(
                    id="top5_countries-table", 
                    style={'width': '100%'}
            )
        ], style={'width': '100%', 'marginTop': '20px'}),
        html.Div([
            html.H4(children='''
            More About''',
            style={'textAlign': 'center'}),
            html.P(children="""Furthermore, a dashboard can also help identify 
              gaps in the data and prompt further research to better understand the factors 
              that contribute to happiness scores in individual countries.""",
            style={'textAlign': 'justify', 'margin': '10px' }),
            html.P(children="""Future work on 
              the dashboard could involve collecting more data about individual countries 
              to further analyze and understand the country-specific factors that influence
                happiness scores, which can ultimately lead to policy recommendations aimed 
                at improving citizens well-being. """,
            style={'textAlign': 'justify', 'margin': '10px' }),
            html.Footer('Tomás Bourdain & Diogo Morgado © 2023',
            style= {'textAlign': 'center', 'marginTop': '75%'}),
        ], style={'width': '100%'})
    ], style={'textAlign': 'center', 'width': '25%', 'paddingRight': '10px', 'borderRight': '1px solid black'}, className="two columns"),
    html.Div([ 
        html.Div([
            dcc.Graph(id='happiness-indicator', style={'width': '33%', 'max-height': '100%', 'height': '220px', 'display': 'inline-block', 'margin':'auto', 'borderRight': '1px solid black'}),
            dcc.Graph(id='regions-indicator', figure=indicator_regions, style={'width': '34%', 'max-height': '100%', 'height': '220px', 'display': 'inline-block', 'margin':'auto', 'borderRight': '1px solid black'}),
            dcc.Graph(id='countries-indicator',  style={'width': '34%', 'max-height': '100%', 'height': '220px',  'display': 'inline-block', 'margin':'auto', 'borderRight': '1px solid black'})
        ], style={'display': 'flex'}),    
            ]),
    html.Div([ 
        html.Div([
        dcc.Dropdown(id='parameter-dropdown', options=dropdown_options, value='Happiness Score'),
            dcc.Graph(id="choropleth-map"),
                ], style={'width': '100%'}),
            ], style={'display': 'flex'}),    
    html.Div([ 
        html.Div([
                dcc.Slider(
                    id='year-slider',
                    min=2015,
                    max=2023,
                    step=1,
                    value=2015,
                    marks={str(year): str(year) for year in range(2015, 2024)},
                ),
            ], style={
                'width': '100%',
                'margin': 'auto',
                'color': 'white',
                'background-color': '#2a3f5f',
                'border-radius': '0.25rem',
                'padding': '1rem'
            }),
        ], style={
            'display': 'flex',
            'justify-content': 'center',
            'align-items': 'center',
            'height': '100px',
            'background-color': '#1e2b3d',
            }),
    html.Div([    
        html.Div([        
            dcc.Graph(id='score-vs-gdp'),    
                ], 
                style={'width': '50%', 'display': 'inline-block'}),
        html.Div([        
            dcc.Graph(id='life-exp-vs-gdp'),    
                ], 
                    style={'width': '50%', 'display': 'inline-block'}),
        ], style={'display': 'flex'}),
    html.Div([ 
        html.Div([
            dcc.Graph(id="happiness-plot"),
                ], style={'width': '100%'}),
            ], style={'display': 'flex'})
])

# Define callback to update graph
@app.callback(
    Output('happiness-indicator', 'figure'),
    [Input('country-dropdown', 'value'),
     Input('region-dropdown', 'value'),
     Input('year-slider', 'value')])
def update_graph(country, region, year):
    if region is not None:
        if year == 2015:

            df_year = globals().get('df_{}'.format(year))  # Select the dataset for the given year

            df_year_before = globals().get('df_{}'.format(year))

            avg_score = round(df_year[df_year['Region'] == region]['Happiness Score'].mean(), 2)

            avg_score_before = round(df_year_before[df_year_before['Region'] == region]['Happiness Score'].mean(), 2)

            indicator = go.Figure(go.Indicator(
            value=avg_score,
            title={"text": "Happiness Score for {} in {}".format(region, year)},
            mode = "number+delta",
            delta = {'position': "top", 'reference': avg_score_before},
            domain = {'x': [0, 1], 'y': [0, 1]}))

        else:
            
            df_year = globals().get('df_{}'.format(year))  # Select the dataset for the given year

            df_year_before = globals().get('df_{}'.format(year-1))

            avg_score = round(df_year[df_year['Region'] == region]['Happiness Score'].mean(), 2)

            avg_score_before = round(df_year_before[df_year_before['Region'] == region]['Happiness Score'].mean(), 2)

            indicator = go.Figure(go.Indicator(
            value=avg_score,
            title={"text": "Happiness Score for {} in {}".format(region, year)},
            mode = "number+delta",
            delta = {'position': "top", 'reference': avg_score_before},
            domain = {'x': [0, 1], 'y': [0, 1]}))
        
    elif country is not None:
        if year == 2015:
            df_year = globals().get('df_{}'.format(year))  # Select the dataset for the given year

            df_year_before = globals().get('df_{}'.format(year))

            avg_score = round(df_year[df_year['Country'] == country]['Happiness Score'].mean() ,2)

            avg_score_before = round(df_year_before[df_year_before['Country'] == country]['Happiness Score'].mean(), 2)

            indicator = go.Figure(go.Indicator(
            value=avg_score,
            title={"text": "Happiness Score for {} in {}".format(country, year)},
            mode = "number+delta",
            delta = {'position': "top", 'reference': avg_score_before},
            domain = {'x': [0, 1], 'y': [0, 1]}))

        else:
            df_year = globals().get('df_{}'.format(year))  # Select the dataset for the given year

            df_year_before = globals().get('df_{}'.format(year-1))

            avg_score = round(df_year[df_year['Country'] == country]['Happiness Score'].mean(), 2)

            avg_score_before = round(df_year_before[df_year_before['Country'] == country]['Happiness Score'].mean(),2)

            indicator = go.Figure(go.Indicator(
            value=avg_score,
            title={"text": "Happiness Score for {} in {}".format(country, year)},
            mode = "number+delta",
            delta = {'position': "top", 'reference': avg_score_before},
            domain = {'x': [0, 1], 'y': [0, 1]}))

    else:
        if year == 2015:

            df_year = globals().get('df_{}'.format(year))  # Select the dataset for the given year

            df_year_before = globals().get('df_{}'.format(year))


            avg_score = round(df_year['Happiness Score'].mean(), 2)

            avg_score_before = round(df_year_before['Happiness Score'].mean(),2)

            indicator = go.Figure(go.Indicator(
            value=avg_score,
            title={"text": "Happiness Score for The World in {}".format(year)},
            mode = "number+delta",
            delta = {'position': "top", 'reference': avg_score_before},
            domain = {'x': [0, 1], 'y': [0, 1]}))

        else:
            df_year = globals().get('df_{}'.format(year))  # Select the dataset for the given year

            df_year_before = globals().get('df_{}'.format(year-1))

            avg_score = round(df_year['Happiness Score'].mean(), 2)

            avg_score_before = round(df_year_before['Happiness Score'].mean(), 2)

            indicator = go.Figure(go.Indicator(
            value=avg_score,
            title={"text": "Happiness Score for The World in {}".format(year)},
            mode = "number+delta",
            delta = {'position': "top", 'reference': avg_score_before},
            domain = {'x': [0, 1], 'y': [0, 1]}))
            

    return indicator

@app.callback(
    Output('countries-indicator', 'figure'),
    [Input('year-slider', 'value'),
     Input('country-dropdown', 'value')]
)
def update_graph(year, country):
    df_year = globals().get('df_{}'.format(year))

    if country is None:
        indicator = go.Figure(go.Indicator(
        mode="number",
        value=len(df_year['Country'].unique()),
        title = {"text": "Number of Countries"}
        ))

        return indicator
    else:
        growth = df_year["Growth Rate"].loc[df_year['Country']==country].values[0]
        # create the indicator
        indicator = go.Figure(go.Indicator(
           mode = "number",
           value = growth,
           title = {"text": "Growth Rate %"}))
        
        return indicator

@app.callback(
    Output('regions-indicator', 'figure'),
    [Input('country-dropdown', 'value')]
)
def update_graph(country):
    df_year = globals().get('df_{}'.format(year))

    if country is None:
        indicator = go.Figure(go.Indicator(
        mode="number",
        value=len(df['Region'].unique()),
        title = {"text": "Number of Regions"}
        ))

        return indicator
    else:
        population = df_year["2022 Population"].loc[df_year['Country']==country].values[0]

        # create the indicator
        indicator = go.Figure(go.Indicator(
            mode = "number",
            value = population,
            title = {"text": "Population"}
        ))
        
        return indicator


@app.callback(
    Output('choropleth-map', 'figure'),
    [Input('region-dropdown', 'value'),
     Input('parameter-dropdown', 'value'),
     Input('country-dropdown', 'value'),
     Input('year-slider', 'value')]
)
def update_choropleth(region, parameter, country, year):
    df = globals().get('df_{}'.format(year))

    if region is None and parameter is None and country is None :
        fig = px.choropleth(df, locations='Code', color='Happiness Score', 
                    hover_data={'Country':True,
                                'Code': False,
                                'Happiness Rank': True, 
                                'Happiness Score': ':.2f'},
                    scope='world', 
                    projection='equirectangular', #orthographic
                    color_continuous_scale='Viridis',
                    range_color=[df['Happiness Score'].min(), df['Happiness Score'].max()],
                    template='plotly_dark',
                    height=550)
        fig.update_layout(
    title_text='World Happiness Map Happiness Score', # Set the map title     
    polar=dict(
        radialaxis=dict(
            visible=True, # Show radial axis
            range=[df['Happiness Score'].min(), df['Happiness Score'].max()] # Set range of radial axis
        )
    )
)
        fig.layout.geo.showframe = False
        fig.layout.geo.showcountries = True
        fig.layout.geo.projection.type == 'natural earth'
        fig.layout.geo.lataxis.range = [-53, 76]
        fig.layout.geo.lonaxis.range = [-167, 188]
        fig.layout.geo.countrycolor = 'gray'
        fig.layout.geo.coastlinecolor = 'gray'

        return fig
    # Filter the DataFrame to include only the countries in the selected region
    elif region is None and country is None:
        fig = px.choropleth(df, locations='Code', color=parameter, 
                    hover_data={'Country':True,
                                'Code': False,
                                'Happiness Rank': True, 
                                parameter: ':.2f'},
                    scope='world', projection='equirectangular',
                    color_continuous_scale='Viridis',
                    range_color=[df[parameter].min(), df[parameter].max()],
                    template='plotly_dark',
                    height=550)
        fig.update_layout(
    title_text='World Happiness Map {}'.format(parameter), # Set the map title     
    polar=dict(
        radialaxis=dict(
            visible=True, # Show radial axis
            range=[df[parameter].min(), df[parameter].max()] # Set range of radial axis
        )
    )
)
        fig.layout.geo.showframe = False
        fig.layout.geo.showcountries = True
        fig.layout.geo.projection.type == 'natural earth'
        fig.layout.geo.lataxis.range = [-53, 76]
        fig.layout.geo.lonaxis.range = [-167, 188]
        fig.layout.geo.countrycolor = 'gray'
        fig.layout.geo.coastlinecolor = 'gray'

        return fig

    elif parameter is None and country is None:
        filtered_df = df[df['Region'] == region]
        
        # Create the choropleth map using the filtered DataFrame
        fig = px.choropleth(
            filtered_df,
            locations='Code',
            color='Happiness Score',
            hover_data={
                'Country': True,
                'Code': False,
                'Happiness Rank': True, 
                'Happiness Score': ':.2f'
            },
            scope='world',
            projection='equirectangular', #orthographic
            color_continuous_scale='Viridis',
            range_color=[filtered_df['Happiness Score'].min(), filtered_df['Happiness Score'].max()],
            template='plotly_dark',
            height=550
        )
        fig.update_layout(
            title_text='World Happiness Map Happiness Score- {}'.format(region), # Set the map title     
            polar=dict(
                radialaxis=dict(
                    visible=True, # Show radial axis
                    range=[filtered_df['Happiness Score'].min(), filtered_df['Happiness Score'].max()] # Set range of radial axis
                )
            )
        )

        fig.layout.geo.showframe = False
        fig.layout.geo.showcountries = True
        fig.layout.geo.projection.type == 'natural earth'
        fig.layout.geo.lataxis.range = [-53, 76]
        fig.layout.geo.lonaxis.range = [-167, 188]
        fig.layout.geo.countrycolor = 'gray'
        fig.layout.geo.coastlinecolor = 'gray'

        return fig  
    elif parameter is not None and region is not None and country is None:
        filtered_df = df[df['Region'] == region]
        
        # Create the choropleth map using the filtered DataFrame
        fig = px.choropleth(
            filtered_df,
            locations='Code',
            color=parameter,
            hover_data={
                'Country': True,
                'Code': False,
                'Happiness Rank': True, 
                parameter: ':.2f'
            },
            scope='world',
            projection='equirectangular', #orthographic
            color_continuous_scale='Viridis',
            range_color=[filtered_df[parameter].min(), filtered_df[parameter].max()],
            template='plotly_dark',
            height=550
        )
        fig.update_layout(
            title_text='World Happiness Map {} - {}'.format(parameter, region), # Set the map title     
            polar=dict(
                radialaxis=dict(
                    visible=True, # Show radial axis
                    range=[filtered_df[parameter].min(), filtered_df[parameter].max()] # Set range of radial axis
                )
            )
        )

        fig.layout.geo.showframe = False
        fig.layout.geo.showcountries = True
        fig.layout.geo.projection.type == 'natural earth'
        fig.layout.geo.lataxis.range = [-53, 76]
        fig.layout.geo.lonaxis.range = [-167, 188]
        fig.layout.geo.countrycolor = 'gray'
        fig.layout.geo.coastlinecolor = 'gray'

        return fig  
    elif country is not None and parameter is not None and region is None:
        filtered_df = df[df['Country'] == country]

        lat = df_coords[['latitude']].loc[df_coords['country']== country].values[0][0]
        lon = df_coords[['longitude']].loc[df_coords['country']== country].values[0][0]

        lat_min = lat - 20
        lat_max = lat + 20
        lon_min = lon - 20
        lon_max = lon + 20
        
        # Create the choropleth map using the filtered DataFrame
        fig = px.choropleth(
            filtered_df,
            locations='Code',
            color=parameter,
            hover_data={
                'Country': True,
                'Code': False,
                'Happiness Rank': True, 
                parameter: ':.2f'
            },
            scope='world',
            center={'lat': lat, 'lon': lon},
            projection='equirectangular', #orthographic
            color_continuous_scale='Viridis',
            range_color=[filtered_df[parameter].min(), filtered_df[parameter].max()],
            template='plotly_dark',
            height=550
        )
        fig.update_layout(
            title_text='World Happiness Map {} - {}'.format(parameter, country), 
            polar=dict(
                radialaxis=dict(
                    visible=True, # Show radial axis
                    range=[filtered_df[parameter].min(), filtered_df[parameter].max()] # Set range of radial axis
                )
            )
        )

        fig.layout.geo.showframe = False
        fig.layout.geo.showcountries = True
        fig.layout.geo.projection.type == 'natural earth'
        fig.layout.geo.lataxis.range = [lat_min,  lat_max]
        fig.layout.geo.lonaxis.range = [lon_min,  lon_max]
        fig.layout.geo.countrycolor = 'gray'
        fig.layout.geo.coastlinecolor = 'gray'

        return fig  
    elif country is not None and parameter is None and region is None:
        filtered_df = df[df['Country'] == country]

        lat = df_coords[['latitude']].loc[df_coords['country']== country].values[0][0]
        lon = df_coords[['longitude']].loc[df_coords['country']== country].values[0][0]

        lat_min = lat - 20
        lat_max = lat + 20
        lon_min = lon - 20
        lon_max = lon + 20

        # Create the choropleth map using the filtered DataFrame
        fig = px.choropleth(
            filtered_df,
            locations='Code',
            color='Happiness Score',
            hover_data={
                'Country': True,
                'Code': False,
                'Happiness Rank': True, 
                'Happiness Score': ':.2f'
            },
            scope='world',
            center={'lat': lat, 'lon': lon},
            projection='equirectangular', #orthographic
            color_continuous_scale='Viridis',
            range_color=[filtered_df['Happiness Score'].min(), filtered_df['Happiness Score'].max()],
            template='plotly_dark',
            height=550
            )
        fig.update_layout(
            title_text='World Happiness Map Happiness Score - {}'.format(country), 
            polar=dict(
                radialaxis=dict(
                    visible=True, # Show radial axis
                    range=[filtered_df['Happiness Score'].min(), filtered_df['Happiness Score'].max()] # Set range of radial axis
                )
            )
        )

        fig.layout.geo.showframe = False
        fig.layout.geo.showcountries = True
        fig.layout.geo.projection.type == 'natural earth'
        fig.layout.geo.lataxis.range = [lat_min,  lat_max]
        fig.layout.geo.lonaxis.range = [lon_min,  lon_max]
        fig.layout.geo.countrycolor = 'gray'
        fig.layout.geo.coastlinecolor = 'gray'

        return fig


@app.callback(
    Output('life-exp-vs-gdp', 'figure'),
    Output('score-vs-gdp', 'figure'),
    [Input('region-dropdown', 'value'),
     Input('year-slider', 'value'),
     Input('country-dropdown', 'value')]
)
def update_scatter_plots(region, year, country):
    df = globals().get('df_{}'.format(year))
    if region is None and country is None:
        fig_scatter_health = px.scatter(df, x="Economy (GDP per Capita)", y="Health (Life Expectancy)",
                 size='2022 Population', color="Region", hover_name="Country",
                 log_x=True, size_max=60,
                 template='plotly_dark')
            
        fig_scatter_health.update_traces(hovertemplate='<b>Country:</b> %{hovertext}<br><b>Economy (GDP per Capita):</b> %{x:.2f}<br><b>Health (Life Expectancy):</b> %{y:.2f}<br><b>Population:</b> %{marker.size}')
        fig_scatter_health.update_layout(
                xaxis=dict(
                    showline=True,
                    showgrid=False,
                    showticklabels=True,
                    linecolor='rgb(204, 204, 204)',
                    linewidth=2,
                    ticks='outside',
                    tickfont=dict(
                        family='Arial',
                        size=12,
                        color='rgb(255, 255, 255)',
                    ),
                ))


        fig_scatter_score = px.scatter(df, x="Economy (GDP per Capita)", y="Happiness Score",
                 size='2022 Population', color="Region", hover_name="Country",
                 log_x=True, size_max=60,
                 template='plotly_dark')
        
        fig_scatter_score.update_traces(hovertemplate='<b>Country:</b> %{hovertext}<br><b>Economy (GDP per Capita):</b> %{x:.2f}<br><b>Happiness Score:</b> %{y:.2f}<br><b>Population:</b> %{marker.size}')
        fig_scatter_score.update_layout(
                xaxis=dict(
                    showline=True,
                    showgrid=False,
                    showticklabels=True,
                    linecolor='rgb(204, 204, 204)',
                    linewidth=2,
                    ticks='outside',
                    tickfont=dict(
                        family='Arial',
                        size=12,
                        color='rgb(255, 255, 255)',
                    ),
                ))
        

        return fig_scatter_health, fig_scatter_score

    elif country is not None and region is None :
        data = df_unemployment[df_unemployment["Country Name"] == country]

        # melt data to convert wide format to long format
        melted_data = data.melt(id_vars=["Country Name", "Country Code"], var_name="Year", value_name="Unemployment Rate")

        # convert year column to numeric
        melted_data["Year"] = pd.to_numeric(melted_data["Year"])

        # plot line graph using Plotly
        fig = px.line(melted_data, x="Year", y="Unemployment Rate", title="Unemployment Rate in {}".format(country), template='plotly_dark', text='Unemployment Rate')
        fig.update_traces(hovertemplate='<b>Year:</b> %{x}<br><b>Unemployment Rate:</b> %{y:.2f}')
        fig.update_traces(line=dict(color='rgb(49,130,189)'), textposition='bottom center')
        fig.update_layout(
                xaxis=dict(
                    showline=True,
                    showgrid=False,
                    showticklabels=True,
                    linecolor='rgb(204, 204, 204)',
                    linewidth=2,
                    ticks='outside',
                    tickfont=dict(
                        family='Arial',
                        size=12,
                        color='rgb(255, 255, 255)',
                    ),
                ),
                yaxis=dict(
                    showgrid=False,
                    zeroline=False,
                    showline=False,
                ),
                autosize=False,
                margin=dict(
                    autoexpand=False,
                    l=100,
                    r=20,
                    t=110,
                ),
        )
        fig.add_annotation(x=2019, y=melted_data[melted_data['Year']==2019]['Unemployment Rate'].iloc[0], 
                   text="Effect of COVID-19")

        # filter data for Afghanistan
        data = df_inflation[df_inflation["Country"] == country]

        # melt data to convert wide format to long format
        melted_data = data.melt(id_vars=["Country", "Country Code"], var_name="Year", value_name="Inflation Rate")

        # convert year column to numeric
        melted_data["Year"] = pd.to_numeric(melted_data["Year"])

        # plot line graph using Plotly
        fig_inflation = px.bar(melted_data, x="Year", y="Inflation Rate", title="inflation Rate in {}".format(country), template='plotly_dark', text='Inflation Rate')
        fig_inflation.update_traces(hovertemplate='<b>Year:</b> %{x}<br><b>Inflation Rate:</b> %{y:.2f}')


        fig_inflation.update_traces(marker_color='rgb(26, 118, 255)', marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5)
        fig_inflation.update_layout(
                xaxis=dict(
                    showline=True,
                    showgrid=False,
                    showticklabels=True,
                    linecolor='rgb(204, 204, 204)',
                    linewidth=2,
                    ticks='outside',
                    tickfont=dict(
                        family='Arial',
                        size=12,
                        color='rgb(255, 255, 255)',
                    ),
                ),
                yaxis=dict(
                    showgrid=False,
                    zeroline=False,
                    showline=False,
                ),
                autosize=False,
                margin=dict(
                    autoexpand=False,
                    l=100,
                    r=20,
                    t=110,
                ),
        )

        fig_inflation.add_annotation(x=2022, y=max(melted_data['Inflation Rate']), text="Effect of war in Ukraine", showarrow=True, arrowhead=1)


        fig.layout.yaxis.ticksuffix='%'
        fig_inflation.layout.yaxis.ticksuffix='%'

        return [fig, fig_inflation]

    elif region is not None and country is None:
        filtered_df = df[df['Region'] == region]
        
        # Update the health scatter plot
        fig_scatter_health = px.scatter(filtered_df, x="Economy (GDP per Capita)", y="Health (Life Expectancy)", size='2022 Population', color="Country",
                        hover_name="Country", log_x=True, size_max=60, template='plotly_dark')
        
        fig_scatter_health.update_traces(hovertemplate='<b>Economy (GDP per Capita):</b> %{x:.2f}<br><b>Health (Life Expectancy):</b> %{y:.2f}<br><b>Population:</b> %{marker.size}')
        fig_scatter_health.update_layout(
                xaxis=dict(
                    showline=True,
                    showgrid=False,
                    showticklabels=True,
                    linecolor='rgb(204, 204, 204)',
                    linewidth=2,
                    ticks='outside',
                    tickfont=dict(
                        family='Arial',
                        size=12,
                        color='rgb(255, 255, 255)',
                    ),
                ))

        
        # Update the score scatter plot
        fig_scatter_score = px.scatter(filtered_df, x="Economy (GDP per Capita)", y="Happiness Score", size='2022 Population', color="Country",
                        hover_name="Country", log_x=True, size_max=60, template='plotly_dark')
        
        fig_scatter_score.update_traces(hovertemplate='<b>Economy (GDP per Capita):</b> %{x:.2f}<br><b>Happiness Score:</b> %{y:.2f}<br><b>Population:</b> %{marker.size}')
        fig_scatter_score.update_layout(
                xaxis=dict(
                    showline=True,
                    showgrid=False,
                    showticklabels=True,
                    linecolor='rgb(204, 204, 204)',
                    linewidth=2,
                    ticks='outside',
                    tickfont=dict(
                        family='Arial',
                        size=12,
                        color='rgb(255, 255, 255)',
                    ),
                ))
        

        
        return fig_scatter_health, fig_scatter_score  

@app.callback(
    Output("top5_countries-table", "figure"),
    [Input("region-dropdown", "value"),
     Input('year-slider', 'value')]
)
def update_top5_countries_table(region, year):
    df = globals().get('df_{}'.format(year))
  
    # Filter the data based on the selected region
    if region is None:
        top_5 = df.sort_values("Happiness Score", ascending=False).head(5)

        # create the table
        table = go.Figure(data=[go.Table(
            columnwidth = [200, 400, 400],
            header=dict(values=["Rank", "Country", "Happiness Score"],
                        fill_color="lightgrey",
                        line_color='darkslategray',
                        align="center",
                        font_size=16,
                        height=30),
            cells=dict(values=[top_5["Happiness Rank"], top_5["Country"], round(top_5["Happiness Score"],3)],
                    fill_color="lavender",
                    line_color='darkslategray',
                    align="center",
                    font_size=14,
                    height=30))
        ])
        table.update_layout(title='Top 5 Happiest Countries in {}'.format(year))

        return table
    else:
        data = df[df["Region"] == region]
    
        # Get the top 5 countries based on happiness score
        top_5 = data.sort_values("Happiness Score", ascending=False).head(5)

        # Create the table figure
        table = go.Figure(data=[go.Table(
            columnwidth = [200, 400, 400],
            header=dict(values=["Rank", "Country", "Happiness Score"],
                        fill_color="lightgrey",
                        line_color='darkslategray',
                        align="center",
                        font_size=16,
                        height=20),
            cells=dict(values=[top_5["Happiness Rank"], top_5["Country"], round(top_5["Happiness Score"],3)],
                    line_color='darkslategray',
                    fill_color="lavender",
                    align="center",
                    font_size=14,
                    height=30))
        ])
        table.update_layout(title='Top 5 Happiest Countries in {} - {}'.format(year, region))

        
        # Return the updated figure and style to update the graph
        return table

@app.callback(
    Output('happiness-plot', 'figure'),
    [Input('region-dropdown', 'value'),
     Input('country-dropdown', 'value')]
)
def update_line_plots(region, country):
    if region is None and country is None:
        years = [2015,2016,2017,2018,2019,2020,2021,2022,2023]
        # calculate the average happiness score for each year
        averages = []
        for year in years:
            df = globals().get('df_{}'.format(year))
            avg_score = df['Happiness Score'].mean()
            averages.append({'Year': year, 'Happiness Score': avg_score})
        df_avg = pd.DataFrame(averages)

        # create the bar graph using Plotly Express
        fig = px.line(df_avg, x="Year", y=df_avg['Happiness Score'].round(2), title='Average Happiness Score by Year', template='plotly_dark', text=df_avg['Happiness Score'].round(2))
        fig.update_traces(hovertemplate='<b>Year:</b> %{x}<br><b>Happiness Score:</b> %{y:.2f}')
        fig.update_traces(line=dict(color='rgb(49,130,189)'), textposition='top center')
        fig.update_layout(yaxis=dict(title='Happiness Score'))


        fig.update_layout(
                xaxis=dict(
                    showline=True,
                    showgrid=False,
                    showticklabels=True,
                    linecolor='rgb(204, 204, 204)',
                    linewidth=2,
                    ticks='outside',
                    tickfont=dict(
                        family='Arial',
                        size=12,
                        color='rgb(255, 255, 255)',
                    ),
                ),
                yaxis=dict(
                    showgrid=False,
                    zeroline=False,
                    showline=False,
                ),
                autosize=False,
                margin=dict(
                    autoexpand=False,
                    l=100,
                    r=20,
                    t=110,
                ),
        )

        return fig
    
    elif region is None and country is not None:
        years = [2015,2016,2017,2018,2019,2020,2021,2022,2023]
        # calculate the average happiness score for each year
        averages = []
        for year in years:
            df = globals().get('df_{}'.format(year))
            avg_score = df[df['Country'] == country]['Happiness Score'].mean()
            averages.append({'Year': year, 'Happiness Score': avg_score, 'Country':country})
        df_avg = pd.DataFrame(averages)

        # create the bar graph using Plotly Express
        fig = px.line(df_avg, x="Year", y=df_avg['Happiness Score'].round(2), title='Average Happiness Score in {} by Year'.format(country), template='plotly_dark', text=df_avg['Happiness Score'].round(2))
        fig.update_traces(hovertemplate='<b>Year:</b> %{x}<br><b>Happiness Score:</b> %{y:.2f}')
        fig.update_traces(line=dict(color='rgb(49,130,189)'), textposition='top center')
        fig.update_layout(yaxis=dict(title='Happiness Score'))


        fig.update_layout(
                xaxis=dict(
                    showline=True,
                    showgrid=False,
                    showticklabels=True,
                    linecolor='rgb(204, 204, 204)',
                    linewidth=2,
                    ticks='outside',
                    tickfont=dict(
                        family='Arial',
                        size=12,
                        color='rgb(255, 255, 255)',
                    ),
                ),
                yaxis=dict(
                    showgrid=False,
                    zeroline=False,
                    showline=False,
                ),
                autosize=False,
                margin=dict(
                    autoexpand=False,
                    l=100,
                    r=20,
                    t=110,
                ),
        )

        return fig

    elif region is not None and country is None: 
        years = [2015,2016,2017,2018,2019,2020,2021,2022,2023]
        # calculate the average happiness score for each year
        averages = []
        for year in years:
            df = globals().get('df_{}'.format(year))
            avg_score = df[df['Region'] == region]['Happiness Score'].mean()
            averages.append({'Year': year, 'Happiness Score': avg_score, 'Region':region})
        df_avg = pd.DataFrame(averages)

        # create the bar graph using Plotly Express
        fig = px.line(df_avg, x="Year", y=df_avg['Happiness Score'].round(2), title='Average Happiness Score in {} by Year'.format(region), template='plotly_dark', text=df_avg['Happiness Score'].round(2))
        fig.update_traces(hovertemplate='<b>Year:</b> %{x}<br><b>Happiness Score:</b> %{y:.2f}')
        fig.update_traces(line=dict(color='rgb(49,130,189)'), textposition='top center')
        fig.update_layout(yaxis=dict(title='Happiness Score'))


        fig.update_layout(
                xaxis=dict(
                    showline=True,
                    showgrid=False,
                    showticklabels=True,
                    linecolor='rgb(204, 204, 204)',
                    linewidth=2,
                    ticks='outside',
                    tickfont=dict(
                        family='Arial',
                        size=12,
                        color='rgb(255, 255, 255)',
                    ),
                ),
                yaxis=dict(
                    showgrid=False,
                    zeroline=False,
                    showline=False,
                ),
                autosize=False,
                margin=dict(
                    autoexpand=False,
                    l=100,
                    r=20,
                    t=110,
                ),
        )

        return fig
    
    
    
if __name__ == '__main__':
    app.run(debug=True)