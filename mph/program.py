from subprocess import run, PIPE
from io import StringIO

class Program(object):
    """
    Represents a userspace program
    """

    def __init__(self, path, args):
        self._path = path
        self._args = args

        self._stdin = bytes()
        self._stdout = bytes()
        self._stderr = bytes()

        self._retval = 0

    @property
    def path(self):
        return self._path

    @property
    def stdout(self):
        return self._stdout

    @property
    def stderr(self):
        return self._stderr

    @property
    def retval(self):
        return self._retval

    @property
    def args(self):
        return self._args
    
    def append_stdin(self, data):
        """
        Appends `data` to the program's standard input
        """
        self._stdin.join(data)

    def append_string_stdin(self, string):
        """
        Encodes `string` as UTF-8 and sends the resulting bytes to the
        program's standard input
        """
        self._stdin += string.encode("utf-8")

    def add_arg(self, pos, arg):
        """
        Add a command line argument (`arg`)  at position `pos`
        """
        self._args.insert(pos, arg)

    def remove_arg(self, pos):
        """
        Remove the command line argument at position `pos`
        """
        self._args.pop(pos)

    def get_arg(self, pos):
        """
        Get the command line argument at position `pos`
        """
        return self._args[pos]

    def set_arg(self, pos, arg):
        """
        Set the command line argument at position `pos` to `arg`
        """
        self._args[pos] = arg

    def exec(self):
        """
        Start execution of the program
        """
        self._prog = run([self.path] + self.args, stdout=PIPE, stderr=PIPE,
                input=self._stdin)
        self._stdout = self._prog.stdout
        self._stderr = self._prog.stderr
        self._retval = self._prog.returncode

