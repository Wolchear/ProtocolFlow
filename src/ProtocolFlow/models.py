from pydantic import (
    BaseModel,
    Field,
    model_validator
)
    

class Notes(BaseModel):
    suggestions: list[str] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)

class Quantity(BaseModel):
    value: float
    unit: str
    max_value: float | None = None

class ReagentItem(BaseModel):
    name: str
    amount: Quantity
    description: str | None = None

class Recipe(BaseModel):
    final_volume: Quantity
    reagents: list[ReagentItem] = Field(default_factory=list)
    steps: list[str]
    notes: Notes | None = None

class Reagent(BaseModel):
    id: str
    name: str
    description: str | None = None
    notes: Notes | None = None
    recipe: Recipe | None = None
    
    
class ReagentRef(BaseModel):
    ref: str
    amount: Quantity | None = None


class Prerequisites(BaseModel):
    reagents: list[ReagentRef] = Field(default_factory=list)


class Step(BaseModel):
    description: str
    reagents: list[ReagentRef] = Field(default_factory=list)
    notes: Notes | None = None


class Stage(BaseModel):
    name: str
    prerequisites: Prerequisites | None = None
    notes: Notes | None = None
    steps: list[Step]
    
    def reagent_refs(self):
        if self.prerequisites is not None:
            yield from self.prerequisites.reagents

        for step in self.steps:
            yield from step.reagents
    

class Metadata(BaseModel):
    description: str | None = None
    author: str | None = None
    sources: list[str] = Field(default_factory=list)

class ProtocolConfig(BaseModel):
    title: str
    metadata: Metadata = Field(default_factory=Metadata)
    reagents: list[str] = Field(default_factory=list)
    stages: list[str] = Field(default_factory=list)
    
    
class Protocol(BaseModel):
    config: ProtocolConfig
    reagents: list[Reagent]
    stages: list[Stage]
    
    @model_validator(mode="after")
    def validate_reagent_references(self):
        reagent_ids = {reagent.id for reagent in self.reagents}

        for stage in self.stages:
            for reagent in stage.reagent_refs():
                if reagent.ref not in reagent_ids:
                    raise ValueError(
                        f"Unknown reagent '{reagent.ref}' "
                        f"in stage '{stage.name}'"
                    )

        return self

class NoteStyle(BaseModel):
    show_warnings: bool
    show_suggestions: bool

class ReagentStyle(BaseModel):
    notes_style: NoteStyle
    show_recipe: bool
    
class StageStyle(BaseModel):
    notes_style: NoteStyle

class Styler(BaseModel):
    reagent_style: ReagentStyle
    stage_style: StageStyle
