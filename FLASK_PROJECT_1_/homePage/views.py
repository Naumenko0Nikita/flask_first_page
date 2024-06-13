import flask

def view_main_page():
    return flask.render_template(template_name_or_list = "index.html")