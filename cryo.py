import psutil
import sys
import os

critical_names = {'systemd', 'init', 'bash', 'zsh', 'sh', 'sshd', 'Xorg', 'gnome-shell', 'kwin_wayland'}

def if_save(proc):
	try:
		if proc.pid <=1 or proc.pid == os.getpid() or proc.pid == os.getppid():
			return False
		if proc.name in critical_names:
			return False
		return True
	except:
		return False


def find_pid(name):
	for proc in psutil.process_iter(['pid','name']):
		if name in proc.info['name']:
			return proc
	print("Cannot find proc "+name)
	return None

def find_children(name):
	pid_parent = find_pid(name)
	if not pid_parent:
		print("Proc "+name+" doesn`t exist")
		return
	try:
		children = pid_parent.children(recursive=True)
		return [pid_parent]+list(children)
	except:
		print("Cannot find children for "+name)

def main():
	try:
		action = sys.argv[1]
		name = sys.argv[2]
	except:
		print("Invalid arguments usage. Use: 'python main.py [freeze|unfreeze] [process_name]'")
		return

	procs = find_children(name)
	if not procs:
		print("We dont find any processes for "+name)
		return

	for proc in procs:
		if not if_save(proc):
			print("System critical proc")
			continue
		try:
			if action == "freeze":
				proc.suspend()
			elif action == "unfreeze":
				proc.resume()
		except:
			pass

	print("Completed seccessfully!")

if __name__ == "__main__":
	main()