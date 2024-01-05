import re
st='asdfaNBGFD789654GESBHlsdrew76954VTRES3456W'

data=re.findall('[A-Z]{5}\d{4}[A-Z]',st)
print(data)
