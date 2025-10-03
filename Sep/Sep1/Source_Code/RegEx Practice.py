import re

from pydantic.v1.utils import sequence_like

#---------------------------beginner---------------------------------

# pattern=r'\b[a-z]+\b'
# sequence=(r'hi rohit Whwah NJEJN Bhd kdiei')
# a=re.findall(pattern,sequence)
# print(a)

#---------------------- 02 ---------------------------------

# pattern=r'^[0-9]+$'
# sequence=('34556 39393')
# b=re.findall(pattern,sequence)
# print(b)

#--------------------- 03 -----------------------------

pattern=r'[a-zA-Z0-9.-]+@[a-zA-Z.-0-9]+\.com'
sequence= "Here are some emails: test.user@example.com, invalid-email@123.com, name@domain.org, hello-world@sample.com"
c=re.findall(pattern,sequence)
print(c)