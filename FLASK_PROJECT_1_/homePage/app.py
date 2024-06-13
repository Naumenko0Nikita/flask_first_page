from flask import Blueprint


home1 = Blueprint(
    name = "home1",
    import_name = "app",
    static_folder = "static/homePage",
    template_folder = "homePage/templates/"
)