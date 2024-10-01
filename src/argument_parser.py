import argparse


def get_argument_parser():
    """
    This function returns the argument parser for this project.
    It does not parse the arguments, this has to be done separately.
    It contains the default values for this project.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d",
        "--device-id",
        dest="device_id",
        help="the id of the camera that shall be used",
        default=1,
        type=int,
    )
    parser.add_argument(
        "--fps",
        dest="fps",
        help="the fps to be used for recording (only available in camera mode)",
        default=15,
        type=int,
    )
    parser.add_argument(
        "--square",
        dest="square",
        help="make the frame square (it will not be resized but cropped to the smaller edge length, only available in camera mode)",
        action="store_true",
        default=False,
    )
    parser.add_argument(
        "--height",
        dest="height",
        help="height of the flipbook in cm",
        default=3.5,
        type=float,
    )
    parser.add_argument(
        "--left-margin",
        dest="left_margin",
        help="margin to the left of the image in cm that can be used to unite the single paper sheets",
        default=2.5,
        type=float,
    )
    parser.add_argument(
        "--border-linewidth",
        dest="border_linewidth",
        help="linewidth of the border in pixels that gets drawn around the image and the left margin. Increase if the border is not visible on the printed sheets.",
        default=1,
        type=int,
    )
    parser.add_argument(
        "--sheet-margin",
        dest="sheet_margin",
        help="margin of the A4 sheet in cm used for top, bottom, left, right. Choose it depending on what your printer is capable of.",
        default=1.27,
        type=float,
    )
    parser.add_argument(
        "-f",
        "--filepath-video",
        dest="filepath_video",
        help="path to a an existing video or GIF that shall be converted to a flipbook. If not set, the camera stream will be used.",
        default=None,
    )

    return parser


def get_args():
    """
    This function gets the argument parser, parses the arguments and also directly reacts to some flags.
    It returns the parsed arguments.
    """
    parser = get_argument_parser()
    args = parser.parse_args()

    # Handle some reactions directly here.

    return args


def print_parser_information_for_readme():
    """
    This function loads the argument parser used in this project and prints the available options in a more
    convenient way in order to easy copy paste it to the projects README.
    """
    # We want to print it in a table, so print the header first.
    print("| flag | name | description | default |")
    print("| :---: | :--- | :--- | :--- |")

    # Now get the parser and print the arguments.
    parser = get_argument_parser()
    for action in parser._actions:
        # Collect short and long versions of the argument.
        flag = ""
        name = ""
        option_strings = action.option_strings
        for option_string in option_strings:
            if option_string.startswith("--"):
                name = "`" + option_string + "`"
            elif option_string.startswith("-"):
                flag = "`" + option_string + "`"
            else:
                raise ValueError(f"unknown option_string {option_string}")
        # Handle the special case for flags (store_true, store_false) that have default of False or True.
        default_value = (
            action.default if action.default is not argparse.SUPPRESS else "None"
        )
        # Print the next line for the table.
        print(f"| {flag} | {name} | {action.help} | `{default_value}` |")


if __name__ == "__main__":
    # Normally we do not execute this file, so if we do, we want the README informations.
    print("\nparser usage:\n")
    print_parser_information_for_readme()
