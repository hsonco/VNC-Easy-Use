import os
os.system('clear')

print("install x11vnc before start!!!!!")
print("make sure HDMI-1 is not used!!!")
print("if you are finish from vnc type this command : (xrandr --output HDMI-1 --off) without ()!")
v = input("are you sure to start Y/n  ")
if v == "y" or "Y" :
    print("start !!!!!!")
    os.system('gtf 1280 720 60')
    os.system('xrandr --newmode "1280x720_60.00"  74.48  1280 1336 1472 1664  720 721 724 746  -HSync +Vsync')
    os.system('xrandr --addmode HDMI-1 1280x720_60.00')
    os.system('xrandr --output HDMI-1 --mode 1280x720_60.00 --right-of eDP-1')
    os.system('x11vnc -clip 1280x720+1366+1280')

elif v == "n" or "N" :
    print("closing")
