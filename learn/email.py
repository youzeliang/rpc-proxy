import base64
a = base64.b64encode(b'binary\x00string')
print(a)
