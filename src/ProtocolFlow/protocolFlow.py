import argparse
import sys

from pydantic import ValidationError

from ProtocolFlow.parser import (
    parse_protocol,
    parce_styler
)
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
    
    parser.add_argument(
            "--styler", "-s",
            type=str,
            required=True,
            help="Render style config."
    )

    return parser.parse_args()


def main() -> None:
    args = parse_args()
    
    try:
        protocol = parse_protocol(args.input)

    except ValidationError as error:
        print("Protocol validation failed:", file=sys.stderr)

        for item in error.errors():
            location = " -> ".join(str(part) for part in item["loc"])
            message = item["msg"].removeprefix("Value error, ")

            print(f"  - {location}: {message}", file=sys.stderr)

        sys.exit(1)
        
    try:
        styler = parce_styler(args.styler)

    except ValidationError as error:
        print("Styler validation failed:", file=sys.stderr)

        for item in error.errors():
            location = " -> ".join(str(part) for part in item["loc"])
            message = item["msg"].removeprefix("Value error, ")

            print(f"  - {location}: {message}", file=sys.stderr)

        sys.exit(1)

    print(render_html(protocol, styler))


if __name__ == "__main__":
    main()