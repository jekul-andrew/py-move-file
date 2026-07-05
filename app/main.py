import os


class CommandStringError(Exception):

    def __str__(self) -> str:
        return ("The command format must be: "
                "mv [source file path] [destination file path]. "
                "Use a single space to separate the arguments.")


class WrongDestinationNameError(Exception):

    def __str__(self) -> str:
        return "Destination filename is wrong"


def move_file(command: str) -> None:

    str_parts = command.strip().split(" ")

    if len(str_parts) != 3 or str_parts[0] != "mv":
        raise CommandStringError

    cmd, origin, destination = str_parts

    # find separator at the end
    if destination[-1] == os.sep:
        raise WrongDestinationNameError

    dir_path = os.path.dirname(destination)

    dest_filename = os.path.basename(destination)

    created_dir = []

    if dir_path:
        path_list = dir_path.split(os.sep)
        for dirname in path_list:

            if not created_dir:
                dir_path = dirname
            else:
                dir_path = os.path.join(*created_dir) + os.sep + dirname

            if not os.path.exists(dir_path):
                os.mkdir(dir_path)

            created_dir.append(dirname)

        dir_path = os.path.join(*created_dir)
        destination_path = os.path.join(dir_path, dest_filename)

    else:
        destination_path = dest_filename

    with (open(origin, "r") as source,
          open(destination_path, "w") as destination_file):

        destination_file.write(source.read())

    os.remove(origin)
