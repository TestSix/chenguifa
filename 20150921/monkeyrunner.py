#!/usr/bin/env python
#-*- coding:utf8 -*-
#导入系统与时间模块
import sys, time
#导入monkeyrunner使用模块
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage
#连接设备
device = MonkeyRunner.waitForConnection()
#激活屏幕并解锁
device.wake()
device.drag((350,900),(350,350),1,10)
#卸载/安装APK
device.removePackage('com.poobo.winlove')
print ("Uninstall")
device.installPackage("D:/WeileAPP_V1.0.0.5_04.apk")
print ("OK")

MonkeyRunner.sleep(5.0)
#启动APP
device.startActivity(component = 'com.poobo.winlove/com.poobo.winlove.activity.MainActivity')
MonkeyRunner.sleep(10.0)
#点击屏幕
device.touch(0,0,'DOWN_AND_UP')
MonkeyRunner.sleep(10.0)
#选译设置时间
device.touch(320,630,'DOWN_AND_UP')
MonkeyRunner.sleep(5.0)
result =device.takeSnapshot()
result.writeToFile("D:\\screenshot\\"+"screenshot1"+".png","png")

MonkeyRunner.sleep(5.0)

device.touch(230,750,'DOWN_AND_UP')
MonkeyRunner.sleep(1.0)
result1 =device.takeSnapshot()
result1.writeToFile("D:\\screenshot\\"+"screenshot2"+".png","png")