from flask import Flask, render_template, request
import requests, json
import random
import datetime
import time

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def home():

  random_item = random.randint(1,30)
  
  prixuser = 0
  historique = []
  firstry = 0
  if request.method == "POST": 
    random_item = int(request.form["random_item"])
    prixuser = int(request.form["prixinput"])
    historique = json.loads(request.form["historique"])
    historique.append(prixuser)
    firstry = float(request.form["firstry"])
    if firstry == 0 :
       firstry = time.time()

  params = {
            "ApiKey": "818e864c-7f59-41db-8546-6498f3d90ef0",
            "SearchRequest": {
              "Keyword": "kitchen",
              "Pagination": {
                "ItemsPerPage": random_item,
                "PageNumber": 1
              },
              "Filters": {
                "Price": {
                  "Min": 0,
                  "Max": 0
                },
                "Navigation": "",
                "IncludeMarketPlace": "false"
              }
            }
          }
      
  url = "https://api.cdiscount.com/OpenApi/json/Search"
 
  r = requests.post(url, data=json.dumps(params))
  name =(r.json()['Products'][0]['Name'])
  prixobjet = int(float(r.json()['Products'][0]['BestOffer']['SalePrice']))
  image =(r.json()['Products'][0]['MainImageUrl'])

  temps = None
  if request.method == "POST": 
    temps = datetime.datetime.now() - datetime.datetime.fromtimestamp(firstry)

  return render_template("projet.html", NAME=name, PRIXOBJET=prixobjet, IMAGE=image, PRIXUSER=prixuser, RANDOM_ITEM=random_item, HISTORIQUE=historique, FIRSTRY=firstry, TEMPS=temps)

if __name__ == "__main__":
    app.run()