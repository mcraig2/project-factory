""" Contains functionality for creating a project """

import os

CD = os.path.dirname(os.path.abspath(__file__))


def make_folder_structure(name):
    """ Makes the folder structure for the project """
    os.mkdir(name)
    folders = ('data/',
               'figures/',
               'models/',
               'notebooks/',
               'src/',
               'test/')
    for fold in folders:
        os.mkdir('{}/{}'.format(name, fold))


def place_file(dir_name, fname, contents):
    """ Place the given file in the correct directory """
    if fname == 'GITIGNORE':
        outfname = '{}/.gitignore'.format(dir_name)
    elif fname in ('README.md', 'Makefile', 'requirements.txt'):
        outfname = '{}/{}'.format(dir_name, fname)
    elif fname in ('process_data.py'):
        outfname = '{}/src/{}'.format(dir_name, fname)
    elif fname in ('test_process_data.py'):
        outfname = '{}/test/{}'.format(dir_name, fname)

    with open(outfname, 'w') as f:
        f.write(contents)


def install_files(dir_name):
    """ Installs the files needed to make the given CLI """
    for pfile in os.listdir('{}/project_maker'.format(CD)):
        if pfile == '__pycache__':
            continue
        fname = '{}/project_maker/{}'.format(CD, pfile)
        with open(fname, 'r') as tmp_file:
            contents = tmp_file.read().format(NAME=dir_name)
            place_file(dir_name, fname=pfile, contents=contents)


def run_prep_commands(dir_name):
    """ Run prep commands to help install, such as creating
        the virtualenv, etc. """
    commands = """
        cd {NAME} && \
        python -m venv venv/ && \
        source venv/bin/activate && \
        pip install -r requirements.txt && \
        deactivate && \
        cd ..
    """.format(NAME=dir_name)
    os.system(commands)


def make_project():
    name = input('Project name: ').replace(' ', '_')
    print('Making project for "{name}"'.format(name=name))

    # Make the folder structure and install the gitignore
    # files, and we're done!
    make_folder_structure(name=name)
    install_files(dir_name=name)
    run_prep_commands(dir_name=name)
