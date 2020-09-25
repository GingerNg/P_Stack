import nltk
# 词干解析
stemmer = nltk.stem.porter.PorterStemmer()
stemmer.stem('flowers')
