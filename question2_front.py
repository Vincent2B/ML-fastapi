from fastapi import FastAPI, Path, Query, WebSocket
from fastapi.responses import HTMLResponse
import numpy as np
import test

#############################################################################
#                       QUESTION 2 : Integration                            #
#############################################################################

app = FastAPI()

html = """
<!DOCTYPE html>
<html>
<body>

<h1>NBA Player's Carrier Estimator</h1>

<form action="/result" method="get" target="_blank">
  <label for="GP">Games played:</label>
  <input type="float" id="GP" name="GP"><br><br>

  <label for="PTS">Points per game:</label>
  <input type="float" id="PTS" name="PTS"><br><br>

  <label for="FG">Field goal %:</label>
  <input type="float" id="FG" name="FG"><br><br>

  <label for="TP"> 3 points attempt %:</label>
  <input type="float" id="TP" name="TP"><br><br>

  <label for="OREB"> Offensive rebounds:</label>
  <input type="float" id="OREB" name="OREB"><br><br>

  <input type="submit" value="Submit">
</form>

<p>Click on the submit button when all field are completed.</p>

</body>
</html>
"""


@app.get("/")
async def get():
    return HTMLResponse(html)

@app.get("/result")
def get_item(GP:int,PTS:float,FG:float,TP:float,OREB:float):
  new_player = np.array([GP,PTS,FG,TP,OREB]).reshape(1,-1)
  result = test.training(new_player)

  if result[0] == 1.0:
    return "Le joueur aura sûrement une carrière suppérieur à 5 ans en NBA."
  else:
    return "Le joueur aura sûrement une carrière inférieur à 5 ans en NBA."
