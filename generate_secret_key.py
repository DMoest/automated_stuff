#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import string
import secrets

default_char_set = string.ascii_letters + string.digits + string.punctuation


def generate_key(length: int = 32, char_set: str = default_char_set):
    """Generate key from a character set with desired length

    Args:
        length (int): length of the key
        char_set (str): char_set to generate key from
    """
    return "".join(secrets.choice(char_set) for _ in range(length))


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.DEBUG)
    logging.info(generate_key())
