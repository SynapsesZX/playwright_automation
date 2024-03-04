from faker import Faker
import json
import requests
from api.api_body import PetStore

fake = Faker()


class TestPetstore:

    def test_pet_registration(self):
        name = fake.name()
        pet_id = fake.unique.random_int()
        request = requests.post('https://petstore.swagger.io/v2/pet',
                                json=PetStore.create_pet(self, name=name, pet_id=pet_id))
        request = request.json()
        assert request['id'] == pet_id
        assert request['name'] == name
        return request['id'], request['name']

    def test_pet_id(self):
        pet_id = self.test_pet_registration()
        request = requests.get(f"https://petstore.swagger.io/v2/pet/{pet_id[0]}")
        request = request.json()
        assert request['id'] == pet_id[0]
        print(request)
