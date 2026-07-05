import os


class CommandStringError(Exception):

    def __str__(self) -> str:
        return ("The command format must be: "
                "mv [source file path] [destination file path]. "
                "Use a single space to separate the arguments.")


class OriginFileNotExistsError(Exception):

    def __init__(self, file_path: str = "") -> None:
        self.file_path = file_path

    def __str__(self) -> str:
        return f"Origin file {self.file_path} doesn't exist on server"


def move_file(command: str) -> None:

    str_parts = command.strip().split(" ")

    if len(str_parts) != 3 or str_parts[0] != "mv":
        raise CommandStringError

    cmd, origin, destination = str_parts

    if not os.path.exists(origin):
        raise OriginFileNotExistsError(file_path=origin)

    dir_path = os.path.dirname(destination)

    dest_filename = os.path.basename(destination)

    # find separator at the end
    if not dest_filename:
        dest_filename = os.path.basename(origin)

    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

    destination_path = os.path.join(dir_path, dest_filename)

    with (open(origin, "r") as source,
          open(destination_path, "w") as destination_file):

        destination_file.write(source.read())

    os.remove(origin)
