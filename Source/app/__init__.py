from flask import Flask, Response
from app.modules.functions import make_link_page, make_svg_widget

def _html(html: str) -> Response:
    r = Response(html, mimetype="text/html")
    r.headers["Cache-Control"] = "s-maxage=1"
    r.headers["Access-Control-Allow-Origin"] = "*"
    return r

def _svg(svg: str) -> Response:
    r = Response(svg, mimetype="image/svg+xml")
    r.headers["Cache-Control"] = "s-maxage=1"
    r.headers["Access-Control-Allow-Origin"] = "*"
    return r

def create_app() -> Flask:
    app = Flask(__name__)

    @app.route("/")
    def home() -> Response:
        # show the playlist page
        return _html(make_link_page())

    @app.route("/link")
    def link() -> Response:
        return _html(make_link_page())

    @app.route("/widget")
    def widget() -> Response:
        return _svg(make_svg_widget())

    return app
