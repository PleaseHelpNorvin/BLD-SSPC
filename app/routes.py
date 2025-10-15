from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.controllers.admin_controller import AdminController
from app.controllers.authentication_controller import AuthenticationController

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")
adminController = AdminController()  
authController = AuthenticationController()


@router.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    data = authController.get_authentication_data("login")  # initialize data
    data["qr_code_img"] = authController.generate_qr_code("LoginQr")
    return templates.TemplateResponse(
        "authentication/login.html",
        {"request": request, **data}
    )
    
@router.get("/admin/dashboard", response_class=HTMLResponse)
async def admin_test1(request: Request):
    data = adminController.get_admin_data("dashboard") 
    return templates.TemplateResponse(
        "admin_pages/dashboard.html",
        {"request": request, **data}
    )

@router.get("/admin/test2", response_class=HTMLResponse)
async def admin_test2(request: Request):
    data = adminController.get_admin_data("test2")
    return templates.TemplateResponse(
        "admin_pages/admin_test_page2.html",
        {"request": request, **data}
    )
