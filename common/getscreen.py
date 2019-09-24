import os
import time
import sys

def getScreen(driver,function_name):
    #根目录
    root_path = os.path.abspath(os.path.join(os.getcwd(), "../.."))
    srceen_path = os.path.join(root_path, 'snapshot')
    print(srceen_path)
    nowtime = time.strftime("%H%M%S")
    driver.get_screenshot_as_file(srceen_path + "/" + f"{function_name}{nowtime}.png")
