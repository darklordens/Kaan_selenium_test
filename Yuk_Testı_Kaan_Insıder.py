from locust import HttpUser, TaskSet, task, between, events
from locust.main import main
import sys
import time

class SearchTasks(TaskSet):
    @task
    def search(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        self.client.get("/", headers=headers)
        self.client.get("/arama?q=telefon", headers=headers)

class WebsiteUser(HttpUser):
    tasks = [SearchTasks]
    wait_time = between(1, 5)
    host = "https://www.n11.com"

@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    print("Test tamamlandı, 5 saniye bekleniyor...")
    time.sleep(5)  # Test bitiminde 5 saniye bekle ve ardından kapat

if __name__ == "__main__":
    sys.argv = ['locust', '-f', __file__, '--headless', '-u', '1', '-r', '1', '-t', '1m']
    main()
