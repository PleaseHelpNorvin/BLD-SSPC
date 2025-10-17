# app/controllers/authentication_controller.py
from app.controllers.base_controller import BaseController
import qrcode
import io
import base64

class AuthenticationController(BaseController):
    def get_authentication_data(self, page_name: str):
        return {
            "app_name": self.get_app_name(),
            "page_title": "Login"
        }

    def generate_qr_code(self, qr_data: str) -> str:
    
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5
        )
        
        qr.add_data(qr_data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        img_str = base64.b64encode(buffer.getvalue()).decode("utf-8")
        return f"data:image/png;base64,{img_str}"  

    def verify_qr_code(self, qr_data: str) -> bool:

        # Example: compare with a known token (you'd normally fetch from DB)
        expected_qr = "user_id_123"  
        return qr_data == expected_qr
