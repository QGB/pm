try:os.open('your_lockfile',os.O_CREAT|os.O_EXCL|os.O_RDWR)
except Exception as e:U.msgbox(e.errno)
