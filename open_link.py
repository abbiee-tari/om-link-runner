
import requests

def open_link():
    url = "https://requestvendorusers-ll2pfavo5q-uc.a.run.app/"  # Replace with your real link
    response = requests.get(url)
    print(f"Requested {url}, Status Code: {response.status_code}")

if __name__ == "__main__":
    open_link()

