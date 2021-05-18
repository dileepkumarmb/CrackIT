from flask import  Flask, render_template, make_response, jsonify, request

app1 = Flask(__name__)
PORT= 3200
HOST= '0.0.0.0'

INFO = {
    "languages": {
        "es":"Spanish",
        "en":"English",
        "fr":"French",
    },
    "colors":{
        "r":"red",
        "g":"green",
        "b":"blue",
    },
    "clouds":{
        "IBM":"IBM CLOUD",
        "AMAZON":"AWS",
        "MICROSOFT":"AZURE",
    }
}

@app1.route("/")
def home():
    return "<h1 style='color:red'> Kestur is famous for Mango fruits </h1>"

@app1.route("/temp")
def template():
    return render_template('index.html')

@app1.route("/qstr")
def query_string():
    if request.args:
        req=request.args
        res = {}
        for key,value in req.items():
            res[key] = value
        res= make_response(jsonify(res),200)
        return res
    res = make_response(jsonify({"Error":"No query syting found"}),400)
    return  res

@app1.route("/json")
def get_json():
    res = make_response(jsonify(INFO),200)
    return  res

@app1.route("/json/<collection>/<member>")
def get_data(collection, member):
    print("getting the value of %s in the collection %s"%(member,collection))
    if collection in INFO:
        member = INFO[collection].get(member)
        if member:
            res = make_response(jsonify({"res":member}), 200)
            return res

        res = make_response(jsonify({"error": "Not found"}), 404)
        return res
    res = make_response(jsonify({"error": "Not found"}), 404)
    return res

@app1.route("/json/<collection>", methods=["POST"])
def create_collection(collection):
    req = request.get_json()
    if collection in INFO:
        res = make_response(jsonify({"Error":"Collection already exist"}))
        return  res
    INFO.update({collection: req})
    res = make_response(jsonify({"message":"Collection craeted"}),201)
    return  res

@app1.route("/dude/<collection>", methods=["DELETE"])
def delete_resource(collection):
    if collection in INFO:
        del INFO[collection]
        res = make_response(jsonify(INFO),300)
        return res
    res = make_response(jsonify({"error":"Collection not found"}),400)
    return res

# Put Method
@app1.route("/json/<collection>/<member>", methods=["PUT"])
def put_col_mem(collection,member):
    req = request.get_json()
    if collection in INFO:
        if member:
            print(req)
            INFO[collection][member] = req["new"]
            res = make_response(jsonify({"res":INFO[collection]}), 200)
            return res

        res = make_response(jsonify({"error": "Not found"}), 404)
        return res

    res = make_response(jsonify({"error": "Not found"}), 404)
    return res


if __name__ == "__main__":
    app1.run(host='127.0.0.1',port=PORT)