import pandas as pd
import plotly.figure_factory as ff
import statistics

df= pd.read_csv("data2.csv")
ratings = df["Avg Rating"].tolist()
figure = ff.create_distplot([ratings], ["Average Ratings"], show_hist = False)
figure.show()
diviation = statistics.stdev(ratings)
print(ratings)

