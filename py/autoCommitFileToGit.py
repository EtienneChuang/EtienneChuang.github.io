import git
import datetime

def doCommit():
	try:
		now = datetime.datetime.now() # current date and time
		date_time = now.strftime("%Y/%m/%d, %H:%M:%S")
		commit_message = "auto update @ " + date_time
		repo = git.Repo("../")
		repo.git.add("./json/")
		repo.index.commit(commit_message)
		origin = repo.remote(name='origin')
		origin.push()
	except Exception as e: 
		print(e)
		raise e
