import json
import auth
import search
import topics
from functools import partial

pp = partial(json.dumps, indent=1)

twitter_world_trends = partial(topics.twitter_trends, auth.twitter_api, topics.WORLD_WOE_ID)

print(pp(twitter_world_trends()))

authenticated_twitter_search = partial(search.twitter_search, auth.twitter_api)
results = authenticated_twitter_search("iPhone")
print(pp(results))

authenticated_iphone_twitter_search = partial(authenticated_twitter_search, "iPhone")
results = authenticated_iphone_twitter_search()
print(pp(results))