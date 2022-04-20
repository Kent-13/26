from flask import Flask, jsonify, request
app=Flask(__name__)
heartrates = [
    {
        "heart_id": 1,
        "date": "20/04/2021",
        "heart_rate": "90"

    },
    {
        "heart_id": 2,
        "date": "20/04/2022",
        "heart_rate": "95"
    }
]
@app.route('/heartrates',methods=['GET'])
def getHeartrate():
    return jsonify(heartrates)

@app.route('/heartrates',methods=['POST'])
def add_heartrate():
    heartrate=request.get_json()
    heartrates.append(heartrate)
    return {'id':len(heartrates)},200

@app.route('/delete_heart_rates/<int:index>',methods=['DELETE'])
def deleteHeartRateID(index):
    for heart_rate in heartrates:
        if heart_rate.get("heart_id")== index:
            heartrates.remove(heart_rate)
            return{"status":"Successfully"}, 200
    return{"status": "Not found"}, 400


@app.route("/update_heart_rate/<int:index>", method=["GET", "POST"])
def updateHeartRateID(index):
    if request.method == "GET":
        for heartrate in heartrates:
            if heartrate.get("heart_id") == index:
                return heartrate, 200
    elif request.method == "POST":
        for heartrate in heartrates:
            if heartrate.get("heart_id") == index:
                data = request.get_json()
                if "heart_rate" in data and "date" in data:
                    heartrate["heart_rate"] = data.get("heart_rate")
                    heartrate["date"] = data.get("date")
                    return data, 200
                return {"status": "No heartrate or date"}, 404
    return{"status": "Not found"}, 404

if __name__ == '__main__':
    app.run()