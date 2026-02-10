from test.config.env_config import API_KEY

TEST_QUERY = "Comedy"
EXPECTED_STATUS_CODE = 200

HEADERS = {
    "X-API-KEY": API_KEY,
    "Accept": "application/json"
}