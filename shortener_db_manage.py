#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import os
import sys
sys.path.insert(0, os.getcwd())
from migration import cli as commands


class DBManage(object):
    def __init__(self):
        self.parser = self.get_main_parser()
        self.subparsers = self.parser.add_subparsers(
            title='subcommands',
            description='Action to perform')
        self.add_revision_args()
        self.add_upgrade_args()
        self.add_history_args()
        self.add_current_args()

    def get_main_parser(self):
        parser = argparse.ArgumentParser(
            description='Shortener Database Manager')
        return parser

    def add_revision_args(self):
        create_parser = self.subparsers.add_parser('revision',
                                                   help='Create a '
                                                        'new DB version file.')

        create_parser.add_argument('--message', '-m', default='DB change',
                                   help='the message for the DB change')
        create_parser.add_argument('--autogenerate',
                                   help='autogenerate from models',
                                   action='store_true')
        create_parser.set_defaults(func=self.revision)

    def add_upgrade_args(self):
        """Create 'upgrade' command parser and arguments."""
        create_parser = self.subparsers.add_parser('upgrade',
                                                   help='Upgrade to a '
                                                        'future version DB '
                                                        'version file')
        create_parser.add_argument('--version', '-v',
                                   default='head',
                                   help='the version to upgrade to, or else '
                                        'the latest/head if not specified.')
        create_parser.set_defaults(func=self.upgrade)

    def add_history_args(self):
        """Create 'history' command parser and arguments."""
        create_parser = self.subparsers.add_parser(
            'history',
            help='List changeset scripts in chronological order.')
        create_parser.add_argument('--verbose', '-V',
                                   action="store_true",
                                   help='Show full information about the '
                                        'revisions.')
        create_parser.set_defaults(func=self.history)

    def add_current_args(self):
        """Create 'current' command parser and arguments."""
        create_parser = self.subparsers.add_parser(
            'current',
            help='Display the current revision for a database.')
        create_parser.add_argument('--verbose', '-V',
                                   action="store_true",
                                   help='Show full information about the '
                                        'revision.')
        create_parser.set_defaults(func=self.current)

    def revision(self, args):
        """Process the 'revision' Alembic command."""
        commands.generate(autogenerate=args.autogenerate,
                          message=args.message)

    def upgrade(self, args):
        """Process the 'upgrade' Alembic command."""
        commands.upgrade(to_version=args.version)

    def history(self, args):
        commands.history(args.verbose)

    def current(self, args):
        commands.current(args.verbose)

    def execute(self):
        """Parse the command line arguments."""
        args = self.parser.parse_args()

        # Perform other setup here...

        args.func(args)


def main():
    dm = DBManage()
    dm.execute()

if __name__ == '__main__':
    main()
