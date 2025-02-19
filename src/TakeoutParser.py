import bs4
import os


class TakeoutParser:
    """
        Purpose: a small tool so anyone can pass a directory of Takeout HTML and get their time data in return
    """

    def __init__(self, directory):
        self.directory = directory

    def parse_html(self, file_path):
        """
        purpose: Extract the date, time, and content that I accessed/searched for. Everything looks to be the same structure.

        :param file_path: the path to a single HTML file
        :return: dataframe object with the data we need to know times I access things
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

        pass

    def write_out_csv(self, file_path):
        """
        Purpose: write the dataframe that we scrape out to a CSV file

        :param file_path:
        :return: None
        """
        pass

    def write_out_json(self, file_path):
        """

        Purpose: Write the dataframe that we scrape out to a JSON file

        :param file_path:
        :return: None
        """
        pass


