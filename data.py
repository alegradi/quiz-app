import requests
from setup import SetupInterface

question_data = []


def get_question_data():
    global question_data
    setup = SetupInterface()
    parameters = setup.parameters
    print(f"Parameters: {parameters}")  # Debug info

    response = requests.get("https://opentdb.com/api.php", params=parameters)
    response.raise_for_status()
    data = response.json()

    question_data = data["results"]
    print(f"Question data: {question_data}")  # Debug info
