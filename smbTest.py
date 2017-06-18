from smb.SMBConnection import SMBConnection

user_name = "qgb"
pass_word = "q"
my_name = "qgb"

remote_smb_IP = "127.0.0.1"
domain_name = remote_smb_IP


conn = SMBConnection(user_name, pass_word, my_name, domain_name, use_ntlm_v2 = True)
# conn.connect(remote_smb_IP , 139)

shareslist = conn.listShares()
for i in shareslist:
	print i.name
