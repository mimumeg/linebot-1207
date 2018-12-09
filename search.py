from icrawler.builtin import GoogleImageCrawler

crawler = GoogleImageCrawler(storage={"root_dir": "images"})
crawler.crawl(keyword="もふもふ", max_num=10)
