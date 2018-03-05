import pandas
from bokeh.plotting import figure, output_file, show

df = pandas.DataFrame(columns=["X", "Y"])
df["X"] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
df["Y"] = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

p = figure(plot_width=900, plot_height=600, title="Tempretaure Observations")

p.title.text_color = "olive"
p.title.text_font = "times"
p.title.text_font_style = "italic"
p.title.text_font_size = "18pt"

p.xaxis.axis_label = "Day of observation"
p.yaxis.axis_label = "Temperature in degrees celcius"

p.circle(df["X"], df["Y"], size=5, color="red", alpha=0.5)

output_file("Weather_chart.html")
show(p)
