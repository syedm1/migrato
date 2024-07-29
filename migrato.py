import argparse
import logging
from command import MigrateCommand, RegressionTestCommand

def main():
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser(description='Migration and Regression Testing Tool')
    subparsers = parser.add_subparsers(dest='command')

    # Migrate command
    migrate_parser = subparsers.add_parser('migrate', help='Run migration command')
    migrate_parser.add_argument('--old-endpoint', type=str, help='Old endpoint URL')
    migrate_parser.add_argument('--new-endpoint', type=str, help='New endpoint URL')

    # Regression test command
    regression_parser = subparsers.add_parser('regression', help='Run regression test command')
    regression_parser.add_argument('csv_file', type=str, help='CSV file with endpoints')

    args = parser.parse_args()

    if args.command == 'migrate':
        command = MigrateCommand(args.old_endpoint, args.new_endpoint)
    elif args.command == 'regression':
        command = RegressionTestCommand(args.csv_file)
    else:
        parser.print_help()
        return

    command.execute()

if __name__ == '__main__':
    main()

