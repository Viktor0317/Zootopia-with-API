import requests


API_KEY = "ioYuuGL8ZfwKjdUkEpY0Cg==1PHoD357ta0E2vmB"
REQUEST_URL = "https://api.api-ninjas.com/v1/animals?name="

def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Args:
        animal_name (str): The name of the animal to fetch data for.
    Returns:
        list: A list of animals, each represented as a dictionary.
    """
    url = REQUEST_URL + animal_name
    try:
        res = requests.get(url, headers={'X-Api-Key': API_KEY})
        res.raise_for_status()
        return res.json()  # List of animals
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return []
