from flask import render_template
from app.controllers.example_controller import template_controller

controller = template_controller()
#diri ta mag routes mura pina laravel norben
def register_routes(app):
    
    @app.route("/admin/test1")
    def admin_test1():
        data = controller.get_admin_data("test1")
        return render_template("admin_pages/admin_test_page.html", **data)

    @app.route("/admin/test2")
    def admin_test2():
        data = controller.get_admin_data("test2")
        return render_template("admin_pages/admin_test_page2.html", **data)
