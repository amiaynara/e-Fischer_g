from selenium import webdriver
file_location='/home/hduser/test_chess'
file_location2='chess_position'
browser=webdriver.Chrome()
browser.implicitly_wait(30)
browser.get('https://nextchessmove.com')
#----- select the gnuchess engine
#black_to_move=browser.find_elements_by_xpath('//input[@type="radio"]')[2]
#black_to_move.click()
gnuchess=browser.find_elements_by_xpath('//input[@type="radio"]')[12]
gnuchess.click()
time.sleep(6)
pgn_link=browser.find_element_by_link_text('PGN')
pgn_link.click()

data=browser.find_element_by_xpath('//input[@type="file"]').send_keys(file_location) # xpath and class find the same element
confirm_upload=browser.find_element_by_link_text('Save To Board')
# select the chess file for the current position
confirm_upload.click()

#board loaded
calculate_move=browser.find_element_by_id('calculate-button')
calculate_move.click()
check_element=browser.find_element_by_link_text('Stockfish 11')
the_move_element=browser.find_elements_by_xpath('//a[@href="#"]')[7] # Don't forget to use 's'
the_move_element.click()
#print(the_move_element.get_attribute("innerHTML"))
print(the_move_element.text)

