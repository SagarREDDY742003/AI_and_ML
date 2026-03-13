import requests
from config import BASE_URL, API_KEY
from exceptions import APIError, AuthenticationError, NotFoundError

class APIClient:
    def __init__(self, base_url = BASE_URL, api_key = API_KEY):
        self.base_url = base_url
        self.headers = {"Authorization": f"Bearer {api_key}"} if api_key else {}
        
    def create(self, resource, data):
        """POST - Create a new resource"""
        url = f"{self.base_url}/{resource}"
        response = requests.post(url, json=data, headers=self.headers)
        return self._handle_response(response)
    
    def read(self, resource, resource_id=None):
        """GET - Read resource(s)"""
        url = f"{self.base_url}/{resource}"
        if resource_id:
            url += f"/{resource_id}"
        response = requests.get(url, headers=self.headers)
        return self._handle_response(response)
    
    def update(self, resource, resource_id, data):
        """PUT - Update an existing resource"""
        url = f"{self.base_url}/{resource}/{resource_id}"
        response = requests.put(url,json=data,headers=self.headers)
        return self._handle_response(response)
    
    def delete(self, resource, resource_id):
        url = f"{self.base_url}/{resource}/{resource_id}"
        response = requests.delete(url, headers=self.headers)
        return self._handle_response(response)
    
    def _handle_response(self, response):
        """Centralized error handling"""
        if response.status_code == 401:
            raise AuthenticationError("Invalid or missing API key.")
        elif response.status_code == 404:
            raise NotFoundError("Resource not found.")
        elif not response.ok:
            raise APIError(f"API error: {response.status_code} - {response.text}")
        return response.json() if response.text else {}