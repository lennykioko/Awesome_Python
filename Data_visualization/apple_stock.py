import pandas
from bokeh.plotting import figure, output_file, show

df = pandas.read_csv("apple.csv", parse_dates=["Date"])
p = figure(plot_width=1200, plot_height=600, title="Apple Stock Prices", x_axis_type="datetime",
           toolbar_location="above")

p.xaxis.axis_label = "Date"
p.yaxis.axis_label = "Price"

p.line(df["Date"], df["Open"], line_width=1, color="gray", alpha=0.3)
p.line(df["Date"], df["Close"], line_width=2, color="blue", alpha=0.6)
p.line(df["Date"], df["High"], line_width=1, color="green", alpha=0.3)
p.line(df["Date"], df["Low"], line_width=1, color="red", alpha=0.3)

output_file("Apple_stock.html")
show(p)
