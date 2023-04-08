import codecademylib3
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')

#1

print(ad_clicks.head())

#2

total_views = ad_clicks.groupby("utm_source").count().reset_index()
print(total_views)

#3

ad_clicks["is_click"] = ~ad_clicks.ad_click_timestamp.isnull()
print(ad_clicks)

#4

clicks_by_source = ad_clicks.groupby(["utm_source","is_click"]).user_id.count().reset_index()

#5

clicks_pivot = clicks_by_source.pivot(
  columns = "is_click",
  index = "utm_source",
  values = "user_id"
).reset_index()

print(clicks_pivot)

#6
clicks_pivot["percent_clicked"] = clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])

print(clicks_pivot)

#7

test = ad_clicks.groupby("experimental_group").count().reset_index()
print(test)

#8
test2 = ad_clicks.groupby(["experimental_group","is_click"]).user_id.count().reset_index()

print(test2)

#9
a_clicks = ad_clicks[ad_clicks.experimental_group == "A"]
b_clicks = ad_clicks[ad_clicks.experimental_group == "B"]

#10
a_perday = a_clicks.groupby(["day","is_click"]).user_id.count().reset_index()
print(a_perday)

b_perday = b_clicks.groupby(["day","is_click"]).user_id.count().reset_index()
print(b_perday)

a_perday_pivot = a_perday.pivot(
  columns = "is_click",
  index = "day",
  values = "user_id"
).reset_index()

#11

a_perday_pivot["percent_clicked"] = a_perday_pivot[True] / (a_perday_pivot[True] + a_perday_pivot[False])

print(a_perday_pivot)

b_perday_pivot = b_perday.pivot(
  columns = "is_click",
  index = "day",
  values = "user_id"
).reset_index()

b_perday_pivot["percent_clicked"] = b_perday_pivot[True] / (b_perday_pivot[True] + b_perday_pivot[False])

print(b_perday_pivot)