import psutil
import sys
import os
import argparse

critical_names = {'systemd', 'init', 'bash', 'zsh', 'sh', 'sshd', 'Xorg', 'gnome-shell', 'kwin_wayland'}

def if_save(proc):
	try:
		if proc.pid < 1000 or proc.pid == os.getpid() or proc.pid == os.getppid():
			return False
		if proc.name in critical_names:
			return False
		return True
	except:
		return False

def show_all_procs():
	print("~~~Active processes~~~")
	for proc in psutil.process_iter(['pid','name']):
		try:
			print(f"{proc.info['pid']} - {proc.info['name']}")
		except: pass


def find_pid(name):
	for proc in psutil.process_iter(['pid','name']):
		try:
			if name == proc.info['name']:
				return proc
		except: continue
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
		return

def main():
	parser = argparse.ArgumentParser(
			description="Cryo: Process Freezer. Stop app without closin them.",
			epilog="Example: cryo freeze firefox"
	)

	subparsers = parser.add_subparsers(dest="command", required=True, help="Aviable commands")


	freeze_parser = subparsers.add_parser("freeze", help="Freeze a Process tree")
	freeze_parser.add_argument("name", type=str, help="Process name (e.g., firefox)")

	unfreeze_parser = subparsers.add_parser("unfreeze", help="Unreeze a Process tree")
	unfreeze_parser.add_argument("name", type=str, help="Process name (e.g., firefox)")

	show_procs = subparsers.add_parser("show", help="Show all active processes")

	try:
		args = parser.parse_args()
	except:
		parser.print_help()
		return

	if args.command == "show":
		show_all_procs()
		return

	name = args.name
	procs = find_children(name)
	if not procs:
		print("We dont find any processes for "+name)
		return

	for proc in procs:
		if not if_save(proc):
			print("System critical proc")
			continue
		try:
			if args.command == "freeze":
				proc.suspend()
			elif args.command == "unfreeze":
				proc.resume()
		except:
			pass

	print("Completed seccessfully!")

if __name__ == "__main__":
	main()