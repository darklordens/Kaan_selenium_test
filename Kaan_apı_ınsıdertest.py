import unittest
import requests

BASE_URL = "https://petstore.swagger.io/v2"

# Test verileri
new_pet = {
    "id": 123456,
    "name": "Kaan's Pet",
    "status": "available"
}

updated_pet = {
    "id": 123456,
    "name": "Kaan's Updated Pet",
    "status": "sold"
}

class TestPetstoreAPI(unittest.TestCase):

    def test_create_pet(self):
        response = requests.post(f"{BASE_URL}/pet", json=new_pet)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['name'], new_pet['name'])
        self.assertEqual(response.json()['status'], new_pet['status'])

    def test_get_pet(self):
        response = requests.get(f"{BASE_URL}/pet/{new_pet['id']}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['name'], new_pet['name'])
        self.assertEqual(response.json()['status'], new_pet['status'])

    def test_update_pet(self):
        response = requests.put(f"{BASE_URL}/pet", json=updated_pet)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['name'], updated_pet['name'])
        self.assertEqual(response.json()['status'], updated_pet['status'])

    def test_delete_pet(self):
        response = requests.delete(f"{BASE_URL}/pet/{updated_pet['id']}")
        self.assertEqual(response.status_code, 200)
        # Silinen pet'i tekrar almaya çalış
        response = requests.get(f"{BASE_URL}/pet/{updated_pet['id']}")
        self.assertEqual(response.status_code, 404)

    def test_get_non_existing_pet(self):
        response = requests.get(f"{BASE_URL}/pet/0")
        self.assertEqual(response.status_code, 404)

    def test_create_pet_with_invalid_data(self):
        invalid_pet = {
            "id": "invalid",
            "name": 123,
            "status": "available"
        }
        response = requests.post(f"{BASE_URL}/pet", json=invalid_pet)
        self.assertEqual(response.status_code, 400, f"Beklenen 400, fakat {response.status_code} alındı. Yanıt: {response.text}")

if __name__ == '__main__':
    unittest.main()
