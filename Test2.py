import sentry_sdk
import time

sentry_sdk.init(
    dsn="",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,
)

sen1=5
sen2=2
senNo=0
while True:
    senNo=senNo+1
    print('Test1 ')
    u1=int(input("Enter commmand:"))
    if u1==1:
        time.sleep(3)
        break
    try:
        sen1+sen2
    except Exception as err:
        sentry_sdk.capture_exception(err)
    try:
        sen1=sen1+3
    except Exception as err:
        sentry_sdk.capture_exception(err)

    
