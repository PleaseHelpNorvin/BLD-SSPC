from fastapi.responses import JSONResponse

class base_api_controller:
    #i want to handle my api here
    #just import this BaseApiController
    def send_response(self, data=None, message="Success", status_code=200):
        return JSONResponse(
            status_code=status_code,
            content={
                "success": True,
                "message": message,
                "data": data
            }
        )

    def send_error(self, error="Something went wrong", status_code=400, errors=None):

        response = {
            "success": False,
            "message": error,
        }

        if errors:
            response["errors"] = errors

        return JSONResponse(status_code=status_code, content=response)
