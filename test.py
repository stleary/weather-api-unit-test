import pytest
import requests
from  weather import get_weather_data
from unittest.mock import patch





def test_weather_data_manipulation():
    # Mock the API response
    mock_response = (20,50,10)

    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "current": {
                "temperature": mock_response[0],
                "humidity": mock_response[1],
                "wind_speed": mock_response[2]
            }
        }

        # Call the function that manipulates the weather data
        manipulated_data = get_weather_data()

        # Check if the data was properly manipulated
        assert manipulated_data == mock_response


def main():
    test_weather_data_manipulation();


if __name__ == '__main__':
    main()