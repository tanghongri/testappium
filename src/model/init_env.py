import logging
import subprocess

logger = logging.getLogger(__name__)


def GetTarDevice():
    exitcode, output = subprocess.getstatusoutput('adb devices')
    if exitcode != 0:
        logger.error('GetTarDevice: %s, %s', str(exitcode), str(output))
        return False, ""
    DeviceList = output.splitlines()
    if not isinstance(DeviceList, list) or len(DeviceList) < 2:
        logger.error('can not find any device')
        return False, ""
    if len(DeviceList) > 2:
        logger.warn(
            'more then one device, select the first oen: %s', DeviceList[1])
    return True, DeviceList[1].split('\t')[0]


if __name__ == '__main__':
    bRet, device = GetTarDevice()
    print("GetTarDevice: " + str(bRet)+", "+str(device))
