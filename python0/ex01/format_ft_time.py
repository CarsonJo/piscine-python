import time as time
import datetime as dt

epoch:float = time.time()
date = dt.date.fromtimestamp(epoch)
print("Seconds since January 1, 1970:", f"{epoch:,.4f} or {epoch:.3} in scientific notation" )
print(date.strftime("%b %d %Y"))
