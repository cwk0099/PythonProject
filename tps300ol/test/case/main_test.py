import os
import pytest

if __name__ == '__main__':
    # 执行用例，且每次运行都清空用例结果数据
    # '-n 3', '--dist=loadfile' ，pytest-xdist插件，多进程运行测试，进程为3个，按照文件名分组测试
    pytest.main(['-s', '-q', '--reruns=2', '-n 3', '--dist=loadfile',
                 '--reruns-delay=1', '--alluredir', '../reports', '--clean-alluredir'])
    os.system('allure generate ../reports -o ../allure-reports --clean')