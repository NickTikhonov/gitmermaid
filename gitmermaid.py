import subprocess
import argparse

def commit_for_log_output(output_group):
    '''
    Builds Commit instance using output from the "git log" call. example input: 
    ["79b47b6", "5ufc952", "Add mermaid CLI call", "12 minutes ago"]
    '''

    if len(output_group) != 4:
        # Can't generate a Commit if the input is invalid
        return None
    else:
        if output_group[0] == "":
            parents = ["root"]
        else:
            parents = map(lambda x: x.strip(), output_group[0].split())

        ident, message, time = output_group
        return Commit(ident, parents, message, time)


class Commit:
    '''
    Represents one commit, in as provided by "git log" 
    '''
    def __init__(self, ident, parent_idents, message, time):
        self.ident = ident
        self.parent_idents = parent_idents
        self.message = message
        self.time = time

    def __str__(self):
        return "{}: {}".format(self.ident, self.message)
    
    def mermaid_ml(self):
        '''
        Return mermaid markdown representing this commit.
        e.g. "hash[name] --> parent"
        '''
        lines = []
        formatstr = ''
        if len(self.parent_idents) == 1:
            formatstr = "{}[{} - {}] --> {}\n"
        else:
            formatstr = "{}({} - {}) --> {}\n"

        for parent in self.parent_idents:
            lines.append(formatstr.format( \
                    self.ident, \
                    self.message, \
                    self.time, \
                    parent
                ))

        return "".join(lines)


parser = argparse.ArgumentParser(description='Generate a tree diagram for git repository in current directory')
parser.add_argument("name")
args = parser.parse_args()

command = "git log --pretty=%p%n%h%n%s%n%ar --abbrev-commit --all"
process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
output = process.communicate()[0]

lines = output.split('\n')

groups = [lines[i:i+4] for i in range(0, len(lines), 4)]

with open(args.name, 'w') as target:
    target.write("graph TD;\n")

    for group in groups:
        c = commit_for_log_output(group)
        if c:
            target.write(c.mermaid_ml())

subprocess.call("mermaid {}".format(args.name).split())
subprocess.call("open {}.png".format(args.name).split())
