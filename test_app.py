import unittest
from app import app

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
