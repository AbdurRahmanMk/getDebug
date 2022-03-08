
# ------ How to run in development ---------
#  uvicorn main:app --reload
# Then run in browser.
#			http://127.0.0.1:8000
# ------------------------------------------

# -------- Lib Import ----------------
from fastapi import FastAPI,Depends, Query,Request # Query = for length checking

from fastapi.middleware.cors import CORSMiddleware
import random 
import datetime


from typing import Optional
from enum import Enum
#from uuid import UUID
#import uuid

# ---- DB
import databases
#from databases import Database
# for enviroment variable reading.
import os

# For redirecting to to fee page ---
from fastapi.responses import RedirectResponse
# -------- Lib Import End --------------

__version__ = '0.1.73'
app = FastAPI( title="Test API", description="Test API",version=__version__)

@app.on_event("startup")
async def startup():
	#await database.connect()
	print("Started..")

@app.on_event("shutdown")
async def shutdown():
	#await database.disconnect()
	print("Stopped..")

@app.get("/get/info/about")
async def info_about():
	executionDateTime = datetime.datetime.now(datetime.timezone.utc).strftime("%m-%d-%Y %H:%M:%S.%f")

	return {'status':'OK',
			'dateTime':executionDateTime,
			'version':__version__
			}


@app.get("/get/info/echoInputParameter")
async def info_echo_input_parameter(request: Request):
	executionDateTime = datetime.datetime.now(datetime.timezone.utc).strftime("%m-%d-%Y %H:%M:%S.%f")
	params = request.query_params

	return {'status':'OK',
			'dateTime':executionDateTime,
			'version':__version__,
			'requestMethod':request.method,
			'requestURLPort':request.url.port,
			'requestURLScheme':request.url.scheme,
			#'requestURL':request.url,
			'requestURLPath':request.url.path,
			'requestQueryParams':request.query_params,
			'requestClientHost':request.client.host,
			'requestClientPort':request.client.port
			}
