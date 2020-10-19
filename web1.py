from flask import Flask, render_template


def page():
    return render_template("index.html", pages=pages)


def hello_name(name=None):
    return render_template("hello.html", name=name)


def hi_name():
    return hello_name()


pages = {
    "/": (page,),
    "/hello/": (hello_name,),
    "/hello/<name>/": (hello_name,),
    "/hi/": (hello_name,)
}


app = Flask(__name__)

for path in pages.keys():
    app.add_url_rule(rule=path, view_func=pages[path][0])

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
