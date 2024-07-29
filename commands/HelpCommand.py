from commands.command import Command


class HelpCommand(Command):

    def execute(self):
        print("Migrate command with path to config file")
        print("migrate <config_file> ")
        print("Regression test command")
        print("regression <csv_file>")
        return True
