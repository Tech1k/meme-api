import praw
from random import choice

CLIENT_ID = "CLIENT_ID_HERE"
CLIENT_SECRET = "CLIENT_SECRET_HERE"
USER_AGENT = "Catbot 1.2.5 by /u/Tech1k catbot.dev"

reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, user_agent=USER_AGENT)

TOPICS = [
    "dankmemes"
]

def ScrapMemes(topic=0, num=1):
    try:
        if num <= 0:
            return {
                "code": 400,
                "message": "Enter a positive Number less than 200"
            }
        result = {}
        num = num % 200
        if topic == 0:
            topic = choice(TOPICS)
        if num == 1:
            subreddit = reddit.subreddit(topic)
            meme = subreddit.random()
            try:
                _ = meme.preview
                result = {
                    "code":200,
                    "post_link": meme.shortlink,
                    "subreddit": topic,
                    "title": meme.title,
                    "url": meme.url,
                    "ups": meme.ups,
                    "author": meme.author.name,
                    "spoilers_enabled": subreddit.spoilers_enabled,
                    "nsfw": subreddit.over18,
                    "image_previews": [i["url"] for i in meme.preview.get("images")[0].get("resolutions")]
                }
            except Exception as e:
                result = {

                    "post_link": meme.shortlink,
                    "subreddit": topic,
                    "title": meme.title,
                    "url": meme.url,
                    "ups": meme.ups,
                    "author": meme.author.name,
                    "spoilers_enabled": subreddit.spoilers_enabled,
                    "nsfw": subreddit.over18,
                    "image_previews": ["No Preview Found For This Meme.. Sorry For That"]
                }
        return result

    except Exception as e:
        return {
            "code": 400,
            "message": str(type(e))+str(e),
            "help": "Subreddit Doesn't Exist, Check if u spelled it correctly.."
        }
