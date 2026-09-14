from pydantic import BaseModel, Field

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
    

class Metadata(BaseModel):
    description: str | None = None
    author: str | None = None
    sources: list[str] = Field(default_factory=list)
    
class DisplaySettings(BaseModel):
    show_reagent_recipes: bool = False
    stages_numbering: bool = False
    stage_inner_numbering: bool = False
    steps_absolute_numbering: bool = True
    
class FileRef(BaseModel):
    file: str

class Paths(BaseModel):
    reagents_path: str = ""
    stages_path: str = ""

class ProtocolConfig(BaseModel):
    title: str
    metadata: Metadata = Field(default_factory=Metadata)
    paths: Paths = Field(default_factory=Paths)
    display: DisplaySettings = Field(default_factory=DisplaySettings)
    reagents: list[FileRef] = Field(default_factory=list)
    stages: list[FileRef] = Field(default_factory=list)