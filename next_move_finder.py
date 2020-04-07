from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains as Actions

file_location='/home/hduser/Projects/e-Fishcer/template'
browser=webdriver.Chrome()
browser.get('https://nextchessmove.com')
browser.implicitly_wait(30)
#----- select the gnuchess engine
#black_to_move=browser.find_elements_by_xpath('//input[@type="radio"]')[2]
#black_to_move.click()
who_moves_btn= browser.find_element_by_xpath('//*[@id="ncm-controls"]/div[1]/label[2]/div[1]/input') 
who_moves_btn.click()
gnuchess_selector=browser.find_element_by_xpath('//*[@id="ncm-pro"]/div[1]/div/div[2]/div[3]/div[2]/div/div[1]/label/div[1]/input')
gnuchess_selector.click()
pgn_link=browser.find_element_by_link_text('PGN') 
pgn_link.click()

data=browser.find_element_by_xpath('//input[@type="file"]').send_keys(file_location) # xpath and class find the same element
confirm_upload=browser.find_element_by_link_text('Save To Board')
# select the chess file for the current position
confirm_upload.click()

#board loaded
calculate_move=browser.find_element_by_id('calculate-button')
calculate_move.click()
check_element=browser.find_element_by_link_text('GNU Chess 6.2.5')
the_move_element=browser.find_elements_by_xpath('//a[@href="#"]')[7] # Don't forget to use 's'
the_move_element.click()
#print(the_move_element.get_attribute("innerHTML"))
print(the_move_element.text)
browser.quit()
