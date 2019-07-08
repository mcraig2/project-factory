""" Contains functionality for creating a CLI """

import os

CD = os.path.dirname(os.path.abspath(__file__))


def place_file(dir_name, cli_name, fname, contents):
    """ Place the file in the correct folder """
    if fname == 'GITIGNORE':
        outfname = '{}/.gitignore'.format(dir_name)
    elif fname in ('cli.py', 'command1.py', 'command2.py',
                 'command3.py', '__main__.py', '__init__.py'):
        outfname = '{}/{}/{}'.format(dir_name, cli_name, fname)
    elif fname in ('Makefile', 'README.md', 'cli-runner.py',
                   'setup.py', 'requirements.txt'):
        outfname = '{}/{}'.format(dir_name, fname)
    elif fname in ('test_command1.py'):
        outfname = '{}/test/{}'.format(dir_name, fname)

    with open(outfname, 'w') as f:
        f.write(contents)


def install_files(dir_name, cli_name):
    """ Installs the files needed to make the given CLI """
    # First make directory structure
    os.mkdir('{}/{}'.format(dir_name, cli_name))
    os.mkdir('{}/test'.format(dir_name))

    for cli_file in os.listdir('{}/cli_maker'.format(CD)):
        if cli_file == '__pycache__':
            continue
        fname = '{}/cli_maker/{}'.format(CD, cli_file)
        with open(fname, 'r') as tmp_file:
            contents = tmp_file.read().format(NAME=cli_name)
            place_file(dir_name, cli_name, fname=cli_file, contents=contents)


def run_prep_commands(dir_name, cli_name):
    """ Run prep commands to help install, such as creating
        the virtualenv, etc. """
    commands = """
        cd {DIR} && \
        mv cli-runner.py {NAME}-runner.py && \
        mv {NAME}/cli.py {NAME}/{NAME}.py && \
        chmod +x {NAME}-runner.py && \
        virtualenv venv/ && \
        source venv/bin/activate && \
        pip install -r requirements.txt && \
        deactivate && \
        cd ..
    """.format(DIR=dir_name, NAME=cli_name)
    os.system(commands)


def make_cli():
    name = input('Project name: ').replace(' ', '_')
    print('Making CLI for "{name}"'.format(name=name))

    # We make the project in a folder that is stored in
    # the current working directory
    os.mkdir(name)
    install_files(dir_name=name, cli_name=name)
    run_prep_commands(dir_name=name, cli_name=name)
