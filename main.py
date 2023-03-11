from fastapi import FastAPI, Request
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )
]


app = FastAPI(middleware=middleware)




@app.get("/Get")
def main(request: Request):
    language = request.client.host
    t = {"data":[{"AppointmentId":3,"Text":"Install New Router in Dev Room","Description":None,"StartDate":"2021-04-26T21:30:00.000Z","EndDate":"2021-04-26T22:30:00.000Z","AllDay":False,"RecurrenceRule":None,"RecurrenceException":None}]}
    return t

