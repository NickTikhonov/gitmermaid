import subprocess
import argparse

parser = argparse.ArgumentParser(description='Generate a tree diagram for git repository in current directory')
parser.add_argument("name")
args = parser.parse_args()

cpmap = dict()

command = "git log --pretty=%P%n%H%n%s --abbrev-commit --all"
process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
output = process.communicate()[0]

lines = output.split('\n')

groups = [lines[i:i+3] for i in range(0, len(lines), 3)]

with open(args.name, 'w') as target:
    target.write("graph TD;\n")

    for group in groups:
        if len(group) < 3:
            continue

        if group[0] == "":
            parents = ["root"]
        else:
            parents = map(lambda x: x.strip(), group[0].split())
        ident = group[1]
        message = group[2]

        for parent in parents:
            target.write("{}[{}] --> {}\n".format(ident[:7], message,
                parent[:7]))

