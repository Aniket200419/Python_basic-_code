
from flask import Flask, request, render_template_string
import feedparser
import urllib.parse
from datetime import datetime

app = Flask(__name__)

NEWS_FEEDS = {
    "India": "https://news.google.com/rss/search?q=India+news&hl=en-IN&gl=IN&ceid=IN:en",
    "World": "https://news.google.com/rss/headlines/section/topic/WORLD?hl=en-US&gl=US&ceid=US:en",
    "Technology": "https://news.google.com/rss/search?q=technology+AI&hl=en-IN&gl=IN&ceid=IN:en",
    "Business": "https://news.google.com/rss/search?q=business+news&hl=en-IN&gl=IN&ceid=IN:en",
    "Sports": "https://news.google.com/rss/search?q=sports+news&hl=en-IN&gl=IN&ceid=IN:en",
}

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Live News Portal</title>
<style>
* { box-sizing: border-box; }
body {
    margin: 0; font-family: Arial, sans-serif;
    background: #f3f5f9; color: #202a3a;
}
header {
    background: #111c35; color: white;
    padding: 25px 7%; text-align: center;
}
header h1 { margin: 0 0 8px; }
header p { color: #cbd5e1; margin: 0; }
nav {
    display: flex; justify-content: center; flex-wrap: wrap;
    gap: 10px; padding: 18px; background: white;
}
nav a {
    text-decoration: none; color: #25324a;
    padding: 10px 16px; border-radius: 7px;
    background: #edf1f8; font-weight: bold;
}
nav a:hover, nav a.active { background: #2563eb; color: white; }
main { max-width: 1100px; margin: 25px auto; padding: 0 16px; }
.toolbar {
    display: flex; gap: 10px; margin-bottom: 22px;
}
input, button {
    padding: 12px; border-radius: 7px;
    border: 1px solid #d5dbe6; font-size: 15px;
}
input { flex: 1; min-width: 0; }
button { background: #2563eb; color: white; cursor: pointer; border: 0; }
h2 { margin: 15px 0 20px; }
.news {
    display: grid; grid-template-columns: repeat(auto-fit, minmax(270px, 1fr));
    gap: 18px;
}
article {
    background: white; border-radius: 12px; padding: 20px;
    box-shadow: 0 3px 12px #15213a0c;
    display: flex; flex-direction: column;
}
.tag { color: #2563eb; font-size: 12px; font-weight: bold; }
article h3 { line-height: 1.45; font-size: 18px; }
article p { color: #64748b; font-size: 14px; }
article a { color: #2563eb; text-decoration: none; font-weight: bold; }
article a:hover { text-decoration: underline; }
footer { text-align: center; padding: 25px; color: #64748b; }
@media(max-width: 500px) {
    .toolbar { flex-direction: column; }
}
</style>
</head>
<body>
<header>
    <h1>🌐 Live News Portal</h1>
    <p>Your daily news dashboard — India, World, Technology & more</p>
</header>

<nav>
{% for name in categories %}
<a class="{{ 'active' if name == category else '' }}"
   href="/?category={{ name }}">{{ name }}</a>
{% endfor %}
</nav>

<main>
<form class="toolbar" action="/" method="get">
    <input type="hidden" name="category" value="{{ category }}">
    <input type="text" name="q" placeholder="Search news..."
           value="{{ query }}">
    <button type="submit">Search</button>
    <button type="button" onclick="location.reload()">Refresh</button>
</form>

<h2>{{ category }} News</h2>
<p>Updated: {{ updated }}</p>

{% if error %}
<p>{{ error }}</p>
{% endif %}

<section class="news">
{% for item in articles %}
<article>
    <span class="tag">{{ item.category }}</span>
    <h3>{{ item.title }}</h3>
    <p>{{ item.published }}</p>
    {% if item.summary %}
    <p>{{ item.summary | safe }}</p>
    {% endif %}
    <p><a href="{{ item.link }}" target="_blank"
          rel="noopener noreferrer">Read full story ↗</a></p>
</article>
{% else %}
<p>No news found. Try another keyword or refresh the page.</p>
{% endfor %}
</section>
</main>

<footer>Live News Portal · Headlines provided by Google News RSS</footer>
</body>
</html>
"""


@app.route("/")
def home():
    category = request.args.get("category", "India")
    query = request.args.get("q", "").strip()

    if category not in NEWS_FEEDS:
        category = "India"

    articles = []
    error = ""

    try:
        if query:
            search_query = urllib.parse.quote(query)
            url = (
                "https://news.google.com/rss/search?q="
                + search_query
                + "&hl=en-IN&gl=IN&ceid=IN:en"
            )
            feeds = [(category, url)]
        else:
            feeds = [(category, NEWS_FEEDS[category])]

        for name, url in feeds:
            feed = feedparser.parse(url)

            if feed.bozo and not feed.entries:
                continue

            for entry in feed.entries:
                articles.append({
                    "category": name,
                    "title": entry.get("title", "Untitled"),
                    "link": entry.get("link", "#"),
                    "published": entry.get(
                        "published", "Publication date unavailable"
                    ),
                    "summary": entry.get("summary", "")[:600],
                })

        if not articles:
            error = (
                "No headlines received. Check your internet connection "
                "or try again later."
            )

    except Exception:
        error = "Unable to fetch news. Please check your internet connection."

    return render_template_string(
        HTML,
        categories=list(NEWS_FEEDS.keys()),
        category=category,
        query=query,
        articles=articles[:50],
        updated=datetime.now().strftime("%d %b %Y, %I:%M:%S %p"),
        error=error,
    )


if __name__ == "__main__":
    print("Live News Portal: http://127.0.0.1:5000")
    app.run(debug=False, host="127.0.0.1", port=5000)
