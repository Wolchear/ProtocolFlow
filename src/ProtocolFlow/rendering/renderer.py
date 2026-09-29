from jinja2 import Environment, PackageLoader

from ProtocolFlow.models import Protocol

env = Environment(
    loader=PackageLoader("ProtocolFlow", "templates")
)

def render_html(protocol: Protocol) -> str:
    template = env.get_template("protocol.html")

    return template.render(
        protocol=protocol
    )