from .base_controller import base_controller

class template_controller(base_controller):
    def __init__(self):
        super().__init__()  

    def get_admin_data(self, page_name):
        # logic hatag ang data gikan sa controller 
        if page_name == "test1":
            return {
                "title": "Admin Test Page 1",
                "welcome_message": "Welcome to Test Page 1",
                "user_count": 5,
                "app_name": self.get_app_name()  
            }
        elif page_name == "test2":
            return {
                "title": "Admin Test Page 2",
                "welcome_message": "Welcome to Test Page 2",
                "user_count": 12,
                "app_name": self.get_app_name()
            }
        else:
            return {
                "title": "Admin Page",
                "welcome_message": "Welcome!",
                "user_count": 0,
                "app_name": self.get_app_name()
            }
