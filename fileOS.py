import os
import time

path = 'c:\\log'
fn = []

for dirpath, dirnames, filenames in os.walk(path):
    print(dirpath, dirnames, filenames)
    fn = fn + filenames

path2 = 'c:\\log\\log_7904_20240215210755.log'
print('filesize:', os.path.getsize(path2))

print('joined path:', os.path.join(path, fn[2]))

filetime = os.path.getmtime(path2)
formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
print('filetime:', filetime, 'formatted time:', formatted_time)

path3 = 'c:\\log\\01'
print(os.path.dirname(path3))
