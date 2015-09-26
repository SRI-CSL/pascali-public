#!/usr/bin/env python2.7

import logging
import os
import sys
import platform
import pprint

import arg
import log
import soot

def log_header():
    logging.info('Running command %s', ' '.join(sys.argv))
    logging.info('Platform: %s', platform.platform())
    logging.info('PATH=%s', os.getenv('PATH'))
    logging.info('SHELL=%s', os.getenv('SHELL'))
    logging.info('PWD=%s', os.getenv('PWD'))

def main():
    args, cmd, imported_module = arg.parse_args()
    log.configure_logging(args.output_directory, args.incremental, args.log_to_stderr)

    log_header()

    results = imported_module.gen_instance(args, cmd).capture()
    logging.info('Results: %s', pprint.pformat(results))
    soot.run_soot(results)


if __name__ == '__main__':
    main()
