import os
import sys

import allure
import pytest

sys.path.append(os.getcwd())
from case import alarmView

# 使用前后置函数
@pytest.mark.usefixtures('get_driver', 'open_url')
@allure.feature('告警窗')
class Test_告警窗:
    @allure.story('修改')