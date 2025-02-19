# tmp test file for development
from TakeoutParser import TakeoutParser
from pprint import pprint

if __name__ == "__main__":
    directory = "../takeout-files"
    tp = TakeoutParser(directory)
    file_path = "../takeout-files/YouTube.html"

    df = tp.parse_html(file_path)

    pprint(df)


