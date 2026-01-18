import psutil
import sys
import os
import argparse

def if_safe(proc):
	try:
		if proc.pid < 1000 or proc.pid == os.getpid() or proc.pid == os.getppid():
			return False
		return True
	except:
		return False

def show_all_procs():
	print("~~~ Active processes ~~~")
	for proc in psutil.process_iter(['pid', 'name']):
		try:
			if proc.info['pid'] < 1000:
				continue
			print(f"{proc.info['pid']} - {proc.info['name']}")
		except:
			pass

def proc_status(name):
	proc = find_pid(name)
	if proc.status() == psutil.STATUS_STOPPED:
		print("Process is frozen ❄️")
	else:
		print("Process is running 🟢")


def find_pid(name):
	for proc in psutil.process_iter(['pid', 'name']):
		try:
			if name == proc.info['name']:
				return proc
		except:
			continue
	print("Cannot find process " + name)
	return None

def find_children(name):
	pid_parent = find_pid(name)
	if not pid_parent:
		print("Process " + name + " doesn't exist")
		return []
	try:
		children = pid_parent.children(recursive=True)
		return [*[pid_parent], *list(children)]
	except:
		print("Cannot find children for " + name)
		return []

def main():
	parser = argparse.ArgumentParser(
		description="Cryo: Process Freezer. Stop apps without closing them.",
		epilog="Example: cryo freeze firefox"
	)

	subparsers = parser.add_subparsers(
		dest="command",
		required=True,
		help="Available commands"
	)

	freeze_parser = subparsers.add_parser(
		"freeze",
		help="Freeze a process tree"
	)
	freeze_parser.add_argument(
		"name",
		type=str,
		help="Process name (e.g., firefox)"
	)

	unfreeze_parser = subparsers.add_parser(
		"unfreeze",
		help="Unfreeze a process tree"
	)
	unfreeze_parser.add_argument(
		"name",
		type=str,
		help="Process name (e.g., firefox)"
	)

	status_parser = subparsers.add_parser(
		"status",
		help="Show process status (e.g freeze/running)"
	)

	status_parser.add_argument(
		"name",
		type=str,
		help="Process name (e.g., firefox)"
	)

	show_procs = subparsers.add_parser(
		"show",
		help="Show all active processes"
	)

	try:
		args = parser.parse_args()
	except:
		parser.print_help()
		return

	if args.command == "show":
		show_all_procs()
		return
	elif args.command == "status":
		proc_status(args.name)
		return


	name = args.name
	procs = find_children(name)
	if not procs:
		print("We didn't find any processes for " + name)
		return

	for proc in procs:
		if not if_safe(proc):
			print(f"System critical process {proc}!!!")
			continue
		try:
			if args.command == "freeze":
				proc.suspend()
			elif args.command == "unfreeze":
				proc.resume()
		except:
			pass

	print("Completed successfully!")

if __name__ == "__main__":
	main()
