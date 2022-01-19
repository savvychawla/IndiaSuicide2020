import pandas as pd
import numpy as np

import plotly.express as px

suicide = pd.read_csv('data.csv')
color_discrete_sequence = ['Gender', 'Age_Bracket', 'Cause']
suicide["Center"] = "India Suicide 2020"
fig = px.sunburst(suicide, path=["Center", "Gender", "Age_Bracket", "Cause", "Sub-Cause"], values='Number_of_cases', color='Age_Bracket')

fig.write_image("output.png", engine="kaleido")
fig.write_html("index.html")
fig.show()
