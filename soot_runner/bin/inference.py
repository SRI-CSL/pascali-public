import logging
import os
import sys
import platform
import pprint
import subprocess
import traceback


def run_inference(javac_commands):

	CFI_dist = os.environ['JSR308']+"/checker-framework-inference/dist"
	CFI_command = []
	# first add the call to the soot jar.
	CFI_command.extend(["java"])
	
	# now add the generic soot args that we want to use.
	# TODO: these should actually be parsed from command line.
	#soot_command.extend(["-pp", "-src-prec", "c"])

	for jc in javac_commands:
		pprint.pformat(jc)
		javac_switches = jc['javac_switches']
		cp = javac_switches['classpath']
		java_files = ' '.join(jc['java_files'])
		cp = cp +":"+ CFI_dist + "/checker.jar:" + CFI_dist + "/plume.jar:" + CFI_dist + "/checker-framework-inference.jar"
		cmd = CFI_command + ["-classpath", cp, "checkers.inference.InferenceLauncher" , "--checker" ,"ostrusted.OsTrustedChecker" , "--solver", "checkers.inference.solver.DebugSolver" , "--mode" , "INFER" , java_files]
		print ("Running %s" % cmd)
		try:
			print (subprocess.check_output(cmd, stderr=subprocess.STDOUT))
		except:
			print ('calling {cmd} failed\n{trace}'.format(cmd=' '.join(cmd),trace=traceback.format_exc()))
