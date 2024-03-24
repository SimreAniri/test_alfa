from fastapi import HTTPException, status

class AppException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)

class NameAlreadyExistsException(AppException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Наименование уже существует"

class NameNotExistsException(AppException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Наименование не существует"