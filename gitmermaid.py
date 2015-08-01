import subprocess
import argparse

parser = argparse.ArgumentParser(description='Generate a tree diagram for git repository in current directory')
parser.add_argument("name")
args = parser.parse_args()

cpmap = dict()

command = "git log --pretty=%p%n%h%n%s%n%ar --abbrev-commit --all"
process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
output = process.communicate()[0]

lines = output.split('\n')

groups = [lines[i:i+4] for i in range(0, len(lines), 4)]

with open(args.name, 'w') as target:
    target.write("graph TD;\n")

    for group in groups:
        if len(group) < 4:
            continue

        if group[0] == "":
            parents = ["root"]
        else:
            parents = map(lambda x: x.strip(), group[0].split())
        ident = group[1]
        message = group[2]
        time = group[3]

        formatstr = ''
        if len(parents) == 1:
            formatstr = "{}[{} - {}] --> {}\n"
        else:
            formatstr = "{}({} - {}) --> {}\n"
            
        for parent in parents:
            target.write(formatstr.format(ident, message,
                time, parent))

gencommand = "mermaid {}".format(args.name)
process = subprocess.Popen(gencommand.split(), stdout=subprocess.PIPE)
output = process.communicate()[0]

opencommand = "open {}.png".format(args.name)
process = subprocess.Popen(gencommand.split(), stdout=subprocess.PIPE)
output = process.communicate()[0]

