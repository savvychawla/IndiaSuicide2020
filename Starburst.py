import pandas as pd
import numpy as np

pd.set_option("max_columns", 30)

import plotly.express as px
import plotly.graph_objects as go

suicide = pd.read_csv('data.csv')
color_discrete_sequence = ['Gender', 'Age_Bracket', 'Cause']
suicide["Center"] = "India Suicide 2020"
fig = px.sunburst(suicide, path=["Center", "Gender", "Age_Bracket", "Cause", "Sub-Cause"], values='Number_of_cases', color='Age_Bracket')

fig.write_image("/Users/Desktop/output.png", engine="kaleido")
fig.write_html("/Users/Desktop/index.html")
fig.show()
