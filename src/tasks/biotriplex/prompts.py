from typing import Dict, List, Type

from ..utils_typing import Entity, Relation, dataclass


"""Entity definitions
"""

@dataclass
class Gene(Entity):
    """{biotriplex_gene}"""
    span: str


@dataclass
class Disease(Entity):
    """{biotriplex_disease}"""
    span: str

ENTITY_DEFINITIONS: List[Type] = [
    Gene,
    Disease,
]


"""Relation definitions
"""


@dataclass
class GeneDiseaseRelation(Relation):
    """{biotriplex_genediseaserelation}"""

    arg1: str
    arg2: str

COARSE_RELATION_DEFINITIONS: List[Type] = [
    GeneDiseaseRelation,
]

@dataclass
class NoRelation(GeneDiseaseRelation):
    """{biotriplex_norelation}"""

    arg1: str
    arg2: str


@dataclass
class UndefinedRelation(GeneDiseaseRelation):
    """{biotriplex_undefinedrelation}"""

    arg1: str
    arg2: str

@dataclass
class CausativeActivation(GeneDiseaseRelation):
    """{biotriplex_causativeactivation}"""

    arg1: str
    arg2: str

@dataclass
class CausativeInhibition(GeneDiseaseRelation):
    """{biotriplex_causativeinhibition}"""

    arg1: str
    arg2: str

@dataclass
class CausativeMutation(GeneDiseaseRelation):
    """{biotriplex_causativemutation}"""

    arg1: str
    arg2: str

@dataclass
class AssociatedMutation(GeneDiseaseRelation):
    """{biotriplex_associatedmutation}"""

    arg1: str
    arg2: str

@dataclass
class IncreasedExpression(GeneDiseaseRelation):
    """{biotriplex_increasedexpression}"""

    arg1: str
    arg2: str

@dataclass
class DecreasedExpression(GeneDiseaseRelation):
    """{biotriplex_decreasedexpression}"""

    arg1: str
    arg2: str

@dataclass
class Dysregulation(GeneDiseaseRelation):
    """{biotriplex_dysregulation}"""

    arg1: str
    arg2: str

@dataclass
class EpigeneticMarker(GeneDiseaseRelation):
   """{biotriplex_epigeneticmarker}"""

   arg1: str
   arg2: str

@dataclass
class ModulatorDecreaseDisease(GeneDiseaseRelation):
    """{biotriplex_modulatordecreasedisease}"""

    arg1: str
    arg2: str

@dataclass
class ModulatorIncreaseDisease(GeneDiseaseRelation):
    """{biotriplex_modulatorincreasedisease}"""

    arg1: str
    arg2: str

@dataclass
class GeneticSusceptibility(GeneDiseaseRelation):
    """{biotriplex_geneticsusceptibility}"""

    arg1: str
    arg2: str

@dataclass
class Biomarker(GeneDiseaseRelation):
    """{biotriplex_biomarker}"""

    arg1: str
    arg2: str

@dataclass
class PrognosticIndicator(GeneDiseaseRelation):
    """{biotriplex_prognosticindicator}"""

    arg1: str
    arg2: str

@dataclass
class NegativePrognosticMarker(GeneDiseaseRelation):
    """{biotriplex_negativeprognosticmarker}"""

    arg1: str
    arg2: str

@dataclass
class PositivePrognosticMarker(GeneDiseaseRelation):
    """{biotriplex_positiveprognosticmarker}"""

    arg1: str
    arg2: str

@dataclass
class DiagnosticTool(GeneDiseaseRelation):
    """{biotriplex_diagnostictool}"""

    arg1: str
    arg2: str

@dataclass
class TherapyResistance(GeneDiseaseRelation):
    """{biotriplex_therapyresistance}"""

    arg1: str
    arg2: str

@dataclass
class TherapeuticTarget(GeneDiseaseRelation):
    """{biotriplex_therapeutictarget}"""

    arg1: str
    arg2: str

@dataclass
class PathologicalRole(GeneDiseaseRelation):
    """{biotriplex_pathologicalrole}"""

    arg1: str
    arg2: str


RELATION_DEFINITIONS: List[Type] = [
    NoRelation,
    UndefinedRelation,
    CausativeActivation,
    CausativeInhibition,
    CausativeMutation,
    AssociatedMutation,
    IncreasedExpression,
    DecreasedExpression,
    Dysregulation,
    EpigeneticMarker,
    ModulatorDecreaseDisease,
    ModulatorIncreaseDisease,
    GeneticSusceptibility,
    Biomarker,
    PrognosticIndicator,
    PositivePrognosticMarker,
    NegativePrognosticMarker,
    DiagnosticTool,
    TherapyResistance,
    TherapeuticTarget,
    PathologicalRole,
]

FINE_TO_COARSE_RELATIONS: Dict[Type, Type] = {_def: _def.__base__ for _def in RELATION_DEFINITIONS}
COARSE_TO_FINE_RELATIONS: Dict[Type, List[Type]] = {}
for fine, coarse in FINE_TO_COARSE_RELATIONS.items():
    if coarse not in COARSE_TO_FINE_RELATIONS:
        COARSE_TO_FINE_RELATIONS[coarse] = []
    COARSE_TO_FINE_RELATIONS[coarse].append(fine)

# __all__ = list(map(str, [*ENTITY_DEFINITIONS, *RELATION_DEFINITIONS, *EVENT_DEFINITIONS]))
