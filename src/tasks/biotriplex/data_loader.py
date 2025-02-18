import inspect
import json
from typing import Tuple, Union

from src.tasks.biotriplex.guidelines import GUIDELINES
from src.tasks.biotriplex.guidelines_gold import EXAMPLES
from src.tasks.biotriplex.prompts import (
    COARSE_RELATION_DEFINITIONS,
    COARSE_TO_FINE_RELATIONS,
    ENTITY_DEFINITIONS,
    FINE_TO_COARSE_RELATIONS,
    RELATION_DEFINITIONS,
    Gene,
    Disease,
    GeneDiseaseRelation,
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
    NegativePrognosticMarker,
    PositivePrognosticMarker,
    DiagnosticTool,
    TherapyResistance,
    TherapeuticTarget,
    PathologicalRole,
)
from src.tasks.biotriplex.nerrel_dataset import BioTriplexNERRELDataset, biotriplex_nerrel_dataset
from ..utils_data import DatasetLoader, Sampler


class BiotriplexDatasetLoader(DatasetLoader):
    """
    A `DatasetLoader` for the Biotriplex dataset.

    Args:
        split (`str`):
            The split mode to load the dataset. It must be one of the following: "train", "val",
            "test".

    Raises:
        `ValueError`:
            raised when a not defined value found.
    """

    ENTITY_TO_CLASS_MAPPING = {
        "GENE": Gene,
        "DISEASE": Disease,
    }

    RELATION_TO_CLASS_MAPPING = {
        "pathological role": (GeneDiseaseRelation, PathologicalRole),
        "causative activation": (GeneDiseaseRelation, CausativeActivation),
        "causative inhibition": (GeneDiseaseRelation, CausativeInhibition),
        "causative mutation": (GeneDiseaseRelation, CausativeMutation),
        "modulator decrease disease": (GeneDiseaseRelation, ModulatorDecreaseDisease),
        "modulator increase disease": (GeneDiseaseRelation, ModulatorIncreaseDisease),
        "biomarker": (GeneDiseaseRelation, Biomarker),
        "associated mutation": (GeneDiseaseRelation, AssociatedMutation),
        "dysregulation": (GeneDiseaseRelation, Dysregulation),
        "increased expression": (GeneDiseaseRelation, IncreasedExpression),
        "decreased expression": (GeneDiseaseRelation, DecreasedExpression),
        "epigenetic marker": (GeneDiseaseRelation, EpigeneticMarker),
        "therapy resistance": (GeneDiseaseRelation, TherapyResistance),
        "prognostic indicator": (GeneDiseaseRelation, PrognosticIndicator),
        "negative prognostic marker": (GeneDiseaseRelation, NegativePrognosticMarker),
        "positive prognostic marker": (GeneDiseaseRelation, PositivePrognosticMarker),
        "therapeutic target": (GeneDiseaseRelation, TherapeuticTarget),
        "diagnostic tool": (GeneDiseaseRelation, DiagnosticTool),
        "genetic susceptibility": (GeneDiseaseRelation, GeneticSusceptibility),
        "no relation": (GeneDiseaseRelation, NoRelation),
        "relation undefined": (GeneDiseaseRelation, UndefinedRelation),
    }

    def __init__(self, split, **kwargs) -> None:

        if split in ["training", "train"]:
            split = "train"
        elif split in ["validation", "val", "dev", "validating"]:
            split = "val"
        elif split in ["testing", "test"]:
            split = "test"
        else:
            raise ValueError(f"Mode {split} not found!")
        self.elements = {}
        dataset_config = biotriplex_nerrel_dataset
        dataset_config.use_entity_tokens_as_targets = False
        dataset = BioTriplexNERRELDataset(dataset_config, split, max_words=None,)

        for item in dataset.data:
            key = item["doc_key"]
            text = item["input"]
            entities = json.loads(item["entities_json"])
            entities = [
                self.ENTITY_TO_CLASS_MAPPING[entity["entity_type"]](span=entity["span"])
                for entity in entities
                if entity["entity_type"] in self.ENTITY_TO_CLASS_MAPPING
            ]
            relations = json.loads(item["relations_json"])
            coarse_relations, fine_relations = [], []
            for rel in relations:
                if rel["relation"] not in self.RELATION_TO_CLASS_MAPPING:
                    raise ValueError(f"Relation {rel['relation']} not found!")
                coarse_relations.append(
                    self.RELATION_TO_CLASS_MAPPING[rel["relation"]][0](
                        arg1=rel["gene"],
                        arg2=rel["disease"],
                    )
                )
                fine_relations.append(
                    self.RELATION_TO_CLASS_MAPPING[rel["relation"]][-1](
                        arg1=rel["gene"],
                        arg2=rel["disease"],
                    )
                )
            self.elements[key] = {
                "id": key,
                "doc_id": key,
                "text": text,
                "entities": entities,
                "coarse_relations": coarse_relations,
                "relations": fine_relations,
                "gold": [],
            }


class BiotriplexSampler(Sampler):
    """
    A data `Sampler` for the Biotriplex dataset.

    Args:
        dataset_loader (`BiotriplexDatasetLoader`):
            The dataset loader that contains the data information.
        task (`str`, optional):
            The task to sample. It must be one of the following: NER, VER, RE, EE.
            Defaults to `None`.
        split (`str`, optional):
            The split to sample. It must be one of the following: "train", "dev" or
            "test". Depending on the split the sampling strategy differs. Defaults to
            `"train"`.
        parallel_instances (`Union[int, Tuple[int, int]]`, optional):
            The number of sentences sampled in parallel. Options:

                * **`int`**: The amount of elements that will be sampled in parallel.
                * **`tuple`**: The range of elements that will be sampled in parallel.

            Defaults to 1.
        max_guidelines (`int`, optional):
            The number of guidelines to append to the example at the same time. If `-1`
            is given then all the guidelines are appended. Defaults to `-1`.
        guideline_dropout (`float`, optional):
            The probability to dropout a guideline definition for the given example. This
            is only applied on training. Defaults to `0.0`.
        seed (`float`, optional):
            The seed to sample the examples. Defaults to `0`.
        prompt_template (`str`, optional):
            The path to the prompt template. Defaults to `"templates/prompt.txt"`.
        ensure_positives_on_train (bool, optional):
            Whether to ensure that the guidelines of annotated examples are not removed.
            Defaults to `False`.
        dataset_name (str, optional):
            The name of the dataset. Defaults to `None`.
        scorer (`str`, optional):
           The scorer class import string. Defaults to `None`.
        sample_only_gold_guidelines (`bool`, optional):
            Whether to sample only guidelines of present annotations. Defaults to `False`.
        is_end_to_end (`bool`, optional):
            Whether or not perform the task in end to end fashion. Defaults to `False`.
    """

    def __init__(
        self,
        dataset_loader: BiotriplexDatasetLoader,
        task: str = None,
        split: str = "train",
        parallel_instances: Union[int, Tuple[int, int]] = 1,
        max_guidelines: int = -1,
        guideline_dropout: float = 0.0,
        seed: float = 0,
        ensure_positives_on_train: bool = False,
        dataset_name: str = None,
        scorer: str = None,
        sample_only_gold_guidelines: bool = False,
        is_end_to_end: bool = False,
        **kwargs,
    ) -> None:
        assert task in [
            "NER",
            "RE",
            "RC",
        ], f"{task} must be either 'NER', 'RE', 'RC'."

        task_definitions, task_target, task_template = {
            "NER": (ENTITY_DEFINITIONS, "entities", "templates/prompt.txt"),
            "RE": (COARSE_RELATION_DEFINITIONS, "coarse_relations", "templates/prompt_ace_re.txt"),
            "RC": (
                RELATION_DEFINITIONS,
                "relations",
                "templates/prompt_ace_rc.txt" if not is_end_to_end else "templates/prompt_ace_re.txt",
            ),
        }[task]

        if task in ["RC",]:
            is_coarse_to_fine: bool = True
            COARSE_TO_FINE = COARSE_TO_FINE_RELATIONS
            FINE_TO_COARSE = FINE_TO_COARSE_RELATIONS
        else:
            is_coarse_to_fine = False
            COARSE_TO_FINE = None
            FINE_TO_COARSE = None

        kwargs.pop("prompt_template")

        super().__init__(
            dataset_loader=dataset_loader,
            task=task,
            split=split,
            parallel_instances=parallel_instances,
            max_guidelines=max_guidelines,
            guideline_dropout=guideline_dropout,
            seed=seed,
            prompt_template=task_template,
            ensure_positives_on_train=ensure_positives_on_train,
            sample_only_gold_guidelines=sample_only_gold_guidelines,
            dataset_name=dataset_name,
            scorer=scorer,
            task_definitions=task_definitions,
            task_target=task_target,
            is_coarse_to_fine=is_coarse_to_fine,
            is_end_to_end=is_end_to_end,
            coarse_to_fine=COARSE_TO_FINE,
            fine_to_coarse=FINE_TO_COARSE,
            definitions=GUIDELINES,
            examples=EXAMPLES,
            **kwargs,
        )

