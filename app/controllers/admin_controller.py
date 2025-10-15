from app.controllers.base_controller import BaseController

class AdminController(BaseController):
    def get_admin_data(self, page_name: str):
        return {
            "app_name": self.get_app_name(),
            "page_title": f"Admin Page - {page_name.capitalize()}"
        }
