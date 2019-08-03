from multiprocessing import Pool
from selenium import webdriver

import cv2
import numpy as np
import os
import re
import requests
import time
import uuid


def save_file(image_info):
	image_link = image_info[0]
	image_source = image_info[2]
	image_ext = os.path.basename(image_link.split(".")[-1])

	try:
		get_img = np.asarray(bytearray(requests.get(image_link).content), dtype="uint8")
		image = cv2.imdecode(get_img, cv2.IMREAD_COLOR)
		cv2.imwrite(f"{uuid.uuid4().hex}.{image_ext}", image)
		print(f"SAVE DATA : {image_source}")
	except:
		print(f"SAVE ERROR: {image_source}")


def crawler(name):
	driver = webdriver.Chrome("chromedriver.exe")
	driver.get(f"https://www.google.co.kr/search?q={name}&tbm=isch")
	driver.implicitly_wait(3)

	last_height = driver.execute_script("return document.body.scrollHeight")
	pause = 0.5

	while True:
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(pause)

		try:
			element = driver.find_elements_by_id("smb")[0]
			element.click()
		except:
			pass

		new_height = driver.execute_script("return document.body.scrollHeight")

		if new_height == last_height:
			break

		last_height = new_height

	# [0]: image_link, [1]: title, [2]: source
	images_info = re.findall(r"\"ou\":\"(.*?)\".*?\"pt\":\"(.*?)\".*?\"ru\":\"(.*?)\"", driver.page_source)
	driver.quit()

	return images_info


def main():
	start_time = time.time()
	name = "조유리즈"
	data = crawler(name)
	
	os.chdir("image")

	pool = Pool(processes=4)
	pool.map(save_file, data[:30])
	pool.close()
	pool.join()
	
	print("---- %s seconds ----" % (time.time() - start_time))


if __name__ == "__main__":
	main()
