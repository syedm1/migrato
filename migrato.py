import argparse
import logging

from MigrateCommand import MigrateCommand
from RegressionCommand import RegressionCommand


def main():
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser(description='Migration and Regression Testing Tool')
    subparsers = parser.add_subparsers(dest='command')

    # Migrate command with path to config file
    migrate_parser = subparsers.add_parser('migrate', help='Run migration command')
    migrate_parser.add_argument('config_file', type=str, help='Path to config file')
    migrate_parser.add_argument('help', type=str, help='Help')

    # Regression test command
    regression_parser = subparsers.add_parser('regression', help='Run regression test command')
    regression_parser.add_argument('csv_file', type=str, help='CSV file with endpoints')

    args = parser.parse_args()

    if args.command == 'migrate':
        command = MigrateCommand(None, None, args.config_file)
    elif args.command == 'regression':
        command = RegressionCommand(args.csv_file)
    elif args.command == 'help':

    else:
        parser.print_help()
        return

    command.execute()

if __name__ == '__main__':
    main()

