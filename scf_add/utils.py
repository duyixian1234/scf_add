import os
import pathlib
import shutil
import subprocess
import sys


def check_requirement() -> bool:
    return False


def download(package: str):
    status, output = subprocess.getstatusoutput(f'pip download {package}')
    if status:
        print(f'Error: {output}')
        sys.exit(status)


def unpack():
    current_directory = pathlib.Path('.')
    for wheel in current_directory.glob('*.whl'):
        status, output = subprocess.getstatusoutput(
            f'wheel unpack {wheel.name}')
        if status:
            print(f'Error {output}')
            sys.exit(status)


def move():
    current_directory = pathlib.Path('.')
    for wheel in current_directory.glob('*.whl'):
        directory = pathlib.Path(wheel.stem.split("-py")[0])
        for sub_dir in directory.iterdir():
            if not sub_dir.name.endswith('dist-info'):
                dst = pathlib.Path(sub_dir.name)
                shutil.copytree(sub_dir.absolute(), sub_dir.name)
                print(f'add package {sub_dir.name}')


def clean():
    current_directory = pathlib.Path('.')
    for wheel in current_directory.glob('*.whl'):
        os.remove(wheel.name)
        temp = wheel.name.split('-py')[0]
        if os.path.exists(temp):
            shutil.rmtree(temp)
