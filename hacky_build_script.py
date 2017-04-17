#! /usr/local/bin/python3

import argparse
import os
import shutil
import subprocess
import sys

TARGET_DIR = "target"


def _build():
    """
    Build the Jars for the AtSea app
    """
    subprocess.check_call([
        "docker", "run", "-it", "-v", "{}:/mobyartshop".format(os.getcwd()),
        "-w", "/mobyartshop", "maven:alpine", "mvn", "package", "-DskipTests"
    ])
    subprocess.check_call(["docker-compose", "build"])


def _clean():
    """
    Remove the target directory which contains intermediate build artifacts
    """
    try:
        print("Removing target directory")
        shutil.rmtree(TARGET_DIR)
    except FileNotFoundError:
        print("No directory to remove")


def main():
    """
    Build the AtSea app
    """
    parser = argparse.ArgumentParser(description=main.__doc__)
    parser.add_argument(
        'action',
        type=str,
        help='the action to perform (build or clean)')
    args = parser.parse_args()
    if args.action == 'build':
        _build()
    elif args.action == 'clean':
        _clean()
    else:
        raise ValueError("Unknown action: {}".format(args.action))


if __name__ == "__main__":
    main()
