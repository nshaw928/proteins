from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import xml.etree.ElementTree as ET
import requests

def check_exists_by_name(name, cur_driver):
    try:
        cur_driver.find_element(by=By.NAME, value=name)
    except NoSuchElementException:
        return False
    return True


def run_pisa(pdb_file, xml_files_path):
    # Load Firefox without GUI
    opts = Options()
    #opts.add_argument("--headless")
    driver = Firefox(options=opts)

    # Go to the website
    driver.get("https://www.ebi.ac.uk/msd-srv/prot_int/pistart.html")
    driver.implicitly_wait(1)

    driver.find_element(by=By.NAME, value='start_server').click()
    driver.implicitly_wait(2)

    # Find the radio button for uploading a coordinate file
    driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[2]/div/form/table/tbody/tr[4]/td/u/input').click()
    driver.implicitly_wait(3)

    # Upload the PDB file that we want to run PISA on
    driver.find_element(by=By.NAME, value='file_upload').send_keys(pdb_file)
    driver.implicitly_wait(2)
    driver.find_element(by=By.NAME, value='btn_upload').click()

    # Wait for upload to finish and submit button to appear
    while not check_exists_by_name('btn_submit_interfaces', driver):
        pass

    # Submit pdb to PISA
    driver.find_element(by=By.NAME, value='btn_submit_interfaces').click()

    # Figure out if contacts are found
    if driver.find_element(by=By.CLASS_NAME, value='phead').text.startswith('No'):
        print("No interface found")

    # Contacts are found, extract data from XML
    else:
        while not check_exists_by_name('downloadXML', driver):
            pass
        # Get XML data
        driver.find_element(by=By.NAME, value='downloadXML').click()
        driver.implicitly_wait(1)
        # Go to window with XML data
        driver.switch_to.window(driver.window_handles[1])
        xml_url = driver.current_url

        # Saves name of input file for identification
        file_name = pdb_file.split('\\')[-1].split('.')[0]
        print(driver.page_source)
        with open(xml_files_path + '/' + file_name + '.xml', 'w') as file:
            file.write(driver.page_source)

# Set vars
pdb_file = 'C:\\Users\\nshaw\\OneDrive\\Desktop\\Projects\\proteins\\datasets\\test_results\\hbb_hba\\ranked_0.pdb'
xml_files_path = 'datasets/xml_files'

run_pisa(pdb_file, xml_files_path)
