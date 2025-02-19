import bs4
import os
import pandas as pd
from datetime import datetime


class TakeoutParser:
    """
        Purpose: a small tool so anyone can pass a directory of Takeout HTML and get their time data in return
    """

    def __init__(self, directory):
        self.directory = directory
        self.df = None

    def parse_html(self, file_path):
        """
        purpose: Extract the date, time, and content that I accessed/searched for. Everything looks to be the same structure.

        :param file_path: the path to a single HTML file
        :return: dataframe object with the data we need to know times I access things

        In the HTML file I am looking for the
        """

        # read in HTML file as a string

        with open(file_path, 'r') as html_doc_reader:
            content = html_doc_reader.read()

        # soupify
        soup = bs4.BeautifulSoup(content, "html.parser")

        # visits
        # "outer-cell mdl-cell mdl-cell--12-col mdl-shadow--2dp"
        visits = soup.find_all(class_="outer-cell mdl-cell mdl-cell--12-col mdl-shadow--2dp")

        content = []
        dates = []
        times = []

        # print(f"Need to search through {len(visits)} records")
        for v in visits:
            try:
                # class ="content-cell mdl-cell mdl-cell--6-col mdl-typography--body-1" >
                # I did this with the help of ChatGPT - mainly just figuring out how to parse the HTML correctly.
                # I identified the tags and class names that I needed, but used ChatGPT for the function calls
                c = v.find(class_="mdl-typography--title").get_text()
                date = v.find(class_="content-cell mdl-cell mdl-cell--6-col mdl-typography--body-1").find_all("br")[
                    -1].find_next_sibling(text=True).strip()
                date = date.replace("\u202f", " ")

                # datetime formatting
                date_format = "%b %d, %Y, %I:%M:%S %p %Z"
                dt = datetime.strptime(date, date_format)
                d = dt.date()
                t = dt.time()

                # append to our date sources
                content.append(c)
                dates.append(d)
                times.append(t)

            except Exception as e:
                print("x")

        # PK will be the date and time
        # Content will not be included in the PK

        tmp_df = pd.DataFrame(
            {
                'date': dates,
                'time': times,
                'content': content
            }
        )
        return tmp_df

    def find_class_variables(self):
        """
            Look for class names in the HTML file to get the correct content. More of an automated approach in case the HTML changes

        :return:
        """
        pass

    def parse_ics(self, file_path):
        """

        :param file_path:
        :return:
        """
        pass

    def scrape_all_takeout_files(self):
        """
        Purpose: iterate through the directory and scrape all files
        :param directory: directory containing all the files we need to parse to get data
        :return:
        """

        files = os.listdir(self.directory)

        # print(f"Beginning HTML extraction for {self.directory} directory")
        html_files = []
        for f in files:
            file_ending = f.split(".")[1]
            if file_ending == "html":
                html_files.append(f)

        total = len(html_files)
        i = 1

        for f in html_files:

            # PERCENTAGE COMPLETION PRINTING MECHANISM (inspired from ChatGPT, minor modifications made)
            percent = (i / total) * 100  # Calculate percentage
            bar = "#" * (i)  # Progress bar (half-length)
            spaces = " " * (total - len(bar))  # Padding to keep the bar aligned
            print(f"\r[{bar}{spaces}] {percent:.2f}%", end="")  # Print on the same line

            # logic
            tmp_df = self.parse_html(self.directory + "/" + f)
            if self.df is not None:
                self.df = pd.concat([self.df, tmp_df])
            else:
                self.df = tmp_df
            i += 1

    def write_out_csv(self, file_path):
        """
        Purpose: write the dataframe that we scrape out to a CSV file

        :param file_path:
        :return: None
        """
        self.df.to_csv(file_path)

    def write_out_json(self, file_path):
        """

        Purpose: Write the dataframe that we scrape out to a JSON file

        :param file_path:
        :return: None
        """
        pass
