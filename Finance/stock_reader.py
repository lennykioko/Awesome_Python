import datetime
from pandas_datareader import data
from bokeh.plotting import figure, show, output_file


start = datetime.datetime(2017, 11, 1)
end = datetime.datetime(2018, 1, 1)

df = data.DataReader(name="AMZN", data_source="google", start=start, end=end)

p = figure(plot_width=900, plot_height=600, title="Stock Prices Analysis", x_axis_type="datetime",
           toolbar_location="above", sizing_mode='scale_width')

p.xaxis.axis_label = "Date"
p.yaxis.axis_label = "Prices"
p.grid.grid_line_alpha = 0.3

def inc_or_dec(closing, opening):
    if closing > opening:
        value = "increase"
    elif closing < opening:
        value = "decrease"
    else:
        value = "equal"
    return value

df["Status"] = [inc_or_dec(closing, opening) for closing, opening in zip(df.Close, df.Open)]
df["Middle"] = (df.Open + df.Close)//2
df["Height"] = abs(df.Close - df.Open)

p.segment(df.index, df.High, df.index, df.Low, color="black")

twelve_hours = 12 * 60 * 60 * 1000
p.rect(df.index[df.Status == "increase"], df.Middle[df.Status == "increase"], twelve_hours,
       df.Height[df.Status == "increase"], fill_color="#47d147", line_color="black")

p.rect(df.index[df.Status == "decrease"], df.Middle[df.Status == "decrease"], twelve_hours,
       df.Height[df.Status == "decrease"], fill_color="#ff3333", line_color="black")

p.rect(df.index[df.Status == "equal"], df.Middle[df.Status == "equal"], twelve_hours,
       df.Height[df.Status == "equal"] + 0.001, fill_color="black", line_color="black")


output_file("Stock_analysis.html")
show(p)
# print(df)
