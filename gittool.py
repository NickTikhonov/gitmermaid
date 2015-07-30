import subprocess

cpmap = dict()
process = subprocess.Popen("git log --pretty=%P,%H,%s// --abbrev-commit --all".split(), stdout=subprocess.PIPE)
output = process.communicate()[0]

print "graph TD;"

lines = output.split('//')[:-1]

print "graph TD;"
for line in lines:
  line = line.strip()
  parents, child, title = line.split(',',2)
  parents = parents.split()
  for parent in parents:
    print "\t",(child[:5] + "[" + title + "]"),"-->",parent[:5]

