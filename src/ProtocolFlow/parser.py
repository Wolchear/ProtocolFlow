from pathlib import Path

import yaml
from pydantic import BaseModel

from ProtocolFlow.models import Protocol, ProtocolConfig, Reagent, Stage


def _load_yaml(path: Path) -> dict:
        with path.open("r", encoding="utf-8") as stream:
            data = yaml.safe_load(stream)
            
        if data is None:
            raise ValueError(f"YAML file is empty: {path}")
        
        return data

def _parse_model[T: BaseModel](path: Path, model: type[T]) -> T:
    return model.model_validate(
        _load_yaml(path)
    )

def parse_protocol(protocol_file: str | Path) -> Protocol:
    protocol_file = Path(protocol_file)
    config = _parse_model(protocol_file, ProtocolConfig)
    
    base_dir = protocol_file.parent
    reagents: list[Reagent] = [
        _parse_model(
            base_dir
            / config.paths.reagents_path
            / reagent_name,
            Reagent,
        )
        for reagent_name in config.reagents
    ]

    stages: list[Stage] = [
        _parse_model(
            base_dir
            / config.paths.stages_path
            / stage_name,
            Stage,
        )
        for stage_name in config.stages
    ]
    
    return Protocol(
        config=config,
        reagents=reagents,
        stages=stages,
    )