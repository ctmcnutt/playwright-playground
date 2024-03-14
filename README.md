# Playwright/Pytest & Python Test Automation Suite

### About

This project demonstrates skills in building a test automation suite from scratch, using Playwright/Pytest and Python. It is focused on [The Internet](https://the-internet.herokuapp.com/), a demo site made for automation practice by [Elemental Selenium](https://elementalselenium.com/). The suite covers a wide selection of the site's pages and functionalities.

### Getting Started

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ctmcnutt/playwright-playground
   ```

2. **(Optional) Set up virtual environment**

    ```bash
    cd playwright-playground
    python3 -m venv venv
    source myenv/bin/activate
    ```

3. **Install dependencies:**

   ```bash
   make install-dependencies
   ```

4. **Configure .env**

- Make a new file in the top folder named `.env`
- Include the following in the file:
  ```txt
  FORM_AUTHENTICATION_USERNAME=tomsmith
  FORM_AUTHENTICATION_PASSWORD=SuperSecretPassword!
  ```
- _Note:_ These variables are plainly available on the target site and are not required to be kept secret. This is to demonstrate how secured variables would be stored in a real-world situation.

### Running Tests

Execute the following commands to run the tests:

- Headless:
  ```bash
  make run-headless
  ```

- Headed (Regular speed):
  ```bash
  make run-headed
  ```

- Headed (Slow speed):
  ```bash
  make run-headed-slow
  ```

### Folder Structure

- `/pages/`: Page objects
- `/tests/`: Test spec files
