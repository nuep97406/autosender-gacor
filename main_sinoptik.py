# Autosender data sinoptik v.BMKGsatu
# Made by Danu (nuep) - 97406

import time
from datetime import datetime, timezone
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
jam_utc = datetime.now(timezone.utc).strftime("%H:00")
xpath_jam = f"//li[text()='{jam_utc}']"

# Setup opsi dan driver Chrome
chrome_option = Options()
chrome_option.add_experimental_option("detach", True)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_option)

# Buat satu objek wait waktu tunggu maksimal (detik)
wait = WebDriverWait(driver, 20)


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
    tombol_login = wait.until(EC.element_to_be_clickable((By.XPATH, LOGIN_BUTTON_XPATH)))
    tombol_login.click()
    print("Login berhasil.")


def sinoptik():
    """Fungsi untuk mengisi form sinoptik."""
    driver.get(url_sinoptik)
    # --- Interaksi Stasiun ---
    # Dropdown daftar stasiun
    stasiun = wait.until(EC.element_to_be_clickable((By.ID, id_station)))
    driver.execute_script("arguments[0].click();", stasiun)

    # Pilih Stasiun
    pilih_stasiun = wait.until(EC.element_to_be_clickable((By.XPATH, STATION_XPATH)))
    pilih_stasiun.click()
    print("Stasiun dipilih.")

    # --- Interaksi Observer ---
    # Dropdown daftar observer
    observer = wait.until(EC.element_to_be_clickable((By.ID, id_observer)))
    driver.execute_script("arguments[0].click();", observer)

    # Pilih observer
    pilih_observer = wait.until(EC.element_to_be_clickable((By.XPATH, OBSERVER_XPATH)))
    pilih_observer.click()
    print("Observer dipilih.")

    # --- Interaksi Tanggal ---
    # Buka Kalender
    tanggal = wait.until(EC.element_to_be_clickable((By.ID, id_tanggal)))
    driver.execute_script("arguments[0].click();", tanggal)

    # Pilih Tanggal
    hari_ini = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_today)))
    hari_ini.click()
    print("Tanggal dipilih.")

    # Dropdown Jam
    daftar_jam = wait.until(EC.element_to_be_clickable((By.ID, id_jam)))
    daftar_jam.click()

    # Pilih Jam
    jam_pengamatan = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_jam)))
    jam_pengamatan.click()
    print("Jam pengamatan dipilih.")

    # Konfirmasi Data Exist
    confirm_button = wait.until(EC.element_to_be_clickable((By.XPATH, DATAEXIST_BUTTON_XPATH)))
    confirm_button.click()

    # Preview Data Sinoptik
    preview_button = wait.until(EC.element_to_be_clickable((By.XPATH, PREVIEW_BUTTON_XPATH)))
    preview_button.click()

    # OK BUTTON
    ok_button = wait.until(EC.element_to_be_clickable((By.XPATH, OK_BUTTON_XPATH)))
    ok_button.click()

    # Pengulangan preview utk fix 5////
    preview_button = wait.until(EC.element_to_be_clickable((By.XPATH, PREVIEW_BUTTON_XPATH)))
    preview_button.click()
    ok_button = wait.until(EC.element_to_be_clickable((By.XPATH, OK_BUTTON_XPATH)))
    ok_button.click()

    # SEND BUTTON
    send_button = wait.until(EC.element_to_be_clickable((By.XPATH, SEND_BUTTON_XPATH)))
    send_button.click()

    # SEND TO INASWITCHING
    inaswtiching_button = wait.until(EC.element_to_be_clickable((By.XPATH, INASWITCHING_BUTTON_XPATH)))
    inaswtiching_button.click()

# --- Alur Eksekusi Utama ---
try:
    login_bmkgsatu()
    time.sleep(5)
    sinoptik()
    print("✅ Proses pengiriman sinoptik selesai.")
except Exception as e:
    print(f"❌ Terjadi error: {e}")
finally:
    driver.quit()
    pass