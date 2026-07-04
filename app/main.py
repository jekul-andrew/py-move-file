import os


def move_file(command: str) -> None:

    str_parts = command.strip().split(" ")

    if len(str_parts) == 3 and str_parts[0] == "mv":

        cmd, origin, destination = str_parts

        if destination[-1] != "/":
            destination = destination.strip("/ ")
            path_list = destination.split("/")

            dest_filename = path_list.pop()

            created_dir = []

            for dirname in path_list:
                if not created_dir:
                    dir_path = dirname
                else:
                    dir_path = "/".join(created_dir) + "/" + dirname

                try:
                    os.mkdir(dir_path)

                except FileExistsError:
                    pass

                created_dir.append(dirname)

            dir_path = "/".join(created_dir)

            if not dir_path:
                destination_path = dest_filename
            else:
                destination_path = dir_path + "/" + dest_filename

            try:
                with (open(origin, "r") as source,
                      open(destination_path, "w") as destination_file):

                    destination_file.write(source.read())

            except FileNotFoundError:
                pass
            else:
                os.remove(origin)
