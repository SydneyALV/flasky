from app.models.crystal import Crystal

# Return empty crystal list
def test_read_all_crystals_returns_empty_list(client):
    # Arrange
    # Act
    response = client.get("/crystals")
    response_body = response.get_json()
    
    # Assert
    assert response_body == []
    assert response.status_code == 200

def test_read_crystal_by_id(client, make_two_crystals):
    # Arrange
    # Act
    response = client.get("/crystals/2")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
            "id": 2,
            "name": "Garnet",
            "color": "Red",
            "powers": "Awesomeness"
        }

def test_create_crystal_route(client):
    # Arrange
    # Act
    response = client.post("/crystals", json={
        "name": "tiger's eye",
        "color": "golden brown",
        "powers": "focus the mind"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == "Crystal tiger's eye has successfully been created!"