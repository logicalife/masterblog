from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
blogs = []

@app.route("/")
def index():
    return render_template("index.html", blogs=blogs)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        blog = {"id": len(blogs) + 1, "author": request.form.get("author_name"), "title": request.form.get("title"),
                "content": request.form.get("content")}
        blogs.append(blog)
        return redirect(url_for("index"))

    return render_template("add.html")


if __name__ == "__main__":
    # Launch the Flask dev server
    app.run(host="0.0.0.0", port=5000, debug=True)
