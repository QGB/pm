import win32gui,pywintypes
from qgb import U
def window_enum_handler(hwnd, resultList):
	if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) != '':
		resultList.append((hwnd, win32gui.GetWindowText(hwnd)))

def get_app_list(handles=[]):
	mlst=[]
	win32gui.EnumWindows(window_enum_handler, handles)
	for handle in handles:
		mlst.append(handle)
	return mlst
	
MAIN_HWND = 0
def is_win_ok(hwnd, starttext):
	s = win32gui.GetWindowText(hwnd)
	if s.startswith(starttext):
		print (s)
		global MAIN_HWND
		MAIN_HWND = hwnd
		return None
	return 1

	
appwindows = get_app_list()
for i in appwindows:
	print i
	
	# print type(i),type(i[0]),type(i[1])
	win32gui.EnumChildWindows(0, is_win_ok, 'GoAgent ')
	# win32gui.ShowWindow(, 0)
	U.msgbox(type(MAIN_HWND))
	# if(i[1][:5]=='start'):
