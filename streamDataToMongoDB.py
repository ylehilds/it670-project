import sys
import datetime
import time
import twitter
import mongo_db
from trends import twitter_world_trends


def get_time_series_data(api_func, mongo_db_name, mongo_db_coll,
                         secs_per_interval=60, max_intervals=15, **mongo_conn_kw):
    # Default settings of 15 intervals and 1 API call per interval ensure that
    # you will not exceed the Twitter rate limit.

    interval = 0

    while True:

        # A timestamp of the form "2013-06-14 12:52:07"
        now = str(datetime.datetime.now()).split(".")[0]

        response = mongo_db.save_to_mongo(api_func(), mongo_db_name, mongo_db_coll, **mongo_conn_kw)

        print("Write {0} trends".format(len(response.inserted_ids)), file=sys.stderr)
        print("Zzz...", file=sys.stderr)
        sys.stderr.flush()

        time.sleep(secs_per_interval)  # seconds
        interval += 1

        if interval >= 15:
            break


# Sample usage

get_time_series_data(twitter_world_trends, 'time-series', 'twitter_world_trends', host='mongodb://localhost:27017')