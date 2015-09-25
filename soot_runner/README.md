Running
=======

To run, invoke from the directory of the project you want to analyze:

    python PATH/TO/soot_runner/bin/capture_javac.py -o logs -- ant build

Where PATH/TO is the full path to this directory, and "ant build" is replaced by whatever command builds your project. Output will be emitted to logs/toplevel.log

LICENSE
=======

Parts of the code in this directory were taken from the Facebook Infer project. Its license is available at

  https://github.com/facebook/infer/blob/master/LICENSE