import re
st='1+399177021+919567509554-9834526745+91-8950473421'

data=re.findall('[+][9][1]-[6-9]\d{9}',st)
print(data)