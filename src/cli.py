import argparse


def read_user_cli_args() -> argparse.Namespace:
    """Handle the CLI arguments and options."""
    parser = argparse.ArgumentParser(
        prog="rpchecker", description="check the availability of websites"
    )
    parser.add_argument(
        "-u",
        "--urls",
        metavar="URLs",
        nargs="+",
        type=str,
        default=[],
        help="enter one or more website URLs",
    )
    parser.add_argument(
        "-f",
        "--input-file",
        metavar="FILE",
        type=str,
        default="",
        help="read URLs from a file",
    )
    return parser.parse_args()
