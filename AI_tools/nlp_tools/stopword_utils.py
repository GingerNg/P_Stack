

def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords
# segs = filter(lambda x: x not in stopwords, segs)  # 去掉停用词
stopwords = stopwordslist("/home/ginger/Projects/StaticResource/stopwords.txt")

