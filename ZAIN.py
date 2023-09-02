import os,platform
os.system('git pull')
ZAIN=platform.architecture()[0]
if ZAIN=="32bit":exit(' Your Device Not Support This tool')
elif ZAIN=="64bit":__import__("NS")
