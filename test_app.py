import unittest
from unittest.mock import patch, mock_open
from flask import Flask, jsonify
import json
import app
from datetime import datetime

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

#omer's unittest:


    # checking retuned code for reaching a valid adress for homepage:
    def test_planting_experiment_route(self):
        response_code = self.app.get('/planting_experiment')
        self.assertEqual(response_code.status_code, 200)    

    #Claude unittest:

    def test_add_plant_authenticated(self):
        """Test adding a plant when user is authenticated."""
        with self.client as c:
            with c.session_transaction() as sess:
                sess['user_email'] = 'test@example.com'

            response = c.post('/add_plant', data={
                'area': 'Garden',
                'type': 'Rose'
             })
            self.assertEqual(response.status_code, 302)  # Redirect after success


<<<<<<< Updated upstream

#Nevo's unittest:

class TestGetWater(unittest.TestCase):
    def setUp(self):
        # מגדיר את אפליקציית Flask לבדיקה
        app.app.testing = True
        self.client = app.app.test_client()

    @patch("builtins.open", new_callable=mock_open, read_data='{"dates": ["2023-12-01", "2023-12-02"], "before_installation": [100, 200], "after_installation": [80, 150]}')
    def test_get_water(self, mock_file):
        # ביצוע בקשה לנתיב /data_water
        response = self.client.get("/data_water")

        # בדיקה אם הבקשה הצליחה
        self.assertEqual(response.status_code, 200)


#Copile's unittest:
        mock_file.assert_called_once_with("static/water_consumption.json", "r")
        class TestGetWater(unittest.TestCase):
            def setUp(self):
                app.app.testing = True
                self.client = app.app.test_client()

            @patch("builtins.open", new_callable=mock_open, read_data='{"dates": ["2023-12-01", "2023-12-02"], "before_installation": [100, 200], "after_installation": [80, 150]}')
            def test_get_water(self, mock_file):
                response = self.client.get("/data_water")
                self.assertEqual(response.status_code, 200)
                expected_data = {
                    "dates": ["2023-12-01", "2023-12-02"],
                    "before_installation": [100, 200],
                    "after_installation": [80, 150],
                }
                self.assertEqual(response.json, expected_data)
                mock_file.assert_called_once_with("static/water_consumption.json", "r")

        class TestDataSensorByDate(unittest.TestCase):
            def setUp(self):
                app.app.testing = True
                self.client = app.app.test_client()

            @patch("app.get_sensor_api_token", return_value="mock_token")
            @patch("app.get_sensor_by_date", return_value=[
                {"Temperature": 25, "Humidity": 60, "sample_time_utc": "2024-12-10T00:00:00Z"},
                {"Temperature": 26, "Humidity": 65, "sample_time_utc": "2024-12-11T00:00:00Z"}
            ])
            def test_data_sensor_by_date(self, mock_get_sensor_by_date, mock_get_sensor_api_token):
                response = self.client.get("/data_sensor_by_date")
                self.assertEqual(response.status_code, 200)
                expected_data = [
                    {"Temperature": 25, "Humidity": 60, "SampleTime": "2024-12-10T00:00:00Z"},
                    {"Temperature": 26, "Humidity": 65, "SampleTime": "2024-12-11T00:00:00Z"}
                ]
                self.assertEqual(response.json, expected_data)
                mock_get_sensor_api_token.assert_called_once()
                mock_get_sensor_by_date.assert_called_once_with("mock_token", "E9:19:79:09:A1:AD", datetime(2024, 12, 10), datetime(2024, 12, 19))

if __name__ == "__main__":
    unittest.main()


=======
#sahar's unittest:

    def test_send_email_no_email(self):
        # Sending a request without an email
        response = self.app.post('/send-email', json={})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Email is required'})
  

#jimmy unittest:
   def test_send_email_missing_email(self):
    # Simulate a request with missing email
      request = {'email': None}
      response, status_code = send_email(request)
      self.assertEqual(status_code, 400)
      self.assertEqual(response.get('error'), 'Email is required')

      
>>>>>>> Stashed changes
