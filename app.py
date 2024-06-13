# app.py
from flask import Flask, jsonify, render_template, request
from models import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/api/availability', methods=['GET'])
def get_availability():
    getActivity = request.args.get('activity')
    availability_data = {
        'billiard': [],
        'bowling': [],
        'watching': []
    }
    dates = cursor.execute("SELECT * FROM Date").fetchall()
    activities = cursor.execute('SELECT * FROM Activity').fetchall()
    for item in activities:
        if getActivity in item:
            for time in dates:
                for activity in activities:
                    cursor.execute(f'SELECT * FROM Booking WHERE activity_name = ? AND booked_date = ?', (activity[1], time[1]))
                    if cursor.fetchall() == []:
                        availability_data[activity[1]].append({"time": time[1], "available": True})

                    else:
                        availability_data[activity[1]].append({"time": time[1], "available": False})
            return jsonify(availability_data.get(getActivity, []))
    else:
        return jsonify({"message": "This activity is not exists"})

@app.route('/api/booking', methods=['POST'])
def booking():
    data = request.json
    print(data)
    setBooking(data["activity"], data["timeslot"], data["people"], data["customer_name"])
    return jsonify({"message": "good"}, 201)




if __name__ == '__main__':
    app.run('0.0.0.0',debug=True)
