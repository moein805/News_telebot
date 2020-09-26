import feedparser

def news (rss):
	NewsFeed = feedparser.parse(rss)
	NewsFeed = NewsFeed.entries
	a = NewsFeed[0]
	title = a.title
	summary =a.summary
	link =a.link
	pub=a.published
	n = "======---->>>>>>>>><<<<<<<<<<----========"
	news = (title,link)
	return str(news)
	print(news)
