from icrawler.builtin import UrlListCrawler

urllist_crawler = UrlListCrawler(downloader_threads=4,
                                 storage={"root_dir": "images"})
urllist_crawler.crawl("url_list.txt")
