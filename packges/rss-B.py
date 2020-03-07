
import feedparser

# https://www.jianshu.com/p/1cd90236fb1a

def rss():
    # rss_subscribe_url = 'http://faxian.smzdm.com/feed'
    rss_subscribe_url = "https://rsshub.app/douban/movie/weekly"
    file = feedparser.parse(rss_subscribe_url)
    print([item.title for item in file.entries])
    print([item.link for item in file.entries])
    print([item.summary for item in file.entries])

if __name__ == '__main__':
    rss()