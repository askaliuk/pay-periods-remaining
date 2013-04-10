from app import app
from flask.ext.testing import TestCase
from flask import url_for
from datetime import datetime
from models import Frequency


class ApiTestCase(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def setUp(self):
        self.client = app.test_client()

    def test_validation(self):
        response = self.client.get(url_for("api_pay_peroids_remaining"))
        self.assert400(response)
        message = {
            'status': 400,
            'message': 'All fields are required'
        }
        self.assertEquals(response.json, message)

        response = self.client.get(
            url_for(
                "api_pay_peroids_remaining",
                start_date="wrong",
                frequency=Frequency.SEMI_MONTHLY))
        self.assert400(response)
        message = {
            'status': 400,
            'message': 'Invalid date'
        }
        self.assertEquals(response.json, message)

    def test_calculation(self):
        start_date = datetime(2013, 4, 9)
        response = self.client.get(
            url_for(
                "api_pay_peroids_remaining",
                start_date=start_date.strftime('%m/%d/%Y'),
                frequency=Frequency.SEMI_MONTHLY))
        self.assert200(response)
        self.assertTrue('pay_periods_remaining' in response.json)
        self.assertTrue(response.json['pay_periods_remaining'] > 0)
