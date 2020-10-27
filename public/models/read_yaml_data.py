# -*- coding: utf-8 -*-
# @Author  : wrx

import os

import yaml
from config.setting import ROOTPATH

filename = r"\testyaml\login.yaml"


def read_yaml_data(filename):
    """
    获取yaml的数据
    :return:
    """
    case_path = ROOTPATH + filename
    yaml_data = open(case_path, 'r', encoding='utf-8')
    data = yaml.load(yaml_data,Loader=yaml.FullLoader)
    yaml_data.close()
    return data


if __name__ == "__main__":
    read_yaml_data(filename)
