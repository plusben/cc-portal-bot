from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
import datetime

def log_action(action):
    """ Schreibt die Aktion und die aktuelle Uhrzeit in eine Logdatei. """
    with open("aktion_log.txt", "a") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp}: {action}\n")

driver_path = ''  # Dein Webdriver-Pfad

try:
    driver = webdriver.Chrome(driver_path)
    driver.get('https://portal.cc-student.com/index.php?cmd=login')

    # Versuche, Benutzername und Passwort einzugeben
    username = driver.find_element(By.ID, 'login_username')
    password = driver.find_element(By.ID, 'login_passwort')
    username.send_keys('XXXXXXXX')
    password.send_keys('XXXXXXXX')

    # Versuche, dich einzuloggen
    login_button = driver.find_element(By.NAME, 'login_submit')
    login_button.click()

    # Navigiere zur spezifischen Unterseite
    driver.get('https://portal.cc-student.com/index.php?cmd=kug')

    # Versuche, den Zeiterfassungsbutton zu klicken
    zeiterfassung_button = driver.find_element(By.NAME, 'showDialogButton')
    zeiterfassung_button.click()

    # Warte auf das Dialogfenster
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'ui-dialog'))
    )

    # Suche den Button anhand seines 'name'-Attributs und prüfe den 'value'-Wert
    buttons = driver.find_elements(By.NAME, 'kommengehenbutton')
    for button in buttons:
        value = button.get_attribute('value')
        if value in ['Kommen', 'Gehen']:
            button.click()
            log_action(value)
            break
    else:
        # Falls kein Button mit 'Kommen' oder 'Gehen' gefunden wurde
        print("Kein passender Button gefunden.")
        driver.quit()
        exit()

    time.sleep(5)

except Exception as e:
    print(f"Ein Fehler ist aufgetreten: {e}")
finally:
    driver.quit()