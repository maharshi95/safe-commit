# Author: Maharshi Gor
import subprocess


def bash(cmd):
    """
    Given a shell command as a string, executes that as a subprocess
    and returns the string output from STDOUT.
    """
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (stdout, stderr) = process.communicate()
    return stdout, stderr, process.returncode