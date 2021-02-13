from flask import Flask, render_template
import requests
import json
from random import randint


app = Flask(__name__)
blog_endpoint = "https://api.npoint.io/5abcca6f4e39b4955965"


@app.route('/post/<blog_id>')
def show_post(blog_id):
    print(f"blog enfpoint is {blog_id}")
    response = requests.get(blog_endpoint)
    posts = json.loads(response.text)
    print(posts)
    blog_id = int(blog_id)
    return render_template("/post.html", blog_id=blog_id, posts=posts)


@app.route('/')
def home():
    response = requests.get(blog_endpoint)
    posts = json.loads(response.text)
    num = randint(2, 3)
    return render_template("index.html", posts=posts, showcase_id=num)


if __name__ == "__main__":
    app.run(debug=True)
