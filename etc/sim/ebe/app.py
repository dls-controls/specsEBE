import sys
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

from ebeclient import EBEClient

help_message = """
-------------------------------------------------------------------------------
A script to send commands to an EBE-4
-------------------------------------------------------------------------------
"""


def parse_args():
    """Parse command line arguments."""
    parser = ArgumentParser(usage=help_message,
                            formatter_class=ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        "-i", "--ip", type=str, default="127.0.0.1", dest="ip",
        help="IP Address of EBE")
    parser.add_argument(
        "-p", "--port", type=int, default=8080, dest="port",
        help="Port of EBE")
    parser.add_argument(
        "--param", type=int, dest="param", help="Param to request")
    parser.add_argument(
        "--value", type=str, dest="value", help="Value to set")
    parser.add_argument(
        "--remote", dest="remote", action="store_true",
        help="Set remote mode")
    parser.add_argument(
        "--local", dest="local", action="store_true",
        help="Set local mode")
    parser.add_argument(
        "--clear-error", dest="clear_error", action="store_true",
        help="Clear any error status on the device")

    args = parser.parse_args()
    if args.value and not args.param:
        parser.error("Must provide param to set with value")
    return args


def main():
    """Run program."""
    args = parse_args()

    ebe = EBEClient(args.ip, args.port, debug=True)
    if args.clear_error:
        ebe.clear_error()
    elif args.remote:
        ebe.set_remote_mode()
    elif args.local:
        ebe.set_local_mode()
    elif args.param:
        if args.value:
            ebe.set(args.param, args.value)
        else:
            ebe.get(args.param)
    else:
        ebe.get_device_name()


if __name__ == "__main__":
    sys.exit(main())
