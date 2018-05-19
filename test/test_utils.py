import os
import pathlib
import shutil

from scf_add.utils import clean as clean0
from scf_add.utils import check_requirement, download, move, unpack

package = 'requests'


def test_download():
    clean()
    download(package)
    current_directory = pathlib.Path('.')
    assert any(
        x.name.startswith(package) for x in current_directory.glob('*.whl'))
    clean()


def test_unpack():
    clean()
    download(package)
    unpack()
    current_directory = pathlib.Path('.')
    assert all(pathlib.Path(f'./{wheel.stem.split("-py")[0]}').is_dir() for wheel in current_directory.glob('*.whl'))
    clean()


def test_move():
    clean()
    download(package)
    unpack()
    move()
    current_directory = pathlib.Path('.')
    assert all(pathlib.Path(f'./{wheel.stem.split("-")[0]}').is_dir() for wheel in current_directory.glob('*.whl'))
    clean()

def test_clean():
    clean()
    download(package)
    unpack()
    move()
    clean0()
    current_directory = pathlib.Path('.')
    assert len(list(current_directory.glob('*.whl'))) == 0
    clean()

def clean():
    current_directory = pathlib.Path('.')
    for wheel in current_directory.glob('*.whl'):
        directory = pathlib.Path(wheel.stem.split("-py")[0])
        target = directory.name.split('-')[0]
        os.remove(wheel.name)
        temp = wheel.name.split('-py')[0]
        if os.path.exists(temp):
            shutil.rmtree(temp)
        target = temp.split('-')[0]
        if os.path.exists(target):
            shutil.rmtree(target)
