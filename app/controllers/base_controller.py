class BaseController:
    def __init__(self):
        self.app_name = "Document QR Manager"

    def get_app_name(self):
        return self.app_name
