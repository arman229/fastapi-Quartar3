 
from fastapi import FastAPI
from tutorialfastapi.topics import body_field
from tutorialfastapi.topics import body_nested_models
from tutorialfastapi.topics import declare_request
from tutorialfastapi.topics import header_parameters
from tutorialfastapi.topics import first_step
from tutorialfastapi.topics import path_parameters
from tutorialfastapi.topics import query_parameters
from tutorialfastapi.topics import request_body
from tutorialfastapi.topics import query_parameters_validation
from tutorialfastapi.topics import path_parameters_validation
from tutorialfastapi.topics import body_multiple_parameters

# app variable will be an "instance" of the class FastAPI
app: FastAPI = FastAPI(title='This is the tutorial of fastapi documentation')


@app.get('/')
async def read_root() -> dict[str, str]:
    return {"message": f"Hello World"}
# app.include_router(module.router) to include routes defined in the
# 'module or filename' into our FastAPI application
app.include_router(first_step.router)
app.include_router(path_parameters.router)
app.include_router(query_parameters.router)
app.include_router(request_body.router)
app.include_router(query_parameters_validation.router)
app.include_router(path_parameters_validation.router)
app.include_router(body_multiple_parameters.router)
app.include_router(body_field.router)
app.include_router(body_nested_models.router)
app.include_router(declare_request.router)

app.include_router(declare_request.router)
app.include_router(header_parameters.router)


# def main():
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
# if __name__ == '__main__':
#     main()
