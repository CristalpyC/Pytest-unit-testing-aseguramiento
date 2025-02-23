# tests/test_pokeapi.py
import pytest
import requests
from requests_mock import Mocker # type: ignore

BASE_URL = "https://pokeapi.co/api/v2"

@pytest.fixture
def mock_requests():
    with Mocker() as mocker:
        yield mocker

# Caso 1: Obtener listado de Pokémon
def test_obtener_listado_pokemon(mock_requests):
    mock_requests.get(f"{BASE_URL}/pokemon", json={"results": [{"name": "bulbasaur", "url": "https://pokeapi.co/api/v2/pokemon/1/"}]})
    response = requests.get(f"{BASE_URL}/pokemon")
    assert response.status_code == 200
    assert "results" in response.json()
    assert response.json()["results"][0]["name"] == "bulbasaur"

# Caso 2: Obtener información de un Pokémon específico (Ivysaur - ID 2)
def test_obtener_pokemon_especifico(mock_requests):
    mock_requests.get(f"{BASE_URL}/pokemon/2", json={"name": "ivysaur", "id": 2})
    response = requests.get(f"{BASE_URL}/pokemon/2")
    assert response.status_code == 200
    assert response.json()["name"] == "ivysaur"
    assert response.json()["id"] == 2

# Caso 3: Obtener tipos de Pokémon
def test_obtener_tipos_pokemon(mock_requests):
    mock_requests.get(f"{BASE_URL}/type", json={"results": [{"name": "fire"}, {"name": "water"}]})
    response = requests.get(f"{BASE_URL}/type")
    assert response.status_code == 200
    assert "results" in response.json()
    assert len(response.json()["results"]) > 0

# Caso 4: Obtener información de una especie de Pokémon (Ivysaur)
def test_obtener_especie_pokemon(mock_requests):
    mock_requests.get(f"{BASE_URL}/pokemon-species/2", json={"name": "ivysaur"})
    response = requests.get(f"{BASE_URL}/pokemon-species/2")
    assert response.status_code == 200
    assert response.json()["name"] == "ivysaur"