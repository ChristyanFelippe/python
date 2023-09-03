from time import sleep
from datetime import datetime, tzinfo

timenow = datetime.now()
init = datetime.now().timestamp()
sleep(1)
fim = datetime.now().timestamp()

dif = fim - init

print(dif)

 