from flask import Flask, jsonify, request

app = Flask(__name__)

contacts = [
    {
        "id":1,
        "name":"pratyush",
        "contact":"1234567890",
        "done":False
    },
    {
        "id":2,
        "name":"pratyush2",
        "contact":"1234567891",
        "done":False
    }
]

@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please add data"
        },400)
    contact = {
        "id": contacts[-1]["id"]+1,
        "name": request.json["name"],
        "contact": request.json.get("contact",""),
        "done":False
    }
    contacts.append(contact)
    return jsonify({
        "status":"Success",
        "message":"contact added succesfully"
    })

if __name__ == "__main__":
    app.run(debug=True)