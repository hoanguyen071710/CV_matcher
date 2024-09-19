import argparse

from .controller.runserver import app
from .service.jobScraper.TimeBased import TimeBasedScrape


def run_daily_job():
    tc = TimeBasedScrape()
    print("Start scraping ...")
    tc.scrape()

def run_server():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--server", action="store_true")
    parser.add_argument("--timebased-crawl", action="store_true")
    args = parser.parse_args()
    if args.server:
        print("run server")
        run_server()
    elif args.timebased_crawl:
        print("Start time-based scrape")
        run_daily_job()
        # print("run daily job")
