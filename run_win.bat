pytest -s --alluredir allure-results --clean-alluredir

allure generate allure-results -c -o allure-report

allure serve allure-report

# 有问题  重写