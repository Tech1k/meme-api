# Reddit Meme API for Catbot
JSON API for a random meme scraped from Reddit for the Catbot.


**Example Response:**

```jsonc
{

    "code": 200,
    "post_link": "https://redd.it/kadq22",
    "subreddit": "AdviceAnimals",
    "title": "The struggle is real during these trying times.",
    "url": "https://i.redd.it/di9suwomhc461.jpg",
    "ups": 22471,
    "author": "bobbydigital_ftw",
    "spoilers_enabled": true,
    "nsfw": false,
    "image_previews": [
        "https://preview.redd.it/di9suwomhc461.jpg?width=108&crop=smart&auto=webp&s=8c033387866f4a2ff608abf3f8cce8507518866c",
        "https://preview.redd.it/di9suwomhc461.jpg?width=216&crop=smart&auto=webp&s=85ea6bc35101b9fd76bbbd1c17a1df3889e21e62",
        "https://preview.redd.it/di9suwomhc461.jpg?width=320&crop=smart&auto=webp&s=263b77afd27714f155a94f15578b042f968cc688"
    ]

}
```
> Note: While using the API always confirm that the response for `"code"` is 200, else there is some error!!!
