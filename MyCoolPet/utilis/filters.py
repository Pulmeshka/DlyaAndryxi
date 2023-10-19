from re import Pattern, compile

from aiogram import types
from aiogram.dispatcher.filters import Filter


class Command(Filter):
    def __init__(
        self,
        commands: [str],
        *arguments,
        prefixes: [str] = ("/",),
        no_args: bool = False
    ):
        self.prefixes = prefixes if not prefixes == "" else [""]

        if not self.check_command_correctness(commands):
            raise TypeError("Command validation failed")

        if isinstance(commands, tuple):
            commands = list(commands)

        if not isinstance(commands, list):
            commands = [commands]

        for i, command in enumerate(commands):
            commands[i] = str(command).lower()

        self.no_args = no_args
        self.commands = commands
        arguments = list(arguments)
        for i, variants in enumerate(arguments):
            if isinstance(variants, tuple):
                arguments[i] = list(variants)
                continue
            if not isinstance(variants, list):
                arguments[i] = [variants]

        for variants in arguments:
            for i, variant in enumerate(variants):
                variants[i] = str(variant).lower()
        self.required_arguments = arguments

    @staticmethod
    def check_command_correctness(command: str) -> bool:
        if isinstance(command, (list, tuple)):
            return all(map(Command.check_command_correctness, command))
        elif isinstance(command, str) and len(command) > 0:
            command = command.lower()
            if "\n" in command or " " in command:
                return False
            return True
        return False

    def check_arguments(self, args):
        if self.no_args:
            return len(args) < 1
        if len(self.required_arguments) < 1:

            return True
        if len(self.required_arguments) > len(args):
            return False
        for equaled_argument, variants in zip(args, self.required_arguments):
            if all(
                map(
                    lambda x: x[0] != x[1],
                    zip([equaled_argument] * len(variants), variants),
                )
            ):
                return False
        return True

    async def check(self, message: types.Message):
        if not any([message.text.startswith(prefix) for prefix in self.prefixes]):
            return False
        for prefix in self.prefixes:
            if not message.text.lower().startswith(prefix):
                continue
            text = message.text[len(prefix):].lower()
            mention = "@" + (await message.bot.me).username.lower()
            if len(text.split()) < 1:
                return False
            for command in self.commands:
                if text.startswith(command):
                    message.command_body = command
                    text_after_command = text[len(command):]

                    if text_after_command.startswith("@"):
                        if text_after_command.startswith(mention):
                            text_after_command = text_after_command[len(mention):]
                        else:
                            return False

                    if len(text_after_command) == 0 or text_after_command[0] in (
                        " ",
                        "\n",
                    ):
                        arguments = text_after_command[1:]
                    else:
                        continue
                    arguments = arguments.split(" ") if len(arguments) else []

                    message.args = arguments
                    return self.check_arguments(message.args)
        return False