import os
import re
import sys
import click
import subprocess
import configparser

@click.command()
@click.option('--name', '-n', help='Name of the entry in the password manager')
@click.option('--config', '-c', show_default=True,
        default=os.path.expanduser('~/.denver.cfg'),
        type=click.File('r'))
# @conf()
def display_eval(name, config):
    cf = configparser.ConfigParser()
    cf.read_string(config.read())

    if 'XXXX' in cf['denver']['command']:
        command = cf['denver']['command'].replace('XXXX', '%s' % name)
    else:
        print("XXXX magic string not found, name wouldn't be used, aborting.", file=sys.stderr)
        sys.exit(1)

    secret = subprocess.getoutput(command)

    env = dict()
    forget = []
    for line in secret.splitlines():
        m = re.match(r"^(\w+)\s*=\s*(\w*.*)$", line)
        if m is not None:
            env[m[1].upper()] = m[2]

    for e in env:
        if os.environ.get(e, None):
            print("# not overwriting %s" % (e), file=sys.stderr)
        else:
            print(" export %s='%s'" % (e, env[e]) )
            forget.append(e)

    if len(forget) > 0:
        print("alias fdenver='unset %s;unalias fdenver'" % " ".join(forget))

if __name__ == '__main__':
    display_eval()
