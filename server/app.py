from datetime import datetime
from flask import Flask, request, jsonify
from errors import validation_error
import logic
from models import Frequency

app = Flask(__name__)


@app.route('/pay_periods_remaining', methods=['GET'])
def api_pay_peroids_remaining():
    start_date = request.args.get('start_date', None)
    print start_date
    frequency = request.args.get('frequency', None)
    if not all([start_date, frequency]):
        return validation_error('All fields are required')
    try:
        start_date = datetime.strptime(start_date, '%m/%d/%Y')
    except ValueError:
        return validation_error('Invalid date')
    if not Frequency.is_valid(frequency):
        return validation_error('Invalid frequency')
    return jsonify({'pay_periods_remaining':
                    logic.pay_periods_remaining(start_date)})

if __name__ == '__main__':
    app.run(debug=True, port=8002)
