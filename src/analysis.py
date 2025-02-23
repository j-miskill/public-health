import pandas as pd
import numpy as np
from pprint import pprint
import matplotlib.pyplot as plt
import seaborn as sns
from ScreentimeParser import ScreentimeParser

if __name__ == "__main__":

    takeout_data = pd.read_csv("output-data/takeout.csv")
    st_data = pd.read_csv("output-data/app-usage-data.csv")

    st_data['date'] = pd.to_datetime(st_data['START']).dt.date
    st_data['time'] = pd.to_datetime(st_data['START']).dt.time

    earliest_times = st_data.groupby("date")['time'].min().reset_index()
    latest_times = st_data.groupby("date")['time'].max().reset_index()

    noon = pd.to_datetime("12:00:00").time()
    six_am = pd.to_datetime("06:00:00").time()
    seven = pd.to_datetime("19:00:00").time()

    earliest_times_filtered = earliest_times[(earliest_times['time'] < noon) & (earliest_times['time'] > six_am)]
    latest_times_filtered = latest_times[latest_times['time'] > seven]

    print(earliest_times_filtered)
    print()
    print(latest_times_filtered)

    # takeout_data['date'] = pd.to_datetime(takeout_data['date'])
    # takeout_data['time'] = pd.to_datetime(takeout_data['time'])
    #
    # # takeout_data = takeout_data.drop("Unnamed: 0")
    #
    # takeout_data['time'] = takeout_data['time'].dt.time
    # # st_data['datetime'] = pd.to_datetime(st_data['date'] + ' ' + st_data['time'])

    # earliest_times = takeout_data.groupby("date")['time'].min().reset_index()
    # latest_times = takeout_data.groupby("date")['time'].max().reset_index()

    # earliest_times_filtered = earliest_times[earliest_times['time'] < noon]
    # earliest_times_filtered = earliest_times_filtered.sort_values(by='time', ascending=True)
    # earliest_times_filtered['timedelta'] = pd.to_timedelta(earliest_times_filtered['time'].astype(str))
    # # print(earliest_times_filtered.count())
    #
    # latest_times_filtered = latest_times[latest_times['time'] > five]
    # latest_times_filtered = latest_times_filtered.sort_values(by='time', ascending=True)
    # latest_times_filtered['timedelta'] = pd.to_timedelta(latest_times_filtered['time'].astype(str))

    # mean_earliest_time = earliest_times_filtered['timedelta'].mean()
    # median_earliest_time = earliest_times_filtered['timedelta'].median()
    #
    # mean_latest_time = latest_times_filtered['timedelta'].mean()
    # median_latest_time = latest_times_filtered['timedelta'].median()
    #
    # print("Mean earliest:", mean_earliest_time)
    # print("Median earliest time:", median_earliest_time)
    #
    # print("Mean latest:", mean_latest_time)
    # print("Median latest time", median_latest_time)

    # plt.figure(figsize=(10, 6))
    # earliest_times_filtered['time_in_seconds'] = earliest_times_filtered['timedelta'].dt.total_seconds()
    # sns.histplot(earliest_times_filtered['time_in_seconds'], kde=True, color="blue", label="Earliest Times",
    #              stat="density", bins=10, linewidth=2)
    # # sns.histplot(latest_seconds, kde=True, color="red", label="Latest Times", stat="density", bins=10, linewidth=2)
    #
    # # Add labels and title
    # plt.xlabel('Time of Day')
    # plt.ylabel('Density')
    # plt.title('Histogram of earliest Times of Day')
    # plt.legend()
    #
    # # Show the plot
    # plt.show()
    #
    #
    # plt.figure(figsize=(10, 6))
    # latest_times_filtered['time_in_seconds'] = latest_times_filtered['timedelta'].dt.total_seconds()
    # sns.histplot(latest_times_filtered['time_in_seconds'], kde=True, color="blue", label="Earliest Times", stat="density", bins=10, linewidth=2)
    # # sns.histplot(latest_seconds, kde=True, color="red", label="Latest Times", stat="density", bins=10, linewidth=2)
    #
    # # Add labels and title
    # plt.xlabel('Time of Day')
    # plt.ylabel('Density')
    # plt.title('Histogram of Latest Times of Day')
    # plt.legend()
    #
    # # Show the plot
    # plt.show()

    # both_early_and_late = pd.concat([earliest_times_filtered, latest_times_filtered])
    # both_early_and_late['date'] = pd.to_datetime(both_early_and_late['date'])
    # valid_dates = both_early_and_late['date']
    #
    # valid_dates_full_table = pd.merge(takeout_data, valid_dates, on=['date'], how='inner')
    #
    # content_type = valid_dates_full_table.groupby("content").agg({
    #     'time': 'count'
    #     })
    # content_type = content_type[content_type['time'] > 5]
    # print(content_type)
    #
    # plt.figure(figsize=(10, 6))
    # sns.barplot(content_type, x='content', y='time')
    # plt.xlabel('Content Type')
    # plt.ylabel('Interaction Count')
    # plt.title('Barplot of content distribution')
    # plt.legend()
    # plt.show()


    # starting with the takeout data
    # I could start with a histogram, though
    # maybe for the earliest times I should remove all values after noon, because that would be an outlier
    # maybe for the latest times, I should remove all values before 5pm, because that would also be an outlier

    #
    # pprint(earliest_times)
    #
    # earliest_seconds = earliest_times.dt.hour * 3600 + earliest_times.dt.minute * 60 + earliest_times.dt.second
    # latest_seconds = latest_times.dt.hour * 3600 + latest_times.dt.minute * 60 + latest_times.dt.second
    #

    #
    # avg_earliest_seconds = earliest_seconds.mean()
    # avg_latest_seconds = latest_seconds.mean()
    #
    # # Step 4: Convert back to hours, minutes, and seconds
    # avg_earliest_time = pd.to_datetime(avg_earliest_seconds, unit='s').time()
    # avg_latest_time = pd.to_datetime(avg_latest_seconds, unit='s').time()

    # print("Earliest time", avg_earliest_time)
    # print("Latest time", avg_latest_time)
