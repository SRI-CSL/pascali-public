Running
=======

To run, invoke from the directory of the project you want to analyze:

    python PATH/TO/do-like-javac/bin/do-like-javac.py -o logs -- ant build

Where PATH/TO is the full path to this directory, and "ant build" is replaced by whatever command builds your project. Output will be emitted to logs/toplevel.log

You may also run a checing tool on the discovered java files, by invoking with the -t option and a tool to use (e.g. "-t soot", "-t inference" or "-t checker").

LICENSE
=======

Parts of the code in this directory were taken from the Facebook Infer project. Its license is available at

  https://github.com/facebook/infer/blob/master/LICENSE
