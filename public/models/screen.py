# # -*- coding: utf-8 -*-
# # @Author : wrx
import functools


# 封装了一个截图装饰器
def screen(func):
    @functools.wraps(func)
    def wrapTheFunction(self, *args, **kwargs):
        # print(func.__name__)
        try:
            func(self, *args, **kwargs)
        except:
            self.main.take_screenshot(self.screen_name)
            raise

    return wrapTheFunction
