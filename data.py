# --- Data yang akan diinput ---
input_username = "97406"
input_password = "opr97406"
nama_stasiun = "Stasiun Meteorologi Gamar Malamo"
url_login = "https://bmkgsatu.bmkg.go.id/login"
url_sinoptik = "https://bmkgsatu.bmkg.go.id/meteorologi/sinoptik"
url_metar = "https://bmkgsatu.bmkg.go.id/meteorologi/metarspeci"

# Daftar ID dan XPATH (SINOPTIK)
id_username = "login-email"
id_password = "login-password"
id_station = "select-station"
id_observer = "select-observer"
id_tanggal = "input-datepicker__value_"
id_jam = "input-jam"
LOGIN_BUTTON_XPATH = "/html/body/div[2]/div[1]/div/div/div/div/div[2]/div/span/form/button"
STATION_XPATH = "/html/body/div[5]/div/div/div/ul/li[2]"
OBSERVER_XPATH= "/html/body/div[6]/div/div/div/ul/li[6]"
DATAEXIST_BUTTON_XPATH = "/html/body/div[8]/div/div[3]/button[1]"
PREVIEW_BUTTON_XPATH = "/html/body/div[2]/div[1]/div[3]/div[3]/div/div/div[2]/div[1]/div/div[2]/div[5]/div/div/div/div[1]/div[2]/div/button[3]"
OK_BUTTON_XPATH = "/html/body/div[8]/div[1]/div/div/footer/button"
SEND_BUTTON_XPATH = "/html/body/div[2]/div[1]/div[3]/div[3]/div/div/div[2]/div[1]/div/div[2]/div[5]/div/div/div/div[1]/div[2]/div/button[1]"
INASWITCHING_BUTTON_XPATH = "/html/body/div[8]/div[1]/div/div/footer/button[2]"

# Daftar ID dan XPATH (METAR)
id_kalender_metar = "datepicker__value_"
id_jam = "input-jam"
id_menit = "input-menit"
WMOID_XPATH = "/html/body/div[2]/div[1]/div[3]/div[3]/div/div/div[2]/div[2]/div/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div[1]/input"
OBSERVER_M_XPATH = "/html/body/div[2]/div[1]/div[3]/div[3]/div/div/div[2]/div[2]/div/div/div/div[1]/div/div[1]/div[2]/div/div/div/div/div[1]/input"
EXISTBUTTON_XPATH = "/html/body/div[5]/div/div[3]/button[1]"
PREVIEW_M_XPATH = "/html/body/div[2]/div[1]/div[3]/div[3]/div/div/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div[2]/button[3]"
SEND_M_XPATH = "/html/body/div[2]/div[1]/div[3]/div[3]/div/div/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div[2]/button[1]"
INASWITCHING_M_XPATH = "/html/body/div[5]/div[1]/div/div/footer/button[2]"