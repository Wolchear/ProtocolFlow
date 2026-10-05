import argparse
import sys
from pathlib import Path

from pydantic import ValidationError

from ProtocolFlow.parser import (
    parse_protocol,
    parce_styler
)
from ProtocolFlow.rendering import render_html

DEFAULT_STYLER = (
    Path(__file__).parent
    / "templates"
    / "default_styler.yml"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="protocolflow",
        description="Parse and process laboratory protocols."
    )

    parser.add_argument(
        "--input", "-i",
        type=Path,
        required=True,
        help="Protocol config file."
    )
    
    parser.add_argument(
        "--styler", "-s",
        type=Path,
        default=None,
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
    
    
    styler_file = args.styler or DEFAULT_STYLER
       
    try:
        styler = parce_styler(styler_file)

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