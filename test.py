try:
    from server import app
    import unittest
    import json

except Exception as e:
    print("Faltan modulos {} ".format(e))

class FlaskTest(unittest.TestCase):

    # Chek for response 200
    def test_index(self):
        tester = app.app.test_client(self)
        response = tester.post("/api/farmacias", json={'numeroComuna': '121', 'nombreFarmacia': 'H'})
        statuscode = response.status_code
        print(response)
        self.assertEqual(statuscode, 200)
        
    
    # check if content return is application/json
    def test_index_content(self):
        tester = app.app.test_client(self)
        response = tester.post("/api/farmacias", json={'numeroComuna': '121', 'nombreFarmacia': 'H'})
        self.assertEqual(response.content_type, "application/json")

    # Validamos que esté toda la información mínima requerida por las especificaciones
    def test_index_data(self):
        tester = app.app.test_client(self)
        response = tester.post("/api/farmacias", json={'numeroComuna': '121', 'nombreFarmacia': 'H'})
        self.assertTrue(b'comuna_nombre' in response.data)
        self.assertTrue(b'local_nombre' in response.data)
        self.assertTrue(b'local_direccion' in response.data)
        self.assertTrue(b'local_telefono' in response.data)
        self.assertTrue(b'local_lat' in response.data)
        self.assertTrue(b'local_lng' in response.data)

    # check for out of bounds location number
    def test_index_outofbounds(self):
        tester = app.app.test_client(self)
        response = tester.post("/api/farmacias", json={'numeroComuna': '999', 'nombreFarmacia': 'H'})
        statuscode = response.status_code
        print(response)
        self.assertEqual(statuscode, 200)

    # check for empty request
    def test_index_empty(self):
        tester = app.app.test_client(self)
        response = tester.post("/api/farmacias", json={'numeroComuna': '', 'nombreFarmacia': ''})
        statuscode = response.status_code
        print(response)
        self.assertEqual(statuscode, 200)
    
    # check for name not in list
    def test_index_name(self):
        tester = app.app.test_client(self)
        response = tester.post("/api/farmacias", json={'numeroComuna': '', 'nombreFarmacia': '99999'})
        statuscode = response.status_code
        print(response)
        self.assertEqual(statuscode, 200)

if __name__ == "__main__":
    unittest.main()