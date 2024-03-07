import pytest
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from time import sleep


# 定义一个用于控制重试次数和间隔时间的装饰器
def retry_on_failure(max_retries=3, delay=5):
    def decorator(test_func):
        def wrapper(*args, **kwargs):
            for i in range(max_retries + 1):
                try:
                    return test_func(*args, **kwargs)
                except WebDriverException as e:
                    if i == max_retries:
                        pytest.fail(f"测试用例在重试{max_retries}次后仍失败：{str(e)}")
                    print(f"尝试 {i + 1}/{max_retries} 出现错误，将在{delay}秒后重试：{str(e)}")
                    sleep(delay)

        return wrapper

    return decorator


# 初始化webdriver
@pytest.fixture
def setup_driver():
    driver = webdriver.Chrome()  # 根据实际情况更改为你的浏览器驱动
    yield driver
    driver.quit()


# 使用装饰器包装测试用例
@retry_on_failure(max_retries=3, delay=5)
def test_example(setup_driver):
    url = 'http://example.com'

    setup_driver.get(url)

    # 添加你的断言或其他验证逻辑
    assert "预期文本" in setup_driver.page_source


if __name__ == '__main__':
    pytest.main()