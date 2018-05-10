import sys
# 测试使用指定目录
sys.path.append("../testappium/src")
from model import dealdevice

if __name__ == '__main__':
    bRet, device = dealdevice.GetTarDevice()
    print("GetTarDevice: " + str(bRet)+", "+str(device))
