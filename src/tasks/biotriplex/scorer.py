from typing import Dict, List, Type

from src.tasks.biotriplex.prompts import (
    COARSE_RELATION_DEFINITIONS,
    ENTITY_DEFINITIONS,
    RELATION_DEFINITIONS,
)
from src.tasks.utils_scorer import RelationScorer, SpanScorer
from src.tasks.utils_typing import Entity


class BiotriplexEntityScorer(SpanScorer):
    """Biotriplex Entity identification and classification scorer."""

    valid_types: List[Type] = ENTITY_DEFINITIONS

    def __call__(self, reference: List[Entity], predictions: List[Entity]) -> Dict[str, Dict[str, float]]:
        output = super().__call__(reference, predictions)
        return {"entities": output["spans"]}


class BiotriplexCoarseRelationScorer(RelationScorer):
    """Biotriplex Relation identification scorer."""

    valid_types: List[Type] = COARSE_RELATION_DEFINITIONS


class BiotriplexRelationScorer(RelationScorer):
    """Biotriplex Relation identification scorer."""

    valid_types: List[Type] = RELATION_DEFINITIONS
