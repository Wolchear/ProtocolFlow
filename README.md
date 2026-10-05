# ProtocolFlow

ProtocolFlow is a small command-line tool for describing laboratory protocols in structured YAML files and rendering them into human-readable documents.

The main goal is to keep the protocol itself separate from its presentation. Reagents, preparation recipes, protocol stages, warnings, and suggestions are stored as structured data and can then be rendered into different output formats.

## Features

- Protocols are defined using YAML files.
- Reagents and protocol stages are stored separately and can be reused.
- Reagent preparation recipes are supported.
- Warnings and suggestions can be attached to reagents, recipes, stages, and individual steps.
- Validation is performed using Pydantic models.
- Optional Styler configuration controls which protocol components are displayed.
- Multiple output formats are supported.

## Output formats

- HTML: A standalone HTML document with embedded CSS.
- PDF: A print-ready PDF document rendered from HTML using WeasyPrint.
- DOCX: A simple editable document containing protocol metadata, reagents, recipes, notes, stages, and protocol steps.

> DOCX output is intended primarily for collaborative editing rather than reproducing the visual appearance of the PDF.

## Installation

```bash
git clone https://github.com/Wolchear/ProtocolFlow.git
cd ProtocolFlow
pip install -e .
```

## Usage
Basic usage:

```bash
protocolFlow -i path/to/protocol_config.yml -o output/path/file_name
```

A custom Styler can be provided:

```bash
protocolFlow \
  -i path/to/protocol_config.yml \
  --styler path/to/styler.yml \
  --format html(default)|pdf|docx \
  -o output/path/file_name
```
> The output file extension is added automatically according to the selected format.

## Configuration format
For a detailed description of the configuration format, see the
[Protocol format guide](example/guide.md).