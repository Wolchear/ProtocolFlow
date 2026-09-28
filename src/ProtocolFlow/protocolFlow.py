import argparse

from ProtocolFlow.parser import parse_protocol

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="protocolflow",
        description="Parse and process laboratory protocols."
    )

    parser.add_argument(
        "--input", "-i",
        type=str,
        required=True,
        help="Protocol config file."
    )

    return parser.parse_args()


def main() -> None:
    args = parse_args()
    protocol = parse_protocol(args.input)
    print(protocol)


if __name__ == "__main__":
    main()