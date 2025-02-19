import pandas as pd
import numpy as np
from pprint import pprint
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == "__main__":
    takeout_data = pd.read_csv("output-data/takeout.csv")
    st_data = pd.read_csv("output-data/app-usage-data.csv")

    takeout_data['date'] = pd.to_datetime(takeout_data['date'])
    takeout_data['time'] = pd.to_datetime(takeout_data['time'])
    # st_data['datetime'] = pd.to_datetime(st_data['date'] + ' ' + st_data['time'])



    # starting with the takeout data
    # I could start with a histogram, though
    # maybe for the earliest times I should remove all values after noon, because that would be an outlier
    # maybe for the latest times, I should remove all values before 5pm, because that would also be an outlier

    earliest_times = takeout_data.groupby("date")['time'].min()
    latest_times = takeout_data.groupby("date")['time'].max()

    pprint(earliest_times)

    earliest_seconds = earliest_times.dt.hour * 3600 + earliest_times.dt.minute * 60 + earliest_times.dt.second
    latest_seconds = latest_times.dt.hour * 3600 + latest_times.dt.minute * 60 + latest_times.dt.second

    plt.figure(figsize=(10, 6))
    sns.histplot(earliest_seconds, kde=True, color="blue", label="Earliest Times", stat="density", bins=10, linewidth=2)
    sns.histplot(latest_seconds, kde=True, color="red", label="Latest Times", stat="density", bins=10, linewidth=2)

    # Add labels and title
    plt.xlabel('Time of Day (seconds since midnight)')
    plt.ylabel('Density')
    plt.title('Histogram of Earliest and Latest Times of Day')
    plt.legend()

    # Show the plot
    plt.show()

    avg_earliest_seconds = earliest_seconds.mean()
    avg_latest_seconds = latest_seconds.mean()

    # Step 4: Convert back to hours, minutes, and seconds
    avg_earliest_time = pd.to_datetime(avg_earliest_seconds, unit='s').time()
    avg_latest_time = pd.to_datetime(avg_latest_seconds, unit='s').time()

    # print("Earliest time", avg_earliest_time)
    # print("Latest time", avg_latest_time)











