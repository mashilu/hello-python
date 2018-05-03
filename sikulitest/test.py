import os  # 导入os包

command = 'taskkill /im calc.exe'  # 定义一个结束进程的命令字符串
# os.popen('calc.exe')   #python打开应用程序的方法
# openApp('calc.exe')    #Sikuli打开应用程序的方法

a = App.open("calc.exe")  # Sikuli打开应用程序的方法

wait("1481855580087.png")  # 等待元素出现

click("1481855580087.png")  # 点击元素

wait("1481855635062.png")

click("1481855635062.png")

wait("1481855675892.png")

click("1481855675892.png")

wait("1481855716969.png")

click("1481855716969.png")

wait("1481855763519.png")

click("1481855763519.png")

wait("1481855820477.png")

click("1481855820477.png")

if exists("66.png"):  # 断言
    print
    "测试通过"
    a.close()  # Sikuli关闭应用程序的方法
    # os.popen(command)    #python关闭应用程序的方法
else:
    print
    "测试失败"
    a.close()
    # os.popen(command)