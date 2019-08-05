#coding=utf-8

from testFunc import *
#第一步，导入xlrd库

import xlrd
filename = "./test.xlsm"

excel = xlrd.open_workbook(filename)
def readCase(sheetname):

    sheet = excel.sheet_by_name(sheetname)
    
    # 获取当前sheet页有多少行数据
    nr = sheet.nrows
    
    # 获取当前sheet页中所有行的数据
    # print sheet.row_values(0)
    for i in range(1, nr):
        n_value = sheet.row_values(i)
        method, find, position, data, status = n_value[2], n_value[3], n_value[4], n_value[5], n_value[6]
        if method =="open":
            testOpen(data)
        elif method == "input":
            testInput(find,position,data)
        elif method == "click":
            testClick(find, position)
        elif method == "frame":
            testFrame(find,position,status)
        elif method == "js":
            testJs(data)
        elif method == "win_input":
            testWinInput(data)
        elif method == "select":
            testSelect(find, position, data)














