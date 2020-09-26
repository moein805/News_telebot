import feedparser

def news (rss):
	NewsFeed = feedparser.parse(rss)
	NewsFeed = NewsFeed.entries
	a = NewsFeed[0]
	n = "======---->>>>>>>>><<<<<<<<<<----========"
#	news = (title,link)
	return n
#	print(news)


#	title = a.title
#	summary =a.summary
#	link =a.link
#	pub=a.published

m =news("https://www.irinn.ir/fa/rss/allnews")

print(m)

