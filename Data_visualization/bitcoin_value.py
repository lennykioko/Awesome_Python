import pandas
from bokeh.plotting import figure, output_file, show

df = pandas.read_csv("bitcoin.csv", parse_dates=["Date"])
p = figure(plot_width=1200, plot_height=600, title="Bitcoin Value", x_axis_type="datetime",
        toolbar_location="above")

p.xaxis.axis_label = "Date"
p.yaxis.axis_label = "Value of Bitcoin"

p.line(df["Date"], df["Value"], line_width=1, color="green", alpha=0.8)
output_file("Bitcoin_value.html")
show(p)
