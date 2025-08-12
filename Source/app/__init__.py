from flask import Flask, Response, redirect, url_for
from app.modules.functions import make_link_page, make_svg_widget

def _html_response(html: str) -> Response:
    resp = Response(response=html, mimetype="text/html")
    resp.headers["Cache-Control"] = "s-maxage=1"
    resp.headers["Access-Control-Allow-Origin"] = "*"
    return resp

def _svg_response(svg: str) -> Response:
    resp = Response(response=svg, mimetype="image/svg+xml")
    resp.headers["Cache-Control"] = "s-maxage=1"
    resp.headers["Access-Control-Allow-Origin"] = "*"
    return resp

def create_app() -> Flask:
    app = Flask(__name__)

    # Home -> playlist embed (HTML)
    @app.route("/")
    def home() -> Response:
        return _html_response(make_link_page())

    # Keep the old /link path working
    @app.route("/link")
    def link() -> Response:
        return _html_response(make_link_page())

    @app.route("/widget")
    def widget() -> Response:
        return _svg_response(make_svg_widget())

    # If you still want a catch-all, send unknown paths to the playlist
    @app.errorhandler(404)
    def not_found(_):
        return _html_response(make_link_page())

    return app
