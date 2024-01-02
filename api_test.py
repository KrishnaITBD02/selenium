from selenium import webdriver
import requests
import json

# Set up the Selenium WebDriver
driver = webdriver.Chrome()  # Use the appropriate webdriver (Chrome, Firefox, etc.)

# Function to perform GET request to the API endpoint
def test_get_request():
    driver.get('https://itbd-dev-frontend.team-gps.net/login/')
    # Check if the endpoint is accessible by verifying the HTTP status code
    assert requests.get('https://itbd-dev-frontend.team-gps.net/login/').status_code == 200

# Function to perform POST request to the API endpoint with correct credentials
def test_correct_credentials():
    driver.get('https://itbd-dev-backend.team-gps.net/login/')
    email = "krishna.sharma@itbd.net"
    password = "EdSheeran@123"
    # Find input fields and fill in the credentials
    email_input = driver.find_element_by_id('email')  # Replace with the actual ID of the email input field
    password_input = driver.find_element_by_id('password')  # Replace with the actual ID of the password input field
    email_input.send_keys(email)
    password_input.send_keys(password)
    # Find and click the login button
    login_button = driver.find_element_by_id('login-button')  # Replace with the actual ID of the login button
    login_button.click()

    # Capture the API response using requests library
    payload = {"email": email, "password": password}
    response = requests.post('https://itbd-dev-backend.team-gps.net/login/', data=json.dumps(payload))

    # Validate the API response status code
    assert response.status_code == 200  # Assuming successful login returns a 200 status code

# Function to perform POST request to the API endpoint with wrong credentials
def test_wrong_credentials():
    driver.get('https://itbd-dev-backend.team-gps.net/login/')
    email = "wrongemail@itbd.net"
    password = "WrongPassword123"
    # Find input fields and fill in the wrong credentials
    email_input = driver.find_element_by_id('email')  # Replace with the actual ID of the email input field
    password_input = driver.find_element_by_id('password')  # Replace with the actual ID of the password input field
    email_input.send_keys(email)
    password_input.send_keys(password)
    # Find and click the login button
    login_button = driver.find_element_by_id('login-button')  # Replace with the actual ID of the login button
    login_button.click()

    # Capture the API response using requests library
    payload = {"email": email, "password": password}
    response = requests.post('https://itbd-dev-backend.team-gps.net/login/', data=json.dumps(payload))

    # Validate the API response status code
    assert response.status_code == 401  # Assuming incorrect credentials return a 401 Unauthorized status code

# Run the test cases
test_get_request()
test_correct_credentials()
test_wrong_credentials()

# Close the browser window
driver.quit()
