# /usr/bin/env python
# MessageBoard (c) 2022 Baltasar MIT License <jbgarcia@uvigo.es>


import flask
import flask_login
import sirope
from flask_login import login_manager

from model.messagedto import MessageDto
from model.userdto import UserDto
import views.search.search_view as search_view


def create_app():
    lmanager = login_manager.LoginManager()
    fapp = flask.Flask(__name__, instance_relative_config=True)
    syrp = sirope.Sirope()

    fapp.config.from_json("config.json")
    lmanager.init_app(fapp)
    fapp.register_blueprint(search_view.search_blprint)
    return fapp, lmanager, syrp


app, lm, srp = create_app()


@lm.user_loader
def user_loader(email):
    return UserDto.find(srp, email)


@app.route('/')
def get_index():
    usr = UserDto.current_user()
    messages_list = list(sirope.Sirope().load_last(MessageDto, 5))

    sust = {
        "usr": usr,
        "messages_list": messages_list,
    }

    return flask.render_template("index.html", **sust)


@app.route("/save_message", methods=["POST"])
def save_message():
    message_txt = flask.request.form.get("edMessage")
    email_txt = flask.request.form.get("edEmail")
    password_txt = flask.request.form.get("edPassword")

    if not message_txt:
        flask.flash("¿Y el mensaje?")
        return flask.redirect("/")

    if not email_txt:
        usr = UserDto.current_user()

        if not usr:
            flask.flash("You must login first!!")
            return flask.redirect("/")
    else:
        usr = UserDto.find(srp, email_txt)
        if not password_txt:
            flask.flash("No password!!??")
            return flask.redirect("/")

        if not usr:
            usr = UserDto(email_txt, password_txt)
            srp.save(usr)
        elif not usr.chk_password(password_txt):
            flask.flash("Passwords do not match")
            return flask.redirect("/")

        flask_login.login_user(usr)

    msg_oid = srp.save(MessageDto(f"'{usr.email} says: {message_txt}"))
    usr.add_message_oid(msg_oid)
    srp.save(usr)
    return flask.redirect("/")


@app.route('/logout')
def logout():
    flask_login.logout_user()
    flask.flash("User logged out")
    return flask.redirect("/")


@lm.unauthorized_handler
def unauthorized_handler():
    flask.flash("Unauthorized")
    return flask.redirect("/")


if __name__ == '__main__':
    app.run()
