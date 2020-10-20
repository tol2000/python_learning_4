from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

pages = {
    "/",
    "/hello/",
    "/hello/Tolicheg/",
    "/article/",
    "/article/42/",
    "/user/"
}


@app.route('/')
def page():
    return render_template('index.html', pages=pages)


@app.route('/hello/')
@app.route('/hello/<name>/')
def hello_name(name=None):
    return render_template('hello.html', name=name)


@app.route("/article/")
@app.route("/article/<int:a_id>/")
def article_page(a_id=None):
    if a_id is not None:
        return render_template('article.html', a_id=a_id)
    else:
        return redirect(url_for('article_page', a_id=1))


@app.route("/article/<string:a_id>/")
def article_page_str(a_id=None):
    return render_template('article_invalid.html', a_id=a_id)


@app.route("/user/", methods=["GET", "POST"])
def user_page():
    user_request_contents = [
        f'Path: {request.environ["PATH_INFO"]}',
        f'Agent: {request.environ["HTTP_USER_AGENT"]}',
        f'Cookie: {request.environ["HTTP_COOKIE"]}'
    ]
    return render_template(
        "user.html",
        user_request_contents=user_request_contents,
        user_name=request.form.get('f_name') if request.method == 'POST' else None
    )


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
