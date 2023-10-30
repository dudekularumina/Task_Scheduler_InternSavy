from datetime import date, time, datetime
from apscheduler.schedulers.background import BackgroundScheduler

def job():
    today=datetime.today()
    date=today.strftime("%B %d, %Y")
    now=datetime.now()
    time=now.strftime("%H:%M:%S")
    
    print("The Current Date and Time is: ",date,time)

bcksch=BackgroundScheduler()
bcksch.add_job(job, trigger='interval', seconds=4)
bcksch.start()

while True:
    pass
