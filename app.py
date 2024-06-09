# app.py
from flask import Flask, jsonify, render_template, request
from models import db, Date, Booking

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///availability.db'
db.init_app(app)


@app.route('/')
def home():
    return render_template('index.html')



@app.route('/availability', methods=['GET'])
def get_availability():
    dates = Date.query.all()
    availability = []

    for date in dates:
        bookings = Booking.query.filter_by(date=date).all()
        date_availability = []

        for booking in bookings:
            date_availability.append({
                "activity": booking.activity.name,
                "date": date.date,
                "available": False
            })

        availability.extend(date_availability)

    return jsonify({"dates": availability})

@app.route('/api/booking', methods=['POST'])
def booking():
    data = request.json
    print(data)
    return jsonify({"message": "good"}, 201)




if __name__ == '__main__':
    app.run('0.0.0.0',debug=True)
