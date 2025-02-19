from src.TakeoutParser import TakeoutParser


def test_takeout_parser():
    directory = ""
    tp = TakeoutParser(directory)
    assert True


def test_find_all_content():
    directory = "../takeout-files"
    tp = TakeoutParser(directory)
    tp.parse_html(file_path='../takeout-files/Ads.html')

    assert True
