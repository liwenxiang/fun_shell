from subprocess import Popen, PIPE
def run_shell(str):
    p = Popen(str , shell=True, stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    return p.returncode, out.rstrip(), err.rstrip()

if __name__ == "__main__":
    code, stdout, stderr = run_shell("free -m   | sort -k2,2n")
    print stdout, code, stderr

