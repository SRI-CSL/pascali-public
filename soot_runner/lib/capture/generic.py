import util

class GenericCapture:
    def __init__(self, cmd):
        self.build_cmd = cmd

    def get_javac_commands(self, verbose_output):
        return []

    def capture(self):
        build_output = util.get_build_output(self.build_cmd)
        javac_commands = self.get_javac_commands(build_output)
        return map(util.javac_parse, javac_commands)
