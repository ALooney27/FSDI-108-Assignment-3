from flask import Flask, request
import json

app = Flask(__name__)

@app.get('/')
def home():
    return "Hello Python"

@app.get('/test')
def test():
    return "This is a test page"

########### API PRODUCTS ################
################JSON#####################

catalog = []

@app.get('/api/products')
def get_products():
    # TODO: read products from DB and return them
    return json.dumps(catalog)

@app.post('/api/products')
def save_product():
    product = request.get_json()
    catalog.append(product)

    return json.dumps(product)

@app.get('/api/products/count')
def get_products_count():
    count = len(catalog)
    return json.dumps(count)

# SJC=124388
# Create an endpoint that return the number of products in the catalog
# the endpoint should respond to a get request on /api/products/count
# google - python count elemeents on a list

# start the server manually
app.run(debug=True)