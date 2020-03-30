# -*- coding: utf-8 -*-
import click
from typing import Union


@click.command()
@click.option('--reverse', '-r')
@click.option('--uppercase', '-u')
def text(reverse, uppercase) -> Union[str, None]:
    if reverse:
        text_string: str = reverse[::-1]  # Reverse the text string
        click.echo(text_string)
        return text_string

    if uppercase:
        text_string: str = uppercase.upper()  # Uppercase the text string
        click.echo(text_string)
        return text_string

    return None


if __name__ == '__main__':
    text()
