# MPH #
---

MPH (managed program host) is a Python package providing an API for interfacing
with arbitrary executables in a generic way. It should be noted that MPH is not
a virtual machine, nor is it a emulator of any sort. MPH simply provides an API
for providing input and output to arbitrary executables.

Using MPH, users can provide input to arbitrary guest executables and retrieve
the output (on both `stdout` and `stderr`) and the return value of the program.

# Examples #

    from mph import program

    prog = program.Program("/path/to/myprog", [])   # initialise program
    prog.append_string_stdin("Hello, world!")       # write to stdin
    prog.exec()                                     # run program

    # check return value of gues executable
    if prog.retval == 0:
        print(prog.stdout)
    else:
        print("Inferior returned with return code " + str(prog.retval) + "\n")

