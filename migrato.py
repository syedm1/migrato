import argparse
import logging

from commands.MigrateCommand import MigrateCommand
from commands.RegressionCommand import RegressionCommand
from commands.HelpCommand import HelpCommand


def main():
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser(description='Migration and Regression Testing Tool')
    subparsers = parser.add_subparsers(dest='command')

    # Migrate command with path to config file
    migrate_parser = subparsers.add_parser('migrate', help='Run migration command')
    migrate_parser.add_argument('config_file', type=str, help='Path to config file')

    # Regression test command
    regression_parser = subparsers.add_parser('regression', help='Run regression test command')
    regression_parser.add_argument('csv_file', type=str, help='CSV file with endpoints')

    # Help command
    help_parser = subparsers.add_parser('help', help='Show help')

    args = parser.parse_args()

    # Set default arguments for PyCharm debugger
    if not args.command:
        args.command = 'migrate'
        args.config_file = 'tests/commands/test_data/mock_config.json'

    if args.command == 'migrate':
        command = MigrateCommand(None, None, args.config_file)
    elif args.command == 'regression':
        command = RegressionCommand(args.csv_file)
    elif args.command == 'help':
        command = HelpCommand()
    else:
        parser.print_help()
        return

    command.execute()


if __name__ == '__main__':
    main()