def run(runfile):
  with open(runfile,"r") as rnf:
    exec(rnf.read())
    print ("aash.py")
