from locust import HttpLocust, TaskSet, task
import random
import string

class StressTest(TaskSet):

    @task(1)
    def profile(self):

        def randomString(stringLength=10):
            """Generate a random string of fixed length """
            letters = string.ascii_lowercase
            return ''.join(random.choice(letters) for i in range(stringLength))

        # self.client.get("/profile")
        self.client.get(
            url="/by-uri/burst0/url1",
            headers={"authorization": randomString(10)}
        )

        # self.client.get(
        #     url="/by-uri/burst0/url2",
        #     headers={"authorization": randomString(10)}
        # )
        #
        # self.client.get(
        #     url="/by-uri/burst0/url2",
        #     headers={"authorization": "sameString"}
        # )




class WebsiteUser(HttpLocust):
    task_set = StressTest
    min_wait = 100
    max_wait = 100
