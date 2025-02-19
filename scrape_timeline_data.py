import bs4


class TakeoutParser:
    """
        Purpose: a small tool so anyone can pass a directory of Takeout HTML and get their time data in return
    """

    def __init__(self, directory):
        self.directory = directory

    def parse_html(self, file_path):
        """
        purpose: Extract the date, time, and content that I accessed/searched for. Everything looks to be the same structure.

        :param file_path:
        :return: dataframe object with the data we need to know times I access things
        """
        pass

    def scrape_all_takeout_files(self):
        """
        Purpose: iterate through the directory and scrape all files
        :param directory: directory containing all the files we need to parse to get data
        :return:
        """
        pass
