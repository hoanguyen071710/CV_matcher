import argparse

from .controller.runserver import app


def run_daily_job():
    pass

def run_server():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--server", action="store_true")
    parser.add_argument("--daily-job-crawl", action="store_true")
    args = parser.parse_args()
    if args.server:
        print("run server")
        run_server()
    elif args.daily_job_crawl:
        # run_daily_job()
        print("run daily job")
