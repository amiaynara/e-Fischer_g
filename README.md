# e-Fischer



# raspberry patch
conda install python=3.6
Install required APT packages:



sudo apt-get update
sudo apt-get install iceweasel
sudo apt-get install xvfb
Install required pip packages:



sudo pip install selenium
sudo pip install PyVirtualDisplay
sudo pip install xvfbwrapper

Then start with the following minimal Python:
from pyvirtualdisplay import Display
from selenium import webdriver
display = Display(visible=0, size=(1024, 768))
display.start()
driver = webdriver.Firefox()
driver.get('http://raspberrypi.stackexchange.com/')
driver.quit()
display.stop()
