from pathlib import Path

from jinja2 import Environment, PackageLoader
from weasyprint import HTML

from ProtocolFlow.models import Protocol, Styler
from ProtocolFlow.enums import OutputFormat

env = Environment(
    loader=PackageLoader("ProtocolFlow", "templates")
)

def render(
    protocol: Protocol,
    styler: Styler,
    output_format: OutputFormat,
    output_file_name: Path
) -> None:
    html = render_html(protocol, styler)
    output = output_file_name.with_suffix(f".{output_format.value}")
    
    if output_format is OutputFormat.HTML:
        output.write_text(html, encoding="utf-8")

    elif output_format is OutputFormat.PDF:
        HTML(string=html).write_pdf(output)


def render_html(protocol: Protocol, styler: Styler) -> str:
    template = env.get_template("protocol.html")

    return template.render(
        protocol=protocol,
        styler = styler
    )
    
