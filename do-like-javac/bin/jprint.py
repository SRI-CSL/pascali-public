import logging
import os
import sys
import platform
import pprint
import subprocess
import traceback


def run_printer(javac_commands):
	pp = pprint.PrettyPrinter(indent=2)
	for jc in javac_commands:		
		#pp.pprint(jc)
		javac_switches = jc['javac_switches']
		cp = javac_switches['classpath']

		cp_entries = cp.split(os.pathsep)
		for cp_entry in cp_entries:
			if cp_entry.endswith(".jar"):
				print cp_entry
