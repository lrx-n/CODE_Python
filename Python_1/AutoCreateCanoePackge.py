import os

def create_dirs(path):
    # 创建主目录
    
    if not os.path.exists(path):
        os.makedirs(path)

    # 在主目录下创建CANoe使用的文件夹
    folders = ['CANSystemDemo', #存放*.cfg文件
               'CANdb',         #存放工程中的的总线数据库文件
               'CAPL_Includes', #存放工程中的CAPL文件调用的头文件
               'CDD',           #存储诊断需要的CDD文件
               'Logging',       #存储日志文件
               'Macros',        #存储宏文件
               'Nodes',         #存储CAPL文件或编译好的文件
               'Panels',        #存储面板设计文件或相关的图片资源
               'Scripts',       #存储VBS脚本文件
               'SystemVariables', #需要导入的系统变量
               'Testmodul',       #测试模块文件
               'Exec32',          #需要调用的DLL文件或插件
               'Code']            #相关的编程代码或工程文件

    for folder in folders:
        folder_path = os.path.join(path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

# 传入你的路径
path = r'D:\TEMP_D\TEST1'
create_dirs(path)