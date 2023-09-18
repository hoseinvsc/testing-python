import datetime
import jdatetime 
def jtom(s):
    a = s.split('-')
    year = int(a[0])
    month = int(a[1])
    day = int(a[2])
    x = jdatetime.date(year,month,day)
    q = x.togregorian()
    return q

s='1402-4-29'
v=jtom(s)
print(v)