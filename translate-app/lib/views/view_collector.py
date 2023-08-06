"""
all_views จะเก็บ view ทุก view
{
    name_view:Class
}
"""
try:
    from views.home_page.home_page import HomePage
except:
    from lib.views.home_page.home_page import HomePage

views ={
    "home_page":HomePage
}