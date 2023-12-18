


from selenium import webdriver

# 指定Chrome WebDriver的路径
webdriver_path = '/path/to/chromedriver'  # 请将路径替换为您的实际路径

# 创建Chrome浏览器实例
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')  # 可以根据需要设置浏览器启动时的窗口大小
driver = webdriver.Chrome(executable_path=webdriver_path, options=options)

# 访问指定网站
url = 'https://mp.toutiao.com/profile_v4/xigua/content-manage-v2'
driver.get(url)

# 可以在这里添加其他操作，如点击按钮、填写表单等

# 关闭浏览器
driver.quit()