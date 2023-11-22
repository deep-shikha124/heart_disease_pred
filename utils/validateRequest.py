from flask import request
from .constant import headers

def validateRequest():
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                if request.json:
                    missing_keys = [key for key in headers if key not in request.json]
                    if(not missing_keys or len(missing_keys)==0):
                        for key, value in request.json.items():
                            if key == "oldpeak" and not (isinstance(value, int) or isinstance(value, float)):
                                return {"message": f"{key} must be of type float."}, 400
                            elif key != "oldpeak" and not isinstance(value, int):
                                return {"message": f"{key} must be of type int."}, 400
                        return func(*args, **kwargs)
                    else:
                        return {"message" : "Missing required fields : " + ", ".join(missing_keys)} ,400
                else:
                    return {"message" : "Empty data."} ,400
            except:
                return {"message" : "Something went wrong. Please check the data."} ,400 
        return wrapper
    return decorator