# ecommerce_test.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_ecommerce_flow():
    # 1. Open chrome browser and login to Flipkart
    driver = webdriver.Chrome()
    driver.get("https://www.flipkart.com/")  # or "https://www.amazon.com/"

    # TODO: Add code for logging in, if required by the website.

    # 2. Go to product list page and search for ear pods
    search_box = driver.find_element(By.NAME, "q")  # Assuming the search box has the name attribute "q"
    search_box.send_keys("ear pods")
    search_box.send_keys(Keys.RETURN)

    # 3. Select the 3rd item in the search results and add it to cart
    try:
        third_item = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//div[@class='col-12-12 _2o7WAb']/div)[3]"))
        )
        third_item.click()

        # TODO: Add code to handle the pop-up or navigate to the product details page if needed.

        # Add the item to the cart
        add_to_cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add to Cart')]"))
        )
        add_to_cart_button.click()

        print("Test case executed successfully.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        # Close the browser window
        driver.quit()

if __name__ == "__main__":
    test_ecommerce_flow()
