class Newspaper:
    def __init__(self):
        self.articles = []

    def publish_article(self, title):
        self.articles.append(title)

        print(f"Published Article: {title}")