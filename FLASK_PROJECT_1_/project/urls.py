
from homePage.views import view_main_page

from homePage.app import home1

home1.add_url_rule(
    #
    rule = "/", 
    #
    view_func = view_main_page
)