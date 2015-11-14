import logging
import os
import sys
import platform
import pprint
import subprocess
import traceback
from glob import glob

def run_randoop(javac_commands):
	pp = pprint.PrettyPrinter(indent=2)
	i = 0
	for jc in javac_commands:		
		#pp.pprint(jc)
		javac_switches = jc['javac_switches']
		cp = javac_switches['classpath']
		class_file_dir = javac_switches['d']
		class_files = [y for x in os.walk(class_file_dir) for y in glob(os.path.join(x[0], '*.class'))]

		if len(class_files)==0:
			continue

		out_dir_name = "randoop_%04d" % (i)
		if not os.path.exists(out_dir_name):
			os.makedirs(out_dir_name)

		class_files_file_name = os.path.join(out_dir_name, 'class_files.txt')
		print ("Creating list of files %d in %s." % (len(class_files), os.path.abspath(out_dir_name)) )
		with open(class_files_file_name, mode='w') as myfile:
			for class_file_name in class_files:
				myfile.write(get_qualified_class_name_from_file(class_file_name, class_file_dir))
				myfile.write(os.linesep)

		cp_entries = cp.split(os.pathsep)
		clean_cp = list()
		clean_cp.append("./randoop/randoop-2.0.jar")

		for cp_entry in cp_entries:
			if cp_entry.endswith(".jar"):
				#print cp_entry
				#TODO copy stuff around
				clean_cp.append(cp_entry)
				pass
			else:
				#todo what happens here?
				clean_cp.append(cp_entry)
		
		randoop_command = ['java', '-ea', '-classpath', os.pathsep.join(clean_cp), 
				"randoop.main.Main", "gentests", "--classlist=%s"%class_files_file_name, 
				"--timelimit=20", "--silently-ignore-bad-class-names=true",
				"--junit-output-dir=%s"%out_dir_name]

		print " ".join(randoop_command)

		i += 1

def get_qualified_class_name_from_file(class_file_name, class_file_path):
	""" terrible hack for now """
	suffix = class_file_name.replace(class_file_path+os.sep, "")
	mid_section = suffix.replace(".class", "")
	return mid_section.replace(os.sep, ".")


def lala(randoop_jar, classpath, class_name, timelimit):
	''' Constructs a randoop command of the form
	java -ea -classpath ../randoop-2.0.jar:.
	randoop.main.Main gentests --testclass=pkg.Main  --timelimit=10
	and run it. 
	'''
	pass