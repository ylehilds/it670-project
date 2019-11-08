import json
import twitter
import auth

def twitter_trends(twitter_api, woe_id):
    # Prefix ID with the underscore for query string parameterization.
    # Without the underscore, the twitter package appends the ID value
    # to the URL itself as a special-case keyword argument.
    return twitter_api.trends.place(_id=woe_id)

# Sample usage

# twitter_api = auth.oauth_login()

# See https://developer.twitter.com/en/docs/trends/trends-for-location/api-reference/get-trends-place
# and http://www.woeidlookup.com to look up different Yahoo! Where On Earth IDs

WORLD_WOE_ID = 1
# world_trends = twitter_trends(twitter_api, WORLD_WOE_ID)
# print(json.dumps(world_trends, indent=1))
#
# US_WOE_ID = 23424977
# us_trends = twitter_trends(twitter_api, US_WOE_ID)
# print(json.dumps(us_trends, indent=1))