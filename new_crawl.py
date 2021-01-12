from datetime import date
import clarku_youtube_crawler as cu
import clarku_youtube_crawler.RawCrawler as rc

print(cu.__version__)
# cu.config_override(True)

raw_crawler = rc.RawCrawler()
raw_crawler.__build__()

start_month = 10
start_day = 25
start_year = 2019
end_month = 12
end_day = 31
end_year = 2019

# start = date(start_year, start_month, start_day)
# end = date(end_year, end_month, end_day)
# delta = end-start
#
# raw_crawler.crawl("teamtrees",
#                   start_day=start_day,
#                   start_month=start_month,
#                   start_year=start_year,
#                   day_count=delta.days)

raw_crawler.crawl_videos_in_list(4)