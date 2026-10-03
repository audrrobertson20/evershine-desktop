"""Evershine Desktop — A local helper for My Time at Evershine settlement folders, workshop files, and album shots."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='evershine_desktop',
        description='A local helper for My Time at Evershine settlement folders, workshop files, and album shots.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Evershine Desktop')
    print('Keep the town workshop on disk before a story patch.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
