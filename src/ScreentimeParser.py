import sqlite3
import os
import sys
import json
from pprint import pprint
import pandas as pd
import numpy as np

"""
Sources:

1. https://apple.stackexchange.com/questions/346091/is-there-a-way-to-download-screen-time-data-from-iphone-or-other-apple-devices/459159#459159 
2. https://www.reddit.com/r/MacOS/comments/lradsq/in_what_folder_is_screen_time_history_data_stored/ 
3. https://github.com/mac4n6/APOLLO/tree/bd725461fbd22c8ceadd04f0c4ded49b66147439 
"""


class ScreentimeParser:

    def __init__(self, filepath):
        self.filepath = filepath
        self.df = None

    def connect_to_db(self):

        try:
            if os.path.exists(self.filepath):
                connection = sqlite3.connect(self.filepath)
                cursor = connection.cursor()
                return cursor, connection
        except Exception as e:
            print("Connecting to DB failed. Try checking to make sure the entire path is there (including the DB)")
            return e

    def run_query(self, cursor, query):
        try:
            cursor.execute(query)
            output = cursor.fetchall()
            return output
        except Exception as e:
            print("Query failed. Review exception below for guidance")
            return e

    def get_app_usage_data(self, filepath):
        with open("assets/queries/app_usage.txt", "r") as file:
            query = file.read()

        cursor, connection = self.connect_to_db()
        output = self.run_query(cursor=cursor, query=query)
        connection.close()

        tmp_df = pd.DataFrame(output)
        tmp_df.to_csv(filepath+'app-usage-data.csv')




