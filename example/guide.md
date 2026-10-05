# Introduction

This is a short guide that briefly explains how protocol files can and should be configured for use with ProtocolFlow.

# Structure

A protocol consists of four types of files:

- **Protocol config**
- **Reagent config**
- **Stage config**
- **Styler** — optional

## Directory structure

ProtocolFlow requires reagent configuration files to be stored in the `reagents` directory and stage configuration files in the `stages` directory. Both directories must be located next to the protocol configuration file (`example_protocol_config.yml` in the example below).

The program does not restrict which files may exist inside these directories. Only the reagents and stages explicitly listed in the Protocol config will be used.

Example directory structure:

```text
example/
├── example_protocol_config.yml
├── reagents
│   ├── example_reagent_1.yml
│   └── example_reagent_2.yml
├── stages
│   └── example_stage.yml
└── styler.yml
```

## Protocol config

The `Protocol config` contains the main information about the protocol and defines which components should be included.
The order of reagents does not matter. Stages are rendered in the same order in which they are listed in the configuration file.

Example configuration:

```yaml
title: "This is Title" # required

metadata: # all fields are optional
  description: "Description of the protocol"
  author: "Wolchear"
  sources:
    - "This is source 1"
    - "This is source 2 with some comments"

reagents: # required
  - "example_reagent_1.yml"
  - "example_reagent_2.yml"

stages: # required
  - "example_stage.yml"
```

## Reagent config

A `Reagent config` describes an individual reagent that is directly used during the protocol.

Example configuration:

```yaml
id: example_reagent_id # required
name: "example_reagent" # required
description: "Description" # optional

notes: # all fields are optional
  suggestions:
    - "Some suggestions"
  warnings:
    - "Some"
    - "warnings"

recipe:
  final_volume:
    value: 500 # required
    unit: "ml" # required

  reagents: # optional
    - name: "prep_reg_1" # required if reagents list exists
      amount: # required if reagents list exists
        value: 10 # required if reagents list exists
        unit: "g" # required if reagents list exists
      description: "Reagent description" # optional

    - name: "prep_reg_2"
      amount:
        value: 5
        unit: "g"

  steps: # required if recipe exists
    - "dissolve reg_1"
    - "dissolve reg_2"

  notes: # optional
    suggestions:
      - "recipe suggestions"
```

## Stage config

A `Stage config` describes an individual part of the protocol, for example `Lysis`, `DNA precipitation`, or `DNA washing`.
The `prerequisites` field is optional. However, it is **strongly recommended** to include it, because without it `ProtocolFlow` cannot validate whether a stage uses a reagent that is not included in the protocol.
For reagent validation to work correctly, each `ref` value must match the `id` of one of the reagents included in the protocol.

Example configuration:

```yaml
name: "Tissue lysis" # required

prerequisites: # optional
  reagents:
    - ref: "example_reagent_1_id"
    - ref: "example_reagent_2_id"

notes: # all fields are optional
  warnings:
    - "Some warning"

  suggestions:
    - "Some suggestions"

steps: # required
  - description: "First step" # required

  - description: "Second step"
    notes: # all fields are optional
      suggestions:
        - "Some suggestions about the second step."

  - description: "Third step"
    notes: # all fields are optional
      warnings:
        - "Some warnings about the third step."
```

## Styler

The Styler is an optional component used to control how different protocol components are displayed.

It is not specified inside the `Protocol config`. Instead, the Styler file is passed to ProtocolFlow as an input argument when the program is executed.

Example configuration:

```yaml
reagent_style:
  notes_style:
    show_warnings: true
    show_suggestions: true
  show_recipe: true

stage_style:
  notes_style:
    show_warnings: true
    show_suggestions: true
```