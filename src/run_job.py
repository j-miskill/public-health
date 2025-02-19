from scrape_timeline_data import TakeoutParser

if __name__ == "__main__":
    print("Please provide the directory")
    directory = "../takeout-files"
    tp = TakeoutParser(directory=directory)
    tp.scrape_all_takeout_files()

