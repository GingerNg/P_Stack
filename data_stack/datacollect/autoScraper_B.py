from autoscraper import AutoScraper

# url = 'https://stackoverflow.com/questions/2081586/web-scraping-with-python'
url = "http://lite.cnn.com/en"
# url = "https://www.zhibo8.cc/"

# We can add one or multiple candidates here.
# You can also put urls here to retrieve urls.
# wanted_list = ["How to call an external command?"]
wanted_list = ["Despite Trump's efforts, the transition is happening"]

scraper = AutoScraper()
result = scraper.build(url, wanted_list)
print(result)
