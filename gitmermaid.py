import subprocess

cpmap = dict()

command = "git log --pretty=%P%n%H%n%s --abbrev-commit --all"
process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
output = process.communicate()[0]

lines = output.split('\n')

groups = [lines[i:i+3] for i in range(0, len(lines), 3)]

print "graph TD;"

for group in groups:
    if len(group) < 3:
        continue

    if group[0] == "":
        parents = ["Repository Created"]
    else:
        parents = map(lambda x: x.strip(), group[0].split())
    ident = group[1]
    message = group[2]

    for parent in parents:
        print "\t{}[{}] --> {}".format(ident, message, parent)

