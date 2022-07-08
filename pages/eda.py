from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly 
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv('pages/data/2019.csv')
df['num_chars'] = df['full_text'].str.len()
df['num_words'] = df['full_text'].str.split().str.len()

df2 = pd.read_csv('pages/data/tweets.csv')
df2['weekday'] = pd.to_datetime(df2['date']).dt.weekday
df2['year'] = pd.to_datetime(df2['date']).dt.year
df2['month'] = pd.to_datetime(df2['date']).dt.month
df2['num_chars'] = df2['full_text'].str.len()
df2['num_words'] = df2['full_text'].str.split().str.len()

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


df3 = df2['year'].value_counts().sort_index().to_frame().reset_index()
fig = px.pie(df3,values='year',names='index', 
    title=f'Pie chart - Tweets distribution by year.')

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
