class base_controller:
    def __init__(self):
        #controller level accessable sa mga mo gamit sa base controller
        self.app_name = "Document QR Manager"

    def get_app_name(self):
        return self.app_name