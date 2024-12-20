import unittest
from unittest.mock import patch, mock_open
from flask import Flask, jsonify
import json
import app 

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

#omer's unittest:

    # checking retuned code for reaching a valid adress for homepage:
    def test_home_route(self):
        response_code = self.app.get('/')
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

        # בדיקה אם התגובה מחזירה את הנתונים הצפויים
        expected_data = {
            "dates": ["2023-12-01", "2023-12-02"],
            "before_installation": [100, 200],
            "after_installation": [80, 150],
        }
        self.assertEqual(response.json, expected_data)

        # בדיקה אם הקובץ נפתח כראוי
        mock_file.assert_called_once_with("static/water_consumption.json", "r")


if __name__ == "__main__":
    unittest.main()
