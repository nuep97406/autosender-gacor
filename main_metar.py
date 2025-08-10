# Autosender data metar v.BMKGsatu
# Made by Danu (nuep) - 97406

import time
from datetime import datetime, timezone
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from data import *

# --- Setup Global ---
# Mendapatkan tanggal hari ini untuk selector
today_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d")
css_today = f"div[data-date='{today_utc}']"

# Mendapatkan jam sekarang
jam_utc = datetime.now(timezone.utc).strftime("%H")
# xpath_jam = f"//li[text()='{jam_utc}']"

# Setup opsi dan driver Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--blink-settings=imagesEnabled=false")
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("detach", True)
chrome_options.page_load_strategy = 'eager'
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
actions = ActionChains(driver)

# Wait waktu tunggu maksimal (detik)
wait = WebDriverWait(driver, 120)


def login_bmkgsatu():
    """Fungsi untuk login ke website."""
    driver.get(url_login)
    # Isi Username
    kolom_username = wait.until(EC.element_to_be_clickable((By.ID, id_username)))
    kolom_username.send_keys(input_username)

    # Isi Password
    kolom_password = driver.find_element(By.ID, id_password)
    kolom_password.send_keys(input_password)

    # Tombol Login
    time.sleep(2)
    tombol_login = wait.until(EC.element_to_be_clickable((By.XPATH, LOGIN_BUTTON_XPATH)))
    tombol_login.click()
    print("Login berhasil.")


def metar():
    """Fungsi untuk mengisi form sinoptik."""
    logout_locator = (By.XPATH, LOGOUT_XPATH)
    wait.until(EC.presence_of_element_located(logout_locator))
    driver.get(url_metar)
    # --- WMO ID ---
    # Pilih WMO ID
    time.sleep(2)
    wmo_id = wait.until(EC.element_to_be_clickable((By.XPATH, WMOID_XPATH)))
    wmo_id.send_keys("97406")
    time.sleep(3)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    print("WMO ID dipilih.")

    # --- Interaksi Observer ---
    # Pilih observer
    time.sleep(2)
    metar_observer = wait.until(EC.element_to_be_clickable((By.XPATH, OBSERVER_M_XPATH)))
    metar_observer.send_keys("Danu")
    time.sleep(3)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    print("Observer dipilih")

    # --- Interaksi Tanggal ---
    # Buka Kalender
    time.sleep(2)
    overlay_locator = (By.CSS_SELECTOR, "div.position-absolute.bg-light.rounded-sm")
    wait.until(EC.invisibility_of_element_located(overlay_locator))
    tanggal = wait.until(EC.element_to_be_clickable((By.ID, id_kalender_metar)))
    driver.execute_script("arguments[0].click();", tanggal)

    # Pilih Tanggal
    hari_ini_metar = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_today)))
    hari_ini_metar.click()
    print("Tanggal dipilih.")

    # Pilih Jam
    daftar_jam = wait.until(EC.element_to_be_clickable((By.ID, id_jam)))
    select_jam = Select(daftar_jam)
    daftar_jam.click()
    select_jam.select_by_value(jam_utc)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    print("Jam pengamatan dipilih.")

    #Pilih menit
    menit = wait.until(EC.element_to_be_clickable((By.ID, id_menit)))
    select_menit = Select(menit)
    menit.click()
    select_menit.select_by_value("00")
    actions.send_keys(Keys.ENTER)
    actions.perform()
    print("Menit pengamatan dipilih")
    

    # Konfirmasi Data Exist
    time.sleep(5)
    confirm_button = wait.until(EC.element_to_be_clickable((By.XPATH, EXISTBUTTON_XPATH)))
    time.sleep(3)
    driver.execute_script("arguments[0].click();", confirm_button)

    # Preview Data METAR
    time.sleep(3)
    preview_button = wait.until(EC.element_to_be_clickable((By.XPATH, PREVIEW_M_XPATH)))
    preview_button.click()

    # SEND BUTTON
    send_button = wait.until(EC.element_to_be_clickable((By.XPATH, SEND_M_XPATH)))
    send_button.click()

    # SEND TO INASWITCHING
    inaswtiching_button = wait.until(EC.element_to_be_clickable((By.XPATH, INASWITCHING_M_XPATH)))
    inaswtiching_button.click()

# --- Alur Eksekusi Utama ---
try:
    time.sleep(3)
    login_bmkgsatu()
    metar()
    print("✅ Proses pengiriman metar selesai.")
except Exception as e:
    print(f"❌ Terjadi error: {e}")
finally:
    driver.quit()
    pass
