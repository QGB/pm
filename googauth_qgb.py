import googauth
#need windows time sycn
secret_key='MPEXHC6LUMKP3CJO'
code = googauth.generate_code(secret_key)

print code