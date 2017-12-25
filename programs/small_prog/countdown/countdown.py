#!/usr/bin/python3

# countdown.py
# ведёт обратный отсчёт времени и сообщает о своём
# завершении звуковым сигналом, можно задавать время

# Использование:
# ./coutdown.py 10

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import subprocess, time, sys, os

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

def start_cowntdown(timeout):
	timeout = int(timeout)
	while timeout > 0:
		os.system("echo '\e[92m{}\e[0m'".format(timeout))
		time.sleep(1)
		os.system('clear')
		timeout -= 1

	subprocess.call(['xdg-open', 'call_of_duty.mp3'])


# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

if len(sys.argv) == 2 and type(int(sys.argv[1])).__name__ == 'int':
	start_cowntdown(sys.argv[1])
else:
	print('Пример использования: ./countdown.py 10')
