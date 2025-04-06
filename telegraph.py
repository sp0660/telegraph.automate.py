from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

driver.get("https://telegra.ph/")
print("Opened page")

# Handle Title Field
try:
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//h1[@data-placeholder='Title']"))
    )
    # Find the title field using XPath
    title_field = driver.find_element(By.XPATH, "//h1[@data-placeholder='Title']")
    
    # Clear any pre-existing text (if any)
    title_field.clear()  # Might be unnecessary, just to ensure
    print("Title field is clear")
    
    # Enter title text
    title_field.send_keys("How To Become Pilot after 10th")
    print("Title Entered Successfully")

except Exception as e:
    print(f"Error: {e}")

time.sleep(2)

# Handle Author Field (contenteditable)
try:
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//address[@data-placeholder='Your name']"))
    )
    
    # Find the author input field using XPath
    author_field = driver.find_element(By.XPATH, "//address[@data-placeholder='Your name']")
    
    # Clear any existing content if needed (using JavaScript to clear contenteditable fields)
    driver.execute_script("arguments[0].innerHTML = ''", author_field)  # Clear the contenteditable field using JS
    print("Author field is cleared")

    # Input the name "Satyam Kramate" using JavaScript to directly set the innerHTML
    driver.execute_script("arguments[0].innerHTML = arguments[1]", author_field, "Satyam Kramate")
    print("Author name entered successfully")

except Exception as e:
    print(f"Error: {e}")

time.sleep(2)

# Handle Story Field (contenteditable)
try:
    # Wait for the <p> element with the placeholder "Your story..."
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//p[@data-placeholder='Your story...']"))
    )
    
    # Find the story input field using XPath
    story_field = driver.find_element(By.XPATH, "//p[@data-placeholder='Your story...']")
    
    # Clear any existing content (in case there is placeholder text)
    driver.execute_script("arguments[0].innerHTML = ''", story_field)  # Using JavaScript to clear content
    print("Story field is cleared")

    # Input a large block of text (your story) using JavaScript to directly set the innerHTML
    story_text = """
    Becoming a pilot is a rewarding and challenging journey that requires commitment, hard work, and a strong academic foundation. After completing your 10th grade, the first step is to choose a career path in aviation. It is recommended to pursue the Science stream with subjects like Physics and Mathematics, which are essential for understanding aviation principles. After completing 12th grade, you can opt for a Bachelor's degree in Aviation or take specialized courses like Commercial Pilot License (CPL) training. Additionally, you must meet the physical and medical fitness requirements set by aviation authorities.

    For more detailed guidance on how to pursue a pilot career in India after 10th grade, you can refer to this link for further information.
    """

    driver.execute_script("arguments[0].innerHTML = arguments[1]", story_field, story_text)  # Directly set the story text
    print("Story text entered successfully")

except Exception as e:
    print(f"Error: {e}")

# Add a delay to view the result (can be removed in production)
time.sleep(2)

# Handle Publish Button (if needed)
try:
    # Wait until the Publish button is clickable
    publish_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "_publish_button"))
    )

    # Click the Publish button
    print("Publish button clicked successfully!")
    # publish_button.click()  # Uncomment this to click the button

except Exception as e:
    print(f"Error: {e}")

# Add a delay to view the result (can be removed in production)
time.sleep(30)

# Close the browser
driver.quit()
