GUIDELINES = {
    "biotriplex_disease": {
        "en": [
            (
                "Refers to a specific human disease or disorder name or a shorthand name. Specifically, we consider"
                " any disease listed in the EMBL-EBI Human Disease Ontology."
            ),
        ]
    },
    "biotriplex_gene": {
        "en": [
            (
                "Refers to human gene names, symbols or synonyms, using \"GeneCards: The Human Gene Database\" as"
                " reference."
            ),
        ]
    },
    "biotriplex_genediseaserelation": {
        "en": [
            (
                "Refers to a relationship between a Gene and a Disease."
            )
        ]
    },
    "biotriplex_norelation": {
        "en": [
            (
                "Indicates that the text looked for a relationship between a gene and a disease, but found no evidence"
                " of one in the context of their experiment."
            )
        ]
    },
    "biotriplex_undefinedrelation": {
        "en": [
            (
                "Refers to a relationship between a gene and a disease that was found in the text, but the type of"
                " relationship was not specified."
            ),
        ],
    },
    "biotriplex_causativeactivation": {
        "en": [
            (
                "Indicates that activation of the gene causes/contributes to disease development."
            ),
          ]
      },
    "biotriplex_causativeinhibition": {
        "en": [
            (
                "Indicates inhibition of the gene causes/contributes to disease development."
            ),
          ]
      },
    "biotriplex_causativemutation": {
        "en": [
            (
                "Indicates that a mutation in a gene causes a disease."
            ),
        ]
    },
    "biotriplex_associatedmutation": {
        "en": [
            (
                "Indicates that a gene mutation is associated with a disease, but it is not known (or not stated in "
                "the text) whether the mutation has a causative or modulatory role."
            ),
        ]
    },
    "biotriplex_increasedexpression": {
        "en": [
            (
                "Refers to a gene expression (RNA or protein) being increased in the disease state above that normally "
                "expected in a given tissue or cell type."
            ),
        ]
    },
    "biotriplex_decreasedexpression": {
        "en": [
            (
                "Refers to a gene expression (RNA or protein) being decreased below that normally expected in a given"
                " tissue or cell type."
            ),
        ]
    },
    "biotriplex_dysregulation": {
        "en": [
            (
                "Refers to the gene's normal regulatory mechanisms being disrupted in the disease state."
            ),
        ]
    },
    "biotriplex_epigeneticmarker": {
        "en": [
            (
                "Refers to chemical modifications affecting gene activity without changing DNA sequence."
            ),
        ]
    },
    "biotriplex_modulatordecreasedisease": {
        "en": [
            (
                "Suggests the gene reduces disease severity",
            ),
        ]
    },
    "biotriplex_modulatorincreasedisease": {
        "en": [
            (
                "Suggests the gene contributes to disease progression."
            ),
        ]
    },
    "biotriplex_geneticsusceptibility": {
        "en": [
            (
                "Indicates the gene increases an individual's likelihood of developing a disease."
            ),
        ],
    },
    "biotriplex_biomarker": {
        "en": [
            (
                "Refers to a protein or RNA marker being associated with a particular disease."
            ),
        ],
    },
    "biotriplex_prognosticindicator": {
        "en": [
            (
                "Refers to a biomarker used for predicting the prognosis of a disease",
            ),
        ]
    },
    "biotriplex_negativeprognosticmarker": {
        "en": [
            (
                "Refers to a biomarker that indicates a negative prognosis for a disease."
            ),
        ]
    },
    "biotriplex_positiveprognosticmarker": {
        "en": [
            (
                "Refers to a biomarker that indicates a positive prognosis for a disease."
            ),
        ]
    },
    "biotriplex_diagnostictool": {
        "en": [
            (
                "Refers to the gene helping to identify or confirm disease presence."
            ),
        ],
    },
    "biotriplex_therapyresistance": {
        "en": [
            (
                "Refers to the gene potentially contributing to disease treatment ineffectiveness."
            ),
        ]
    },
    "biotriplex_therapeutictarget": {
        "en": [
            (
                "Indicates the gene could be or is currently a focus for disease treatment."
            )
        ]
    },
    "biotriplex_pathologicalrole": {
        "en": [
            (
                "Describes a gene's fundamental involvement in creating, maintaining, or progressing a disease state. "
                "Unlike other more specific relations, \"PathologicalRole\" is a broader term that indicates the gene "
                "plays a critical part in the disease process, but doesn't specify the exact mechanism."
            ),
        ]
    },
  }

EXAMPLES = {
    "biotriplex_disease_examples": {
        "en": [
            "SLC02A1",
            "PCSK5",
        ]
    },
    "biotriplex_gene_examples": {
        "en": [
            "lung adenocarcinoma",
            "coronary artery disease",
            "CHD",
            "ADHD",
        ]
    },
}
