from sys import argv
from datetime import datetime
def work_capture(date, prompt):
	work_notes = input(prompt)
	today_log = "\n\n%s\n%s\n%s\n\n" % (date,prompt,work_notes)
	return today_log

def log_update(update):
	log.write(update)
	
script, log_file = argv

log = open(log_file, 'a')
today_date = datetime.today()
prompt = "What did you work on today:"
today_log = work_capture(today_date, prompt)
log_update(today_log)