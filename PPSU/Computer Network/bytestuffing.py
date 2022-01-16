string = "dafbeZgfvaeEfw"
flagbyte = "Z"
escapebyte = "E"

x = string.replace(escapebyte, escapebyte * 2)
y = x.replace(flagbyte, escapebyte + flagbyte)
print(flagbyte + y + flagbyte)
