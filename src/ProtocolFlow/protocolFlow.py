import argparse
import sys

from pydantic import ValidationError

from ProtocolFlow.parser import parse_protocol
from ProtocolFlow.rendering import render_html

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
    
    try:
        protocol = parse_protocol(args.input)

    except ValidationError as error:
        print("Protocol validation failed:", file=sys.stderr)

        for item in error.errors():
            message = item["msg"].removeprefix("Value error, ")
            print(f"  - {message}", file=sys.stderr)

        sys.exit(1)

    print(render_html(protocol))


if __name__ == "__main__":
    main()