from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
blogs = []


def fetch_post_by_id(blog_id):
    """
    This function accepts Blog id as argument and returns blog as dictionary
    """
    for blog in blogs:
        if blog["id"] == blog_id:
            return blog


@app.route("/")
def index():
    """
    Using for redirecting and as a home page for the Route
    """
    return render_template("index.html", blogs=blogs)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        try:
            blog_id = blogs[-1]["id"] + 1
        except IndexError:
            blog_id = 1
        blog = {"id": int(blog_id), "author": request.form.get("author_name"), "title": request.form.get("title"),
                "content": request.form.get("content")}
        blogs.append(blog)
        return redirect(url_for("index"))

    return render_template("add.html")


@app.route("/delete/<int:blog_id>", methods=["POST"])
def delete(blog_id):
    for blog in blogs:
        if blog["id"] == blog_id:
            blogs.remove(blog)
            break
    return redirect(url_for("index"))


@app.route("/update/<int:blog_id>", methods=["GET", "POST"])
def update(blog_id):
    blog = fetch_post_by_id(blog_id)
    if blog is None:
        return "Post Not Found", 404
    if request.method == "POST":
        blog["author"] = request.form.get("author")
        blog["title"] = request.form.get("title")
        blog["content"] = request.form.get("content")
        return redirect(url_for("index"))
    else:
        return render_template("update.html", blog=blog)


if __name__ == "__main__":
    # Launch the Flask dev server
    app.run(host="0.0.0.0", port=5000, debug=True)
