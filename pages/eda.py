from dash import Dash, dcc, html, Input, Output
from datetime import datetime 
import dash_bootstrap_components as dbc
import pandas as pd
import plotly 
import plotly.express as px
import plotly.graph_objects as go

# Reading csv 2019.csv
df = pd.read_csv('pages/data/2019.csv')
df2 = pd.read_csv('pages/data/tweets.csv')

months = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May',
          6:'June', 7:'July', 8:'August', 9:'September', 10:'October',
          11:'November', 12:'December'}

lineas_estrategicas = {'Medellin Development Plan': 1,
                       'Línea estratégica 1: Reactivación Económica y Valle del Software': 2,
                       'Línea estratégica 2: Transformación Educativa y Cultura': 3,
                       'Línea estratégica 3: Medellin Me Cuida': 4,
                       'Línea estratégica 4: Ecociudad': 5,
                       'Línea estratégica 5: Gobernanza y Gobernabilidad': 6,
                       }

df_words = pd.read_csv('pages/data/word_fre_2019.csv')

def rep_words():
    fig = px.bar(df_words.head(35).sort_values(by='frequency'), 
                 x='frequency', 
                 y='word',
                 orientation='h',
                 height=600,
                 color_discrete_sequence=['#5BC0BE']
                 )
    fig.update_layout(title_font_size=15)
    fig.layout.paper_bgcolor = '#FFFFFF'
    fig.layout.plot_bgcolor = '#FFFFFF'

    return fig



p1 = """
Welcome to the EDA, in this section you can interact with the data sets used to 
develop the model, through interactive content you can learn first hand some of 
the most important findings of each of the sections, as well as brief explanations 
of how those responsible for the project manipulated, cleaned, enriched and visualized 
the information to draw conclusions for the construction of the model and its future 
interpretation, always guiding the analysis to find answers to the two hypotheses 
proposed in the definition of the problem.

"""

p2 = """

This section focuses on show you the needs of the population of Medellin before 
the PDM comes into force (2020-2023) using the **Tweets 2019** dataset. The objective 
of this analysis was to know the dynamics of interaction on the Twitter platform, and 
the usefulness of the queries made to conform this dataset.

"""


p3 = """


The first variable of interest was the tweet text, this variable provides 
information about the tweet composition and also some inputs to improve the API 
request to excel in the sentiment analysis model. The following figures show you 
the length distribution of tweets text  measured in characters and words. For the 
project purpose, “word” is defined as  characters sequence separated by a single 
white space.


"""

p4 = """
Separately, both figures do not provide additional information, but when you 
comparing them, some key pieces come into the picture. Focusing on the 75th 
percentile for the first figure, it finds a distribution with sharp spikes, 
unlike the distribution of the second figure in which there is a smooth behavior. A 
proposed hypothesis to explain this could be the values of this distribution by 
character length through the use of emojis, punctuation marks, mentions, hashtags, 
white spaces or words like ``hellooo". The presence of these type of elements in the 
text of the tweet distances its length value from the central tendencies. 

"""

p5 = """
This section shows an exploration of the textual content of the tweets in order to obtain 
information about the use of words such as Medellín, the use of elements such as emoticons, 
hashtags and regional lexicon. There is an option available for you to generate a random tweet 
from this dataset Tweets - 2019 in order for you to identify the above mentioned features.

"""

p6_1 = """

As you can observe by exploring text contents of the Tweets, “Medellín” does not only refer to a geographical location. This word is also used to make comparisons or comments using this word as a reference city. Some main topics of the city such as “Metro” appear in the tweets and could be related to some of the needs of the people of Medellín. Other important conclusions about this section are summarized as follows: 
"""

p6_2 = """
1. The large use of mentions with the at-word extends the length of the tweet and would not provide relevant information for sentiment analysis so its elimination could be considered.

"""

p6_3 = """
2. It should be taken into account that the word “Medellín” depends on the context, i.e., it will not always refer to the city, but also to the soccer team, to the alcoholic beverage, as a comparison, or to other meaning. So it has to be careful when drawing conclusions and narrowing your search.

"""

p6_4 = """
3. When finding different places it is to be expected that any resident abroad can mention the word “Medellin” and its different connotations, so it may not reflect problems in the city. When interpreting the results, grouping by localities or focusing only on the city of Medellin could solve this limitation.

"""

p7 = """
The following figures show you the frequency of words within the text of the tweets 
through a bar chart and a word cloud, the ones at the top of the list are: pronouns, prepositions, definite determiners, quantifier determiners, punctuation marks and the word "Medellín" with its variants. These types of words are intrinsic to the use of language and hence their high recurrence.

"""

p8 = """
Analyzing the results of the previous figures, it was identified that not all the most frequent words referred to topics of interest for the city of Medellín. Therefore, making a more rigorous analysis, a list of 9 categories was determined (called in this project **keywords**) that encompassed transcendent topics to which the tweets alluded. These keywords were the following: 

1. "metro"
2. "vida"
3. "cultura"
4. "trabajo"
5. "movilidad"
6. "jovenes"
7. "seguridad"
8. "empresa"
9. "tecnologia"

"""

p9 = """
The purpose of the MPD document is to establish the different guidelines and projects in terms of public policies for the city of Medellin in the period 2020-2023. In order to answer the first question proposed in the overview section, this EDA show you a text analysis that was carried out on the MPD with the purpose of determine if the topics expressed in this document were aligned with the categories (keywords) obtained in the EDA:Tweets 2019. For this analysis, a cleaning text process was carried out taking into account the stop words defined in **EDA: Tweets 2019** in order to obtain a suitable set of words with which to perform the required comparison.

As a result of this process was obtained a word cloud from the PMD text. From this Figure, it is possible to observe words that describe a project execution and the metrics to evaluate its impact and evolution. Another relevant fact is the presence of words such as “seguridad”, “vida”, and “cultura”, which are included in the list of keywords in the EDA: Tweets - 2019. You can observe this Figure selecting Medellin Development Plan.

"""

p10 = """
This section shows the exploratory analysis performed for the tweets coming from the 2019-2022 dataset. This step allows obtaining information about the distribution of all the tweets by year, month and day, in order to understand some important dynamics and trends at the level of the city of Medellin associated with events with high interaction on twitter grouped by keywords.


"""

p11 = """
The following graphs show the distribution of tweet text length measured in characters and words for **Tweets 2019 -2022** for each year and keyword. In these graphs you may be able to observe the behavior of tweets under this metric grouped for different years and beans number.

"""

p12 = """
In these graphs you could observe the different distributions of tweet length in terms of words and characters for the topics encompassed by the keywords. It is observed that for certain particular topics there are substantial differences in the amount of words that a user uses to express his opinion, and these graphs give you the option to interact to determine the topics with more characters per tweet.
"""

p13 = """
In this section you can explore the tweets 2019-2022 discriminating by keyword, year and month, so that each time random tweets appear on the screen under the above two parameters chosen, in order to observe the content of the tweets, elements used as hashtags, emoticons, among others.

"""

p14 = """
In this section you can explore the tweets 2019-2022 discriminating by keyword, year and month, so that each time random tweets appear on the screen under the above two parameters chosen, in order to observe the content of the tweets, elements used as hashtags, emoticons, among others.

"""

# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUMEN])


def make_empty_fig():
    fig = go.Figure()
    fig.layout.paper_bgcolor = '#FFFFFF'
    fig.layout.plot_bgcolor = '#FFFFFF'
    return fig


layout = html.Div([
################ Section Title ############################

    dbc.Col([
        html.Br(),
        html.H1('Exploratory Data Analisis - EDA'),
        ], style={'textAlign': 'center'}),
    html.Br(), html.Br(),
        html.P(p1),

############### Tabs #############################

    dbc.Tabs([

############### EDA: Tweets 2019 (Tab 1) #################

############### Data understanding I #################
        
        dbc.Tab([
            dbc.Col([
                html.Br(),
                html.H2('Data understanding I'),
        ], style={'textAlign': 'center'}),
            html.Br(),
            html.Br(),
            html.P(p2),
            html.Br(),

############### Distribution of tweet text length #################

            dbc.CardHeader(html.H3('Distribution of tweet text length')),
            html.Br(),
            html.P(p3),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    dcc.Loading([
                        dcc.Graph(id='chars_freq_hist')
                        ]),
                ], lg=6),
                dbc.Col([
                    dcc.Loading([
                        dcc.Graph(id='words_freq_hist')
                        ]),                 
                ], lg=6),
        ]),
            html.Br(),
            html.Div([
                dbc.Alert(f"Please select the number of bins before generating the graphs, otherwise the default will be used.",
                         color='info',
                         fade=True,
                         is_open=True,
                         dismissable=True,)
                ],

                id='feedback_1'),
            dbc.Row([
                dbc.Col(lg=1),
                dbc.Col([
                    dbc.Label('Modify number of bins:'),
                    dcc.Slider(id='hist_bins_slider', 
                       dots=True, min=0, max=100, step=5, included=False,
                       marks={x: str(x) for x in range(0, 105, 5)}),
                ], lg=10),
                dbc.Col(lg=1),
            ]),
            html.Br(),
            html.Div([
                dbc.Button("Generate Graphs",
                outline=True,
                color="primary",
                className="me-1",
                size="sm",
                id="button1"),
                ],  className="d-grid gap-2 col-6 mx-auto"),      
            html.Br(),
            html.P(p4),

############### Explore the text content of the tweet #################
            html.Br(),html.Br(),
            dbc.CardHeader(html.H3('Explore the text content of the tweets')),
            html.Br(),
            html.P(p5),
            html.Br(),
            dcc.Loading([
                dcc.Markdown(id='display_tweet_md',
                             style={'backgroundColor': '#FFFFFF', 'border': '2px solid powderblue', 'padding': '30px'}),
            ]),
            html.Br(),
            html.Div([
                dbc.Alert(f"Click the buton to generate a random tweet, each time you press it a new tweet is generated.",
                         color='info',
                         fade=True,
                         is_open=True,
                         dismissable=True,)
                ],
                id='feedback_2'), 
            html.Br(),
            html.Div([
                dbc.Button("Generate a random tweet",
                outline=True,
                color="primary",
                className="me-1",
                size="sm", id="button2"),
                ], className="d-grid gap-2 col-6 mx-auto"),
            html.Br(), html.Br(),
            html.P(p6_1),html.P(p6_2),html.P(p6_3),html.P(p6_4),


############### Words frequency #################
            html.Br(),html.Br(),
            dbc.CardHeader(html.H3('Words frequency')),
            html.Br(),
            html.P(p7),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    dcc.Loading([
                        dcc.Graph(id='freq_words', figure=rep_words())
                        ]),
                    ], lg=6),
                dbc.Col([
                    dcc.Loading([
                        html.Div([
                            html.Img(src='assets/images/wc_text.jpg')
                        ]),
                    ]),

                ], lg=3),

            ]),
            html.Br(), html.Br(),
            html.P(p8),



        ],label='EDA: Tweets 2019'),

############### Medellin Development Plan (Tab 2) #################

        dbc.Tab([
            dbc.Col([
                    html.Br(),
                    html.H2('Text Analysis'),
            ], style={'textAlign': 'center'}),
            html.Br(),
            html.Br(),
            html.P(p9),
            html.Br(),
            dbc.CardHeader(html.H3('Wordclouds by "Linea Estrategica"')),
            html.P('Explicacion de esta sección'),
            html.Br(),
            dcc.Dropdown(id='lineas_estrategicas',
                         placeholder='Select one "Linea Estrategica"',
                         options=[{'label':linea, 'value':i}
                                  for linea ,i in lineas_estrategicas.items()]),
            html.Br(),
            html.Div([
                dbc.Alert(f"Select a value from the dropdown to generate a short description and its word cloud.",
                         color='info',
                         fade=True,
                         is_open=True,
                         dismissable=True,)
                ],
                id='feedback_wc_mdp'),
            html.Br(), 
            html.Div([
                dbc.Button("Generate Wordclouds",
                outline=True,
                color="primary",
                className="me-1",
                size="sm", id="button_lestr"),
                ],  className="d-grid gap-2 col-6 mx-auto"),
            html.Br(),html.Br(),
            dbc.Row([
                dbc.Col(),
                dbc.Col([
                    dcc.Loading([
                        dcc.Markdown(id='mdp_details_md',
                                     style={'backgroundColor': '#FFFFFF', 'border': '2px solid powderblue', 'padding': '10px'}),
                        ]),
                    ]),
                dbc.Col([
                    dcc.Loading([
                    html.Div([
                    html.Img(id='word_cloud_linea')]),
                ]),
                    ]),
                dbc.Col(),
                ]),
            

        ], label='Medellin Development Plan'),



############### EDA: Tweets keywords 2019 - 2022 (Tab 3) #################

############### Data understanding II #################

        dbc.Tab([
            dbc.Col([
                html.Br(),
                html.H2('Data understanding II'),
        ], style={'textAlign': 'center'}),
            html.Br(),
            html.Br(),
            html.P(p10),
            html.Br(),

############### Distribution of tweet text length #################

            dbc.CardHeader(html.H3('Distribution of tweet text length')),
            html.Br(),
            html.P(p11),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    dbc.Label('Years:'),
                    dcc.Dropdown(id='hist_year_dropdown_2022',
                                 multi=True,
                                 placeholder='Select one or more years',
                                 options=[{'label': year, 'value': year} for year in [2019,2020,2021,2022]]),
                    ]),
                dbc.Col([
                    dbc.Label('Keyword:'),
                    dcc.Dropdown(id='keyword_selector_20221',
                                 placeholder='Select one keyword',
                                 options=[{'label':keyword.title(), 'value':keyword}
                                          for keyword in ['cultura','empresa','jovenes','metro','movilidad',
                                                            'seguridad','tecnologia','trabajo','vida']]),
                ]),
                ]),
            dbc.Row([
                dbc.Col([
                    dcc.Loading([
                        dcc.Graph(id='chars_freq_hist_2022')
                        ]),
                ], lg=6),
                dbc.Col([
                    dcc.Loading([
                        dcc.Graph(id='words_freq_hist_2022')
                        ]),                 
                ], lg=6),
        ]),
            html.Br(),
            html.Div([
                dbc.Alert(f"Please select the number of bins, year(s) and keyword before generating the charts.",
                         color='info',
                         fade=True,
                         is_open=True,
                         dismissable=True,)
                ],id='feedback_1_2022'),
            dbc.Row([
                dbc.Col(lg=1),
                dbc.Col([
                    dbc.Label('Modify number of bins:'),
                    dcc.Slider(id='hist_bins_slider_2022',
                       dots=True, min=0, max=100, step=5, included=False,
                       marks={x: str(x) for x in range(0, 105, 5)}),
                ], lg=10),
                dbc.Col(lg=1),
            ]),
            html.Br(),
            html.Div([
                dbc.Button("Generate Graphs",
                outline=True,
                color="primary",
                className="me-1",
                size="sm",
                id="button1_2022"),
                ],  className="d-grid gap-2 col-6 mx-auto"),      
            html.Br(),
            html.P(p12),

############### Explore the text content of the tweet #################

            html.Br(),html.Br(),
            dbc.CardHeader(html.H3('Explore the text content of the tweets')),
            html.Br(),
            html.P(p13),
            html.Br(), 
            dbc.Label('Keyword:'),
            dcc.Dropdown(id='keyword_selector_20222',
                         placeholder='Select one keyword',
                         value='cultura',
                         options=[{'label':keyword.title(), 'value':keyword}
                                   for keyword in ['cultura','empresa','jovenes','metro','movilidad',
                                                    'seguridad','tecnologia','trabajo','vida']]),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    dbc.Label('Year:'),
                    dcc.Slider(id='years_random_tweet_slider_2022',
                       dots=True, min=2019, max=2022, step=1, included=False, value=2019,
                       marks={x: str(x) for x in range(2019, 2023, 1)}),
                    ]),
                dbc.Col([
                    dbc.Label('Month:'),
                    dcc.Dropdown(id='month_selector_2022',
                         placeholder='Select one month', value=1,
                         options=[{'label':month, 'value':i}
                                   for i, month in months.items()]),
                    ]),


                ]),
            html.Br(),
            dcc.Loading([
                dcc.Markdown(id='display_tweet_text_2022_md',
                             style={'backgroundColor': '#FFFFFF', 'border': '2px solid powderblue', 'padding': '30px'}),
            ]),
            html.Br(),
            html.Div([
                dbc.Alert(f"Select a value for keyword, year and month, otherwise the default value will be selected, then press the button to generate a random tweet, every time you press it a new random tweet will be generated.",
                         color='info',
                         fade=True,
                         is_open=True,
                         dismissable=True,)
                ],id='feedback_2_2022'),
            html.Br(),
            html.Div([
                dbc.Button("Generate a random tweet",
                outline=True,
                color="primary",
                className="me-1",
                size="sm", id="button2_2022"),
                ], className="d-grid gap-2 col-6 mx-auto"),
            html.Br(),html.Br()   


        ],label='EDA: Tweets keywords 2019 - 2022'),
        
        ]),
    ])
