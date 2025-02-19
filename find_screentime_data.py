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

db = os.getenv("DB")
print("looking for: ", f"../../{db}")
if os.path.exists(f"../../{db}"):
    print("DB exists where we think it does")

print()
print("Attempting to connect to DB")

connection = sqlite3.connect(f"./../{db}")

print('connection established...')
print()

cursor = connection.cursor()

# PREVIOUS QUERIES THAT WORK
"""

- "SELECT name FROM sqlite_master WHERE type='table';"
- "SELECT DISTINCT ZOBJECT.ZSTREAMNAME FROM ZOBJECT ORDER BY ZSTREAMNAME;"


"""


app_data_query = """
SELECT
  DATETIME(ZOBJECT.ZSTARTDATE + 978307200, 'UNIXEPOCH') AS 'START',
  DATETIME(ZOBJECT.ZENDDATE + 978307200, 'UNIXEPOCH') AS 'END',
  ZOBJECT.ZVALUESTRING AS 'BUNDLE ID',
  (ZOBJECT.ZENDDATE - ZOBJECT.ZSTARTDATE) AS 'USAGE IN SECONDS',
  (ZOBJECT.ZENDDATE - ZOBJECT.ZSTARTDATE) / 60.00 AS 'USAGE IN MINUTES',
  ZSOURCE.ZDEVICEID AS 'DEVICE ID (HARDWARE UUID)',
  ZCUSTOMMETADATA.ZNAME AS 'NAME',
  ZCUSTOMMETADATA.ZDOUBLEVALUE AS 'VALUE',
  CASE ZOBJECT.ZSTARTDAYOFWEEK
    WHEN '1' THEN 'Sunday'
    WHEN '2' THEN 'Monday'
    WHEN '3' THEN 'Tuesday'
    WHEN '4' THEN 'Wednesday'
    WHEN '5' THEN 'Thursday'
    WHEN '6' THEN 'Friday'
    WHEN '7' THEN 'Saturday'
  END AS 'DAY OF WEEK',
  ZOBJECT.ZSECONDSFROMGMT / 3600 AS 'GMT OFFSET',
  DATETIME(ZOBJECT.ZCREATIONDATE + 978307200, 'UNIXEPOCH') AS 'ENTRY CREATION',
  ZOBJECT.ZUUID AS 'UUID',
  ZSTRUCTUREDMETADATA.ZMETADATAHASH,
  ZOBJECT.Z_PK AS 'ZOBJECT TABLE ID'
FROM ZOBJECT
  LEFT JOIN ZSTRUCTUREDMETADATA
    ON ZOBJECT.ZSTRUCTUREDMETADATA = ZSTRUCTUREDMETADATA.Z_PK
  LEFT JOIN ZSOURCE
    ON ZOBJECT.ZSOURCE = ZSOURCE.Z_PK
  LEFT JOIN Z_4EVENT
    ON ZOBJECT.Z_PK = Z_4EVENT.Z_11EVENT
  LEFT JOIN ZCUSTOMMETADATA
    ON Z_4EVENT.Z_4CUSTOMMETADATA = ZCUSTOMMETADATA.Z_PK
WHERE ZSTREAMNAME = '/app/usage'
ORDER BY START DESC;
"""


try:
    cursor.execute(app_data_query)
    response = cursor.fetchall()
    output_df = pd.DataFrame(response)
    output_df.to_csv("../knowledge.csv")

except Exception as e:
    print("query did not work for following reason:", e)

connection.close()



print("Closed")
