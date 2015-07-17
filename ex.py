from sys import argv
script, log_file = argv

log = open(log_file, 'a')
today_date = time.strftime("%c")
prompt = "What did you work on today:"

log_update(work_capture(today_date, prompt))


def work_capture(date, prompt):
	work_notes = input(prompt)
	today_log = "%s \n%s \n %s(date, prompt, work_notes)"
	return today_log

def log_update(update):
	log.write(update)