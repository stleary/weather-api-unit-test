import pytest
from  weather import manipulate_weather_data
from unittest.mock import patch





def test_weather_data_manipulation():
    # Mock the API response
    mock_response = {
        "temperature": 20,
        "humidity": 50,
        "wind_speed": 10
    }


    with patch("weather.manipulate_weather_data") as mock_get_weather_data:
        mock_get_weather_data.return_value = mock_response

        # Call the function that manipulates the weather data
        manipulated_data = manipulate_weather_data()

        # Check if the data was properly manipulated
        assert manipulated_data == {
            "temperature": 68,
            "humidity": 50,
            "wind_speed": 22.3694
        }


def main():
    test_weather_data_manipulation();


if __name__ == '__main__':
    main()