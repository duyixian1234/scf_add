import click

from .utils import check_requirement, clean, download, move, unpack


@click.group()
def cli():
    pass


@click.command()
@click.argument('package')
def add(package: str):
    check_requirement()
    download(package)
    unpack()
    move()
    clean()
    print('End')


def main():
    cli.add_command(add)
    cli()


if __name__ == '__main__':
    main()
