from typing import Union
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import requests
import urllib

appendedText = ""

lastQueryParams = None

overriddenParams: dict = {}

app = FastAPI()



@app.get("/atis.php", response_class=HTMLResponse)
async def getMETAR(request: Request):
    global lastQueryParams
    lastQueryParams = request.query_params
    finalParams = dict(lastQueryParams).copy()
    finalParams.update(overriddenParams)
    print(f"https://www.uniatis.net/atis.php?{finalParams}")
    print(requests.get(f"https://www.uniatis.net/atis.php?{urllib.parse.urlencode(finalParams)}").url)
    uniatisText = requests.get(f"https://www.uniatis.net/atis.php?{urllib.parse.urlencode(finalParams)}").text
    finalText = uniatisText + appendedText
    return finalText

# Set different Variables

@app.get("/setAppended")
async def append(text: str = ""):
    global appendedText
    appendedText = text
    return appendedText

@app.get("/getAppended")
async def getAppend():
    return appendedText

@app.get("/getLastQueryParams")
async def getLastQueryParams():
    return lastQueryParams

@app.get("/getCurrentParams")
async def getCurrentParams():
    if lastQueryParams:
        z = dict(lastQueryParams).copy()
        z.update(overriddenParams)
    else:
        z = overriddenParams.copy()
    return z

@app.get("/setOverridden")
async def setOverridden(request: Request):
    global overriddenParams
    if request.query_params != None:
        overriddenParams = request.query_params
    return overriddenParams

@app.get("/getOverridden")
async def getOverridden():
    return overriddenParams

@app.get("/test")
async def text(request: Request):
    return ""