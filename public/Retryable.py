import pytest
import logging
from functools import wraps
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from time import sleep

# 配置日志
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 定义一个用于控制重试次数和间隔时间的装饰器
import time

def retry_on_failure(max_retries=3, delay=5):
    def decorator(test_func):
        @wraps(test_func)
        def wrapper(*args, **kwargs):
            # 从args中提取setup_driver作为最后一个位置参数
            setup_driver = args[-1] if len(args) > 0 else None

            retry_delays = [delay] * max_retries + [delay]
            for i, current_delay in enumerate(retry_delays):
                try:
                    return test_func(*args, **kwargs)
                except Exception as e:
                    if isinstance(e, AssertionError) and "实际标题为：" in str(e):
                        actual_title = str(e).split("实际标题为：")[1].strip()
                        print(f"尝试 {i + 1}/{max_retries} 获取页面标题失败，实际标题为: {actual_title}")
                    elif i == max_retries:
                        print(f"测试用例在重试{max_retries}次后仍失败：{str(e)}")
                        pytest.fail(f"测试用例在重试{max_retries}次后仍失败：{str(e)}")

                    time.sleep(current_delay)  # 修正这里的导入和调用

        return wrapper

    return decorator


# 初始化webdriver
@pytest.fixture
def setup_driver():
    driver = webdriver.Chrome()  # 根据实际情况更改为你的浏览器驱动
    try:
        yield driver
    finally:
        driver.quit()  # 确保资源被释放


# 使用装饰器包装测试用例
@retry_on_failure(max_retries=3, delay=1)
def test_example(setup_driver):
    url = 'http://aiweinewtest.zizaicloud.cn/home'

    setup_driver.get(url)

    # 添加你的断言或其他验证逻辑
    assert setup_driver.title == '预期标题', f"实际标题为：{setup_driver.title}"

if __name__ == '__main__':
    pytest.main()
