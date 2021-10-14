#!/usr/bin/env python3
# encoding: utf-8

"""
@author: hzjsea
@file: utils.py.py
@time: 2021/10/7 4:59 下午
"""
import time
import os
from datetime import date, datetime
import datetime as dd
from typing import Dict, List


def get_current_time() -> str:
    """
    获取当前时间
    :return:
    """
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return date


def get_current_timestamp() -> int:
    """
    获取当前时间戳
    :return:
    """
    return int(time.time())


def path_of_record() -> str:
    """
    记录文件的文件位置
    :return:
    """
    file_path = os.environ.get("LOG_RECORD")
    if file_path is None:
        current_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        log_record = current_path + "/.log_record"
        return log_record

    return file_path


class ShowJob:

    def __init__(self) -> None:
        pass


    def lines_to_list(self) -> List:
        path = path_of_record()
        with open(path, 'r+', encoding="utf-8") as f:
           contents = f.readlines()
           return contents

    def lines_to_json(self) -> Dict:
        contents = self.lines_to_list()
        contents_json = {}
        for content in contents:
            values = content.split("|")
            id = str(values[0]).strip()
            date = str(values[1]).strip()
            strp_date = time.strptime(date, "%Y-%m-%d %H:%M:%S")
            day = strp_date.tm_mday
            month = strp_date.tm_mon
            line = str(values[2]+values[3]+values[4]).strip()
            contents_json.update({
                f"{id}":{
                    "date": date.split( )[0],
                    "day": day,
                    "month": month,
                    "line": line
                }}
            )
        return contents_json


    def show_all_content(self) -> str:
        contents = self.lines_to_list()
        result = ""
        for content in contents:
            result = str(result + "".join(content.split("|")[1:]))
        return result.strip()

    def show_content_time(self, day: int, month: int) -> str:
        contents = self.lines_to_json()
        rl = []
        if month is None:
            month = datetime.today().month
        
        if day is None:
            for index, content in contents.items():
                if content["month"] == month:
                    line = f"{content['date']} {content['line']} \n"
                    rl.append(line)
            return "".join(rl).strip()
        
        current_time = datetime.strptime(get_current_time(),'%Y-%m-%d %H:%M:%S')
        c = []
        for i in range(1,day+1):
            c.append(str(current_time - dd.timedelta(days=i)).split(" ")[0])
        
        for index, content in contents.items():
            if content["date"] in c:
                line = f"{content['date']} {content['line']} \n"
                rl.append(line)
        return "".join(rl).strip()

    def show_content_keywards(self, keywards: List) -> str:
        contents = self.lines_to_json()
        rl = []
        for key in keywards:
            for  index, content in contents.items():
                if key in content["line"]:
                    line = f"{content['date']} {content['line']} \n"
                    rl.append(line)
        return "".join(rl).strip()



if __name__ == '__main__':
    path_of_record()
    get_current_timestamp()
    get_current_time()
