# MessageBoard (c) 2022 Baltasar MIT License <jbgarcia@uvigo.es>


import flask
import flask_login
import sirope

from model.userdto import UserDto


def get_blprint():
    search = flask.blueprints.Blueprint("search", __name__,
                                        url_prefix="/search",
                                        template_folder="templates",
                                        static_folder="static")
    syrp = sirope.Sirope()

    return search, syrp


search_blprint, srp = get_blprint()


@flask_login.login_required
@search_blprint.route("/")
def search():
    return flask.send_from_directory(search_blprint.static_folder, "search.html")


@flask_login.login_required
@search_blprint.route("/results", methods=["POST"])
def results():
    msgs = []
    txt_search = flask.request.form.get("edSearch")
    usr = srp.find_first(UserDto, lambda u: txt_search.strip() in u.email)

    if usr:
        msgs = srp.multi_load(usr.oids_messages)

    sust = {
        "msgs": msgs
    }

    return flask.render_template("results.html", **sust)
