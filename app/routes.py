from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.controllers.admin_controller import AdminController

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")
adminController = AdminController()  # ✅ instantiate it

@router.get("/admin/test1", response_class=HTMLResponse)
async def admin_test1(request: Request):
    data = adminController.get_admin_data("test1")  # ✅ use the instance
    return templates.TemplateResponse(
        "admin_pages/admin_test_page.html",
        {"request": request, **data}
    )

@router.get("/admin/test2", response_class=HTMLResponse)
async def admin_test2(request: Request):
    data = adminController.get_admin_data("test2")
    return templates.TemplateResponse(
        "admin_pages/admin_test_page2.html",
        {"request": request, **data}
    )
