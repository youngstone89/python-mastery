from locust import HttpUser, task


class SharedObjectsClient(HttpUser):
    @task
    def get_shared_objects(self):
        with self.client.get("/v1/shared-objects/objects/1", catch_response=True) as response:
            try:
                if response.json()["count"] != 10000:
                    response.failure("Did not get expected value")
                else:
                    print(response.json()["count"])
            except JSONDecodeError:
                response.failure("Response could not be decoded as JSON")
            except KeyError:
                response.failure(
                    "Response did not contain expected key")
        with self.client.get("/v1/shared-objects/objects/2", catch_response=True) as response:
            try:
                if response.json()["count"] != 10000:
                    response.failure("Did not get expected value")
                else:
                    print(response.json()["count"])
            except JSONDecodeError:
                response.failure("Response could not be decoded as JSON")
            except KeyError:
                response.failure(
                    "Response did not contain expected key")
        with self.client.get("/v1/shared-objects/objects/3", catch_response=True) as response:
            try:
                if response.json()["count"] != 10000:
                    response.failure("Did not get expected value")
                else:
                    print(response.json()["count"])
            except JSONDecodeError:
                response.failure("Response could not be decoded as JSON")
            except KeyError:
                response.failure(
                    "Response did not contain expected key")
        with self.client.get("/v1/shared-objects/objects/4", catch_response=True) as response:
            try:
                if response.json()["count"] != 10000:
                    response.failure("Did not get expected value")
                else:
                    print(response.json()["count"])
            except JSONDecodeError:
                response.failure("Response could not be decoded as JSON")
            except KeyError:
                response.failure(
                    "Response did not contain expected key")
