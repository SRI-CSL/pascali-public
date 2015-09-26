# Copyright (c) 2015 - present Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the BSD style license found in the
# LICENSE file in the root directory of this source tree. An additional grant
# of patent rights can be found in the PATENTS file in the same directory.

import logging
import os
import util
import tempfile

MODULE_NAME = __name__
MODULE_DESCRIPTION = '''Run analysis of code built with a command like:
gradle [options] [task]

Analysis examples:
infer -- gradle build
infer -- ./gradlew build'''



def gen_instance(*args):
    return GradleCapture(*args)

# This creates an empty argparser for the module, which provides only
# description/usage information and no arguments.
create_argparser = util.base_argparser(MODULE_DESCRIPTION, MODULE_NAME)


class GradleCapture:

    def __init__(self, args, cmd):
        self.args = args
        # TODO: make the extraction of targets smarter
        self.build_cmd = [cmd[0], '--debug'] + cmd[1:]
        # That contains javac version as well
        version_str = util.run_cmd_ignore_fail([cmd[0], '--version'])
        logging.info("Running with:\n" + version_str)

    def get_javac_commands(self, verbose_output):
        argument_start_pattern = ' Compiler arguments: '
        results = []

        for line in verbose_output:
            if argument_start_pattern in line:
                content = line.partition(argument_start_pattern)[2].strip()
                results.append(content.split(' '))

        return results

    def capture(self):
        return map(util.javac_parse,self.get_javac_commands(util.get_build_output(self.build_cmd)))

