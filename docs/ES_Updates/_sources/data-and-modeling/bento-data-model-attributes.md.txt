# Bento TailoRx Model Attributes


## Document Conventions
Descriptors for each attribute:
<br>a. **Attribute Name**: name of the attribute
<br>b. **Definition**: a concise description of the attribute. Attribute definitions have been developed by the BENTO\_TAILORx data team and are specific to the BENTO\_TAILORx data model.
<br>c. **Attribute Of Node/Relationship**: the parent node or relationship type of attribute.
<br>d. **Required**: a true/false label that indicates if attribute is a required field for data submitters.
<br>e. **Type**: the data type of the attribute (string, integer, number, boolean).
<br>f. **Constraints**: rules enforced on attribute values.
<br>g. **Enumeration**: If applicable, the list of possible values for the attribute.


## Attributes

<br>Attribute Name: institution\_id
<br>Description: A unique id assigned by the data commons to the institution.
<br>Attribute of Node: institution
<br>Required: true
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: institution\_name
<br>Description: The name of the institution in charge of conducting the clinical or research program.
<br>Attribute of Node: institution
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: institution\_url
<br>Description: The institute URL.
<br>Attribute of Node: institution
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: institution\_acronymn
<br>Description: Official acronymn of the institute as it should be displayed on the UI.
<br>Attribute of Node: institution
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: program\_id
<br>Description: A unique id assigned by the data commons to the program.
<br>Attribute of Node: program
<br>Required: true
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: program\_name
<br>Description: Full name/title of the program.
<br>Attribute of Node: program
<br>Required: true
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: program\_acronym
<br>Description: Official acronym for the name of the program as it should be displayed within the UI.
<br>Attribute of Node: program
<br>Required: true
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: program\_full\_description
<br>Description: Full length (multiple sentence) version of the program description.
<br>Attribute of Node: program
<br>Required: true
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: program\_external\_url
<br>Description: External url to which users should be directed to learn more about the program.
<br>Attribute of Node: program
<br>Required: true
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: program\_short\_description
<br>Description: Abbreviated (single sentence) version of the program description.
<br>Attribute of Node: program
<br>Required: true
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: date\_of\_approval
<br>Description: If applicable, date upon which study was approved.
<br>Attribute of Node: program, project, study
<br>Required: false
<br>Type: datetime
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: start\_date
<br>Description: Start date of the study.
<br>Attribute of Node: program, project, study
<br>Required: false
<br>Type: datetime
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: end\_date
<br>Description: End date of the study.
<br>Attribute of Node: program, project, study
<br>Required: false
<br>Type: datetime
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: embargo\_date
<br>Description: Specifies the embargo date, i.e., the release of information with the condition that it cannot be published or disseminated before a certain date.
<br>Attribute of Node: program, project, study
<br>Required: false
<br>Type: datetime
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: index\_date
<br>Description: The text term used to describe the reference or anchor date used when for date obfuscation, where a single date is obscured by creating one or more date ranges in relation to this date.
<br>Attribute of Node: program, project, study, study\_subject
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Diagnosis", "First Patient Visit", "First Treatment", "Initial Genomic Sequencing", "Sample Procurement", "Study Enrollment"

<br>Attribute Name: dbgap\_accession\_number
<br>Description: The dbgap accession number provided for the study.
<br>Attribute of Node: program, project, study
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: sponsor
<br>Description: Funding agency.
<br>Attribute of Node: program
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: program\_sort\_order
<br>Description: Value upon which to arbitrarily prioritize display of the program within the UI.
<br>Attribute of Node: program
<br>Required: false
<br>Type: integer
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: state
<br>Description: The possible states a study can be in.  All but `open` are equivalent to some type of locked state.
<br>Attribute of Node: program, project, study
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "open", "review", "submitted", "processing", "processed", "closed", "legacy"

<br>Attribute Name: in\_review
<br>Description: Indicates that the study is under review by the submitter. Upload and data modification is disabled.
<br>Attribute of Node: program, project, study
<br>Required: false
<br>Type: boolean
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: is\_legacy
<br>Description: Indicates whether a study will appear in the Legacy Archive.
<br>Attribute of Node: program, project, study
<br>Required: false
<br>Type: boolean
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: pubmed\_id
<br>Description: PubMed ID of the primary publication associated with project.
<br>Attribute of Node: program
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: intended\_release\_date
<br>Description: Tracks a study's intended release date.
<br>Attribute of Node: program, project, study
<br>Required: false
<br>Type: datetime
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: program\_manager
<br>Description: Name of the program manager from the sponsoring agency.
<br>Attribute of Node: program
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: release\_requested
<br>Description: User requests that the data commons release the study. Release can only be requested if the study is releasable.
<br>Attribute of Node: program, project, study
<br>Required: false
<br>Type: boolean
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: released
<br>Description: To release a study is to tell the data commons to include all submitted entities in the next data commons index.
<br>Attribute of Node: program, project, study
<br>Required: false
<br>Type: boolean
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: releasable
<br>Description: A study can only be released by the user when `releasable` is true.
<br>Attribute of Node: program, project, study
<br>Required: false
<br>Type: boolean
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: request\_submission
<br>Description: Indicates that the user has requested submission to the data commons for harmonization.
<br>Attribute of Node: program, project, study
<br>Required: false
<br>Type: boolean
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: submission\_enabled
<br>Description: Indicates if submission to a study is allowed.
<br>Attribute of Node: program, project, study
<br>Required: false
<br>Type: boolean
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: project\_id
<br>Description: A unique id assigned by the data commons to the project.
<br>Attribute of Node: project
<br>Required: true
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: project\_name
<br>Description: Full name/title of the project.
<br>Attribute of Node: project
<br>Required: true
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: project\_acronym
<br>Description: Official acronym for the name of the project as it should be displayed within the UI.
<br>Attribute of Node: project
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: project\_full\_description
<br>Description: Full length (multiple sentence) version of the project description.
<br>Attribute of Node: project
<br>Required: true
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: project\_external\_url
<br>Description: External url to which users should be directed to learn more about the project.
<br>Attribute of Node: project
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: project\_short\_description
<br>Description: Abbreviated (single sentence) version of the project description.
<br>Attribute of Node: project
<br>Required: true
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: project\_type
<br>Description: Arbitrary designation of the project to indicate its underlying nature, eg, genomics, proteomics, transcriptomics project, etc.
<br>Attribute of Node: project
<br>Required: true
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: primary\_site
<br>Description: The text term used to describe the general location of the malignant disease, as categorized by the World Health Organization's (WHO) International Classification of Diseases for Oncology (ICD-O).
<br>Attribute of Node: project, study, study\_subject
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Accessory sinuses", "Adrenal gland", "Anus and anal canal", "Base of tongue", "Bladder", "Bones, joints and articular cartilage of limbs", "Bones, joints and articular cartilage of other and unspecified sites", "Brain", "Breast", "Bronchus and lung", "Cervix uteri", "Colon", "Connective, subcutaneous and other soft tissues", "Corpus uteri", "Esophagus", "Eye and adnexa", "Floor of mouth", "Gallbladder", "Gum", "Heart, mediastinum, and pleura", "Hematopoietic and reticuloendothelial systems", "Hypopharynx", "Kidney", "Larynx", "Lip", "Liver and intrahepatic bile ducts", "Lymph nodes", "Meninges", "Nasal cavity and middle ear", "Nasopharynx", "Oropharynx", "Other and ill-defined digestive organs", "Other and ill-defined sites", "Other and ill-defined sites in lip, oral cavity and pharynx", "Other and ill-defined sites within respiratory system and intrathoracic organs", "Other and unspecified female genital organs", "Other and unspecified major salivary glands", "Other and unspecified male genital organs", "Other and unspecified parts of biliary tract", "Other and unspecified parts of mouth", "Other and unspecified parts of tongue", "Other and unspecified urinary organs", "Other endocrine glands and related structures", "Ovary", "Palate", "Pancreas", "Parotid gland", "Penis", "Peripheral nerves and autonomic nervous system", "Placenta", "Prostate gland", "Pyriform sinus", "Rectosigmoid junction", "Rectum", "Renal pelvis", "Retroperitoneum and peritoneum", "Skin", "Small intestine", "Spinal cord, cranial nerves, and other parts of central nervous system", "Stomach", "Testis", "Thymus", "Thyroid gland", "Tonsil", "Trachea", "Ureter", "Uterus, NOS", "Vagina", "Vulva", "Unknown", "Not Reported", "Adrenal Gland", "Bile Duct", "Blood", "Bone", "Bone Marrow", "Cervix", "Colorectal", "Eye", "Head and Neck", "Liver", "Lung", "Lymph Nodes", "Nervous System", "Not Applicable", "Pleura", "Prostate", "Soft Tissue", "Thyroid", "Uterus"

<br>Attribute Name: project\_manager
<br>Description: Name of the project manager.
<br>Attribute of Node: project
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: project\_sort\_order
<br>Description: Value upon which to arbitrarily prioritize display of the project within the UI.
<br>Attribute of Node: project
<br>Required: false
<br>Type: integer
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: acquisition\_type
<br>Description: The modes of acquisition used in study- data dependent acquisition (DDA), data independent acquisition (DIA). Relevant for proteomic studies.
<br>Attribute of Node: project, study
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: analytical\_fraction
<br>Description: Type of analyte being processed/examined.
<br>Attribute of Node: project, study
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: cross\_reference\_database\_id
<br>Description: A unique id assigned by the data commons to  the data repository that cross-references study subject.
<br>Attribute of Node: cross\_reference\_database
<br>Required: true
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: cross\_reference\_database\_name
<br>Description: Name of the data repository that cross-references the study subject.
<br>Attribute of Node: cross\_reference\_database
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: cross\_reference\_database\_url
<br>Description: The URL of the data repository that cross-references study subject.
<br>Attribute of Node: cross\_reference\_database
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: study\_id
<br>Description: A unique id assigned by the data commons to the study by the data commons.
<br>Attribute of Node: study
<br>Required: true
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: study\_name
<br>Description: Full name/title of the study.
<br>Attribute of Node: study
<br>Required: true
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: study\_acronym
<br>Description: Official acronym for the name of the study as it should be displayed within the UI.
<br>Attribute of Node: study
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: study\_full\_description
<br>Description: Full length (multiple sentence) version of the study description.
<br>Attribute of Node: study
<br>Required: true
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: study\_short\_description
<br>Description: Abbreviated (single sentence) version of the study description.
<br>Attribute of Node: study
<br>Required: true
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: study\_type
<br>Description: Arbitrary designation of the study to indicate its underlying nature, e.g. clinical trial, transcriptomics study, etc.
<br>Attribute of Node: study
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: study\_external\_url
<br>Description: External url to which users should be directed to learn more about the study.
<br>Attribute of Node: study
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: study\_manager
<br>Description: Name of the study manager.
<br>Attribute of Node: study
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: study\_sort\_order
<br>Description: Value upon which to arbitrarily prioritize display of the study within the UI.
<br>Attribute of Node: study
<br>Required: false
<br>Type: integer
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: study\_subject\_id
<br>Description: A unique id assigned by the data commons to the study subject.
<br>Attribute of Node: study\_subject
<br>Required: true
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: study\_subject\_source\_id
<br>Description: ID by which data owner can uniquely identify a specific study subject, at least within a single study/trial, maintained exactly in the submitter's format. This may or may not be globally unique.
<br>Attribute of Node: study\_subject
<br>Required: true
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: consent\_type
<br>Description: The text term used to describe the type of consent obtain from the subject for participation in the study.
<br>Attribute of Node: study\_subject
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: lost\_to\_followup
<br>Description: The yes/no/unknown indicator used to describe whether a study subject was unable to be contacted or seen for follow-up information.
<br>Attribute of Node: study\_subject
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Yes", "No", "Unknown"

<br>Attribute Name: status
<br>Description: Specifies if the aliquot is qualified or disqualified for any reason. Usually the data releated to such aliquots are not used in the data analysis.
<br>Attribute of Node: study\_subject, aliquot
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Qualified", "Disqualified"

<br>Attribute Name: disease\_type
<br>Description: The text term used to describe the type of malignant disease, as categorized by the World Health Organization's (WHO) International Classification of Diseases for Oncology (ICD-O).
<br>Attribute of Node: study\_subject
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Acinar Cell Neoplasms", "Adenomas and Adenocarcinomas", "Adnexal and Skin Appendage Neoplasms", "Basal Cell Neoplasms", "Blood Vessel Tumors", "Chronic Myeloproliferative Disorders", "Complex Epithelial Neoplasms", "Complex Mixed and Stromal Neoplasms", "Cystic, Mucinous and Serous Neoplasms", "Ductal and Lobular Neoplasms", "Epithelial Neoplasms, NOS", "Fibroepithelial Neoplasms", "Fibromatous Neoplasms", "Germ Cell Neoplasms", "Giant Cell Tumors", "Gliomas", "Granular Cell Tumors and Alveolar Soft Part Sarcomas", "Hodgkin Lymphoma", "Immunoproliferative Diseases", "Leukemias, NOS", "Lipomatous Neoplasms", "Lymphatic Vessel Tumors", "Lymphoid Leukemias", "Malignant Lymphomas, NOS or Diffuse", "Mast Cell Tumors", "Mature B-Cell Lymphomas", "Mature T- and NK-Cell Lymphomas", "Meningiomas", "Mesonephromas", "Mesothelial Neoplasms", "Miscellaneous Bone Tumors", "Miscellaneous Tumors", "Mucoepidermoid Neoplasms", "Myelodysplastic Syndromes", "Myeloid Leukemias", "Myomatous Neoplasms", "Myxomatous Neoplasms", "Neoplasms, NOS", "Neoplasms of Histiocytes and Accessory Lymphoid Cells", "Nerve Sheath Tumors", "Neuroepitheliomatous Neoplasms", "Nevi and Melanomas", "Odontogenic Tumors", "Osseous and Chondromatous Neoplasms", "Other Hematologic Disorders", "Other Leukemias", "Paragangliomas and Glomus Tumors", "Plasma Cell Tumors", "Precursor Cell Lymphoblastic Lymphoma", "Soft Tissue Tumors and Sarcomas, NOS", "Specialized Gonadal Neoplasms", "Squamous Cell Neoplasms", "Synovial-like Neoplasms", "Thymic Epithelial Neoplasms", "Transitional Cell Papillomas and Carcinomas", "Trophoblastic neoplasms", "Unknown", "Not Reported", "Not Applicable", "Acute Lymphoblastic Leukemia", "Acute Myeloid Leukemia", "Adrenocortical Carcinoma", "Bladder Urothelial Carcinoma", "Brain Lower Grade Glioma", "Breast Invasive Carcinoma", "Burkitt Lymphoma", "Cervical Squamous Cell Carcinoma and Endocervical Adenocarcinoma", "Cholangiocarcinoma", "Chronic Lymphocytic Leukemia", "Clear Cell Sarcoma of the Kidney", "Colon Adenocarcinoma", "Esophageal Carcinoma", "Glioblastoma Multiforme", "Head and Neck Squamous Cell Carcinoma", "High-Risk Wilms Tumor", "HIV+ Tumor Molecular Characterization Project - Cervical Cancer", "HIV+ Tumor Molecular Characterization Project - Lung Cancer", "Kidney Chromophobe", "Kidney Renal Clear Cell Carcinoma", "Kidney Renal Papillary Cell Carcinoma", "Liver Hepatocellular Carcinoma", "Lung Adenocarcinoma", "Lung Squamous Cell Carcinoma", "Lymphoid Neoplasm Diffuse Large B-cell Lymphoma", "Mesothelioma", "Multiple Myeloma", "Neuroblastoma", "Osteosarcoma", "Ovarian Serous Cystadenocarcinoma", "Pancreatic Adenocarcinoma", "Pheochromocytoma and Paraganglioma", "Prostate Adenocarcinoma", "Rectum Adenocarcinoma", "Rhabdoid Tumor", "Sarcoma", "Skin Cutaneous Melanoma", "Stomach Adenocarcinoma", "Testicular Germ Cell Tumors", "Thymoma", "Thyroid Carcinoma", "Uterine Carcinosarcoma", "Uterine Corpus Endometrial Carcinoma", "Uveal Melanoma"

<br>Attribute Name: disease\_subtype
<br>Description: A more granular classification of disease type.
<br>Attribute of Node: study\_subject
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Infiltrating Ductal Carcinoma", "Infiltrating Lobular Carcinoma", "Infiltrating Ductal & Lobular Carcinoma", "Medullary Carcinoma", "Mucinous (colloid) Carcinoma", "Comedocarcinoma", "Paget's Disease", "Papillary Carcinoma", "Tubular Carcinoma", "Adenocarcinoma", "Carcinoma, NOS", "Not Reported"

<br>Attribute Name: taxon
<br>Description: A taxonomic group, such as a species that study\_subject belongs to.
<br>Attribute of Node: study\_subject
<br>Required: true
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: in\_analysis
<br>Description: Indicator variable of whether the patient was in the primary analysis set for the publication.
<br>Attribute of Node: study\_subject
<br>Required: false
<br>Type: boolean
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: case\_report\_form\_submitted
<br>Description: Indicator variable of whether the TAILORx On-Study case report form (baseline data) was submitted.
<br>Attribute of Node: study\_subject
<br>Required: false
<br>Type: boolean
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: consent\_withdrawn
<br>Description: Indicator of whether patient withdrew consent for further follow-up
<br>Attribute of Node: study\_subject
<br>Required: false
<br>Type: boolean
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: study\_subject\_first\_name
<br>Description: Study subject's first name, in full.
<br>Attribute of Node: study\_subject
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: study\_subject\_is\_ref
<br>Description: A biospecimen entity which is used as a reference sample for determining relative protein abundances in labeling experiments.
<br>Attribute of Node: study\_subject
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: days\_to\_consent
<br>Description: Number of days between the date used for index and the date the subject consent was obtained for participation in the study.
<br>Attribute of Node: study\_subject
<br>Required: false
<br>Type: integer
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: days\_to\_lost\_to\_followup
<br>Description: The number of days between the date used for index and to the date the study subject was lost to follow-up.
<br>Attribute of Node: study\_subject
<br>Required: false
<br>Type: integer
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: pool
<br>Description: Any biospecimen entity where multiple cases, samples or aliquots are combined to produce a reference. Sample pooling is commonly used for determining relative protein abundances in labeling experiments.
<br>Attribute of Node: study\_subject, sample, aliquot
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: sample\_id
<br>Description: A unique id assigned by the data commons to the sample.
<br>Attribute of Node: sample
<br>Required: true
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: tissue\_type
<br>Description: Text term that represents a description of the kind of tissue collected with respect to disease status or proximity to tumor tissue.
<br>Attribute of Node: sample
<br>Required: true
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Tumor", "Normal", "Abnormal", "Peritumoral", "Unknown", "Not Reported", "Not Allowed To Collect"

<br>Attribute Name: sample\_type
<br>Description: Text term to describe the source of a sample used for a laboratory test.
<br>Attribute of Node: sample
<br>Required: true
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Additional Metastatic", "Additional - New Primary", "Benign Neoplasms", "Blood Derived Cancer - Bone Marrow", "Blood Derived Cancer - Bone Marrow, Post-treatment", "Blood Derived Cancer - Peripheral Blood", "Blood Derived Cancer - Peripheral Blood, Post-treatment", "Blood Derived Liquid Biopsy", "Blood Derived Normal", "Bone Marrow Normal", "Buccal Cell Normal", "Cell Line Derived Xenograft Tissue", "Cell Lines", "Control Analyte", "DNA", "EBV Immortalized Normal", "Expanded Next Generation Cancer Model", "FFPE Recurrent", "FFPE Scrolls", "Fibroblasts from Bone Marrow Normal", "GenomePlex (Rubicon) Amplified DNA", "Granulocytes", "Human Tumor Original Cells", "In Situ Neoplasms", "Lymphoid Normal", "Metastatic", "Mononuclear Cells from Bone Marrow Normal", "Neoplasms of Uncertain and Unknown Behavior", "Next Generation Cancer Model", "Primary Blood Derived Cancer - Peripheral Blood", "Recurrent Blood Derived Cancer - Peripheral Blood", "Pleural Effusion", "Primary Blood Derived Cancer - Bone Marrow", "Primary Tumor", "Primary Xenograft Tissue", "Post neo-adjuvant therapy", "Recurrent Blood Derived Cancer - Bone Marrow", "Recurrent Tumor", "Repli-G (Qiagen) DNA", "Repli-G X (Qiagen) DNA", "RNA", "Slides", "Solid Tissue Normal", "Total RNA", "Tumor Adjacent Normal - Post Neo-adjuvant Therapy", "Tumor", "Xenograft Tissue", "Unknown", "Not Reported", "Not Allowed To Collect"

<br>Attribute Name: composition
<br>Description: Text term that represents the cellular composition of the sample.
<br>Attribute of Node: sample
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "2D Classical Conditionally Reprogrammed Cells", "2D Modified Conditionally Reprogrammed Cells", "3D Organoid", "3D Air-Liquid Interface Organoid", "3D Neurosphere", "Adherent Cell Line", "Buccal Cells", "Buffy Coat", "Bone Marrow Components", "Bone Marrow Components NOS", "Control Analyte", "Cell", "Derived Cell Line", "EBV Immortalized", "Fibroblasts from Bone Marrow Normal", "Granulocytes", "Human Original Cells", "Liquid Suspension Cell Line", "Lymphocytes", "Mononuclear Cells from Bone Marrow Normal", "Peripheral Blood Components NOS", "Pleural Effusion", "Plasma", "Peripheral Whole Blood", "Serum", "Saliva", "Sputum", "Solid Tissue", "Sorted Cells", "Whole Bone Marrow", "Unknown", "Not Reported", "Not Allowed To Collect"

<br>Attribute Name: method\_of\_sample\_procurement
<br>Description: The method used to procure the sample used to extract analyte(s).
<br>Attribute of Node: sample
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Abdomino-perineal Resection of Rectum", "Anterior Resection of Rectum", "Ascites Drainage", "Aspirate", "Autopsy", "Biopsy", "Blood Draw", "Bone Marrow Aspirate", "Core Biopsy", "Cystectomy", "Endo Rectal Tumor Resection", "Endoscopic Biopsy", "Endoscopic Mucosal Resection (EMR)", "Enucleation", "Excisional Biopsy", "Fine Needle Aspiration", "Full Hysterectomy", "Gross Total Resection", "Hand Assisted Laparoscopic Radical Nephrectomy", "Hysterectomy NOS", "Incisional Biopsy", "Indeterminant", "Laparoscopic Biopsy", "Laparoscopic Partial Nephrectomy", "Laparoscopic Radical Nephrectomy", "Laparoscopic Radical Prostatectomy with Robotics", "Laparoscopic Radical Prostatectomy without Robotics", "Left Hemicolectomy", "Liquid Biopsy", "Lobectomy", "Local Resection (Exoresection; wall resection)", "Lumpectomy", "Lymphadenectomy", "Metastasectomy", "Modified Radical Mastectomy", "Needle Biopsy", "Omentectomy", "Oophorectomy", "Open Craniotomy", "Open Partial Nephrectomy", "Open Radical Nephrectomy", "Open Radical Prostatectomy", "Orchiectomy", "Other", "Other Surgical Resection", "Pan-Procto Colectomy", "Pancreatectomy", "Paracentesis", "Partial Hepatectomy", "Peritoneal Lavage", "Pneumonectomy", "Punch Biopsy", "Radical Hysterectomy", "Right Hemicolectomy", "Salpingectomy", "Salpingo-oophorectomy", "Sigmoid Colectomy", "Simple Hysterectomy", "Simple Mastectomy", "Subtotal Resection", "Supracervical Hysterectomy", "Surgical Resection", "Thoracentesis", "Thoracoscopic Biopsy", "Total Colectomy", "Total Hepatectomy", "Total Mastectomy", "Transplant", "Transurethral resection (TURBT)", "Transverse Colectomy", "Tumor Debulking", "Tumor Resection", "Wedge Resection", "Whipple Procedure", "Unknown", "Not Reported", "Not Allowed To Collect"

<br>Attribute Name: sample\_type\_id
<br>Description: The accompanying sample type id for the sample type.
<br>Attribute of Node: sample
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "20", "30", "31", "32", "40", "41", "42", "50", "60", "61", "85", "86", "99"

<br>Attribute Name: total\_tissue\_area
<br>Description: The total area of a tissue sample.
<br>Attribute of Node: sample
<br>Required: false
<br>Type: number
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: passage\_count
<br>Description: Number of passages (splits) between the original tissue and this model.
<br>Attribute of Node: sample
<br>Required: false
<br>Type: integer
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: sample\_anatomic\_site
<br>Description: Text term that represents the name of the primary disease site of the submitted tumor sample.
<br>Attribute of Node: sample
<br>Required: true
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Abdomen", "Abdominal Wall", "Acetabulum", "Adenoid", "Adipose", "Adrenal", "Alveolar Ridge", "Amniotic Fluid", "Ampulla Of Vater", "Anal Sphincter", "Ankle", "Anorectum", "Antecubital Fossa", "Antrum", "Anus", "Aorta", "Aortic Body", "Appendix", "Aqueous Fluid", "Arm", "Artery", "Ascending Colon", "Ascending Colon Hepatic Flexure", "Auditory Canal", "Autonomic Nervous System", "Axilla", "Back", "Bile Duct", "Bladder", "Blood", "Blood Vessel", "Bone", "Bone Marrow", "Bowel", "Brain", "Brain Stem", "Breast", "Broad Ligament", "Bronchiole", "Bronchus", "Brow", "Buccal Cavity", "Buccal Mucosa", "Buttock", "Calf", "Capillary", "Cardia", "Carina", "Carotid Artery", "Carotid Body", "Cartilage", "Cecum", "Cell-Line", "Central Nervous System", "Cerebellum", "Cerebral Cortex", "Cerebrospinal Fluid", "Cerebrum", "Cervical Spine", "Cervix", "Chest", "Chest Wall", "Chin", "Clavicle", "Clitoris", "Colon", "Colon - Mucosa Only", "Common Duct", "Conjunctiva", "Connective Tissue", "Dermal", "Descending Colon", "Diaphragm", "Duodenum", "Ear", "Ear Canal", "Ear, Pinna (External)", "Effusion", "Elbow", "Endocrine Gland", "Epididymis", "Epidural Space", "Esophageal; Distal", "Esophageal; Mid", "Esophageal; Proximal", "Esophagogastric Junction", "Esophagus", "Esophagus - Mucosa Only", "Eye", "Fallopian Tube", "Femoral Artery", "Femoral Vein", "Femur", "Fibroblasts", "Fibula", "Finger", "Floor Of Mouth", "Fluid", "Foot", "Forearm", "Forehead", "Foreskin", "Frontal Cortex", "Frontal Lobe", "Fundus Of Stomach", "Gallbladder", "Ganglia", "Gastroesophageal Junction", "Gastrointestinal Tract", "Groin", "Gum", "Hand", "Hard Palate", "Head & Neck", "Head - Face Or Neck, Nos", "Heart", "Hepatic", "Hepatic Duct", "Hepatic Flexure", "Hepatic Vein", "Hip", "Hippocampus", "Humerus", "Hypopharynx", "Ileum", "Ilium", "Index Finger", "Ischium", "Islet Cells", "Jaw", "Jejunum", "Joint", "Kidney", "Knee", "Lacrimal Gland", "Large Bowel", "Laryngopharynx", "Larynx", "Leg", "Leptomeninges", "Ligament", "Lip", "Liver", "Lumbar Spine", "Lung", "Lymph Node", "Lymph Node(s) Axilla", "Lymph Node(s) Cervical", "Lymph Node(s) Distant", "Lymph Node(s) Epitrochlear", "Lymph Node(s) Femoral", "Lymph Node(s) Hilar", "Lymph Node(s) Iliac-Common", "Lymph Node(s) Iliac-External", "Lymph Node(s) Inguinal", "Lymph Node(s) Internal Mammary", "Lymph Node(s) Mammary", "Lymph Node(s) Mesenteric", "Lymph Node(s) Occipital", "Lymph Node(s) Paraaortic", "Lymph Node(s) Parotid", "Lymph Node(s) Pelvic", "Lymph Node(s) Popliteal", "Lymph Node(s) Regional", "Lymph Node(s) Retroperitoneal", "Lymph Node(s) Scalene", "Lymph Node(s) Splenic", "Lymph Node(s) Subclavicular", "Lymph Node(s) Submandibular", "Lymph Node(s) Supraclavicular", "Lymph Nodes(s) Mediastinal", "Mandible", "Maxilla", "Mediastinal Soft Tissue", "Mediastinum", "Mesentery", "Mesothelium", "Middle Finger", "Mitochondria", "Muscle", "Nails", "Nasal Cavity", "Nasal Soft Tissue", "Nasopharynx", "Neck", "Nerve", "Nerve(s) Cranial", "Occipital Cortex", "Ocular Orbits", "Omentum", "Oral Cavity", "Oral Cavity - Mucosa Only", "Oropharynx", "Other", "Ovary", "Palate", "Pancreas", "Paraspinal Ganglion", "Parathyroid", "Parotid Gland", "Patella", "Pelvis", "Penis", "Pericardium", "Periorbital Soft Tissue", "Peritoneal Cavity", "Peritoneum", "Pharynx", "Pineal", "Pineal Gland", "Pituitary Gland", "Placenta", "Pleura", "Popliteal Fossa", "Prostate", "Pylorus", "Rectosigmoid Junction", "Rectum", "Retina", "Retro-Orbital Region", "Retroperitoneum", "Rib", "Ring Finger", "Round Ligament", "Sacrum", "Salivary Gland", "Scalp", "Scapula", "Sciatic Nerve", "Scrotum", "Seminal Vesicle", "Shoulder", "Sigmoid Colon", "Sinus", "Sinus(es), Maxillary", "Skeletal Muscle", "Skin", "Skull", "Small Bowel", "Small Bowel - Mucosa Only", "Small Finger", "Soft Tissue", "Spinal Column", "Spinal Cord", "Spleen", "Splenic Flexure", "Sternum", "Stomach", "Stomach - Mucosa Only", "Subcutaneous Tissue", "Synovium", "Temporal Cortex", "Tendon", "Testis", "Thigh", "Thoracic Spine", "Thorax", "Throat", "Thumb", "Thymus", "Thyroid", "Tibia", "Tongue", "Tonsil", "Tonsil (Pharyngeal)", "Trachea / Major Bronchi", "Transverse Colon", "Trunk", "Umbilical Cord", "Ureter", "Urethra", "Urinary Tract", "Uterus", "Uvula", "Vagina", "Vas Deferens", "Vein", "Venous", "Vertebra", "Vulva", "White Blood Cells", "Wrist", "Unknown", "Not Reported", "Not Allowed To Collect"

<br>Attribute Name: sample\_laterality
<br>Description: For tumors in paired organs, designates the side on which the specimen was obtained.
<br>Attribute of Node: sample
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Bilateral", "Left", "Right", "Unknown", "Not Reported"

<br>Attribute Name: comment
<br>Description: A written explanation, observation or criticism added to textual material.
<br>Attribute of Node: sample
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: necropsy\_sample
<br>Description: A sample collected during the surgical examination of a dead body.
<br>Attribute of Node: sample
<br>Required: false
<br>Type: boolean
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: date\_of\_sample\_collection
<br>Description: The date on which the sample or data was collected.
<br>Attribute of Node: sample
<br>Required: false
<br>Type: datetime
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: days\_to\_collection
<br>Description: Time interval from the date of sample collection to the date of initial pathologic diagnosis, represented as a calculated number of days.
<br>Attribute of Node: sample
<br>Required: false
<br>Type: integer
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: days\_to\_sample\_procurement
<br>Description: The number of days from the date the study subject was diagnosed to the date of the procedure that produced the sample.
<br>Attribute of Node: sample
<br>Required: false
<br>Type: integer
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: current\_weight
<br>Description: Numeric value that represents the current weight of the sample.
<br>Attribute of Node: sample
<br>Required: false
<br>Type: number
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: initial\_weight
<br>Description: Numeric value that represents the initial weight of the sample.
<br>Attribute of Node: sample
<br>Required: false
<br>Type: number
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: longest\_dimension
<br>Description: Numeric value that represents the longest dimension of the sample.
<br>Attribute of Node: sample
<br>Required: false
<br>Type: number
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: intermediate\_dimension
<br>Description: Intermediate dimension of the sample.
<br>Attribute of Node: sample
<br>Required: false
<br>Type: number
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: shortest\_dimension
<br>Description: Numeric value that represents the shortest dimension of the sample.
<br>Attribute of Node: sample
<br>Required: false
<br>Type: number
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: growth\_rate
<br>Description: Rate at which the model grows, measured as hours to time to split.
<br>Attribute of Node: sample
<br>Required: false
<br>Type: integer
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: analysis\_area
<br>Description: The total area of a sample that is used for analysis.
<br>Attribute of Node: sample
<br>Required: false
<br>Type: number
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: preservation\_method
<br>Description: Text term that represents the method used to preserve the sample.
<br>Attribute of Node: sample
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Cryopreserved", "FFPE", "Fresh", "OCT", "Snap Frozen", "Frozen", "Unknown", "Not Reported", "Not Allowed To Collect"

<br>Attribute Name: tumor\_descriptor
<br>Description: Text that describes the kind of disease present in the tumor specimen as related to a specific timepoint.
<br>Attribute of Node: sample
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Metastatic", "Not Applicable", "Primary", "Recurrence", "Xenograft", "NOS", "Unknown", "Not Reported", "Not Allowed To Collect"

<br>Attribute Name: tumor\_code
<br>Description: Diagnostic tumor code of the tissue sample source.
<br>Attribute of Node: sample
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Non cancerous tissue", "Diffuse Large B-Cell Lymphoma (DLBCL)", "Lung Cancer (all types)", "Cervical Cancer (all types)", "Anal Cancer (all types)", "Acute Leukemia of Ambiguous Lineage (ALAL)", "Acute lymphoblastic leukemia (ALL)", "Acute myeloid leukemia (AML)", "Induction Failure AML (AML-IF)", "Neuroblastoma (NBL)", "Osteosarcoma (OS)", "Ewing sarcoma", "Wilms tumor (WT)", "Clear cell sarcoma of the kidney (CCSK)", "Rhabdoid tumor (kidney) (RT)", "CNS, ependymoma", "CNS, glioblastoma (GBM)", "CNS, rhabdoid tumor", "CNS, low grade glioma (LGG)", "CNS, medulloblastoma", "CNS, other", "NHL, anaplastic large cell lymphoma", "NHL, Burkitt lymphoma (BL)", "Rhabdomyosarcoma", "Soft tissue sarcoma, non-rhabdomyosarcoma"

<br>Attribute Name: tumor\_code\_id
<br>Description: BCR-defined id code for the tumor sample.
<br>Attribute of Node: sample
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "00", "01", "02", "03", "04", "10", "15", "20", "21", "30", "40", "41", "50", "51", "52", "60", "61", "62", "63", "64", "65", "70", "71", "80", "81"

<br>Attribute Name: diagnosis\_pathologically\_confirmed
<br>Description: The histologic description of tissue or cells confirmed by a pathology review of frozen or formalin fixed slide(s) completed after the diagnostic pathology review of the tumor sample used to extract analyte(s).
<br>Attribute of Node: sample
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Yes", "No", "Unknown", "Not Reported", "Not Allowed To Collect"

<br>Attribute Name: analysis\_area\_percentage\_glass
<br>Description: The area of a sample on a slide that is represented by glass; the area of the sample that represents gaps in the sample.
<br>Attribute of Node: sample
<br>Required: false
<br>Type: number
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: analysis\_area\_percentage\_pigmented\_tumor
<br>Description: The area of a sample on a slide that is represented by pigmented tumor tissue, which will be analyzed.
<br>Attribute of Node: sample
<br>Required: false
<br>Type: number
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: analysis\_area\_percentage\_stroma
<br>Description: The percentage of the analysis area that is represented by stromal tissue.
<br>Attribute of Node: sample
<br>Required: false
<br>Type: number
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: analysis\_area\_percentage\_tumor
<br>Description: The percentage of the analysis area that is represented by tumor tissue.
<br>Attribute of Node: sample
<br>Required: false
<br>Type: number
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: tumor\_tissue\_area
<br>Description: The area within a sample that is comprised of tumor tissue.
<br>Attribute of Node: sample
<br>Required: false
<br>Type: number
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: width\_of\_tumor
<br>Description: The longest diameter of a tumor from the pathology examination of a specimen.
<br>Attribute of Node: sample
<br>Required: false
<br>Type: number
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: non\_tumor\_tissue\_area
<br>Description: The area within a sample that is represented by non-tumor tissue.
<br>Attribute of Node: sample
<br>Required: false
<br>Type: number
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: percentage\_stroma
<br>Description: The percentage of stromal tissue in a sample.
<br>Attribute of Node: sample
<br>Required: false
<br>Type: number
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: percentage\_tumor
<br>Description: The percentage of tumor tissue in a sample.
<br>Attribute of Node: sample
<br>Required: false
<br>Type: number
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: distance\_normal\_to\_tumor
<br>Description: Text term to signify the distance between the tumor tissue and the normal control tissue that was procured for matching normal DNA.
<br>Attribute of Node: sample
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Adjacent (< or = 2cm)", "Distal (>2cm)", "Unknown", "Not Reported"

<br>Attribute Name: time\_between\_clamping\_and\_freezing
<br>Description: Numeric representation of the elapsed time between the surgical clamping of blood supply and freezing of the sample.
<br>Attribute of Node: sample
<br>Required: false
<br>Type: number
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: time\_between\_excision\_and\_freezing
<br>Description: Numeric representation of the elapsed time between the excision and freezing of the sample.
<br>Attribute of Node: sample
<br>Required: false
<br>Type: number
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: catalog\_reference
<br>Description: HCMI catalog reference number for cancer model.
<br>Attribute of Node: sample
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: distributor\_reference
<br>Description: Distributor reference number for cancer model.
<br>Attribute of Node: sample
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: sample\_is\_ref
<br>Description: A sample entity which is used as a reference sample for determining relative protein abundances in labeling experiments.
<br>Attribute of Node: sample
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: fraction\_id
<br>Description: A unique id assigned by the data commons to a specific fraction of a specific sample.
<br>Attribute of Node: fraction
<br>Required: true
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: creation\_datetime
<br>Description: The datetime of fraction creation encoded as seconds from epoch.
<br>Attribute of Node: fraction
<br>Required: false
<br>Type: number
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: fraction\_number
<br>Description: Numeric value that represents the sequential number assigned to a fraction of the sample.
<br>Attribute of Node: fraction
<br>Required: false
<br>Type: number
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: weight
<br>Description: The weight of the patient.
<br>Attribute of Node: fraction, demographic\_data, follow\_up
<br>Required: false
<br>Type: number
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: fraction\_type
<br>Description: A brief description of the molecular or chemical nature of the sample fraction.
<br>Attribute of Node: fraction
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: analyte\_id
<br>Description: A unique id assigned by the data commons to the analyte derived from the sample.
<br>Attribute of Node: analyte
<br>Required: true
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: analyte\_type\_id
<br>Description: A single letter code used to identify a type of molecular analyte.
<br>Attribute of Node: analyte
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "D", "E", "G", "H", "R"

<br>Attribute Name: analyte\_type
<br>Description: Text term that represents the kind of molecular specimen analyte.
<br>Attribute of Node: analyte
<br>Required: true
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: analyte\_quantity
<br>Description: The weight  of analyte
<br>Attribute of Node: analyte
<br>Required: false
<br>Type: number
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: analyte\_volume
<br>Description: The volume of analyte
<br>Attribute of Node: analyte
<br>Required: false
<br>Type: number
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: analyte\_concentration
<br>Description: Numeric value that represents the concentration of an analyte or aliquot extracted from the sample or sample fraction.
<br>Attribute of Node: analyte
<br>Required: false
<br>Type: number
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: a260\_a280\_ratio
<br>Description: Numeric value that represents the sample ratio of nucleic acid absorbance at 260 nm and 280 nm, used to determine a measure of DNA purity.
<br>Attribute of Node: analyte
<br>Required: false
<br>Type: number
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: ribosomal\_rna\_28s\_16s\_ratio
<br>Description: The 28S/18S ribosomal RNA band ratio used to assess the quality of total RNA.
<br>Attribute of Node: analyte
<br>Required: false
<br>Type: number
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: spectrophotometer\_method
<br>Description: Name of the method used to determine the concentration of purified nucleic acid within a solution.
<br>Attribute of Node: analyte
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: well\_number
<br>Description: Numeric value that represents the the well location within a plate for the analyte or aliquot from the sample.
<br>Attribute of Node: analyte
<br>Required: false
<br>Type: integer
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: normal\_tumor\_genotype\_snp\_match
<br>Description: Text term that represents whether or not the genotype of the normal tumor matches or if the data is not available.
<br>Attribute of Node: analyte
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Yes", "No", "Unknown", "Not Reported"

<br>Attribute Name: aliquot\_id
<br>Description: A unique id assigned by the data commons to the analyte derived from a sample, fraction or analyte.
<br>Attribute of Node: aliquot
<br>Required: true
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: aliquot\_is\_ref
<br>Description: A biospecimen entity which is used as a reference sample for determining relative protein abundances in labeling experiments.
<br>Attribute of Node: aliquot
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: aliquot\_quantity
<br>Description: The weight of the aliquot(s) derived from the analyte(s).
<br>Attribute of Node: aliquot
<br>Required: false
<br>Type: number
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: aliquot\_volume
<br>Description: The volume of the aliquot(s) derived from the analyte(s).
<br>Attribute of Node: aliquot
<br>Required: false
<br>Type: number
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: aliquot\_concentration
<br>Description: Numeric value that represents the concentration of an analyte or aliquot extracted from the sample or sample fraction.
<br>Attribute of Node: aliquot
<br>Required: false
<br>Type: number
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: no\_matched\_normal\_low\_pass\_wgs
<br>Description: There will be no matched normal low pass WGS aliquots for this case that can be used for variant calling purposes.
<br>Attribute of Node: aliquot
<br>Required: false
<br>Type: boolean
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: no\_matched\_normal\_targeted\_sequencing
<br>Description: There will be no matched normal Targeted Sequencing aliquots for this case that can be used for variant calling purposes.
<br>Attribute of Node: aliquot
<br>Required: false
<br>Type: boolean
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: no\_matched\_normal\_wgs
<br>Description: There will be no matched normal WGS aliquots for this case that can be used for variant calling purposes.
<br>Attribute of Node: aliquot
<br>Required: false
<br>Type: boolean
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: no\_matched\_normal\_wxs
<br>Description: There will be no matched normal WXS aliquots for this case that can be used for variant calling purposes.
<br>Attribute of Node: aliquot
<br>Required: false
<br>Type: boolean
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: selected\_normal\_low\_pass\_wgs
<br>Description: Denotes which low-pass WGS normal aliquot the submitter prefers to use for variant calling. Only one normal per experimental strategy per case can be selected.
<br>Attribute of Node: aliquot
<br>Required: false
<br>Type: boolean
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: selected\_normal\_targeted\_sequencing
<br>Description: Denotes which targeted\_sequencing normal aliquot the submitter prefers to use for variant calling. Only one normal per experimental strategy per case can be selected.
<br>Attribute of Node: aliquot
<br>Required: false
<br>Type: boolean
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: selected\_normal\_wgs
<br>Description: Denotes which WGS normal aliquot the submitter prefers to use for variant calling. Only one normal per experimental strategy per case can be selected.
<br>Attribute of Node: aliquot
<br>Required: false
<br>Type: boolean
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: selected\_normal\_wxs
<br>Description: Denotes which WXS normal aliquot the submitter prefers to use for variant calling. Only one normal per experimental strategy per case can be selected.
<br>Attribute of Node: aliquot
<br>Required: false
<br>Type: boolean
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: laboratory\_procedure\_id
<br>Description: A unique id assigned by the data commons to the laboratory procedure
<br>Attribute of Node: laboratory\_procedure
<br>Required: true
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: laboratory\_procedure\_type
<br>Description: A short description of the laboratory procedure. Example- Whole Genome Sequencing, RT-PCR, Flow Cytometry, Immunohistochemistry Assay, Microscopy.
<br>Attribute of Node: laboratory\_procedure
<br>Required: true
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: laboratory\_procedure\_target\_type
<br>Description: The specific biological material that is processed by the laboratory procedure. Examples- RNA, DNA, peptide, protein, T cell, Macrophage.
<br>Attribute of Node: laboratory\_procedure
<br>Required: true
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: test\_name
<br>Description: The name of the test, if applicable. Example- OncotypeDX, Oncomine Comprehensive Cancer Panel.
<br>Attribute of Node: laboratory\_procedure
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: instrument\_name
<br>Description: The name of the instrument used for the laboratory procedure, if applicable. Example- Next Generation Sequencer, Flow Cytometer, Mass Spectrophotometer
<br>Attribute of Node: laboratory\_procedure
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: instrument\_model
<br>Description: The make of the instrument used for the laboratory procedure, if applicable. Example- Illumina.
<br>Attribute of Node: laboratory\_procedure
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: instrument\_version
<br>Description: The instrument version used for the laboratory procedure, if applicable.
<br>Attribute of Node: laboratory\_procedure
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: software\_name
<br>Description: The name of any software application used in the laboratory procedure, if applicable. Example- NextSeq Control Software version 4.0
<br>Attribute of Node: laboratory\_procedure
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: software\_version
<br>Description: The specific version of the software used in the laboratory procedure, if applicable.
<br>Attribute of Node: laboratory\_procedure
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: reagent\_description
<br>Description: Name of a key reagent used in laboratory procedure, if applicable. Example- MiSeq Reagent Kit V2.
<br>Attribute of Node: laboratory\_procedure
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: report\_id
<br>Description: A unique id assigned by the data commons to a report.
<br>Attribute of Node: report
<br>Required: true
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: report\_name
<br>Description: Report name as assigned by data submitter.
<br>Attribute of Node: report
<br>Required: true
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: report\_type
<br>Description: Indicator as to the nature of the report in terms of its content.Examples- Pathology Report, Bioanlaytical Report, Variant Report, Test Result Report, Clinical Report
<br>Attribute of Node: report
<br>Required: true
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: md5sum
<br>Description: Md5 checksum.
<br>Attribute of Node: report, file
<br>Required: true
<br>Type: string
<br>Constraints: Is Unique
<br>Enumeration: None

<br>Attribute Name: report\_description
<br>Description: Optional description of the report and its content.
<br>Attribute of Node: report
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: report\_format
<br>Description: The specific format of the report as derived by the loader.
<br>Attribute of Node: report
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: report\_location
<br>Description: Location or Path to report.
<br>Attribute of Node: report
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: report\_size
<br>Description: Size of the report as derived by the loader.
<br>Attribute of Node: report
<br>Required: false
<br>Type: number
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: file\_id
<br>Description: A unique id assigned by the data commons to a file.
<br>Attribute of Node: file
<br>Required: true
<br>Type: string
<br>Constraints: Is Unique
<br>Enumeration: None

<br>Attribute Name: file\_description
<br>Description: Optional description of the file and its content.
<br>Attribute of Node: file
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: file\_format
<br>Description: The specific format of the file as derived by the loader.
<br>Attribute of Node: file
<br>Required: true
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: file\_location
<br>Description: Location or Path to file.
<br>Attribute of Node: file
<br>Required: true
<br>Type: string
<br>Constraints: Is Unique
<br>Enumeration: None

<br>Attribute Name: file\_name
<br>Description: File name as assigned by data submitter.
<br>Attribute of Node: file
<br>Required: true
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: file\_size
<br>Description: Size of the file as derived by the loader.
<br>Attribute of Node: file
<br>Required: true
<br>Type: number
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: file\_status
<br>Description: Enumerated representation of the status of files.
<br>Attribute of Node: file
<br>Required: true
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "uploading", "uploaded", "md5summing", "md5summed", "validating", "error", "invalid", "suppressed", "redacted", "live", "validated", "submitted", "released"

<br>Attribute Name: file\_type
<br>Description: Indicator as to the nature of the file in terms of its content.
<br>Attribute of Node: file
<br>Required: true
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: demographic\_data\_id
<br>Description: A unique id assigned by the data commons to the demographic\_data node.
<br>Attribute of Node: demographic\_data
<br>Required: true
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: age\_at\_index
<br>Description: The study subject's age (in years) on the reference or anchor date date used during date obfuscation.
<br>Attribute of Node: demographic\_data
<br>Required: false
<br>Type: integer
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: cause\_of\_death
<br>Description: Text term to identify the cause of death for a patient.
<br>Attribute of Node: demographic\_data, diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: "Protocol treatment", "Breast cancer", "Cardiovascular disease", "Other chronic disease", "Other cancer", "Other", "Unknown", "Not\_applicable"

<br>Attribute Name: survival\_time
<br>Description: Days from registration to death or date last known alive.
<br>Attribute of Node: demographic\_data
<br>Required: false
<br>Type: integer
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: days\_to\_death
<br>Description: Time interval from a person's date of death to the date of initial pathologic diagnosis, represented as a calculated number of days.
<br>Attribute of Node: demographic\_data, diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: ethnicity
<br>Description: An individual's self-described social and cultural grouping, specifically whether an individual describes themselves as Hispanic or Latino. The provided values are based on the categories defined by the U.S. Office of Management and Business and used by the U.S. Census Bureau.
<br>Attribute of Node: demographic\_data
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Hispanic or Latino", "Not Hispanic or Latino", "Unknown", "Not Reported", "Not Allowed to Collect"

<br>Attribute Name: race
<br>Description: An arbitrary classification of a taxonomic group that is a division of a species. It usually arises as a consequence of geographical isolation within a species and is characterized by shared heredity, physical attributes and behavior, and in the case of humans, by common history, nationality, or geographic distribution. The provided values are based on the categories defined by the U.S. Office of Management and Business and used by the U.S. Census Bureau.
<br>Attribute of Node: demographic\_data
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "White", "American Indian or Alaska Native", "Black or African American", "Asian", "Native Hawaiian or Other Pacific Islander", "Other", "Unknown", "Not Reported", "Not Allowed to Collect", "Multirace"

<br>Attribute Name: vital\_status
<br>Description: The survival state of the person registered on the protocol.
<br>Attribute of Node: demographic\_data
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Alive", "Dead", "Unknown", "Not Reported"

<br>Attribute Name: menopause\_status
<br>Description: Text term used to describe the patient's menopause status.
<br>Attribute of Node: demographic\_data, follow\_up
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Premenopausal", "Perimenopausal", "Postmenopausal", "Unknown", "Not Reported"

<br>Attribute Name: gender
<br>Description: Text designations that identify gender. Gender is described as the assemblage of properties that distinguish people on the basis of their societal roles. [Explanatory Comment 1- Identification of gender is based upon self-report and may come from a form, questionnaire, interview, etc.]
<br>Attribute of Node: demographic\_data
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Female", "Male", "Unknown", "Unspecified", "Not Reported"

<br>Attribute Name: age\_is\_obfuscated
<br>Description: The age of the study subject has been modified for compliance reasons. The actual age differs from what is reported. Other date intervals for this study subject may also be modified.
<br>Attribute of Node: demographic\_data
<br>Required: false
<br>Type: boolean
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: breed
<br>Description: A group of animals homogeneous in appearance and other characteristics that distinguish it from other animals of the same species.
<br>Attribute of Node: demographic\_data
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Affenpinscher", "Afghan Hound", "Airedale Terrier", "Akita", "Alaskan Malamute", "American Eskimo Dog", "American Foxhound", "American Staffordshire Terrier", "American Water Spaniel", "Anatolian Shepherd Dog", "Australian Cattle Dog", "Australian Shepherd", "Australian Terrier", "Basenji", "Basset Hound", "Beagle", "Bearded Collie", "Bedlington Terrier", "Belgian Malinois", "Belgian Sheepdog", "Belgian Tervuren", "Bernese Mountain Dog", "Bichon Frise", "Black and Tan Coonhound", "Black Russian Terrier", "Bloodhound", "Border Collie", "Border Terrier", "Borzoi", "Boston Terrier", "Bouvier des Flandres", "Boxer", "Briard", "Brittany", "Brussels Griffon", "Bull Terrier", "Bulldog", "Bullmastiff", "Cairn Terrier", "Canaan Dog", "Cardigan Welsh Corgi", "Catahoula Hound", "Cavalier King Charles Spaniel", "Chesapeake Bay Retriever", "Chihuahua", "Chinese Crested", "Chinese Shar-Pei", "Chow Chow", "Clumber Spaniel", "Cocker Spaniel", "Collie", "Curly-Coated Retriever", "Dachshund", "Dalmatian", "Dandie Dinmont Terrier", "Doberman Pinscher", "English Cocker Spaniel", "English Foxhound", "English Setter", "English Springer Spaniel", "English Toy Spaniel", "Field Spaniel", "Finnish Spitz", "Flat-Coated Retriever", "French Bulldog", "German Pinscher", "German Shepherd Dog", "German Shorthaired Pointer", "German Wirehaired Pointer", "Giant Schnauzer", "Glen of Imaal Terrier", "Golden Retriever", "Gordon Setter", "Great Dane", "Great Pyrenees", "Greater Swiss Mountain Dog", "Greyhound", "Harrier", "Havanese", "Ibizan Hound", "Irish Setter", "Irish Terrier", "Irish Water Spaniel", "Irish Wolfhound", "Italian Greyhound", "Japanese Chin", "Keeshond", "Kerry Blue Terrier", "Komondor", "Kuvasz", "Labrador Retriever", "Lakeland Terrier", "Lhasa Apso", "Lowchen", "Maltese", "Manchester Terrier", "Mastiff", "Miniature Bull Terrier", "Miniature Pinscher", "Miniature Schnauzer", "Mixed Breed", "Neapolitan Mastiff", "Newfoundland", "Norfolk Terrier", "Norwegian Elkhound", "Norwich Terrier", "Nova Scotia Duck Tolling Retriever", "Old English Sheepdog", "Other", "Otterhound", "Papillon", "Parson Russell Terrier", "Pekingese", "Pembroke Welsh Corgi", "Petit Basset Griffon Vendeen", "Pharaoh Hound", "Pointer", "Polish Lowland Sheepdog", "Pomeranian", "Poodle", "Portuguese Water Dog", "Pug", "Puli", "Rhodesian Ridgeback", "Rottweiler", "Saint Bernard", "Saluki", "Samoyed", "Schipperke", "Scottish Deerhound", "Scottish Terrier", "Sealyham Terrier", "Shetland Sheepdog", "Shiba Inu", "Shih Tzu", "Siberian Husky", "Silky Terrier", "Skye Terrier", "Smooth Fox Terrier", "Soft Coated Wheaten Terrier", "Spinone Italiano", "Staffordshire Bull Terrier", "Standard Schnauzer", "Sussex Spaniel", "Tibetan Spaniel", "Tibetan Terrier", "Toy Fox Terrier", "Vizsla", "Weimaraner", "Welsh Springer Spaniel", "Welsh Terrier", "West Highland White Terrier", "Whippet", "Wire Fox Terrier", "Wirehaired Pointing Griffon", "Yorkshire Terrier"

<br>Attribute Name: cause\_of\_death\_source
<br>Description: The text term used to describe the source used to determine the study subject's cause of death.
<br>Attribute of Node: demographic\_data
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Autopsy", "Death Certificate", "Medical Record", "Social Security Death Index", "Unknown", "Not Reported"

<br>Attribute Name: date\_of\_birth
<br>Description: The date (and time) on which the biologic entity is born.
<br>Attribute of Node: demographic\_data
<br>Required: false
<br>Type: datetime
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: days\_to\_birth
<br>Description: Time interval from a person's date of birth to the date of initial pathologic diagnosis, represented as a calculated negative number of days.
<br>Attribute of Node: demographic\_data, diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: neutered\_indicator
<br>Description: Boolean indicator as to whther the study subject has been either spayed (female study subjects)or neutered (male study subjects)
<br>Attribute of Node: demographic\_data
<br>Required: false
<br>Type: boolean
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: occupation\_duration\_years
<br>Description: The number of years a study subject worked in a specific occupation.
<br>Attribute of Node: demographic\_data
<br>Required: false
<br>Type: integer
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: premature\_at\_birth
<br>Description: The yes/no/unknown indicator used to describe whether the study subject was premature (less than 37 weeks gestation) at birth.
<br>Attribute of Node: demographic\_data
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Yes", "No", "Unknown", "Not Reported"

<br>Attribute Name: weeks\_gestation\_at\_birth
<br>Description: Numeric value used to describe the number of weeks starting from the approximate date of the biological mother's last menstrual period and ending with the birth of the study subject.
<br>Attribute of Node: demographic\_data
<br>Required: false
<br>Type: number
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: height
<br>Description: The height of the patient.
<br>Attribute of Node: demographic\_data, follow\_up
<br>Required: false
<br>Type: number
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: year\_of\_birth
<br>Description: Numeric value to represent the calendar year in which an individual was born.
<br>Attribute of Node: demographic\_data
<br>Required: false
<br>Type: integer
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: year\_of\_death
<br>Description: Numeric value to represent the year of the death of an individual.
<br>Attribute of Node: demographic\_data
<br>Required: false
<br>Type: integer
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: exposure\_node\_id
<br>Description: A unique id assigned by the data commons to the exposure data node.
<br>Attribute of Node: exposure
<br>Required: true
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: alcohol\_days\_per\_week
<br>Description: Numeric value used to describe the average number of days each week that a person consumes an alcoholic beverage.
<br>Attribute of Node: exposure
<br>Required: false
<br>Type: number
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: alcohol\_drinks\_per\_day
<br>Description: Numeric value used to describe the average number of alcoholic beverages a person consumes per day.
<br>Attribute of Node: exposure
<br>Required: false
<br>Type: number
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: alcohol\_history
<br>Description: A response to a question that asks whether the participant has consumed at least 12 drinks of any kind of alcoholic beverage in their lifetime.
<br>Attribute of Node: exposure
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Yes", "No", "Unknown", "Not Reported"

<br>Attribute Name: alcohol\_intensity
<br>Description: Category to describe the patient's current level of alcohol use as self-reported by the patient.
<br>Attribute of Node: exposure
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Drinker", "Heavy Drinker", "Lifelong Non-Drinker", "Non-Drinker", "Occasional Drinker", "Unknown", "Not Reported"

<br>Attribute Name: asbestos\_exposure
<br>Description: The yes/no/unknown indicator used to describe whether the patient was exposed to asbestos.
<br>Attribute of Node: exposure
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Yes", "No", "Unknown", "Not Reported"

<br>Attribute Name: bmi
<br>Description: A calculated numerical quantity that represents an individual's weight to height ratio.
<br>Attribute of Node: exposure, follow\_up
<br>Required: false
<br>Type: number
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: cigarettes\_per\_day
<br>Description: The average number of cigarettes smoked per day.
<br>Attribute of Node: exposure
<br>Required: false
<br>Type: number
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: coal\_dust\_exposure
<br>Description: The yes/no/unknown indicator used to describe whether a patient was exposed to fine powder derived by the crushing of coal.
<br>Attribute of Node: exposure
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Yes", "No", "Unknown", "Not Reported"

<br>Attribute Name: environmental\_tobacco\_smoke\_exposure
<br>Description: The yes/no/unknown indicator used to describe whether a patient was exposed to smoke that is emitted from burning tobacco, including cigarettes, pipes, and cigars. This includes tobacco smoke exhaled by smokers.
<br>Attribute of Node: exposure
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Yes", "No", "Unknown", "Not Reported"

<br>Attribute Name: pack\_years\_smoked
<br>Description: Numeric computed value to represent lifetime tobacco exposure defined as number of cigarettes smoked per day x number of years smoked divided by 20.
<br>Attribute of Node: exposure
<br>Required: false
<br>Type: number
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: radon\_exposure
<br>Description: The yes/no/unknown indicator used to describe whether the patient was exposed to radon.
<br>Attribute of Node: exposure
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Yes", "No", "Unknown", "Not Reported"

<br>Attribute Name: respirable\_crystalline\_silica\_exposure
<br>Description: The yes/no/unknown indicator used to describe whether a patient was exposured to respirable crystalline silica, a widespread, naturally occurring, crystalline metal oxide that consists of different forms including quartz, cristobalite, tridymite, tripoli, ganister, chert and novaculite.
<br>Attribute of Node: exposure
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Yes", "No", "Unknown", "Not Reported"

<br>Attribute Name: smoking\_frequency
<br>Description: The text term used to generally decribe how often the patient smokes.
<br>Attribute of Node: exposure
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Every day", "Some days", "Unknown"

<br>Attribute Name: time\_between\_waking\_and\_first\_smoke
<br>Description: The text term used to describe the approximate amount of time elapsed between the time the patient wakes up in the morning to the time they smoke their first cigarette.
<br>Attribute of Node: exposure
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Within 5 Minutes", "6-30 Minutes", "31-60 Minutes", "After 60 Minutes", "Unknown"

<br>Attribute Name: tobacco\_smoking\_onset\_year
<br>Description: The year in which the participant began smoking.
<br>Attribute of Node: exposure
<br>Required: false
<br>Type: integer
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: tobacco\_smoking\_quit\_year
<br>Description: The year in which the participant quit smoking.
<br>Attribute of Node: exposure
<br>Required: false
<br>Type: integer
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: tobacco\_smoking\_status
<br>Description: Category describing current smoking status and smoking history as self-reported by a patient.
<br>Attribute of Node: exposure
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "1", "2", "3", "4", "5", "6", "7", "Unknown", "Not Reported"

<br>Attribute Name: type\_of\_smoke\_exposure
<br>Description: The text term used to describe the patient's specific type of smoke exposure.
<br>Attribute of Node: exposure
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Accidental building fire smoke", "Accidental fire smoke, grass", "Accidental fire smoke, NOS", "Accidental forest fire smoke", "Accidental vehicle fire smoke", "Aircraft smoke", "Burning tree smoke", "Coal smoke, NOS", "Cooking-related smoke, NOS", "Electrical fire smoke", "Electronic cigarette smoke, NOS", "Environmental tobacco smoke", "Factory smokestack smoke", "Field burning smoke", "Fire smoke, NOS", "Furnace or boiler smoke", "Gas burning smoke, propane", "Grease fire smoke", "Grilling smoke", "Hashish smoke", "Indoor stove or fireplace smoke, coal burning", "Indoor stove or fireplace smoke, NOS", "Indoor stove or fireplace smoke, wood burning", "Machine smoke", "Marijuana smoke", "No Smoke Exposure", "Oil burning smoke, Kerosene", "Oil burning smoke, NOS", "Recreational fire smoke", "Smoke exposure, NOS", "Smokehouse smoke", "Tobacco smoke, cigar", "Tobacco smoke, cigarettes", "Tobacco smoke, pipe", "Volcanic smoke", "Waste burning smoke", "Wood burning smoke, factory", "Wood burning smoke, NOS", "Work-related smoke, artificial smoke machines", "Work-related smoke, fire fighting", "Work-related smoke, foundry", "Work-related smoke, generators", "Work-related smoke, military", "Work-related smoke, NOS", "Work-related smoke, paint baking", "Work-related smoke, plastics factory", "Work-related smoke, plumbing", "Work-related smoke, soldering/welding", "Unknown"

<br>Attribute Name: type\_of\_tobacco\_used
<br>Description: The text term used to describe the specific type of tobacco used by the patient.
<br>Attribute of Node: exposure
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Cigar", "Cigarette", "Electronic Cigarette", "Other", "Pipe"

<br>Attribute Name: years\_smoked
<br>Description: Numeric value (or unknown) to represent the number of years a person has been smoking.
<br>Attribute of Node: exposure
<br>Required: false
<br>Type: number
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: family\_history\_id
<br>Description: A unique id assigned by the data commons to the family history node.
<br>Attribute of Node: family\_medical\_history
<br>Required: true
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: relationship\_age\_at\_diagnosis
<br>Description: The age when the study subject's relative was first diagnosed.
<br>Attribute of Node: family\_medical\_history
<br>Required: false
<br>Type: number
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: relationship\_gender
<br>Description: The text term used to describe the gender of the study subject's relative with a history of cancer.
<br>Attribute of Node: family\_medical\_history
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "female", "male", "unknown"

<br>Attribute Name: relationship\_primary\_diagnosis
<br>Description: The text term used to describe the malignant diagnosis of the study subject's relative with a history of cancer.
<br>Attribute of Node: family\_medical\_history
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Adrenal Gland Cancer", "Basal Cell Cancer", "Bile Duct Cancer", "Bladder Cancer", "Blood Cancer", "Bone Cancer", "Brain Cancer", "Breast Cancer", "Cancer", "Cervical Cancer", "Chondrosarcoma", "CNS Cancer", "Colorectal Cancer", "Esophageal Cancer", "Ewing Sarcoma", "Gallbladder Cancer", "Gastric Cancer", "Glioblastoma", "Gynecologic Cancer", "Head and Neck Cancer", "Hematologic Cancer", "Kaposi Sarcoma", "Kidney Cancer", "Laryngeal Cancer", "Leukemia", "Liver Cancer", "Lung Cancer", "Lymph Node Cancer", "Lymphoma", "Melanoma", "Mesothelioma", "Multiple Myeloma", "Neuroblastoma", "Osteosarcoma", "Ovarian Cancer", "Pancreas Cancer", "Pediatric Liver Cancer", "Prostate Cancer", "Rectal Cancer", "Rhabdomyosarcoma", "Sarcoma", "Skin Cancer", "Spleen Cancer", "Testicular Cancer", "Throat Cancer", "Thyroid Cancer", "Tongue Cancer", "Tonsillar Cancer", "Uterine Cancer", "Wilms Tumor", "Unknown", "Not Reported"

<br>Attribute Name: relationship\_type
<br>Description: The subgroup that describes the state of connectedness between members of the unit of society organized around kinship ties.
<br>Attribute of Node: family\_medical\_history
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Adopted Brother", "Adopted Daughter", "Adopted Sister", "Adopted Son", "Adoptive Father", "Adoptive Mother", "Aunt", "Brother", "Brother-in-law", "Child", "Cousin", "Daughter", "Daughter-in-law", "Domestic Partner", "Father", "Father-in-law", "Female Cousin", "Female Sibling of Adopted Child", "First Cousin", "First Cousin Once Removed", "Foster Brother", "Foster Daughter", "Foster Father", "Foster Mother", "Foster Sister", "Foster Son", "Fraternal Twin Brother", "Fraternal Twin Sibling", "Fraternal Twin Sister", "Full Brother", "Full Sister", "Grand Nephew", "Grand Niece", "Grandchild", "Granddaughter", "Grandfather", "Grandmother", "Grandparent", "Grandson", "Great Grandchild", "Half Brother", "Half Sibling", "Half Sister", "Husband", "Identical Twin Brother", "Identical Twin Sibling", "Identical Twin Sister", "Legal Guardian", "Male Cousin", "Male Sibling of Adopted Child", "Maternal Aunt", "Maternal First Cousin", "Maternal First Cousin Once Removed", "Maternal Grandfather", "Maternal Grandmother", "Maternal Grandparent", "Maternal Great Aunt", "Maternal Great Grandparent", "Maternal Great Uncle", "Maternal Half Brother", "Maternal Half Sibling", "Maternal Half Sister", "Maternal Uncle", "Mother", "Mother-in-law", "Natural Brother", "Natural Child", "Natural Daughter", "Natural Father", "Natural Grandchild", "Natural Grandfather", "Natural Grandmother", "Natural Grandparent", "Natural Mother", "Natural Parent", "Natural Sibling", "Natural Sister", "Natural Son", "Nephew", "Niece", "Niece Second Degree Relative", "Other", "Parent", "Paternal Aunt", "Paternal First Cousin", "Paternal First Cousin Once Removed", "Paternal Grandfather", "Paternal Grandmother", "Paternal Grandparent", "Paternal Great Aunt", "Paternal Great Grandparent", "Paternal Great Uncle", "Paternal Half Brother", "Paternal Half Sibling", "Paternal Half Sister", "Paternal Uncle", "Sibling", "Sister", "Sister-in-law", "Son", "Son-in-law", "Spouse", "Step Child", "Step Sibling", "Stepbrother", "Stepdaughter", "Stepfather", "Stepmother", "Stepsister", "Stepson", "Twin Sibling", "Uncle", "Unrelated", "Ward", "Wife", "Unknown", "Not Reported"

<br>Attribute Name: relative\_with\_cancer\_history
<br>Description: The yes/no/unknown indicator used to describe whether any of the study subject's relatives have a history of cancer.
<br>Attribute of Node: family\_medical\_history
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "yes", "no", "unknown", "not reported"

<br>Attribute Name: relatives\_with\_cancer\_history\_count
<br>Description: The number of relatives the study subject has with a known history of cancer.
<br>Attribute of Node: family\_medical\_history
<br>Required: false
<br>Type: integer
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: therapeutic\_procedure\_id
<br>Description: A unique id assigned by the data commons to the therapeutic\_procedure node.
<br>Attribute of Node: therapeutic\_procedure
<br>Required: true
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: days\_to\_treatment\_end
<br>Description: Number of days between the date used for index and the date the treatment ended.
<br>Attribute of Node: therapeutic\_procedure
<br>Required: false
<br>Type: integer
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: days\_to\_treatment\_start
<br>Description: Number of days between the date used for index and the date the treatment started.
<br>Attribute of Node: therapeutic\_procedure
<br>Required: false
<br>Type: integer
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: chemotherapy\_regimen
<br>Description: Chemotherapy regimen given (more granular classification than previous variable).
<br>Attribute of Node: therapeutic\_procedure
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Oral CMF (4 week cycles)", "IV CMF (3 week cycles)", "Standard AC (3 week cycles)", "Dose dense AC (2 week cycles)", "standard AC followed by a taxane", "Dose dense AC followed by a taxane", "FEC (3 week cycles)", "TAC (3 week cycles)", "TC (3 week cycles, includes any taxane with cyclophosphamide)", "Other treatment given as part of a CTSU protocol", "Other", "None", "Other anthracycline with no taxane", "Taxane only", "Other anthracycline with a taxane", "Not Reported"

<br>Attribute Name: chemotherapy\_regimen\_group
<br>Description: Chemotherapy regimen given (grouped as reported in manuscript).
<br>Attribute of Node: therapeutic\_procedure
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "CMF", "Anthracycline w/o Taxane", "Anthracycline and Taxane", "TC and variations", "Other or Not Specified", "None"

<br>Attribute Name: all\_endocrine\_therapy\_stopped
<br>Description: Indicator of whether all endocrine therapy had been stopped (used as event indicator for duration analysis).
<br>Attribute of Node: therapeutic\_procedure
<br>Required: false
<br>Type: boolean
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: primary\_surgical\_procedure
<br>Description: Primary surgical procedure.
<br>Attribute of Node: therapeutic\_procedure
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Mastectomy", "Tumorectomy", "Not Reported"

<br>Attribute Name: received\_chemotherapy
<br>Description: Indicator of whether patients were treated with chemotherapy (cases with no follow-up data are coded as 0).
<br>Attribute of Node: therapeutic\_procedure
<br>Required: false
<br>Type: boolean
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: endocrine\_therapy\_type
<br>Description: Type of endocrine therapy
<br>Attribute of Node: therapeutic\_procedure
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "AI", "OFS", "OFS & AI", "Tam", "Tam & AI", "Other", "None", "Not Reported"

<br>Attribute Name: initial\_disease\_status
<br>Description: The text term used to describe the status of the patient's malignancy when the treatment began.
<br>Attribute of Node: therapeutic\_procedure
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Initial Diagnosis", "Progressive Disease", "Recurrent Disease", "Residual Disease", "Unknown", "Not Reported"

<br>Attribute Name: regimen\_or\_line\_of\_therapy
<br>Description: The text term used to describe the regimen or line of therapy.
<br>Attribute of Node: therapeutic\_procedure
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: therapeutic\_agents
<br>Description: Text identification of the individual agent(s) used as part of a treatment regimen.
<br>Attribute of Node: therapeutic\_procedure
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: treatment\_anatomic\_site
<br>Description: The anatomic site or field targeted by a treatment regimen or single agent therapy.
<br>Attribute of Node: therapeutic\_procedure
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Abdomen, total", "Abdominal Wall", "Acetabulum", "Adenoid", "Adipose", "Adrenal", "Alveolar Ridge", "Amniotic Fluid", "Ampulla of Vater", "Anal Sphincter", "Ankle", "Anorectum", "Antecubital Fossa", "Antrum", "Anus", "Aorta", "Aortic Body", "Appendix", "Aqueous Fluid", "Arm", "Artery", "Ascending Colon", "Ascending Colon Hepatic Flexure", "Ascites", "Auditory Canal", "Autonomic Nervous System", "Axilla", "Back", "Bile Duct", "Bladder", "Blood", "Blood Vessel", "Body, total", "Bone", "Bone Marrow", "Bone, non-spine", "Bowel", "Brain", "Brain Stem", "Breast", "Broad Ligament", "Bronchiole", "Bronchus", "Brow", "Buccal Cavity", "Buccal Mucosa", "Buttock", "Calf", "Capillary", "Cardia", "Carina", "Carotid Artery", "Carotid Body", "Cartilage", "Cecum", "Cell-Line", "Central Nervous System", "Cerebellum", "Cerebral Cortex", "Cerebrospinal Fluid", "Cerebrum", "Cervical Spine", "Cervix", "Chest", "Chest Wall", "Chin", "Clavicle", "Clitoris", "Colon", "Colon - Mucosa Only", "Common Duct", "Conjunctiva", "Connective Tissue", "Dermal", "Descending Colon", "Diaphragm", "Distant Site", "Duodenum", "Ear", "Ear Canal", "Ear, Pinna (External)", "Elbow", "Endocrine Gland", "Epididymis", "Epidural Space", "Epitrochlear", "Esophagogastric Junction", "Esophagus", "Esophagus - Mucosa Only", "Eye", "Fallopian Tube", "Femoral Artery", "Femoral Vein", "Femur", "Fibroblasts", "Fibula", "Finger", "Floor of Mouth", "Fluid", "Foot", "Forearm", "Forehead", "Foreskin", "Frontal Cortex", "Frontal Lobe", "Fundus of Stomach", "Gallbladder", "Ganglia", "Gastroesophageal Junction", "Gastrointestinal Tract", "Gastrointestinal, Intestine", "Genitourinary, NOS", "Groin", "Gum", "Hand", "Hard Palate", "Head - Face Or Neck, Nos", "Head and Neck", "Heart", "Hepatic", "Hepatic Duct", "Hepatic Vein", "Hilar", "Hip", "Hippocampus", "Humerus", "Hypopharynx", "Ileocecal Valve", "Ileum", "Ilium", "Index Finger", "Ischium", "Islet Cells", "Jaw", "Jejunum", "Joint", "Kidney", "Knee", "Lacrimal Gland", "Large Bowel", "Laryngopharynx", "Larynx", "Leg", "Leptomeninges", "Ligament", "Lip", "Liver", "Lumbar Spine", "Lung", "Lymph Node", "Lymph Node(s) Axilla", "Lymph Node(s) Cervical", "Lymph Node(s) Distant", "Lymph Node(s) Epitrochlear", "Lymph Node(s) Femoral", "Lymph Node(s) Hilar", "Lymph Node(s) Iliac-Common", "Lymph Node(s) Iliac-External", "Lymph Node(s) Inguinal", "Lymph Node(s) Internal Mammary", "Lymph Node(s) Mammary", "Lymph Node(s) Mediastinal", "Lymph Node(s) Mesenteric", "Lymph Node(s) Occipital", "Lymph Node(s) Paraaortic", "Lymph Node(s) Parotid", "Lymph Node(s) Pelvic", "Lymph Node(s) Popliteal", "Lymph Node(s) Regional", "Lymph Node(s) Retroperitoneal", "Lymph Node(s) Scalene", "Lymph Node(s) Splenic", "Lymph Node(s) Subclavicular", "Lymph Node(s) Submandibular", "Lymph Node(s) Supraclavicular", "Mandible", "Mantle", "Maxilla", "Mediastinal Soft Tissue", "Mediastinum", "Mesentery", "Mesothelium", "Middle Finger", "Mitochondria", "Muscle", "Nails", "Nasal Cavity", "Nasal Soft Tissue", "Nasopharynx", "Neck", "Nerve", "Nerve(s) Cranial", "Occipital Cortex", "Ocular Orbits", "Omentum", "Oral Cavity", "Oral Cavity - Mucosa Only", "Oropharynx", "Other", "Ovary", "Palate", "Pancreas", "Parametrium", "Paraspinal Ganglion", "Parathyroid", "Parotid Gland", "Patella", "Pelvis", "Penis", "Pericardium", "Periorbital Soft Tissue", "Peritoneal Cavity", "Peritoneum", "Pharynx", "Pineal", "Pineal Gland", "Pituitary Gland", "Placenta", "Pleura", "Popliteal Fossa", "Pouch", "Primary Tumor Field", "Primary tumor site", "Prostate", "Prostate Bed", "Prostate, Seminal Vesicles and Lymph Nodes", "Pylorus", "Rectosigmoid Junction", "Rectum", "Regional Site", "Retina", "Retro-Orbital Region", "Retroperitoneum", "Rib", "Ring Finger", "Round Ligament", "Sacrum", "Salivary Gland", "Scalp", "Scapula", "Sciatic Nerve", "Scrotum", "Seminal Vesicle", "Shoulder", "Sigmoid Colon", "Sinus", "Sinus(es), Maxillary", "Skeletal Muscle", "Skin", "Skin, lower extremity, local", "Skin, total", "Skin, trunk, local", "Skin, upper extremity, local", "Skull", "Small Bowel", "Small Bowel - Mucosa Only", "Small Finger", "Soft Tissue", "Spinal Column", "Spinal Cord", "Spine", "Spleen", "Splenic Flexure", "Sternum", "Stomach", "Stomach - Mucosa Only", "Subcutaneous Tissue", "Synovium", "Temporal Cortex", "Tendon", "Testis", "Thigh", "Thoracic Spine", "Thorax", "Throat", "Thumb", "Thymus", "Thyroid", "Tibia", "Tongue", "Tonsil", "Tonsil (Pharyngeal)", "Trachea / Major Bronchi", "Transverse Colon", "Trunk", "Umbilical Cord", "Unknown", "Ureter", "Urethra", "Urinary Tract", "Uterus", "Uvula", "Vagina", "Vas Deferens", "Vein", "Venous", "Vertebra", "Vulva", "White Blood Cells", "Wrist", "Not Reported"

<br>Attribute Name: treatment\_effect
<br>Description: The text term used to describe the pathologic effect a treatment(s) had on the tumor.
<br>Attribute of Node: therapeutic\_procedure
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Complete Necrosis (No Viable Tumor)", "Incomplete Necrosis (Viable Tumor Present)", "No Necrosis", "Unknown", "Not Reported"

<br>Attribute Name: treatment\_intent\_type
<br>Description: Text term to identify the reason for the administration of a treatment regimen. [Manually-curated]
<br>Attribute of Node: therapeutic\_procedure
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Adjuvant", "Cancer Control", "Cure", "Neoadjuvant", "Palliative", "Prevention", "Unknown", "Not Reported"

<br>Attribute Name: treatment\_or\_therapy
<br>Description: A yes/no/unknown/not applicable indicator related to the administration of therapeutic agents received.
<br>Attribute of Node: therapeutic\_procedure
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "yes", "no", "unknown", "not reported"

<br>Attribute Name: treatment\_outcome
<br>Description: Text term that describes the patient's final outcome after the treatment was administered.
<br>Attribute of Node: therapeutic\_procedure
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Complete Response", "Mixed Response", "No Measurable Disease", "No Response", "Partial Response", "Persistent Disease", "Progressive Disease", "Stable Disease", "Treatment Ongoing", "Treatment Stopped Due to Toxicity", "Very Good Partial Response", "Unknown", "Not Reported"

<br>Attribute Name: treatment\_type
<br>Description: Text term that describes the kind of treatment administered.
<br>Attribute of Node: therapeutic\_procedure
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Ablation, Cryo", "Ablation, Ethanol Injection", "Ablation, Microwave", "Ablation, NOS", "Ablation, Radiofrequency", "Ablation, Radiosurgical", "Ancillary Treatment", "Antiseizure Treatment", "Bisphosphonate Therapy", "Blinded Study, Treatment Unknown", "Brachytherapy, High Dose", "Brachytherapy, Low Dose", "Brachytherapy, NOS", "Chemoembolization", "Chemoprotectant", "Chemotherapy", "Concurrent Chemoradiation", "Cryoablation", "Embolization", "Ethanol Injection Ablation", "External Beam Radiation", "Hormone Therapy", "I-131 Radiation Therapy", "Internal Radiation", "Immunotherapy (Including Vaccines)", "Isolated Limb Perfusion (ILP)", "Organ Transplantation", "Other", "Pharmaceutical Therapy, NOS", "Pleurodesis", "Radiation, 2D Conventional", "Radiation, 3D Conformal", "Radiation, Combination", "Radiation, Cyberknife", "Radiation, External Beam", "Radiation, Implants", "Radiation, Intensity-Modulated Radiotherapy", "Radiation, Internal", "Radiation, Proton Beam", "Radiation, Radioisotope", "Radiation, Stereotactic/Gamma Knife/SRS", "Radiation, Systemic", "Radiation Therapy, NOS", "Radioactive Iodine Therapy", "Radioembolization", "Radiosensitizing Agent", "Stem Cell Treatment", "Stem Cell Transplantation, Autologous", "Stem Cell Transplantation, Double Autologous", "Stem Cell Transplantation, Allogeneic", "Stem Cell Transplantation, Non-Myeloablative", "Stem Cell Transplantation, Syngenic", "Stem Cell Transplantation, Haploidentical", "Stem Cell Transplantation, NOS", "Stereotactic Radiosurgery", "Steroid Therapy", "Surgery", "Targeted Molecular Therapy", "Unknown", "Not Reported", "Not Allowed To Collect"

<br>Attribute Name: diagnosis\_id
<br>Description: A unique id assigned by the data commons to the diagnosis node.
<br>Attribute of Node: diagnosis
<br>Required: true
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: tumor\_grade
<br>Description: Numeric value to express the degree of abnormality of cancer cells, a measure of differentiation and aggressiveness.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "G1", "G2", "G3", "G4", "GX", "GB", "High Grade", "Intermediate Grade", "Low Grade", "Unknown", "Not Reported"

<br>Attribute Name: tumor\_largest\_dimension\_diameter
<br>Description: Numeric value used to describe the maximum diameter or dimension of the primary tumor. A value of -1 indicates that tumor dimension was not reported.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: number
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: er\_status
<br>Description: Estrogen Receptor Status
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Negative", "Positive", "Not Reported"

<br>Attribute Name: nuclear\_grade
<br>Description: Nuclear grade (as reported by local site).
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Low", "Medium", "High", "Not Reported"

<br>Attribute Name: pr\_status
<br>Description: Progesterone Receptor Status
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Negative", "Positive", "Not Reported"

<br>Attribute Name: recurrence\_score
<br>Description: The recurrence score reported by OncotypeDX assay.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: integer
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: tumor\_size\_group
<br>Description: Tumor size category
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "<=1", "(1,2]", "(2,3]", "(3,4]", ">4", "Not Reported"

<br>Attribute Name: age\_at\_diagnosis
<br>Description: Age at the time of diagnosis expressed in number of days since birth.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: integer
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: ajcc\_clinical\_m
<br>Description: Extent of the distant metastasis for the cancer based on evidence obtained from clinical assessment parameters determined prior to treatment.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "M0", "M1", "M1a", "M1b", "M1c", "MX", "cM0 (i+)", "Unknown", "Not Reported"

<br>Attribute Name: ajcc\_clinical\_n
<br>Description: Extent of the regional lymph node involvement for the cancer based on evidence obtained from clinical assessment parameters determined prior to treatment.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "N0", "N0 (i+)", "N0 (i-)", "N0 (mol+)", "N0 (mol-)", "N1", "N1a", "N1b", "N1bI", "N1bII", "N1bIII", "N1bIV", "N1c", "N1mi", "N2", "N2a", "N2b", "N2c", "N3", "N3a", "N3b", "N3c", "N4", "NX", "Unknown", "Not Reported"

<br>Attribute Name: ajcc\_clinical\_stage
<br>Description: Stage group determined from clinical information on the tumor (T), regional node (N) and metastases (M) and by grouping cases with similar prognosis for cancer.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Stage 0", "Stage 0a", "Stage 0is", "Stage I", "Stage IA", "Stage IA1", "Stage IA2", "Stage IB", "Stage IB1", "Stage IB2", "Stage IC", "Stage II", "Stage IIA", "Stage IIA1", "Stage IIA2", "Stage IIB", "Stage IIC", "Stage IIC1", "Stage III", "Stage IIIA", "Stage IIIB", "Stage IIIC", "Stage IIIC1", "Stage IIIC2", "Stage IS", "Stage IV", "Stage IVA", "Stage IVB", "Stage IVC", "Stage Tis", "Stage X", "Unknown", "Not Reported"

<br>Attribute Name: ajcc\_clinical\_t
<br>Description: Extent of the primary cancer based on evidence obtained from clinical assessment parameters determined prior to treatment.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "T0", "T1", "T1a", "T1a1", "T1a2", "T1b", "T1b1", "T1b2", "T1c", "T1mi", "T2", "T2a", "T2a1", "T2a2", "T2b", "T2c", "T2d", "T3", "T3a", "T3b", "T3c", "T3d", "T4", "T4a", "T4b", "T4c", "T4d", "T4e", "TX", "Ta", "Tis", "Tis (DCIS)", "Tis (LCIS)", "Tis (Paget's)", "Unknown", "Not Reported"

<br>Attribute Name: ajcc\_pathologic\_m
<br>Description: Code to represent the defined absence or presence of distant spread or metastases (M) to locations via vascular channels or lymphatics beyond the regional lymph nodes, using criteria established by the American Joint Committee on Cancer (AJCC).
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "M0", "M1", "M1a", "M1b", "M1c", "M2", "MX", "cM0 (i+)", "Unknown", "Not Reported"

<br>Attribute Name: ajcc\_pathologic\_n
<br>Description: The codes that represent the stage of cancer based on the nodes present (N stage) according to criteria based on multiple editions of the AJCC's Cancer Staging Manual.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "N0", "N0 (i+)", "N0 (i-)", "N0 (mol+)", "N0 (mol-)", "N1", "N1a", "N1b", "N1bI", "N1bII", "N1bIII", "N1bIV", "N1c", "N1mi", "N2", "N2a", "N2b", "N2c", "N3", "N3a", "N3b", "N3c", "N4", "NX", "Unknown", "Not Reported"

<br>Attribute Name: ajcc\_pathologic\_stage
<br>Description: The extent of a cancer, especially whether the disease has spread from the original site to other parts of the body based on AJCC staging criteria.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Stage 0", "Stage 0a", "Stage 0is", "Stage I", "Stage IA", "Stage IA1", "Stage IA2", "Stage IB", "Stage IB1", "Stage IB2", "Stage IC", "Stage II", "Stage IS", "Stage IIA", "Stage IIA1", "Stage IIA2", "Stage IIB", "Stage IIC", "Stage III", "Stage IIIA", "Stage IIIB", "Stage IIIC", "Stage IIIC1", "Stage IIIC2", "Stage IIID", "Stage IV", "Stage IVA", "Stage IVB", "Stage IVC", "Stage Tis", "Stage X", "Unknown", "Not Reported"

<br>Attribute Name: ajcc\_pathologic\_t
<br>Description: Code of pathological T (primary tumor) to define the size or contiguous extension of the primary tumor (T), using staging criteria from the American Joint Committee on Cancer (AJCC).
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "T0", "T1", "T1a", "T1a1", "T1a2", "T1b", "T1b1", "T1b2", "T1c", "T1mi", "T2", "T2a", "T2a1", "T2a2", "T2b", "T2c", "T2d", "T3", "T3a", "T3b", "T3c", "T3d", "T4", "T4a", "T4b", "T4c", "T4d", "T4e", "TX", "Ta", "Tis", "Tis (DCIS)", "Tis (LCIS)", "Tis (Paget's)", "Unknown", "Not Reported"

<br>Attribute Name: ajcc\_staging\_system\_edition
<br>Description: The text term used to describe the version or edition of the American Joint Committee on Cancer Staging Handbooks, a publication by the group formed for the purpose of developing a system of staging for cancer that is acceptable to the American medical profession and is compatible with other accepted classifications.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "Unknown", "Not Reported"

<br>Attribute Name: anaplasia\_present
<br>Description: Yes/no/unknown/not reported indicator used to describe whether anaplasia was present at the time of diagnosis.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Yes", "No", "Unknown", "Not Reported"

<br>Attribute Name: anaplasia\_present\_type
<br>Description: The text term used to describe the morphologic findings indicating the presence of a malignant cellular infiltrate characterized by the presence of large pleomorphic cells, necrosis, and high mitotic activity in a tissue sample.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Absent", "Diffuse", "Equivocal", "Focal", "Present", "Sclerosis", "Unknown", "Not Reported"

<br>Attribute Name: ann\_arbor\_b\_symptoms
<br>Description: Text term to signify whether lymphoma B-symptoms are present as noted in the patient's medical record.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Yes", "No", "Unknown", "Not Reported"

<br>Attribute Name: ann\_arbor\_clinical\_stage
<br>Description: The text term used to describe the clinical classification of lymphoma, as defined by the Ann Arbor Lymphoma Staging System.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Stage I", "Stage II", "Stage III", "Stage IV", "Unknown", "Not Reported"

<br>Attribute Name: ann\_arbor\_extranodal\_involvement
<br>Description: Indicator that identifies whether a patient with malignant lymphoma has lymphomatous involvement of an extranodal site.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Yes", "No", "Unknown", "Not Reported"

<br>Attribute Name: ann\_arbor\_pathologic\_stage
<br>Description: The text term used to describe the pathologic classification of lymphoma, as defined by the Ann Arbor Lymphoma Staging System.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Stage I", "Stage II", "Stage III", "Stage IV", "Unknown", "Not Reported"

<br>Attribute Name: best\_overall\_response
<br>Description: The best improvement achieved throughout the entire course of protocol treatment.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "AJ-Adjuvant Therapy", "CPD-Clinical Progression", "CR-Complete Response", "CRU-Complete Response Unconfirmed", "DU-Disease Unchanged", "IMR-Immunoresponse", "IPD-Immunoprogression", "MR-Minimal/Marginal Response", "MX-Mixed Response", "Non-CR/Non-PD-Non-CR/Non-PD", "NPB-No Palliative Benefit", "NR-No Response", "PA-Palliative Therapy", "PB-Palliative Benefit", "PD-Progressive Disease", "PPD-Pseudoprogression", "PR-Partial Response", "PSR-Pseudoresponse", "RD-Responsive Disease", "RP-Response", "RPD-Radiographic Progressive Disease", "sCR-Stringent Complete Response", "SD-Stable Disease", "SPD-Surgical Progression", "TE-Too Early", "VGPR-Very Good Partial Response"

<br>Attribute Name: breslow\_thickness
<br>Description: The number that describes the distance, in millimeters, between the upper layer of the epidermis and the deepest point of tumor penetration.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: number
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: burkitt\_lymphoma\_clinical\_variant
<br>Description: Burkitt's lymphoma categorization based on clinical features that differ from other forms of the same disease.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Endemic", "Immunodeficiency-associated, adult", "Immunodeficiency-associated, pediatric", "Sporadic, adult", "Sporadic, pediatric", "Unknown", "Not Reported"

<br>Attribute Name: child\_pugh\_classification
<br>Description: The text term used to describe the classification used in the prognosis of chronic liver disease, mainly cirrhosis.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "A", "A5", "A6", "B", "B7", "B8", "B9", "C", "C10", "C11", "C12", "Unknown", "Not Reported"

<br>Attribute Name: circumferential\_resection\_margin
<br>Description: Numeric value used to describe the non-peritonealised bare area of rectum, comprising anterior and posterior segments, when submitted as a surgical specimen resulting from excision of cancer of the rectum.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: number
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: classification\_of\_tumor
<br>Description: Text that describes the kind of disease present in the tumor specimen as related to a specific timepoint.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "metastasis", "other", "Premalignant", "primary", "recurrence", "Unknown", "not reported", "Not Allowed To Collect"

<br>Attribute Name: cog\_liver\_stage
<br>Description: The text term used to describe the staging classification of liver tumors, as defined by the Children's Oncology Group (COG). This staging system specifically describes the extent of the primary tumor prior to treatment.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Stage I", "Stage II", "Stage III", "Stage IV", "Unknown", "Not Reported"

<br>Attribute Name: cog\_neuroblastoma\_risk\_group
<br>Description: Text term that represents the categorization of patients on the basis of prognostic factors per a system developed by Children's Oncology Group (COG). Risk level is used to assign treatment intensity.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "High Risk", "Intermediate Risk", "Low Risk", "Unknown", "Not Reported"

<br>Attribute Name: cog\_renal\_stage
<br>Description: The text term used to describe the staging classification of renal tumors, as defined by the Children's Oncology Group (COG).
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Stage I", "Stage II", "Stage III", "Stage IV", "Unknown", "Not Reported"

<br>Attribute Name: cog\_rhabdomyosarcoma\_risk\_group
<br>Description: Text term used to describe the classification of rhabdomyosarcoma, as defined by the Children's Oncology Group (COG).
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "High Risk", "Intermediate Risk", "Low Risk", "Unknown", "Not Reported"

<br>Attribute Name: colon\_polyps\_history
<br>Description: Yes/No indicator to describe if the subject had a previous history of colon polyps as noted in the history/physical or previous endoscopic report (s).
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: concurrent\_disease
<br>Description: Indicator as to whether the patient is has any significant secondary disease condition(s).
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Yes", "No"

<br>Attribute Name: concurrent\_disease\_type
<br>Description: Specifics of any notable secondary disease condition(s) within the patient
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: date\_of\_diagnosis
<br>Description: Date of diagnosis.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: datetime
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: date\_of\_histology\_confirmation
<br>Description: Date of histology confirmation.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: datetime
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: days\_to\_best\_overall\_response
<br>Description: Number of days between the date used for index and the date of the patient was thought to have the best overall response to their disease.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: integer
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: days\_to\_diagnosis
<br>Description: Number of days between the date used for index and the date the patient was diagnosed with the malignant disease.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: integer
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: days\_to\_hiv\_diagnosis
<br>Description: Time interval from the date of the initial pathologic diagnosis to the date of human immunodeficiency diagnosis, represented as a calculated number of days.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: days\_to\_last\_follow\_up
<br>Description: Time interval from the date of last follow up to the date of initial pathologic diagnosis, represented as a calculated number of days.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: number
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: days\_to\_last\_known\_disease\_status
<br>Description: Time interval from the date of last follow up to the date of initial pathologic diagnosis, represented as a calculated number of days.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: number
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: days\_to\_new\_event
<br>Description: Time interval from the date of new tumor event including progression, recurrence and new primary malignancies to the date of initial pathologic diagnosis, represented as a calculated number of days.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: days\_to\_recurrence
<br>Description: Number of days between the date used for index and the date the patient's disease recurred.
<br>Attribute of Node: diagnosis, follow\_up
<br>Required: false
<br>Type: integer
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: enneking\_msts\_grade
<br>Description: The text term used to describe the surgical grade of the musculoskeletal sarcoma, using the Enneking staging system approved by the Musculoskeletal Tumor Society (MSTS).
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "High Grade (G2)", "Low Grade (G1)", "Unknown", "Not Reported"

<br>Attribute Name: enneking\_msts\_metastasis
<br>Description: Text term and code that represents the metastatic stage of the musculoskeletal sarcoma, using the Enneking staging system approved by the Musculoskeletal Tumor Society (MSTS).
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "No Metastasis (M0)", "Regional or Distant Metastasis (M1)", "Unknown", "Not Reported"

<br>Attribute Name: enneking\_msts\_stage
<br>Description: Text term used to describe the stage of the musculoskeletal sarcoma, using the Enneking staging system approved by the Musculoskeletal Tumor Society (MSTS).
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Stage IA", "Stage IB", "Stage IIA", "Stage IIB", "Stage III", "Unknown", "Not Reported"

<br>Attribute Name: enneking\_msts\_tumor\_site
<br>Description: Text term and code that represents the tumor site of the musculoskeletal sarcoma, using the Enneking staging system approved by the Musculoskeletal Tumor Society (MSTS).
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Extracompartmental (T2)", "Intracompartmental (T1)", "Unknown", "Not Reported"

<br>Attribute Name: esophageal\_columnar\_dysplasia\_degree
<br>Description: Text term to describe the amount of dysplasia found within the benign esophageal columnar mucosa.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "High Grade Dysplasia", "Indefinite for Dysplasia", "Low Grade Dysplasia", "Negative/ No Dysplasia", "Unknown", "Not Reported"

<br>Attribute Name: esophageal\_columnar\_metaplasia\_present
<br>Description: The yes/no/unknown indicator used to describe whether esophageal columnar metaplasia was determined to be present.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Yes", "No", "Unknown", "Not Reported"

<br>Attribute Name: figo\_stage
<br>Description: The extent of a cervical or endometrial cancer within the body, especially whether the disease has spread from the original site to other parts of the body, as described by the International Federation of Gynecology and Obstetrics (FIGO) stages.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Stage 0", "Stage I", "Stage IA", "Stage IA1", "Stage IA2", "Stage IB", "Stage IB1", "Stage IB2", "Stage IC", "Stage II", "Stage IIA", "Stage IIA1", "Stage IIA2", "Stage IIB", "Stage IIC", "Stage III", "Stage IIIA", "Stage IIIB", "Stage IIIC", "Stage IIIC1", "Stage IIIC2", "Stage IV", "Stage IVA", "Stage IVB", "Unknown", "Not Reported", "Not Allowed To Collect"

<br>Attribute Name: first\_symptom\_prior\_to\_diagnosis
<br>Description: Text term used to describe the patient's first symptom experienced prior to diagnosis and thought to be related to the disease.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Altered Mental Status", "Headaches", "Motor or Movement Changes", "Seizures", "Sensory Changes", "Visual Changes", "Unknown", "Not Reported"

<br>Attribute Name: follow\_up\_data
<br>Description: Indicator as to whether follow up data for the patient exists
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Yes", "No"

<br>Attribute Name: gastric\_esophageal\_junction\_involvement
<br>Description: The yes/no/unknown/not reported indicator used to describe whether the tumor is located across the gastroesophageal junction.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Yes", "No", "Unknown", "Not Reported"

<br>Attribute Name: gleason\_grade\_group
<br>Description: The text term used to describe the overall grouping of grades defined by the Gleason grading classification, which is used to determine the aggressiveness of prostate cancer. Note that this grade describes the entire prostatectomy specimen and is not specific to the sample used for sequencing.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Group 1", "Group 2", "Group 3", "Group 4", "Group 5"

<br>Attribute Name: goblet\_cells\_columnar\_mucosa\_present
<br>Description: The yes/no/unknown indicator used to describe whether goblet cells were determined to be present in the esophageal columnar mucosa.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Yes", "No", "Unknown", "Not Reported"

<br>Attribute Name: gross\_tumor\_weight
<br>Description: Numeric value used to describe the gross pathologic tumor weight.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: number
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: hiv\_positive
<br>Description: Text term to signify whether a physician has diagnosed HIV infection in a patient.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: hpv\_positive\_type
<br>Description: Text classification to represent the strain or type of human papillomavirus identified in an individual.
<br>Attribute of Node: diagnosis, follow\_up
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "16", "18", "26", "31", "33", "35", "39", "45", "51", "52", "53", "56", "58", "59", "63", "66", "68", "70", "73", "82", "Other", "Unknown", "Not Reported"

<br>Attribute Name: hpv\_status
<br>Description: The findings of the oncogenic HPV.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: icd\_10\_code
<br>Description: Alphanumeric value used to describe the disease code from the tenth version of the International Classification of Disease (ICD-10).
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: igcccg\_stage
<br>Description: The text term used to describe the International Germ Cell Cancer Collaborative Group (IGCCCG), a grouping used to further classify metastatic testicular tumors.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Good Prognosis", "Intermediate Prognosis", "Poor Prognosis", "Unknown", "Not Reported"

<br>Attribute Name: inpc\_grade
<br>Description: Text term used to describe the classification of neuroblastic differentiation within neuroblastoma tumors, as defined by the International Neuroblastoma Pathology Classification (INPC).
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Differentiating", "Poorly Differentiated", "Undifferentiated", "Unknown", "Not Reported"

<br>Attribute Name: inpc\_histologic\_group
<br>Description: The text term used to describe the classification of neuroblastomas distinguishing between favorable and unfavorable histologic groups. The histologic score, defined by the International Neuroblastoma Pathology Classification (INPC), is based on age, mitosis-karyorrhexis index (MKI), stromal content and degree of tumor cell differentiation.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Favorable", "Unfavorable", "Unknown", "Not Reported"

<br>Attribute Name: inrg\_stage
<br>Description: The text term used to describe the staging classification of neuroblastic tumors, as defined by the International Neuroblastoma Risk Group (INRG).
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "L1", "L2", "M", "Ms", "Unknown", "Not Reported"

<br>Attribute Name: inss\_stage
<br>Description: Text term used to describe the staging classification of neuroblastic tumors, as defined by the International Neuroblastoma Staging System (INSS).
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Stage 1", "Stage 2A", "Stage 2B", "Stage 3", "Stage 4", "Stage 4S", "Unknown", "Not Reported"

<br>Attribute Name: international\_prognostic\_index
<br>Description: The text term used to describe the International Prognostic Index, which classifies the prognosis of patients with aggressive non-Hodgkin's lymphoma.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Low Risk", "Low-Intermediate Risk", "High-Intermediate Risk", "High Risk"

<br>Attribute Name: irs\_group
<br>Description: Text term used to describe the classification of rhabdomyosarcoma tumors, as defined by the Intergroup Rhabdomyosarcoma Study (IRS).
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Group I", "Group Ia", "Group Ib", "Group II", "Group IIa", "Group IIb", "Group IIc", "Group III", "Group IIIa", "Group IIIb", "Group IV", "Unknown", "Not Reported"

<br>Attribute Name: irs\_stage
<br>Description: The text term used to describe the classification of rhabdomyosarcoma tumors, as defined by the Intergroup Rhabdomyosarcoma Study (IRS).
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "1", "2", "3", "4", "Unknown", "Not Reported"

<br>Attribute Name: ishak\_fibrosis\_score
<br>Description: The text term used to describe the classification of the histopathologic degree of liver damage.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "0 - No Fibrosis", "1,2 - Portal Fibrosis", "3,4 - Fibrous Septa", "5 - Nodular Formation and Incomplete Cirrhosis", "6 - Established Cirrhosis", "Unknown", "Not Reported"

<br>Attribute Name: iss\_stage
<br>Description: The multiple myeloma disease stage at diagnosis.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "I", "II", "III", "Not Reported", "Unknown"

<br>Attribute Name: largest\_extrapelvic\_peritoneal\_focus
<br>Description: The text term used to describe the diameter of the largest focus originating outside of the pelvic peritoneal region.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Macroscopic (2cm or less)", "Macroscopic (greater than 2cm)", "Microscopic", "Unknown", "Not Reported"

<br>Attribute Name: last\_known\_disease\_status
<br>Description: Text term that describes the last known state or condition of an individual's neoplasm.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Distant met recurrence/progression", "Loco-regional recurrence/progression", "Biochemical evidence of disease without structural correlate", "Tumor free", "Unknown tumor status", "With tumor", "not reported", "Not Allowed To Collect"

<br>Attribute Name: laterality
<br>Description: For tumors in paired organs, designates the side on which the cancer originates.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Bilateral", "Left", "Midline", "Right", "Unilateral", "Unknown", "Not Reported"

<br>Attribute Name: ldh\_level\_at\_diagnosis
<br>Description: The 2 decimal place numeric laboratory value measured, assigned or computed related to the assessment of lactate dehydrogenase in a specimen.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: ldh\_normal\_range\_upper
<br>Description: The top value of the range of statistical characteristics that are supposed to represent accepted standard, non-pathological pattern for lactate dehydrogenase (units not specified).
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: lymph\_nodes\_positive
<br>Description: The number of lymph nodes involved with disease as determined by pathologic examination.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: integer
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: lymph\_nodes\_tested
<br>Description: The number of lymph nodes tested to determine whether lymph nodes were involved with disease as determined by a pathologic examination.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: integer
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: lymphatic\_invasion\_present
<br>Description: A yes/no indicator to ask if small or thin-walled vessel invasion is present, indicating lymphatic involvement
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Yes", "No", "Unknown", "Not Reported"

<br>Attribute Name: masaoka\_stage
<br>Description: The text term used to describe the Masaoka staging system, a classification that defines prognostic indicators for thymic malignancies and predicts tumor recurrence.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Stage I", "Stage IIa", "Stage IIb", "Stage III", "Stage IVa", "Stage IVb"

<br>Attribute Name: medulloblastoma\_molecular\_classification
<br>Description: The text term used to describe the classification of medulloblastoma tumors based on molecular features.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Not Determined", "Non-WNT/non-SHH Activated", "SHH-Activated", "WNT-Activated", "Unknown", "Not Reported"

<br>Attribute Name: metastasis\_at\_diagnosis
<br>Description: The text term used to describe the extent of metastatic disease present at diagnosis.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Distant Metastasis", "Metastasis, NOS", "No Metastasis", "Regional Metastasis", "Unknown", "Not Reported"

<br>Attribute Name: metastasis\_at\_diagnosis\_site
<br>Description: Text term to identify an anatomic site in which metastatic disease involvement is found.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Abdomen", "Adrenal Gland", "Ascites", "Bone", "Bone Marrow", "Brain", "Cerebrospinal Fluid", "Central Nervous System", "Colon", "Distant Nodes", "Distant Organ", "Groin", "Kidney", "Liver", "Lung", "Lymph Node, Axillary", "Lymph Node, Inguinal", "Lymph Node, NOS", "Mediastinum", "Omentum", "Ovary", "Pelvis", "Peritoneal Cavity", "Peritoneum", "Pleura", "Scalp", "Skin", "Small Intestine", "Soft Tissue", "Spinal Cord", "Unknown", "Not Reported"

<br>Attribute Name: method\_of\_diagnosis
<br>Description: Text term used to describe the method used to confirm the patients malignant diagnosis.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Autopsy", "Biopsy", "Blood Draw", "Bone Marrow Aspirate", "Core Biopsy", "Cytology", "Cystoscopy", "Debulking", "Diagnostic Imaging", "Dilation and Curettage Procedure", "Enucleation", "Excisional Biopsy", "Fine Needle Aspiration", "Imaging", "Incisional Biopsy", "Laparoscopy", "Laparotomy", "Other", "Pap Smear", "Physical Exam", "Pathologic Review", "Surgical Resection", "Thoracentesis", "Ultrasound Guided Biopsy", "Unknown", "Not Reported", "Not Allowed To Collect"

<br>Attribute Name: micropapillary\_features
<br>Description: The yes/no/unknown indicator used to describe whether micropapillary features were determined to be present.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Absent", "Present", "Unknown", "Not Reported"

<br>Attribute Name: mitosis\_karyorrhexis\_index
<br>Description: Text term that represents the component of the International Neuroblastoma Pathology Classification (INPC) for mitosis-karyorrhexis index (MKI).
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "High", "Intermediate", "Low", "Unknown", "Not Reported"

<br>Attribute Name: mitotic\_count
<br>Description: The number of mitoses identified under the microscope in tumors. The method of counting varies, according to the specific tumor examined. Usually, the mitotic count is determined based on the number of mitoses per high power field (40X) or 10 high power fields.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: integer
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: morphology
<br>Description: The third edition of the International Classification of Diseases for Oncology, published in 2000 used principally in tumor and cancer registries for coding the site (topography) and the histology (morphology) of neoplasms. The study of the structure of the cells and their arrangement to constitute tissues and, finally, the association among these to form organs. In pathology, the microscopic process of identifying normal and abnormal morphologic characteristics in tissues, by employing various cytochemical and immunocytochemical stains. A system of numbered categories for representation of data.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "8000/0", "8000/1", "8000/3", "8000/6", "8000/9", "8001/0", "8001/1", "8001/3", "8002/3", "8003/3", "8004/3", "8005/0", "8005/3", "8010/0", "8010/2", "8010/3", "8010/6", "8010/9", "8011/0", "8011/3", "8012/3", "8013/3", "8014/3", "8015/3", "8020/3", "8020/6", "8021/3", "8022/3", "8023/3", "8030/3", "8031/3", "8032/3", "8033/3", "8034/3", "8035/3", "8040/0", "8040/1", "8041/3", "8041/34", "8041/6", "8042/3", "8043/3", "8044/3", "8045/3", "8046/3", "8050/0", "8050/2", "8050/3", "8051/0", "8051/3", "8052/0", "8052/2", "8052/3", "8053/0", "8060/0", "8070/2", "8070/3", "8070/33", "8070/6", "8071/2", "8071/3", "8072/3", "8073/3", "8074/3", "8075/3", "8076/2", "8076/3", "8077/0", "8077/2", "8078/3", "8080/2", "8081/2", "8082/3", "8083/3", "8084/3", "8085/3", "8086/3", "8090/1", "8090/3", "8091/3", "8092/3", "8093/3", "8094/3", "8095/3", "8096/0", "8097/3", "8098/3", "8100/0", "8101/0", "8102/0", "8102/3", "8103/0", "8110/0", "8110/3", "8120/0", "8120/1", "8120/2", "8120/3", "8121/0", "8121/1", "8121/3", "8122/3", "8123/3", "8124/3", "8130/1", "8130/2", "8130/3", "8131/3", "8140/0", "8140/1", "8140/2", "8140/3", "8140/33", "8140/6", "8141/3", "8142/3", "8143/3", "8144/3", "8145/3", "8146/0", "8147/0", "8147/3", "8148/0", "8148/2", "8149/0", "8150/0", "8150/1", "8150/3", "8151/0", "8151/3", "8152/1", "8152/3", "8153/1", "8153/3", "8154/3", "8155/1", "8155/3", "8156/1", "8156/3", "8158/1", "8160/0", "8160/3", "8161/0", "8161/3", "8162/3", "8163/0", "8163/2", "8163/3", "8170/0", "8170/3", "8171/3", "8172/3", "8173/3", "8174/3", "8175/3", "8180/3", "8190/0", "8190/3", "8191/0", "8200/0", "8200/3", "8201/2", "8201/3", "8202/0", "8204/0", "8210/0", "8210/2", "8210/3", "8211/0", "8211/3", "8212/0", "8213/0", "8213/3", "8214/3", "8215/3", "8220/0", "8220/3", "8221/0", "8221/3", "8230/2", "8230/3", "8231/3", "8240/1", "8240/3", "8241/3", "8242/1", "8242/3", "8243/3", "8244/3", "8245/1", "8245/3", "8246/3", "8247/3", "8248/1", "8249/3", "8250/1", "8250/2", "8250/3", "8251/0", "8251/3", "8252/3", "8253/3", "8254/3", "8255/3", "8256/3", "8257/3", "8260/0", "8260/3", "8261/0", "8261/2", "8261/3", "8262/3", "8263/0", "8263/2", "8263/3", "8264/0", "8265/3", "8270/0", "8270/3", "8271/0", "8272/0", "8272/3", "8280/0", "8280/3", "8281/0", "8281/3", "8290/0", "8290/3", "8300/0", "8300/3", "8310/0", "8310/3", "8310/6", "8311/1", "8311/3", "8311/6", "8312/3", "8313/0", "8313/1", "8313/3", "8314/3", "8315/3", "8316/3", "8317/3", "8318/3", "8319/3", "8320/3", "8321/0", "8322/0", "8322/3", "8323/0", "8323/3", "8324/0", "8325/0", "8330/0", "8330/1", "8330/3", "8331/3", "8332/3", "8333/0", "8333/3", "8334/0", "8335/3", "8336/0", "8337/3", "8339/3", "8340/3", "8341/3", "8342/3", "8343/2", "8343/3", "8344/3", "8345/3", "8346/3", "8347/3", "8350/3", "8360/1", "8361/0", "8370/0", "8370/1", "8370/3", "8371/0", "8372/0", "8373/0", "8374/0", "8375/0", "8380/0", "8380/1", "8380/2", "8380/3", "8381/0", "8381/1", "8381/3", "8382/3", "8383/3", "8384/3", "8390/0", "8390/3", "8391/0", "8392/0", "8400/0", "8400/1", "8400/3", "8401/0", "8401/3", "8402/0", "8402/3", "8403/0", "8403/3", "8404/0", "8405/0", "8406/0", "8407/0", "8407/3", "8408/0", "8408/1", "8408/3", "8409/0", "8409/3", "8410/0", "8410/3", "8413/3", "8420/0", "8420/3", "8430/1", "8430/3", "8440/0", "8440/3", "8441/0", "8441/2", "8441/3", "8441/6", "8442/1", "8443/0", "8444/1", "8450/0", "8450/3", "8451/1", "8452/1", "8452/3", "8453/0", "8453/2", "8453/3", "8454/0", "8460/0", "8460/2", "8460/3", "8461/0", "8461/3", "8462/1", "8463/1", "8470/0", "8470/2", "8470/3", "8471/0", "8471/3", "8472/1", "8473/1", "8474/1", "8474/3", "8480/0", "8480/1", "8480/3", "8480/6", "8481/3", "8482/3", "8482/6", "8490/3", "8490/6", "8500/2", "8500/3", "8501/2", "8501/3", "8502/3", "8503/0", "8503/2", "8503/3", "8504/0", "8504/2", "8504/3", "8505/0", "8506/0", "8507/2", "8507/3", "8508/3", "8509/2", "8509/3", "8510/3", "8512/3", "8513/3", "8514/3", "8519/2", "8520/2", "8520/3", "8521/1", "8521/3", "8522/1", "8522/2", "8522/3", "8523/3", "8524/3", "8525/3", "8530/3", "8540/3", "8541/3", "8542/3", "8543/3", "8550/0", "8550/1", "8550/3", "8551/3", "8552/3", "8560/0", "8560/3", "8561/0", "8562/3", "8570/3", "8571/3", "8572/3", "8573/3", "8574/3", "8575/3", "8576/3", "8580/0", "8580/1", "8580/3", "8581/1", "8581/3", "8582/1", "8582/3", "8583/1", "8583/3", "8584/1", "8584/3", "8585/1", "8585/3", "8586/3", "8587/0", "8588/3", "8589/3", "8590/1", "8591/1", "8592/1", "8593/1", "8594/1", "8600/0", "8600/3", "8601/0", "8602/0", "8610/0", "8620/1", "8620/3", "8621/1", "8622/1", "8623/1", "8630/0", "8630/1", "8630/3", "8631/0", "8631/1", "8631/3", "8632/1", "8633/1", "8634/1", "8634/3", "8640/1", "8640/3", "8641/0", "8642/1", "8650/0", "8650/1", "8650/3", "8660/0", "8670/0", "8670/3", "8671/0", "8680/0", "8680/1", "8680/3", "8681/1", "8682/1", "8683/0", "8690/1", "8691/1", "8692/1", "8693/1", "8693/3", "8700/0", "8700/3", "8710/3", "8711/0", "8711/3", "8712/0", "8713/0", "8714/3", "8720/0", "8720/2", "8720/3", "8721/3", "8722/0", "8722/3", "8723/0", "8723/3", "8725/0", "8726/0", "8727/0", "8728/0", "8728/1", "8728/3", "8730/0", "8730/3", "8740/0", "8740/3", "8741/2", "8741/3", "8742/2", "8742/3", "8743/3", "8744/3", "8745/3", "8746/3", "8750/0", "8760/0", "8761/0", "8761/1", "8761/3", "8762/1", "8770/0", "8770/3", "8771/0", "8771/3", "8772/0", "8772/3", "8773/3", "8774/3", "8780/0", "8780/3", "8790/0", "8800/0", "8800/3", "8800/9", "8801/3", "8802/3", "8803/3", "8804/3", "8805/3", "8806/3", "8806/6", "8810/0", "8810/1", "8810/3", "8811/0", "8811/1", "8811/3", "8812/0", "8812/3", "8813/0", "8813/3", "8814/3", "8815/0", "8815/1", "8815/3", "8820/0", "8821/1", "8822/1", "8823/0", "8824/0", "8824/1", "8825/0", "8825/1", "8825/3", "8826/0", "8827/1", "8830/0", "8830/1", "8830/3", "8831/0", "8832/0", "8832/3", "8833/3", "8834/1", "8835/1", "8836/1", "8840/0", "8840/3", "8841/1", "8842/0", "8842/3", "8850/0", "8850/1", "8850/3", "8851/0", "8851/3", "8852/0", "8852/3", "8853/3", "8854/0", "8854/3", "8855/3", "8856/0", "8857/0", "8857/3", "8858/3", "8860/0", "8861/0", "8862/0", "8870/0", "8880/0", "8881/0", "8890/0", "8890/1", "8890/3", "8891/0", "8891/3", "8892/0", "8893/0", "8894/0", "8894/3", "8895/0", "8895/3", "8896/3", "8897/1", "8898/1", "8900/0", "8900/3", "8901/3", "8902/3", "8903/0", "8904/0", "8905/0", "8910/3", "8912/3", "8920/3", "8921/3", "8930/0", "8930/3", "8931/3", "8932/0", "8933/3", "8934/3", "8935/0", "8935/1", "8935/3", "8936/0", "8936/1", "8936/3", "8940/0", "8940/3", "8941/3", "8950/3", "8951/3", "8959/0", "8959/1", "8959/3", "8960/1", "8960/3", "8963/3", "8964/3", "8965/0", "8966/0", "8967/0", "8970/3", "8971/3", "8972/3", "8973/3", "8974/1", "8975/1", "8980/3", "8981/3", "8982/0", "8982/3", "8983/0", "8983/3", "8990/0", "8990/1", "8990/3", "8991/3", "9000/0", "9000/1", "9000/3", "9010/0", "9011/0", "9012/0", "9013/0", "9014/0", "9014/1", "9014/3", "9015/0", "9015/1", "9015/3", "9016/0", "9020/0", "9020/1", "9020/3", "9030/0", "9040/0", "9040/3", "9041/3", "9042/3", "9043/3", "9044/3", "9045/3", "9050/0", "9050/3", "9051/0", "9051/3", "9052/0", "9052/3", "9053/3", "9054/0", "9055/0", "9055/1", "9060/3", "9061/3", "9062/3", "9063/3", "9064/2", "9064/3", "9065/3", "9070/3", "9071/3", "9072/3", "9073/1", "9080/0", "9080/1", "9080/3", "9081/3", "9082/3", "9083/3", "9084/0", "9084/3", "9085/3", "9086/3", "9090/0", "9090/3", "9091/1", "9100/0", "9100/1", "9100/3", "9101/3", "9102/3", "9103/0", "9104/1", "9105/3", "9110/0", "9110/1", "9110/3", "9120/0", "9120/3", "9121/0", "9122/0", "9123/0", "9124/3", "9125/0", "9130/0", "9130/1", "9130/3", "9131/0", "9132/0", "9133/1", "9133/3", "9135/1", "9136/1", "9137/3", "9140/3", "9141/0", "9142/0", "9150/0", "9150/1", "9150/3", "9160/0", "9161/0", "9161/1", "9170/0", "9170/3", "9171/0", "9172/0", "9173/0", "9174/0", "9174/1", "9175/0", "9180/0", "9180/3", "9181/3", "9182/3", "9183/3", "9184/3", "9185/3", "9186/3", "9187/3", "9191/0", "9192/3", "9193/3", "9194/3", "9195/3", "9200/0", "9200/1", "9210/0", "9210/1", "9220/0", "9220/1", "9220/3", "9221/0", "9221/3", "9230/0", "9230/3", "9231/3", "9240/3", "9241/0", "9242/3", "9243/3", "9250/1", "9250/3", "9251/1", "9251/3", "9252/0", "9252/3", "9260/3", "9261/3", "9262/0", "9270/0", "9270/1", "9270/3", "9271/0", "9272/0", "9273/0", "9274/0", "9275/0", "9280/0", "9281/0", "9282/0", "9290/0", "9290/3", "9300/0", "9301/0", "9302/0", "9302/3", "9310/0", "9310/3", "9311/0", "9312/0", "9320/0", "9321/0", "9322/0", "9330/0", "9330/3", "9340/0", "9341/1", "9341/3", "9342/3", "9350/1", "9351/1", "9352/1", "9360/1", "9361/1", "9362/3", "9363/0", "9364/3", "9365/3", "9370/3", "9371/3", "9372/3", "9373/0", "9380/3", "9381/3", "9382/3", "9383/1", "9384/1", "9385/3", "9390/0", "9390/1", "9390/3", "9391/3", "9392/3", "9393/3", "9394/1", "9395/3", "9396/3", "9400/3", "9401/3", "9410/3", "9411/3", "9412/1", "9413/0", "9420/3", "9421/1", "9423/3", "9424/3", "9425/3", "9430/3", "9431/1", "9432/1", "9440/3", "9441/3", "9442/1", "9442/3", "9444/1", "9445/3", "9450/3", "9451/3", "9460/3", "9470/3", "9471/3", "9472/3", "9473/3", "9474/3", "9475/3", "9476/3", "9477/3", "9478/3", "9480/3", "9490/0", "9490/3", "9491/0", "9492/0", "9493/0", "9500/3", "9501/0", "9501/3", "9502/0", "9502/3", "9503/3", "9504/3", "9505/1", "9505/3", "9506/1", "9507/0", "9508/3", "9509/1", "9510/0", "9510/3", "9511/3", "9512/3", "9513/3", "9514/1", "9520/3", "9521/3", "9522/3", "9523/3", "9530/0", "9530/1", "9530/3", "9531/0", "9532/0", "9533/0", "9534/0", "9535/0", "9537/0", "9538/1", "9538/3", "9539/1", "9539/3", "9540/0", "9540/1", "9540/3", "9541/0", "9542/3", "9550/0", "9560/0", "9560/1", "9560/3", "9561/3", "9562/0", "9570/0", "9571/0", "9571/3", "9580/0", "9580/3", "9581/3", "9582/0", "9590/3", "9591/3", "9596/3", "9597/3", "9650/3", "9651/3", "9652/3", "9653/3", "9654/3", "9655/3", "9659/3", "9661/3", "9662/3", "9663/3", "9664/3", "9665/3", "9667/3", "9670/3", "9671/3", "9673/3", "9675/3", "9678/3", "9679/3", "9680/3", "9684/3", "9687/3", "9688/3", "9689/3", "9690/3", "9691/3", "9695/3", "9698/3", "9699/3", "9700/3", "9701/3", "9702/3", "9705/3", "9708/3", "9709/3", "9712/3", "9714/3", "9716/3", "9717/3", "9718/3", "9719/3", "9724/3", "9725/3", "9726/3", "9727/3", "9728/3", "9729/3", "9731/3", "9732/3", "9733/3", "9734/3", "9735/3", "9737/3", "9738/3", "9740/1", "9740/3", "9741/1", "9741/3", "9742/3", "9750/3", "9751/1", "9751/3", "9752/1", "9753/1", "9754/3", "9755/3", "9756/3", "9757/3", "9758/3", "9759/3", "9760/3", "9761/3", "9762/3", "9764/3", "9765/1", "9766/1", "9767/1", "9768/1", "9769/1", "9800/3", "9801/3", "9805/3", "9806/3", "9807/3", "9808/3", "9809/3", "9811/3", "9812/3", "9813/3", "9814/3", "9815/3", "9816/3", "9817/3", "9818/3", "9820/3", "9823/3", "9826/3", "9827/3", "9831/3", "9832/3", "9833/3", "9834/3", "9835/3", "9836/3", "9837/3", "9840/3", "9860/3", "9861/3", "9863/3", "9865/3", "9866/3", "9867/3", "9869/3", "9870/3", "9871/3", "9872/3", "9873/3", "9874/3", "9875/3", "9876/3", "9891/3", "9895/3", "9896/3", "9897/3", "9898/1", "9898/3", "9910/3", "9911/3", "9920/3", "9930/3", "9931/3", "9940/3", "9945/3", "9946/3", "9948/3", "9950/3", "9960/3", "9961/3", "9962/3", "9963/3", "9964/3", "9965/3", "9966/3", "9967/3", "9970/1", "9971/1", "9971/3", "9975/3", "9980/3", "9982/3", "9983/3", "9984/3", "9985/3", "9986/3", "9987/3", "9989/3", "9991/3", "9992/3", "Unknown", "Not Reported"

<br>Attribute Name: new\_event\_anatomic\_site
<br>Description: Text term to specify the anatomic location of the return of tumor after treatment.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: new\_event\_type
<br>Description: Text term to identify a new tumor event.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: non\_nodal\_regional\_disease
<br>Description: The text term used to describe whether the patient had non-nodal regional disease.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Absent", "Indeterminate", "Present", "Unknown", "Not Reported"

<br>Attribute Name: non\_nodal\_tumor\_deposits
<br>Description: The yes/no/unknown indicator used to describe the presence of tumor deposits in the pericolic or perirectal fat or in adjacent mesentery away from the leading edge of the tumor.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Yes", "No", "Unknown", "Not Reported"

<br>Attribute Name: ovarian\_specimen\_status
<br>Description: The text term used to describe the physical condition of the involved ovary.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Ovarian Capsule Intact", "Ovarian Capsule Ruptured", "Ovarian Capsule Fragmented", "Unknown", "Not Reported"

<br>Attribute Name: ovarian\_surface\_involvement
<br>Description: The text term that describes whether the surface tissue (outer boundary) of the ovary shows evidence of involvement or presence of cancer.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Absent", "Present", "Indeterminate", "Unknown", "Not Reported"

<br>Attribute Name: overall\_survival
<br>Description: Number of days between the date used for index and the patient's date of death or the date the patient was last known to be alive.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: pathology\_report
<br>Description: Indicator as to whether a detailed pathology report upon which the diagnosis was based exists.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Yes", "No"

<br>Attribute Name: percent\_tumor\_invasion
<br>Description: The percentage of tumor cells spread locally in a malignant neoplasm through infiltration or destruction of adjacent tissue.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: number
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: perineural\_invasion\_present
<br>Description: a yes/no indicator to ask if perineural invasion or infiltration of tumor or cancer is present.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Yes", "No", "Unknown", "Not Reported"

<br>Attribute Name: peripancreatic\_lymph\_nodes\_positive
<br>Description: Enumerated numeric value or range of values used to describe the number of peripancreatic lymph nodes determined to be positive.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "0", "1-3", "4 or More", "Unknown", "Not Reported"

<br>Attribute Name: peripancreatic\_lymph\_nodes\_tested
<br>Description: The total number of peripancreatic lymph nodes tested for the presence of pancreatic cancer cells.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: number
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: peritoneal\_fluid\_cytological\_status
<br>Description: The text term used to describe the malignant status of the peritoneal fluid determined by cytologic testing.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Atypical", "Malignant", "Non-Malignant", "Unsatisfactory", "Unknown", "Not Reported"

<br>Attribute Name: primary\_diagnosis
<br>Description: Text term used to describe the patient's histologic diagnosis, as described by the World Health Organization's (WHO) International Classification of Diseases for Oncology (ICD-O).
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Abdominal desmoid", "Abdominal fibromatosis", "Achromic nevus", "Acidophil adenocarcinoma", "Acidophil adenoma", "Acidophil carcinoma", "Acinar adenocarcinoma", "Acinar adenocarcinoma, sarcomatoid", "Acinar adenoma", "Acinar carcinoma", "Acinar cell adenoma", "Acinar cell carcinoma", "Acinar cell cystadenocarcinoma", "Acinar cell tumor", "Acinic cell adenocarcinoma", "Acinic cell adenoma", "Acinic cell tumor", "Acoustic neuroma", "Acquired cystic disease-associated renal cell carcinoma (RCC)", "Acquired tufted hemangioma", "Acral lentiginous melanoma, malignant", "ACTH-producing tumor", "Acute basophilic leukaemia", "Acute bilineal leukemia", "Acute biphenotypic leukemia", "Acute erythremia", "Acute erythremic myelosis", "Acute erythroid leukaemia", "Acute granulocytic leukemia", "Acute leukemia, Burkitt type", "Acute leukemia, NOS", "Acute lymphatic leukemia", "Acute lymphoblastic leukemia-lymphoma, NOS", "Acute lymphoblastic leukemia, L2 type, NOS", "Acute lymphoblastic leukemia, mature B-cell type", "Acute lymphoblastic leukemia, NOS", "Acute lymphoblastic leukemia, precursor cell type", "Acute lymphocytic leukemia", "Acute lymphoid leukemia", "Acute megakaryoblastic leukaemia", "Acute mixed lineage leukemia", "Acute monoblastic and monocytic leukemia", "Acute monoblastic leukemia", "Acute monocytic leukemia", "Acute myeloblastic leukemia", "Acute myelocytic leukemia", "Acute myelofibrosis", "Acute myelogenous leukemia", "Acute myeloid leukaemia, t(8;21)(q22;q22)", "Acute myeloid leukemia (megakaryoblastic) with t(1;22)(p13;q13); RBM15-MKL1", "Acute myeloid leukemia with abnormal marrow eosinophils (includes all variants)", "Acute myeloid leukemia with inv(3)(q21q26.2) or t(3;3)(q21;q26.2); RPN1-EVI1", "Acute myeloid leukemia with maturation", "Acute myeloid leukemia with multilineage dysplasia", "Acute myeloid leukemia with mutated CEBPA", "Acute myeloid leukemia with mutated NPM1", "Acute myeloid leukemia with myelodysplasia-related changes", "Acute myeloid leukemia with prior myelodysplastic syndrome", "Acute myeloid leukemia with t(6;9)(p23;q34); DEK-NUP214", "Acute myeloid leukemia with t(8;21)(q22;q22); RUNX1-RUNX1T1", "Acute myeloid leukemia with t(9;11)(p22;q23); MLLT3-MLL", "Acute myeloid leukemia without maturation", "Acute myeloid leukemia without prior myelodysplastic syndrome", "Acute myeloid leukemia, AML1(CBF-alpha)/ETO", "Acute myeloid leukemia, CBF-beta/MYH11", "Acute myeloid leukemia, inv(16)(p13;q22)", "Acute myeloid leukemia, M6 type", "Acute myeloid leukemia, minimal differentiation", "Acute myeloid leukemia, MLL", "Acute myeloid leukemia, NOS", "Acute myeloid leukemia, PML/RAR-alpha", "Acute myeloid leukemia, t(15:17)(g22;q11-12)", "Acute myeloid leukemia, t(16;16)(p 13;q 11)", "Acute myelomonocytic leukemia", "Acute myelomonocytic leukemia with abnormal eosinophils", "Acute myelosclerosis, NOS", "Acute myloid leukemia, 11q23 abnormalities", "Acute non-lymphocytic leukemia", "Acute panmyelosis with myelofibrosis", "Acute panmyelosis, NOS", "Acute progressive histiocytosis X", "Acute promyelocytic leukaemia, PML-RAR-alpha", "Acute promyelocytic leukaemia, t(15;17)(q22;q11-12)", "Acute promyelocytic leukemia, NOS", "Adamantinoma of long bones", "Adamantinoma, malignant", "Adamantinoma, NOS", "Adenoacanthoma", "Adenoameloblastoma", "Adenocarcinoid tumor", "Adenocarcinoma admixed with neuroendocrine carcinoma", "Adenocarcinoma combined with other types of carcinoma", "Adenocarcinoma in a polyp, NOS", "Adenocarcinoma in adenomatous polyp", "Adenocarcinoma in adenomatous polyposis coli", "Adenocarcinoma in multiple adenomatous polyps", "Adenocarcinoma in polypoid adenoma", "Adenocarcinoma in situ in a polyp, NOS", "Adenocarcinoma in situ in adenomatous polyp", "Adenocarcinoma in situ in polypoid adenoma", "Adenocarcinoma in situ in tubular adenoma", "Adenocarcinoma in situ in tubulovillous adenoma", "Adenocarcinoma in situ in villous adenoma", "Adenocarcinoma in situ, mucinous", "Adenocarcinoma in situ, non-mucinous", "Adenocarcinoma in situ, NOS", "Adenocarcinoma in tubolovillous adenoma", "Adenocarcinoma in tubular adenoma", "Adenocarcinoma in villous adenoma", "Adenocarcinoma of anal ducts", "Adenocarcinoma of anal glands", "Adenocarcinoma of rete ovarii", "Adenocarcinoma with apocrine metaplasia", "Adenocarcinoma with cartilaginous and osseous metaplasia", "Adenocarcinoma with cartilaginous metaplasia", "Adenocarcinoma with mixed subtypes", "Adenocarcinoma with neuroendocrine differentiation", "Adenocarcinoma with osseous metaplasia", "Adenocarcinoma with spindle cell metaplasia", "Adenocarcinoma with squamous metaplasia", "Adenocarcinoma, cribriform comedo-type", "Adenocarcinoma, cylindroid", "Adenocarcinoma, diffuse type", "Adenocarcinoma, endocervical type", "Adenocarcinoma, intestinal type", "Adenocarcinoma, metastatic, NOS", "Adenocarcinoma, NOS", "Adenocarcinoma, pancreatobiliary type", "Adenocystic carcinoma", "Adenofibroma, NOS", "Adenoid basal carcinoma", "Adenoid cystic carcinoma", "Adenolipoma", "Adenolymphoma", "Adenoma of nipple", "Adenoma, NOS", "Adenomatoid odontogenic tumor", "Adenomatoid tumor, NOS", "Adenomatosis, NOS", "Adenomatous polyp, NOS", "Adenomatous polyposis coli", "Adenomyoepithelioma", "Adenomyoepithelioma with carcinoma", "Adenomyoma", "Adenosarcoma", "Adenosquamous carcinoma", "Adnexal carcinoma", "Adnexal tumor, benign", "Adrenal cortical adenocarcinoma", "Adrenal cortical adenoma, clear cell", "Adrenal cortical adenoma, compact cell", "Adrenal cortical adenoma, glomerulosa cell", "Adrenal cortical adenoma, mixed cell", "Adrenal cortical adenoma, NOS", "Adrenal cortical adenoma, pigmented", "Adrenal cortical carcinoma", "Adrenal cortical tumor, benign", "Adrenal cortical tumor, malignant", "Adrenal cortical tumor, NOS", "Adrenal medullary paraganglioma", "Adrenal medullary paraganglioma, malignant", "Adrenal rest tumor", "Adult cystic teratoma", "Adult granulosa cell tumor", "Adult rhabdomyoma", "Adult T-cell leukemia", "Adult T-cell leukemia/lymphoma (HTLV-1 positive) (includes all variants)", "Adult T-cell lymphoma", "Adult T-cell lymphoma/leukemia", "Adult teratoma, NOS", "Aggressive angiomyxoma", "Aggressive digital papillary adenoma", "Aggressive fibromatosis", "Aggressive NK-cell leukaemia", "Aggressive osteoblastoma", "Aggressive systemic mastocytosis", "Agnogenic myeloid metaplasia", "AIN III", "Aleukemic granulocytic leukemia", "Aleukemic leukemia, NOS", "Aleukemic lymphatic leukemia", "Aleukemic lymphocytic leukemia", "Aleukemic lymphoid leukemia", "Aleukemic monocytic leukemia", "Aleukemic myelogenous leukemia", "Aleukemic myeloid leukemia", "ALK positive large B-cell lymphoma", "Alpha cell tumor, malignant", "Alpha cell tumor, NOS", "Alpha heavy chain disease", "Alveolar adenocarcinoma", "Alveolar adenoma", "Alveolar carcinoma", "Alveolar cell carcinoma", "Alveolar rhabdomyosarcoma", "Alveolar soft part sarcoma", "Amelanotic melanoma", "Ameloblastic carcinoma", "Ameloblastic fibro-odontoma", "Ameloblastic fibro-odontosarcoma", "Ameloblastic fibrodentinoma", "Ameloblastic fibrodentinosarcoma", "Ameloblastic fibroma", "Ameloblastic fibrosarcoma", "Ameloblastic odontosarcoma", "Ameloblastic sarcoma", "Ameloblastoma, malignant", "Ameloblastoma, NOS", "AML M6", "Anal intraepithelial neoplasia, grade III", "Anal intraepithelial neoplasia, low grade", "Anaplastic astrocytoma, IDH-mutant", "Anaplastic astrocytoma, IDH-wildtype", "Anaplastic large B-cell lymphoma", "Anaplastic large cell lymphoma, ALK negative", "Anaplastic large cell lymphoma, ALK positive", "Anaplastic large cell lymphoma, CD30+", "Anaplastic large cell lymphoma, NOS", "Anaplastic large cell lymphoma, T cell and Null cell type", "Anaplastic medulloblastoma", "Anaplastic oligoastrocytoma", "Anaplastic oligodendroglioma, IDH-mutant and 1p/19q-codeleted", "Anaplastic pleomorphic xanthroastrocytoma", "Ancient schwannoma", "Androblastoma, benign", "Androblastoma, malignant", "Androblastoma, NOS", "Angioblastic meningioma", "Angioblastoma", "Angiocentric glioma", "Angiocentric immunoproliferative lesion", "Angiocentric T-cell lymphoma", "Angioendothelioma", "Angioendotheliomatosis", "Angiofibroma, NOS", "Angioimmunoblastic lymphadenopathy", "Angioimmunoblastic lymphoma", "Angioimmunoblastic T-cell lymphoma", "Angiokeratoma", "Angioleiomyoma", "Angiolipoma, NOS", "Angioma, NOS", "Angiomatoid fibrous histiocytoma", "Angiomatous meningioma", "Angiomyofibroblastoma", "Angiomyolipoma", "Angiomyoma", "Angiomyosarcoma", "Angiomyxoma", "Angiosarcoma", "Angiotropic lymphoma", "Aortic body paraganglioma", "Aortic body tumor", "Aorticopulmonary paraganglioma", "Apocrine adenocarcinoma", "Apocrine adenoma", "Apocrine cystadenoma", "Apudoma", "Argentaffinoma, malignant", "Argentaffinoma, NOS", "Arrhenoblastoma, benign", "Arrhenoblastoma, malignant", "Arrhenoblastoma, NOS", "Arteriovenous hemangioma", "Askin tumor", "Astroblastoma", "Astrocytic glioma", "Astrocytoma, anaplastic", "Astrocytoma, low grade", "Astrocytoma, NOS", "Astroglioma", "Atypical adenoma", "Atypical carcinoid tumor", "Atypical choroid plexus papilloma", "Atypical chronic myeloid leukemia, BCR/ABL negative", "Atypical chronic myeloid leukemia, Philadelphia chromosome (Ph1) negative", "Atypical fibrous histiocytoma", "Atypical fibroxanthoma", "Atypical follicular adenoma", "Atypical hyperplasia/Endometrioid intraepithelial neoplasm", "Atypical leiomyoma", "Atypical lipoma", "Atypical medullary carcinoma", "Atypical meningioma", "Atypical polypoid adenomyoma", "Atypical proliferating clear cell tumor", "Atypical proliferating serous tumor", "Atypical proliferative endometrioid tumor", "Atypical proliferative mucinous tumor", "Atypical proliferative papillary serous tumor", "Atypical teratoid/rhabdoid tumor", "B cell lymphoma, NOS", "B lymphoblastic leukemia/lymphoma with hyperdiploidy", "B lymphoblastic leukemia/lymphoma with hypodiploidy (Hypodiploid ALL)", "B lymphoblastic leukemia/lymphoma with t(1;19)(q23;p13.3); E2A-PBX1 (TCF3-PBX1)", "B lymphoblastic leukemia/lymphoma with t(12;21)(p13;q22); TEL-AML1 (ETV6-RUNX1)", "B lymphoblastic leukemia/lymphoma with t(5;14)(q31;q32); IL3-IGH", "B lymphoblastic leukemia/lymphoma with t(9;22)(q34;q11.2); BCR-ABL1", "B lymphoblastic leukemia/lymphoma with t(v;11q23); MLL rearranged", "B lymphoblastic leukemia/lymphoma, NOS", "B-ALL", "B-cell lymphocytic leukemia/small lymphocytic lymphoma", "B-cell lymphoma, unclassifiable, with features intermediate between diffuse large B-cell lymphoma and Burkitt lymphoma", "B-cell lymphoma, unclassifiable, with features intermediate between diffuse large B-cell lymphoma and classical Hodgkin lymphoma", "Balloon cell melanoma", "Balloon cell nevus", "BALT lymphoma", "Basal cell adenocarcinoma", "Basal cell adenoma", "Basal cell carcinoma, desmoplastic type", "Basal cell carcinoma, fibroepithelial", "Basal cell carcinoma, micronodular", "Basal cell carcinoma, morpheic", "Basal cell carcinoma, nodular", "Basal cell carcinoma, NOS", "Basal cell epithelioma", "Basal cell tumor", "Basaloid carcinoma", "Basaloid squamous cell carcinoma", "Basophil adenocarcinoma", "Basophil adenoma", "Basophil carcinoma", "Basosquamous carcinoma", "Bednar tumor", "Bellini duct carcinoma", "Benign cystic nephroma", "Benign fibrous histiocytoma", "Beta cell adenoma", "Beta cell tumor, malignant", "Bile duct adenocarcinoma", "Bile duct adenoma", "Bile duct carcinoma", "Bile duct cystadenocarcinoma", "Bile duct cystadenoma", "Biliary intraepithelial neoplasia, grade 3", "Biliary intraepithelial neoplasia, high grade", "Biliary intraepithelial neoplasia, low grade", "Biliary papillomatosis", "Biphenotypic sinonasal sarcoma", "Bizarre leiomyoma", "Black adenoma", "Blast cell leukemia", "Blastic NK cell lymphoma", "Blastic plasmacytoid dendritic cell neoplasm", "Blastoma, NOS", "Blue nevus, malignant", "Blue nevus, NOS", "Botryoid sarcoma", "Bowen disease", "Brenner tumor, borderline malignancy", "Brenner tumor, malignant", "Brenner tumor, NOS", "Brenner tumor, proliferating", "Bronchial adenoma, carcinoid", "Bronchial adenoma, cylindroid", "Bronchial adenoma, NOS", "Bronchial-associated lymphoid tissue lymphoma", "Bronchio-alveolar carcinoma, mixed mucinous and non-mucinous", "Bronchio-alveolar carcinoma, mucinous", "Bronchiolar adenocarcinoma", "Bronchiolar carcinoma", "Bronchiolo-alveolar adenocarcinoma, NOS", "Bronchiolo-alveolar carcinoma, Clara cell", "Bronchiolo-alveolar carcinoma, Clara cell and goblet cell type", "Bronchiolo-alveolar carcinoma, goblet cell type", "Bronchiolo-alveolar carcinoma, indeterminate type", "Bronchiolo-alveolar carcinoma, non-mucinous", "Bronchiolo-alveolar carcinoma, NOS", "Bronchiolo-alveolar carcinoma, type II pneumocyte and goblet cell type", "Bronchiolo-alveolar carcinoma; type II pneumocyte", "Brooke tumor", "Brown fat tumor", "Burkitt cell leukemia", "Burkitt lymphoma, NOS (Includes all variants)", "Burkitt tumor", "Burkitt-like lymphoma", "C cell carcinoma", "c-ALL", "Calcifying epithelial odontogenic tumor", "Calcifying epithelioma of Malherbe", "Calcifying nested epithelial stromal tumor", "Calcifying odontogenic cyst", "Canalicular adenoma", "Cancer", "Capillary hemangioma", "Capillary lymphangioma", "Carcinofibroma", "Carcinoid tumor of uncertain malignant potential", "Carcinoid tumor, argentaffin, malignant", "Carcinoid tumor, argentaffin, NOS", "Carcinoid tumor, NOS", "Carcinoid tumor, NOS, of appendix", "Carcinoid, NOS", "Carcinoid, NOS, of appendix", "Carcinoma in a polyp, NOS", "Carcinoma in adenomatous polyp", "Carcinoma in pleomorphic adenoma", "Carcinoma in situ in a polyp, NOS", "Carcinoma in situ in adenomatous polyp", "Carcinoma in situ, NOS", "Carcinoma showing thymus-like differentiation", "Carcinoma showing thymus-like element", "Carcinoma simplex", "Carcinoma with apocrine metaplasia", "Carcinoma with chondroid differentiation", "Carcinoma with neuroendocrine differentiation", "Carcinoma with osseous differentiation", "Carcinoma with osteoclast-like giant cells", "Carcinoma with other types mesenchymal differentiation", "Carcinoma with productive fibrosis", "Carcinoma, anaplastic, NOS", "Carcinoma, diffuse type", "Carcinoma, intestinal type", "Carcinoma, metastatic, NOS", "Carcinoma, NOS", "Carcinoma, undifferentiated, NOS", "Carcinomatosis", "Carcinosarcoma, embryonal", "Carcinosarcoma, NOS", "Carotid body paraganglioma", "Carotid body tumor", "Cartilaginous exostosis", "CASTLE", "Cavernous hemangioma", "Cavernous lymphangioma", "Cellular angiofibroma", "Cellular blue nevus", "Cellular ependymoma", "Cellular fibroma", "Cellular leiomyoma", "Cellular schwannoma", "Cementifying fibroma", "Cemento-ossifying fibroma", "Cementoblastoma, benign", "Cementoma, NOS", "Central neuroblastoma", "Central neurocytoma", "Central odontogenic fibroma", "Central osteosarcoma", "Central primitive neuroectodermal tumor, NOS", "Cerebellar liponeurocytoma", "Cerebellar sarcoma, NOS", "Ceruminous adenocarcinoma", "Ceruminous adenoma", "Ceruminous carcinoma", "Cervical intraepithelial neoplasia, grade III", "Cervical intraepithelial neoplasia, low grade", "Chemodectoma", "Chief cell adenoma", "Chloroma", "Cholangiocarcinoma", "Cholangioma", "Chondroblastic osteosarcoma", "Chondroblastoma, malignant", "Chondroblastoma, NOS", "Chondroid chordoma", "Chondroid lipoma", "Chondroid syringoma", "Chondroma, NOS", "Chondromatosis, NOS", "Chondromatous giant cell tumor", "Chondromyxoid fibroma", "Chondrosarcoma grade 2/3", "Chondrosarcoma, NOS", "Chordoid glioma", "Chordoid glioma of third ventricle", "Chordoid meningioma", "Chordoma, NOS", "Chorioadenoma", "Chorioadenoma destruens", "Chorioangioma", "Choriocarcinoma combined with embryonal carcinoma", "Choriocarcinoma combined with other germ cell elements", "Choriocarcinoma combined with teratorna", "Choriocarcinoma, NOS", "Chorioepithelioma", "Chorionepithelioma", "Choroid plexus carcinoma", "Choroid plexus papilloma, anaplastic", "Choroid plexus papilloma, malignant", "Choroid plexus papilloma, NOS", "Chromaffin paraganglioma", "Chromaffin tumor", "Chromaffinoma", "Chromophobe adenocarcinoma", "Chromophobe adenoma", "Chromophobe carcinoma", "Chromophobe cell renal carcinoma", "Chronic eosinophilic leukemia, NOS", "Chronic erythremia", "Chronic granulocytic leukemia, BCR/ABL", "Chronic granulocytic leukemia, NOS", "Chronic granulocytic leukemia, Philadelphia chromosome (Ph1) positive", "Chronic granulocytic leukemia, t(9;22)(q34;q11)", "Chronic idiopathic myelofibrosis", "Chronic leukemia, NOS", "Chronic lymphatic leukemia", "Chronic lymphocytic leukemia", "Chronic lymphocytic leukemia, B-cell type (includes all variants of BCLL)", "Chronic lymphoid leukemia", "Chronic lymphoproliferative disorder of NK cells", "Chronic monocytic leukemia", "Chronic myelocytic leukemia, NOS", "Chronic myelogenous leukemia, BCR-ABL positive", "Chronic myelogenous leukemia, Philadelphia chromosome (Ph 1) positive", "Chronic myelogenous leukemia, t(9;22)(q34;q11)", "Chronic myeloid leukemia, NOS", "Chronic myelomonocytic leukemia in transformation", "Chronic myelomonocytic leukemia, NOS", "Chronic myelomonocytic leukemia, Type 1", "Chronic myelomonocytic leukemia, Type II", "Chronic myeloproliferative disease, NOS", "Chronic myeloproliferative disorder", "Chronic neutrophilic leukemia", "CIN III with severe dysplasia", "Cin III, NOS", "Circumscribed arachnoidal cerebellar sarcoma", "Classical Hodgkin lymphoma, lymphocyte depletion, diffuse fibrosis", "Classical Hodgkin lymphoma, lymphocyte depletion, NOS", "Classical Hodgkin lymphoma, lymphocyte depletion, reticular", "Classical Hodgkin lymphoma, lymphocyte-rich", "Classical Hodgkin lymphoma, mixed cellularity, NOS", "Classical Hodgkin lymphoma, nodular sclerosis, cellular phase", "Classical Hodgkin lymphoma, nodular sclerosis, grade 1", "Classical Hodgkin lymphoma, nodular sclerosis, grade 2", "Classical Hodgkin lymphoma, nodular sclerosis, NOS", "Clear cell (glycogen-rich) urothelial carcinoma", "Clear cell adenocarcinofibroma", "Clear cell adenocarcinoma, mesonephroid", "Clear cell adenocarcinoma, NOS", "Clear cell adenofibroma", "Clear cell adenofibroma of borderline malignancy", "Clear cell adenoma", "Clear cell carcinoma", "Clear cell chondrosarcoma", "Clear cell cystadenocarcinofibroma", "Clear cell cystadenofibroma", "Clear cell cystadenofibroma of borderline malignancy", "Clear cell cystadenoma", "Clear cell cystic tumor of borderline malignancy", "Clear cell ependymoma", "Clear cell hidradenoma", "Clear cell meningioma", "Clear cell odontogenic carcinoma", "Clear cell odontogenic tumor", "Clear cell sarcoma of kidney", "Clear cell sarcoma, NOS", "Clear cell sarcoma, of tendons and aponeuroses", "Clear cell tumor, NOS", "Cloacogenic carcinoma", "CNS Embryonal tumor with rhabdoid features", "Codman tumor", "Collecting duct carcinoma", "Colloid adenocarcinoma", "Colloid adenoma", "Colloid carcinoma", "Columnar cell papilloma", "Combined carcinoid and adenocarcinoma", "Combined hepatocellular carcinoma and cholangiocarcinoma", "Combined large cell neuroendocrine carcinoma", "Combined small cell carcinoma", "Combined small cell-adenocarcinoma", "Combined small cell-large carcinoma", "Combined small cell-squamous cell carcinoma", "Combined/mixed carcinoid and adenocarcinoma", "Comedocarcinoma, noninfiltrating", "Comedocarcinoma, NOS", "Common ALL", "Common precursor B ALL", "Complete hydatidiform mole", "Complex odontoma", "Composite carcinoid", "Composite Hodgkin and non-Hodgkin lymphoma", "Compound nevus", "Compound odontoma", "Condylomatous carcinoma", "Congenital fibrosarcoma", "Congenital generalized fibromatosis", "Congenital peribronchial myofibroblastic tumor", "Conventional central osteosarcoma", "Cortical T ALL", "CPNET", "Craniopharyngioma", "Craniopharyngioma, adamantinomatous", "Craniopharyngioma, papillary", "Cribriform carcinoma in situ", "Cribriform carcinoma, NOS", "Cribriform comedo-type carcinoma", "Cutaneous histiocytoma, NOS", "Cutaneous lymphoma, NOS", "Cutaneous mastocytosis", "Cutaneous T-cell lymphoma, NOS", "Cylindrical cell carcinoma", "Cylindrical cell papilloma", "Cylindroma of skin", "Cylindroma, NOS", "Cyst-associated renal cell carcinoma", "Cystadenocarcinoma, NOS", "Cystadenofibroma, NOS", "Cystadenoma, NOS", "Cystic astrocytoma", "Cystic hygroma", "Cystic hypersecretory carcinoma", "Cystic lymphangioma", "Cystic mesothelioma, benign", "Cystic mesothelioma, NOS", "Cystic partially differentiated nephroblastoma", "Cystic teratoma, NOS", "Cystic tumor of atrio-ventricular node", "Cystoma, NOS", "Cystosarcoma phyllodes, benign", "Cystosarcoma phyllodes, malignant", "Cystosarcoma phyllodes, NOS", "Dabska tumor", "DCIS, comedo type", "DCIS, NOS", "DCIS, papillary", "Dedifferentiated chondrosarcoma", "Dedifferentiated chordoma", "Dedifferentiated liposarcoma", "Deep histiocytoma", "Degenerated schwannoma", "Dendritic cell sarcoma, NOS", "Dentinoma", "Dermal and epidermal nevus", "Dermal nevus", "Dermatofibroma lenticulare", "Dermatofibroma, NOS", "Dermatofibrosarcoma protuberans, NOS", "Dermatofibrosarcoma, NOS", "Dermoid cyst with malignant transformation", "Dermoid cyst with secondary tumor", "Dermoid cyst, NOS", "Dermoid, NOS", "Desmoid, NOS", "Desmoplastic fibroma", "Desmoplastic infantile astrocytoma", "Desmoplastic infantile ganglioglioma", "Desmoplastic medulloblastoma", "Desmoplastic melanoma, amelanotic", "Desmoplastic melanoma, malignant", "Desmoplastic mesothelioma", "Desmoplastic nodular medulloblastoma", "Desmoplastic small round cell tumor", "Di Guglielmo disease", "Differentiated penile intraepithelial neoplasia", "Differentiated-type vulvar intraepithelial neoplasia", "Diffuse astrocytoma", "Diffuse astrocytoma, IDH-mutant", "Diffuse astrocytoma, IDH-wildtype", "Diffuse astrocytoma, low grade", "Diffuse cutaneous mastocytosis", "Diffuse intraductal papillomatosis", "Diffuse large B-cell lymphoma associated with chronic inflammation", "Diffuse large B-cell lymphoma, NOS", "Diffuse leptomeningeal glioneuronal tumor", "Diffuse melanocytosis", "Diffuse meningiomatosis", "Diffuse midline glioma, H3 K27M-mutant", "Digital papillary adenocarcinoma", "Diktyoma, benign", "Diktyoma, malignant", "DIN 3", "Duct adenocarcinoma, NOS", "Duct adenoma, NOS", "Duct carcinoma, desmoplastic type", "Duct carcinoma, NOS", "Duct cell carcinoma", "Ductal carcinoma in situ, comedo type", "Ductal carcinoma in situ, cribriform type", "Ductal carcinoma in situ, micropapillary", "Ductal carcinoma in situ, NOS", "Ductal carcinoma in situ, papillary", "Ductal carcinoma in situ, solid type", "Ductal carcinoma, cribriform type", "Ductal carcinoma, NOS", "Ductal intraepithelial neoplasia 3", "Ductal papilloma", "Dysembryoplastic neuroepithelial tumor", "Dysgerminoma", "Dysplastic gangliocytoma of cerebellum (Lhermitte-Duclos)", "Dysplastic nevus", "EBV positive diffuse large B-cell lymphoma of the elderly", "EC cell carcinoid", "Ecchondroma", "Ecchondrosis", "Eccrine acrospiroma", "Eccrine adenocarcinoma", "Eccrine cystadenoma", "Eccrine dermal cylindroma", "Eccrine papillary adenocarcinoma", "Eccrine papillary adenoma", "Eccrine poroma", "Eccrine poroma, malignant", "Eccrine spiradenoma", "ECL cell carcinoid, malignant", "ECL cell carcinoid, NOS", "Ectomesenchymoma", "Ectopic hamartomatous thymoma", "Elastofibroma", "Embryonal adenocarcinoma", "Embryonal adenoma", "Embryonal carcinoma, infantile", "Embryonal carcinoma, NOS", "Embryonal carcinoma, polyembryonal type", "Embryonal hepatoma", "Embryonal rhabdomyosarcoma, NOS", "Embryonal rhabdomyosarcoma, pleomorphic", "Embryonal sarcoma", "Embryonal teratoma", "Embryonal tumor with multilayered rosettes C19MC-altered", "Embryonal tumor with multilayered rosettes, NOS", "Embryonal tumor with rhabdoid features", "Encapsulated follicular variant of papillary thyroid carcinoma, NOS (EFVPTC, NOS)", "Encapsulated papillary carcinoma", "Encapsulated papillary carcinoma with invasion", "Enchondroma", "Endocervical adenocarcinoma usual type", "Endocrine adenomatosis", "Endocrine tumor, functioning, NOS", "Endodermal sinus tumor", "Endolymphatic stromal myosis", "Endometrial sarcoma, NOS", "Endometrial stromal nodule", "Endometrial stromal sarcoma, high grade", "Endometrial stromal sarcoma, low grade", "Endometrial stromal sarcoma, NOS", "Endometrial stromatosis", "Endometrioid adenocarcinoma, ciliated cell variant", "Endometrioid adenocarcinoma, NOS", "Endometrioid adenocarcinoma, secretory variant", "Endometrioid adenocarcinoma, villoglandular", "Endometrioid adenofibroma, borderline malignancy", "Endometrioid adenofibroma, malignant", "Endometrioid adenofibroma, NOS", "Endometrioid adenoma, borderline malignancy", "Endometrioid adenoma, NOS", "Endometrioid carcinoma with squamous differentiation", "Endometrioid carcinoma, NOS", "Endometrioid cystadenocarcinoma", "Endometrioid cystadenofibroma, borderline malignancy", "Endometrioid cystadenofibroma, malignant", "Endometrioid cystadenofibroma, NOS", "Endometrioid cystadenoma, borderline malignancy", "Endometrioid cystadenoma, NOS", "Endometrioid tumor of low malignant potential", "Endotheliomatous meningioma", "Endovascular papillary angioendothelioma", "Enteric adenocarcinoma", "Enterochromaffin cell carcinoid", "Enterochromaffin-like cell carcinoid, NOS", "Enterochromaffin-like cell tumor, malignant", "Enteroglucagonoma, malignant", "Enteroglucagonoma, NOS", "Enteropathy associated T-cell lymphoma", "Enteropathy type intestinal T-cell lymphoma", "Eosinophil adenocarcinoma", "Eosinophil adenoma", "Eosinophil carcinoma", "Eosinophilic granuloma", "Eosinophilic leukemia", "Ependymoblastoma", "Ependymoma, anaplastic", "Ependymoma, NOS", "Ependymoma, RELA fusion-positive", "Epidermoid carcinoma in situ with questionable stromal invasion", "Epidermoid carcinoma in situ, NOS", "Epidermoid carcinoma, keratinizing", "Epidermoid carcinoma, large cell, nonkeratinizing", "Epidermoid carcinoma, NOS", "Epidermoid carcinoma, small cell, nonkeratinizing", "Epidermoid carcinoma, spindle cell", "Epithelial ependymoma", "Epithelial tumor, benign", "Epithelial tumor, malignant", "Epithelial-myoepithelial carcinoma", "Epithelioid and spindle cell nevus", "Epithelioid cell melanoma", "Epithelioid cell nevus", "Epithelioid cell sarcoma", "Epithelioid glioblastoma", "Epithelioid hemangioendothelioma, malignant", "Epithelioid hemangioendothelioma, NOS", "Epithelioid hemangioma", "Epithelioid leiomyoma", "Epithelioid leiomyosarcoma", "Epithelioid malignant peripheral nerve sheath tumor", "Epithelioid mesothelioma, benign", "Epithelioid mesothelioma, malignant", "Epithelioid mesothelioma, NOS", "Epithelioid MPNST", "Epithelioid sarcoma", "Epithelioma adenoides cysticum", "Epithelioma, benign", "Epithelioma, malignant", "Epithelioma, NOS", "Erythremic myelosis, NOS", "Erythroleukemia", "Esophageal glandular dysplasia (intraepithelial neoplasia), high grade", "Esophageal glandular dysplasia (intraepithelial neoplasia), low grade", "Esophageal intraepithelial neoplasia, high grade", "Esophageal squamous intraepithelial neoplasia (dysplasia), high grade", "Esophageal squamous intraepithelial neoplasia (dysplasia), low grade", "Essential hemorrhagic thrombocythaemia", "Essential thrombocythemia", "Esthesioneuroblastoma", "Esthesioneurocytoma", "Esthesioneuroepithelioma", "Ewing sarcoma", "Ewing tumor", "Extra-abdominal desmoid", "Extra-adrenal paraganglioma, malignant", "Extra-adrenal paraganglioma, NOS", "Extracutaneous mastocytoma", "Extranodal marginal zone lymphoma of mucosa-associated lymphoid tissue", "Extranodal NK/T-cell lymphoma, nasal type", "Extraosseous plasmacytoma", "Extraventricular neurocytoma", "FAB L2", "FAB L3", "FAB Ll", "FAB M1", "FAB M2, AML1(CBF-alpha)/ETO", "FAB M2, NOS", "FAB M2, t(8;21)(q22;q22)", "FAB M3 (includes all variants)", "FAB M4", "FAB M4Eo", "FAB M5 (includes all variants)", "FAB M6", "FAB M7", "FAB MO", "Familial polyposis coli", "Fascial fibroma", "Fascial fibrosarcoma", "Fetal adenocarcinoma", "Fetal adenoma", "Fetal fat cell lipoma", "Fetal lipoma, NOS", "Fetal lipomatosis", "Fetal rhabdomyoma", "Fibrillary astrocytoma", "Fibro-osteoma", "Fibroadenoma, NOS", "Fibroameloblastic odontoma", "Fibroblastic liposarcoma", "Fibroblastic meningioma", "Fibroblastic osteosarcoma", "Fibroblastic reticular cell tumor", "Fibrochondrosarcoma", "Fibroepithelial basal cell carcinoma, Pinkus type", "Fibroepithelioma of Pinkus type", "Fibroepithelioma, NOS", "Fibrofolliculoma", "Fibroid uterus", "Fibrolipoma", "Fibroliposarcoma", "Fibroma, NOS", "Fibromatosis-like metaplastic carcinoma", "Fibromyoma", "Fibromyxolipoma", "Fibromyxoma", "Fibromyxosarcoma", "Fibrosarcoma, NOS", "Fibrosarcomatous dermatofibrosarcoma protuberans", "Fibrous astrocytoma", "Fibrous histiocytoma of tendon sheath", "Fibrous histiocytoma, NOS", "Fibrous meningioma", "Fibrous mesothelioma, benign", "Fibrous mesothelioma, malignant", "Fibrous mesothelioma, NOS", "Fibrous papule of nose", "Fibroxanthoma, malignant", "Fibroxanthoma, NOS", "Flat adenoma", "Flat intraepithelial glandular neoplasia, high grade", "Flat intraepithelial neoplasia, high grade", "Florid osseous dysplasia", "Follicular adenocarcinoma, moderately differentiated", "Follicular adenocarcinoma, NOS", "Follicular adenocarcinoma, trabecular", "Follicular adenocarcinoma, well differentiated", "Follicular adenoma", "Follicular adenoma, oxyphilic cell", "Follicular carcinoma, encapsulated", "Follicular carcinoma, minimally invasive", "Follicular carcinoma, moderately differentiated", "Follicular carcinoma, NOS", "Follicular carcinoma, oxyphilic cell", "Follicular carcinoma, trabecular", "Follicular carcinoma, well differentiated", "Follicular dendritic cell sarcoma", "Follicular dendritic cell tumor", "Follicular fibroma", "Follicular lymphoma, grade 1", "Follicular lymphoma, grade 2", "Follicular lymphoma, grade 3", "Follicular lymphoma, grade 3A", "Follicular lymphoma, grade 3B", "Follicular lymphoma, NOS", "Follicular lymphoma, small cleaved cell", "Follicular thyroid carcinoma (FTC), encapsulated angioinvasive", "Folliculome lipidique", "Franklin disease", "G cell tumor, malignant", "G cell tumor, NOS", "Gamma heavy chain disease", "Gangliocytic paraganglioma", "Gangliocytoma", "Ganglioglioma, anaplastic", "Ganglioglioma, NOS", "Ganglioneuroblastoma", "Ganglioneuroma", "Ganglioneuromatosis", "GANT", "Gastrin cell tumor", "Gastrin cell tumor, malignant", "Gastrinoma, malignant", "Gastrinoma, NOS", "Gastrointestinal autonomic nerve tumor", "Gastrointestinal pacemaker cell tumor", "Gastrointestinal stromal sarcoma", "Gastrointestinal stromal tumor, benign", "Gastrointestinal stromal tumor, malignant", "Gastrointestinal stromal tumor, NOS", "Gastrointestinal stromal tumor, uncertain malignant potential", "Gelatinous adenocarcinoma", "Gelatinous carcinoma", "Gemistocytic astrocytoma", "Gemistocytoma", "Genital rhabdomyoma", "Germ cell tumor, nonseminomatous", "Germ cell tumor, NOS", "Germ cell tumors with associated hematological malignancy", "Germinoma", "Ghost cell odontogenic carcinoma", "Giant cell and spindle cell carcinoma", "Giant cell angiofibroma", "Giant cell carcinoma", "Giant cell fibroblastoma", "Giant cell glioblastoma", "Giant cell sarcoma", "Giant cell sarcoma of bone", "Giant cell tumor of bone, malignant", "Giant cell tumor of bone, NOS", "Giant cell tumor of soft parts, NOS", "Giant cell tumor of tendon sheath", "Giant cell tumor of tendon sheath, malignant", "Giant fibroadenoma", "Giant osteoid osteoma", "Giant pigmented nevus, NOS", "Gigantiform cementoma", "GIST, benign", "GIST, malignant", "GIST, NOS", "Glandular intraepithelial neoplasia, grade I", "Glandular intraepithelial neoplasia, grade II", "Glandular intraepithelial neoplasia, grade III", "Glandular intraepithelial neoplasia, high grade", "Glandular intraepithelial neoplasia, low grade", "Glandular papilloma", "Glassy cell carcinoma", "Glioblastoma", "Glioblastoma multiforme", "Glioblastoma with sarcomatous component", "Glioblastoma, IDH wildtype", "Glioblastoma, IDH-mutant", "Gliofibroma", "Glioma, malignant", "Glioma, NOS", "Gliomatosis cerebri", "Glioneuroma", "Gliosarcoma", "Glomangioma", "Glomangiomyoma", "Glomangiosarcoma", "Glomoid sarcoma", "Glomus jugulare tumor, NOS", "Glomus tumor, malignant", "Glomus tumor, NOS", "Glucagon-like peptide-producing tumor", "Glucagonoma, malignant", "Glucagonoma, NOS", "Glycogen-rich carcinoma", "Glycogenic rhabdomyoma", "Goblet cell carcinoid", "Gonadal stromal tumor, NOS", "Gonadoblastoma", "Gonocytoma", "Granular cell adenocarcinoma", "Granular cell carcinoma", "Granular cell myoblastoma, malignant", "Granular cell myoblastoma, NOS", "Granular cell tumor of the sellar region", "Granular cell tumor, malignant", "Granular cell tumor, NOS", "Granulocytic leukemia, NOS", "Granulocytic sarcoma", "Granulosa cell carcinoma", "Granulosa cell tumor, adult type", "Granulosa cell tumor, juvenile", "Granulosa cell tumor, malignant", "Granulosa cell tumor, NOS", "Granulosa cell tumor, sarcomatoid", "Granulosa cell-theca cell tumor", "Grawitz tumor", "Gynandroblastoma", "Haemangioblastoma", "Haemangiosarcoma", "Hairy cell leukaemia variant", "Hairy cell leukemia", "Hairy cell leukemia variant", "Hairy nevus", "Halo nevus", "Hand-Schuller-Christian disease", "Heavy chain disease, NOS", "Hemangioblastic meningioma", "Hemangioendothelial sarcoma", "Hemangioendothelioma, benign", "Hemangioendothelioma, malignant", "Hemangioendothelioma, NOS", "Hemangioma simplex", "Hemangioma, NOS", "Hemangiopericytic meningioma", "Hemangiopericytoma, benign", "Hemangiopericytoma, malignant", "Hemangiopericytoma, NOS", "Hemolymphangioma", "Hepatoblastoma", "Hepatoblastoma, epithelioid", "Hepatoblastoma, mixed epithelial-mesenchymal", "Hepatocarcinoma", "Hepatocellular adenoma", "Hepatocellular carcinoma, clear cell type", "Hepatocellular carcinoma, fibrolamellar", "Hepatocellular carcinoma, NOS", "Hepatocellular carcinoma, pleomorphic type", "Hepatocellular carcinoma, sarcomatoid", "Hepatocellular carcinoma, scirrhous", "Hepatocellular carcinoma, spindle cell variant", "Hepatocholangiocarcinoma", "Hepatoid adenocarcinoma", "Hepatoid carcinoma", "Hepatoid yolk sac tumor", "Hepatoma, benign", "Hepatoma, malignant", "Hepatoma, NOS", "Hepatosplenic gamma-delta cell lymphoma", "Hepatosplenic T-cell lymphoma", "Hereditary leiomyomatosis & RCC-associated renal cell carcinoma", "Hibernoma", "Hidradenocarcinoma", "Hidradenoma papilliferum", "Hidradenoma, NOS", "Hidrocystoma", "High grade surface osteosarcoma", "High-grade neuroendocrine carcinoma", "High-grade serous carcinoma", "Hilar cell tumor", "Hilus cell tumor", "Histiocyte-rich large B-cell lymphoma", "Histiocytic medullary reticulosis", "Histiocytic sarcoma", "Histiocytoid hemangioma", "Histiocytoma, NOS", "Histiocytosis X, NOS", "Hodgkin disease, lymphocyte predominance, diffuse", "Hodgkin disease, lymphocyte predominance, NOS", "Hodgkin disease, lymphocytic-histiocytic predominance", "Hodgkin disease, nodular sclerosis, lymphocyte depletion", "Hodgkin disease, nodular sclerosis, lymphocyte predominance", "Hodgkin disease, nodular sclerosis, mixed cellularity", "Hodgkin disease, nodular sclerosis, NOS", "Hodgkin disease, nodular sclerosis, syncytial variant", "Hodgkin disease, NOS", "Hodgkin granuloma", "Hodgkin lymphoma, lymphocyte depletion, diffuse fibrosis", "Hodgkin lymphoma, lymphocyte depletion, NOS", "Hodgkin lymphoma, lymphocyte depletion, reticular", "Hodgkin lymphoma, lymphocyte predominance, nodular", "Hodgkin lymphoma, lymphocyte-rich", "Hodgkin lymphoma, mixed cellularity, NOS", "Hodgkin lymphoma, nodular lymphocyte predominance", "Hodgkin lymphoma, nodular sclerosis, cellular phase", "Hodgkin lymphoma, nodular sclerosis, grade 1", "Hodgkin lymphoma, nodular sclerosis, grade 2", "Hodgkin lymphoma, nodular sclerosis, NOS", "Hodgkin lymphoma, NOS", "Hodgkin paragranuloma, nodular", "Hodgkin paragranuloma, NOS", "Hodgkin sarcoma", "Hurthle cell adenocarcinoma", "Hurthle cell adenoma", "Hurthle cell carcinoma", "Hurthle cell tumor", "Hutchinson"

<br>Attribute Name: primary\_gleason\_grade
<br>Description: The text term used to describe the primary Gleason score, which describes the pattern of cells making up the largest area of the tumor. The primary and secondary Gleason pattern grades are combined to determine the patient's Gleason grade group, which is used to determine the aggresiveness of prostate cancer. Note that this grade describes the entire prostatectomy specimen and is not specific to the sample used for sequencing.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Pattern 1", "Pattern 2", "Pattern 3", "Pattern 4", "Pattern 5"

<br>Attribute Name: prior\_malignancy
<br>Description: The yes/no/unknown indicator used to describe the patient's history of prior cancer diagnosis.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "yes", "no", "unknown", "not reported", "Not Allowed To Collect"

<br>Attribute Name: prior\_treatment
<br>Description: A yes/no/unknown/not applicable indicator related to the administration of therapeutic agents received before the body specimen was collected.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Yes", "No", "Unknown", "Not Reported", "Not Allowed To Collect"

<br>Attribute Name: progression\_free\_survival
<br>Description: Number of days between the date used for index and the first date the patient is known to be free of disease progression.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: progression\_free\_survival\_event
<br>Description: The event used to define the patient''s disease progression.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: progression\_or\_recurrence
<br>Description: Yes/No/Unknown indicator to identify whether a patient has had a new tumor event after initial treatment.
<br>Attribute of Node: diagnosis, follow\_up
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Yes", "No", "Unknown", "Not Reported"

<br>Attribute Name: residual\_disease
<br>Description: Text terms to describe the status of a tissue margin following surgical resection.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "R0", "R1", "R2", "RX", "Unknown", "Not Reported"

<br>Attribute Name: secondary\_gleason\_grade
<br>Description: The text term used to describe the secondary Gleason score, which describes the pattern of cells making up the second largest area of the tumor. The primary and secondary Gleason pattern grades are combined to determine the patient's Gleason grade group, which is used to determine the aggresiveness of prostate cancer. Note that this grade describes the entire prostatectomy specimen and is not specific to the sample used for sequencing.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Pattern 1", "Pattern 2", "Pattern 3", "Pattern 4", "Pattern 5"

<br>Attribute Name: site\_of\_resection\_or\_biopsy
<br>Description: The text term used to describe the anatomic site of origin, of the patient's malignant disease, as described by the World Health Organization's (WHO) International Classification of Diseases for Oncology (ICD-O).
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Abdomen, NOS", "Abdominal esophagus", "Accessory sinus, NOS", "Acoustic nerve", "Adrenal gland, NOS", "Ampulla of Vater", "Anal canal", "Anterior 2/3 of tongue, NOS", "Anterior floor of mouth", "Anterior mediastinum", "Anterior surface of epiglottis", "Anterior wall of bladder", "Anterior wall of nasopharynx", "Anus, NOS", "Aortic body and other paraganglia", "Appendix", "Ascending colon", "Autonomic nervous system, NOS", "Axillary tail of breast", "Base of tongue, NOS", "Biliary tract, NOS", "Bladder neck", "Bladder, NOS", "Blood", "Body of pancreas", "Body of penis", "Body of stomach", "Bone marrow", "Bone of limb, NOS", "Bone, NOS", "Bones of skull and face and associated joints", "Border of tongue", "Brain stem", "Brain, NOS", "Branchial cleft", "Breast, NOS", "Broad ligament", "Cardia, NOS", "Carotid body", "Cauda equina", "Cecum", "Central portion of breast", "Cerebellum, NOS", "Cerebral meninges", "Cerebrum", "Cervical esophagus", "Cervix uteri", "Cheek mucosa", "Choroid", "Ciliary body", "Clitoris", "Cloacogenic zone", "Colon, NOS", "Commissure of lip", "Conjunctiva", "Connective, subcutaneous and other soft tissues of abdomen", "Connective, subcutaneous and other soft tissues of head, face, and neck", "Connective, subcutaneous and other soft tissues of lower limb and hip", "Connective, subcutaneous and other soft tissues of pelvis", "Connective, subcutaneous and other soft tissues of thorax", "Connective, subcutaneous and other soft tissues of trunk, NOS", "Connective, subcutaneous and other soft tissues of upper limb and shoulder", "Connective, subcutaneous and other soft tissues, NOS", "Cornea, NOS", "Corpus uteri", "Cortex of adrenal gland", "Cranial nerve, NOS", "Craniopharyngeal duct", "Descended testis", "Descending colon", "Dome of bladder", "Dorsal surface of tongue, NOS", "Duodenum", "Endocervix", "Endocrine gland, NOS", "Endometrium", "Epididymis", "Esophagus, NOS", "Ethmoid sinus", "Exocervix", "External ear", "External lip, NOS", "External lower lip", "External upper lip", "Extrahepatic bile duct", "Eye, NOS", "Eyelid", "Fallopian tube", "Female genital tract, NOS", "Floor of mouth, NOS", "Frontal lobe", "Frontal sinus", "Fundus of stomach", "Fundus uteri", "Gallbladder", "Gastric antrum", "Gastrointestinal tract, NOS", "Glans penis", "Glottis", "Greater curvature of stomach, NOS", "Gum, NOS", "Hard palate", "Head of pancreas", "Head, face or neck, NOS", "Heart", "Hematopoietic system, NOS", "Hepatic flexure of colon", "Hypopharyngeal aspect of aryepiglottic fold", "Hypopharynx, NOS", "Ileum", "Ill-defined sites within respiratory system", "Intestinal tract, NOS", "Intra-abdominal lymph nodes", "Intrahepatic bile duct", "Intrathoracic lymph nodes", "Islets of Langerhans", "Isthmus uteri", "Jejunum", "Kidney, NOS", "Labium majus", "Labium minus", "Lacrimal gland", "Laryngeal cartilage", "Larynx, NOS", "Lateral floor of mouth", "Lateral wall of bladder", "Lateral wall of nasopharynx", "Lateral wall of oropharynx", "Lesser curvature of stomach, NOS", "Lingual tonsil", "Lip, NOS", "Liver", "Long bones of lower limb and associated joints", "Long bones of upper limb, scapula and associated joints", "Lower gum", "Lower limb, NOS", "Lower lobe, lung", "Lower third of esophagus", "Lower-inner quadrant of breast", "Lower-outer quadrant of breast", "Lung, NOS", "Lymph node, NOS", "Lymph nodes of axilla or arm", "Lymph nodes of head, face and neck", "Lymph nodes of inguinal region or leg", "Lymph nodes of multiple regions", "Main bronchus", "Major salivary gland, NOS", "Male genital organs, NOS", "Mandible", "Maxillary sinus", "Meckel diverticulum", "Mediastinum, NOS", "Medulla of adrenal gland", "Meninges, NOS", "Middle ear", "Middle lobe, lung", "Middle third of esophagus", "Mouth, NOS", "Mucosa of lip, NOS", "Mucosa of lower lip", "Mucosa of upper lip", "Myometrium", "Nasal cavity", "Nasopharynx, NOS", "Nervous system, NOS", "Nipple", "Occipital lobe", "Olfactory nerve", "Optic nerve", "Orbit, NOS", "Oropharynx, NOS", "Other ill-defined sites", "Other specified parts of female genital organs", "Other specified parts of male genital organs", "Other specified parts of pancreas", "Ovary", "Overlapping lesion of accessory sinuses", "Overlapping lesion of biliary tract", "Overlapping lesion of bladder", "Overlapping lesion of bones, joints and articular cartilage", "Overlapping lesion of bones, joints and articular cartilage of limbs", "Overlapping lesion of brain", "Overlapping lesion of brain and central nervous system", "Overlapping lesion of breast", "Overlapping lesion of cervix uteri", "Overlapping lesion of colon", "Overlapping lesion of connective, subcutaneous and other soft tissues", "Overlapping lesion of corpus uteri", "Overlapping lesion of digestive system", "Overlapping lesion of endocrine glands and related structures", "Overlapping lesion of esophagus", "Overlapping lesion of eye and adnexa", "Overlapping lesion of female genital organs", "Overlapping lesion of floor of mouth", "Overlapping lesion of heart, mediastinum and pleura", "Overlapping lesion of hypopharynx", "Overlapping lesion of ill-defined sites", "Overlapping lesion of larynx", "Overlapping lesion of lip", "Overlapping lesion of lip, oral cavity and pharynx", "Overlapping lesion of lung", "Overlapping lesion of major salivary glands", "Overlapping lesion of male genital organs", "Overlapping lesion of nasopharynx", "Overlapping lesion of other and unspecified parts of mouth", "Overlapping lesion of palate", "Overlapping lesion of pancreas", "Overlapping lesion of penis", "Overlapping lesion of peripheral nerves and autonomic nervous system", "Overlapping lesion of rectum, anus and anal canal", "Overlapping lesion of respiratory system and intrathoracic organs", "Overlapping lesion of retroperitoneum and peritoneum", "Overlapping lesion of skin", "Overlapping lesion of small intestine", "Overlapping lesion of stomach", "Overlapping lesion of tongue", "Overlapping lesion of tonsil", "Overlapping lesion of urinary organs", "Overlapping lesion of vulva", "Overlapping lesions of oropharynx", "Palate, NOS", "Pancreas, NOS", "Pancreatic duct", "Parametrium", "Parathyroid gland", "Paraurethral gland", "Parietal lobe", "Parotid gland", "Pelvic bones, sacrum, coccyx and associated joints", "Pelvic lymph nodes", "Pelvis, NOS", "Penis, NOS", "Peripheral nerves and autonomic nervous system of abdomen", "Peripheral nerves and autonomic nervous system of head, face, and neck", "Peripheral nerves and autonomic nervous system of lower limb and hip", "Peripheral nerves and autonomic nervous system of pelvis", "Peripheral nerves and autonomic nervous system of thorax", "Peripheral nerves and autonomic nervous system of trunk, NOS", "Peripheral nerves and autonomic nervous system of upper limb and shoulder", "Peritoneum, NOS", "Pharynx, NOS", "Pineal gland", "Pituitary gland", "Placenta", "Pleura, NOS", "Postcricoid region", "Posterior mediastinum", "Posterior wall of bladder", "Posterior wall of hypopharynx", "Posterior wall of nasopharynx", "Posterior wall of oropharynx", "Prepuce", "Prostate gland", "Pylorus", "Pyriform sinus", "Rectosigmoid junction", "Rectum, NOS", "Renal pelvis", "Reticuloendothelial system, NOS", "Retina", "Retromolar area", "Retroperitoneum", "Rib, sternum, clavicle and associated joints", "Round ligament", "Scrotum, NOS", "Short bones of lower limb and associated joints", "Short bones of upper limb and associated joints", "Sigmoid colon", "Skin of lip, NOS", "Skin of lower limb and hip", "Skin of other and unspecified parts of face", "Skin of scalp and neck", "Skin of trunk", "Skin of upper limb and shoulder", "Skin, NOS", "Small intestine, NOS", "Soft palate, NOS", "Specified parts of peritoneum", "Spermatic cord", "Sphenoid sinus", "Spinal cord", "Spinal meninges", "Spleen", "Splenic flexure of colon", "Stomach, NOS", "Subglottis", "Sublingual gland", "Submandibular gland", "Superior wall of nasopharynx", "Supraglottis", "Tail of pancreas", "Temporal lobe", "Testis, NOS", "Thoracic esophagus", "Thorax, NOS", "Thymus", "Thyroid gland", "Tongue, NOS", "Tonsil, NOS", "Tonsillar fossa", "Tonsillar pillar", "Trachea", "Transverse colon", "Trigone of bladder", "Undescended testis", "Unknown primary site", "Upper gum", "Upper limb, NOS", "Upper lobe, lung", "Upper respiratory tract, NOS", "Upper third of esophagus", "Upper-inner quadrant of breast", "Upper-outer quadrant of breast", "Urachus", "Ureter", "Ureteric orifice", "Urethra", "Urinary system, NOS", "Uterine adnexa", "Uterus, NOS", "Uvula", "Vagina, NOS", "Vallecula", "Ventral surface of tongue, NOS", "Ventricle, NOS", "Vertebral column", "Vestibule of mouth", "Vulva, NOS", "Waldeyer ring", "Unknown", "Not Reported"

<br>Attribute Name: supratentorial\_localization
<br>Description: Text term to specify the location of the supratentorial tumor.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Cerebral Cortex", "Deep Gray (e.g. Basal Ganglia, Thalamus)", "Spinal Cord", "White Matter", "Unknown", "Not Reported"

<br>Attribute Name: synchronous\_malignancy
<br>Description: A yes/no/unknown indicator used to describe whether the patient had an additional malignant diagnosis at the same time the tumor used for sequencing was diagnosed. If both tumors were sequenced, both tumors would have synchronous malignancies.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Yes", "No", "Unknown", "Not Reported"

<br>Attribute Name: tissue\_or\_organ\_of\_origin
<br>Description: The text term used to describe the anatomic site of origin, of the patient's malignant disease, as described by the World Health Organization's (WHO) International Classification of Diseases for Oncology (ICD-O).
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Abdomen, NOS", "Abdominal esophagus", "Accessory sinus, NOS", "Acoustic nerve", "Adrenal gland, NOS", "Ampulla of Vater", "Anal canal", "Anterior 2/3 of tongue, NOS", "Anterior floor of mouth", "Anterior mediastinum", "Anterior surface of epiglottis", "Anterior wall of bladder", "Anterior wall of nasopharynx", "Anus, NOS", "Aortic body and other paraganglia", "Appendix", "Ascending colon", "Autonomic nervous system, NOS", "Axillary tail of breast", "Base of tongue, NOS", "Biliary tract, NOS", "Bladder neck", "Bladder, NOS", "Blood", "Body of pancreas", "Body of penis", "Body of stomach", "Bone marrow", "Bone of limb, NOS", "Bone, NOS", "Bones of skull and face and associated joints", "Border of tongue", "Brain stem", "Brain, NOS", "Branchial cleft", "Breast, NOS", "Broad ligament", "Cardia, NOS", "Carotid body", "Cauda equina", "Cecum", "Central portion of breast", "Cerebellum, NOS", "Cerebral meninges", "Cerebrum", "Cervical esophagus", "Cervix uteri", "Cheek mucosa", "Choroid", "Ciliary body", "Clitoris", "Cloacogenic zone", "Colon, NOS", "Commissure of lip", "Conjunctiva", "Connective, subcutaneous and other soft tissues of abdomen", "Connective, subcutaneous and other soft tissues of head, face, and neck", "Connective, subcutaneous and other soft tissues of lower limb and hip", "Connective, subcutaneous and other soft tissues of pelvis", "Connective, subcutaneous and other soft tissues of thorax", "Connective, subcutaneous and other soft tissues of trunk, NOS", "Connective, subcutaneous and other soft tissues of upper limb and shoulder", "Connective, subcutaneous and other soft tissues, NOS", "Cornea, NOS", "Corpus uteri", "Cortex of adrenal gland", "Cranial nerve, NOS", "Craniopharyngeal duct", "Descended testis", "Descending colon", "Dome of bladder", "Dorsal surface of tongue, NOS", "Duodenum", "Endocervix", "Endocrine gland, NOS", "Endometrium", "Epididymis", "Esophagus, NOS", "Ethmoid sinus", "Exocervix", "External ear", "External lip, NOS", "External lower lip", "External upper lip", "Extrahepatic bile duct", "Eye, NOS", "Eyelid", "Fallopian tube", "Female genital tract, NOS", "Floor of mouth, NOS", "Frontal lobe", "Frontal sinus", "Fundus of stomach", "Fundus uteri", "Gallbladder", "Gastric antrum", "Gastrointestinal tract, NOS", "Glans penis", "Glottis", "Greater curvature of stomach, NOS", "Gum, NOS", "Hard palate", "Head of pancreas", "Head, face or neck, NOS", "Heart", "Hematopoietic system, NOS", "Hepatic flexure of colon", "Hypopharyngeal aspect of aryepiglottic fold", "Hypopharynx, NOS", "Ileum", "Ill-defined sites within respiratory system", "Intestinal tract, NOS", "Intra-abdominal lymph nodes", "Intrahepatic bile duct", "Intrathoracic lymph nodes", "Islets of Langerhans", "Isthmus uteri", "Jejunum", "Kidney, NOS", "Labium majus", "Labium minus", "Lacrimal gland", "Laryngeal cartilage", "Laryngeal Commissure", "Larynx, NOS", "Lateral floor of mouth", "Lateral wall of bladder", "Lateral wall of nasopharynx", "Lateral wall of oropharynx", "Lesser curvature of stomach, NOS", "Lingual tonsil", "Lip, NOS", "Liver", "Long bones of lower limb and associated joints", "Long bones of upper limb, scapula and associated joints", "Lower gum", "Lower limb, NOS", "Lower lobe, lung", "Lower third of esophagus", "Lower-inner quadrant of breast", "Lower-outer quadrant of breast", "Lung, NOS", "Lymph node, NOS", "Lymph nodes of axilla or arm", "Lymph nodes of head, face and neck", "Lymph nodes of inguinal region or leg", "Lymph nodes of multiple regions", "Main bronchus", "Major salivary gland, NOS", "Male genital organs, NOS", "Mandible", "Maxillary sinus", "Meckel diverticulum", "Mediastinum, NOS", "Medulla of adrenal gland", "Meninges, NOS", "Middle ear", "Middle lobe, lung", "Middle third of esophagus", "Mouth, NOS", "Mucosa of lip, NOS", "Mucosa of lower lip", "Mucosa of upper lip", "Myometrium", "Nasal cavity", "Nasopharynx, NOS", "Nervous system, NOS", "Nipple", "Occipital lobe", "Olfactory nerve", "Optic nerve", "Orbit, NOS", "Oropharynx, NOS", "Other ill-defined sites", "Other specified parts of female genital organs", "Other specified parts of male genital organs", "Other specified parts of pancreas", "Ovary", "Overlapping lesion of accessory sinuses", "Overlapping lesion of biliary tract", "Overlapping lesion of bladder", "Overlapping lesion of bones, joints and articular cartilage", "Overlapping lesion of bones, joints and articular cartilage of limbs", "Overlapping lesion of brain", "Overlapping lesion of brain and central nervous system", "Overlapping lesion of breast", "Overlapping lesion of cervix uteri", "Overlapping lesion of colon", "Overlapping lesion of connective, subcutaneous and other soft tissues", "Overlapping lesion of corpus uteri", "Overlapping lesion of digestive system", "Overlapping lesion of endocrine glands and related structures", "Overlapping lesion of esophagus", "Overlapping lesion of eye and adnexa", "Overlapping lesion of female genital organs", "Overlapping lesion of floor of mouth", "Overlapping lesion of heart, mediastinum and pleura", "Overlapping lesion of hypopharynx", "Overlapping lesion of ill-defined sites", "Overlapping lesion of larynx", "Overlapping lesion of lip", "Overlapping lesion of lip, oral cavity and pharynx", "Overlapping lesion of lung", "Overlapping lesion of major salivary glands", "Overlapping lesion of male genital organs", "Overlapping lesion of nasopharynx", "Overlapping lesion of other and unspecified parts of mouth", "Overlapping lesion of palate", "Overlapping lesion of pancreas", "Overlapping lesion of penis", "Overlapping lesion of peripheral nerves and autonomic nervous system", "Overlapping lesion of rectum, anus and anal canal", "Overlapping lesion of respiratory system and intrathoracic organs", "Overlapping lesion of retroperitoneum and peritoneum", "Overlapping lesion of skin", "Overlapping lesion of small intestine", "Overlapping lesion of stomach", "Overlapping lesion of tongue", "Overlapping lesion of tonsil", "Overlapping lesion of urinary organs", "Overlapping lesion of vulva", "Overlapping lesions of oropharynx", "Palate, NOS", "Pancreas, NOS", "Pancreatic duct", "Parametrium", "Parathyroid gland", "Paraurethral gland", "Parietal lobe", "Parotid gland", "Pelvic bones, sacrum, coccyx and associated joints", "Pelvic lymph nodes", "Pelvis, NOS", "Penis, NOS", "Peripheral nerves and autonomic nervous system of abdomen", "Peripheral nerves and autonomic nervous system of head, face, and neck", "Peripheral nerves and autonomic nervous system of lower limb and hip", "Peripheral nerves and autonomic nervous system of pelvis", "Peripheral nerves and autonomic nervous system of thorax", "Peripheral nerves and autonomic nervous system of trunk, NOS", "Peripheral nerves and autonomic nervous system of upper limb and shoulder", "Peritoneum, NOS", "Pharynx, NOS", "Pineal gland", "Pituitary gland", "Placenta", "Pleura, NOS", "Postcricoid region", "Posterior mediastinum", "Posterior wall of bladder", "Posterior wall of hypopharynx", "Posterior wall of nasopharynx", "Posterior wall of oropharynx", "Prepuce", "Prostate gland", "Pylorus", "Pyriform sinus", "Rectosigmoid junction", "Rectum, NOS", "Renal pelvis", "Reticuloendothelial system, NOS", "Retina", "Retromolar area", "Retroperitoneum", "Rib, sternum, clavicle and associated joints", "Round ligament", "Scrotum, NOS", "Short bones of lower limb and associated joints", "Short bones of upper limb and associated joints", "Sigmoid colon", "Skin of lip, NOS", "Skin of lower limb and hip", "Skin of other and unspecified parts of face", "Skin of scalp and neck", "Skin of trunk", "Skin of upper limb and shoulder", "Skin, NOS", "Small intestine, NOS", "Soft palate, NOS", "Specified parts of peritoneum", "Spermatic cord", "Sphenoid sinus", "Spinal cord", "Spinal meninges", "Spleen", "Splenic flexure of colon", "Stomach, NOS", "Subglottis", "Sublingual gland", "Submandibular gland", "Superior wall of nasopharynx", "Supraglottis", "Tail of pancreas", "Temporal lobe", "Testis, NOS", "Thoracic esophagus", "Thorax, NOS", "Thymus", "Thyroid gland", "Tongue, NOS", "Tonsil, NOS", "Tonsillar fossa", "Tonsillar pillar", "Trachea", "Transverse colon", "Trigone of bladder", "Undescended testis", "Unknown primary site", "Upper Gum", "Upper limb, NOS", "Upper lobe, lung", "Upper respiratory tract, NOS", "Upper third of esophagus", "Upper-inner quadrant of breast", "Upper-outer quadrant of breast", "Urachus", "Ureter", "Ureteric orifice", "Urethra", "Urinary system, NOS", "Uterine adnexa", "Uterus, NOS", "Uvula", "Vagina, NOS", "Vallecula", "Ventral surface of tongue, NOS", "Ventricle, NOS", "Vertebral column", "Vestibule of mouth", "Vulva, NOS", "Waldeyer ring", "Unknown", "Not Reported"

<br>Attribute Name: treatment\_data
<br>Description: Indicator as to whether treatment data for the patient exists.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Yes", "No"

<br>Attribute Name: tumor\_confined\_to\_organ\_of\_origin
<br>Description: The yes/no/unknown indicator used to describe whether the tumor is confined to the organ where it originated and did not spread to a proximal or distant location within the body.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Yes", "No", "Unknown", "Not Reported"

<br>Attribute Name: tumor\_focality
<br>Description: The text term used to describe whether the patient's disease originated in a single location or multiple locations.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Multifocal", "Unifocal", "Unknown", "Not Reported"

<br>Attribute Name: tumor\_regression\_grade
<br>Description: A numeric value used to measure therapeutic response of the primary tumor and predict patient outcomes based on a three-point tumor regression grading system.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "0", "1", "2", "3", "Unknown", "Not Reported"

<br>Attribute Name: tumor\_stage
<br>Description: The extent of a cancer in the body. Staging is usually based on the size of the tumor, whether lymph nodes contain cancer, and whether the cancer has spread from the original site to other parts of the body. The accepted values for tumor\_stage depend on the tumor site, type, and accepted staging system. These items should accompany the tumor\_stage value as associated metadata.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: vascular\_invasion\_present
<br>Description: The yes/no indicator to ask if large vessel or venous invasion was detected by surgery or presence in a tumor specimen.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Yes", "No", "Unknown", "Not Reported", "Not Allowed To Collect"

<br>Attribute Name: vascular\_invasion\_type
<br>Description: Text term that represents the type of vascular tumor invasion.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Extramural", "Intramural", "Macro", "Micro", "No Vascular Invasion", "Unknown", "Not Reported"

<br>Attribute Name: weiss\_assessment\_score
<br>Description: The text term used to describe the overall Weiss assessment score, a commonly used assessment describing the malignancy of adrenocortical tumors. The Weiss score is determined based on nine histological criteria including the following- high nuclear grade, mitotic rate greater than five per 50 high power fields (HPF), atypical mitotic figures, eosinophilic tumor cell cytoplasm (greater than 75% tumor cells), diffuse architecture (greater than 33% of tumor), necrosis, venous invasion, sinusoidal invasion, and capsular invasion.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"

<br>Attribute Name: wilms\_tumor\_histologic\_subtype
<br>Description: The text term used to describe the classification of Wilms tumors distinguishing between favorable and unfavorable histologic groups.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Favorable", "Unfavorable", "Unknown", "Not Reported"

<br>Attribute Name: year\_of\_diagnosis
<br>Description: Numeric value to represent the year of an individual's initial pathologic diagnosis of cancer.
<br>Attribute of Node: diagnosis
<br>Required: false
<br>Type: integer
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: follow\_up\_id
<br>Description: A unique id assigned by the data commons to the follow\_up node.
<br>Attribute of Node: follow\_up
<br>Required: true
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: days\_to\_progression
<br>Description: Number of days between the date used for index and the date the patient's disease progressed.
<br>Attribute of Node: follow\_up
<br>Required: false
<br>Type: integer
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: dfs\_event\_indicator
<br>Description: Disease Free Survival event indicator.
<br>Attribute of Node: follow\_up
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "DFS event reported (dfs is time of first DFS event)", "No DFS event"

<br>Attribute Name: days\_to\_distant\_recurrence
<br>Description: Distant recurrence-free interval- Days from registration to first distant recurrence or last disease evaluation.
<br>Attribute of Node: follow\_up
<br>Required: false
<br>Type: integer
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: distant\_recurrence\_indicator
<br>Description: Distant recurrence indicator.
<br>Attribute of Node: follow\_up
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Distant recurrence (drfi is time of distant recurrence)", "No distant recurrence"

<br>Attribute Name: recurrence\_free\_indicator
<br>Description: Recurrence indicator.
<br>Attribute of Node: follow\_up
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Recurrence (rfi is time of recurrence)", "No recurrence"

<br>Attribute Name: dfs\_event\_type
<br>Description: Type of first DFS event.
<br>Attribute of Node: follow\_up
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Ipsilateral breast recurrence", "Recurrence at local-regional site", "Recurrence at distant site (includes concurrent distant and local-regional)", "New cancer of the opposite breast", "New primary cancer at other than breast or non-melanoma skin cancer", "Death without another event reported", "No recurrence"

<br>Attribute Name: first\_recurrence\_type
<br>Description: Type of first recurrence
<br>Attribute of Node: follow\_up
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Ipsilateral breast recurrence", "Recurrence at local-regional site", "Recurrence at distant site (includes concurrent distant and local-regional)", "No recurrence"

<br>Attribute Name: adverse\_event
<br>Description: Text that represents the Common Terminology Criteria for Adverse Events low level term name for an adverse event.
<br>Attribute of Node: follow\_up
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Abdominal Distension", "Abdominal Infection", "Abdominal Pain", "Abdominal Soft Tissue Necrosis", "Abducens Nerve Disorder", "Accessory Nerve Disorder", "Acidosis", "Acoustic Nerve Disorder NOS", "Activated Partial Thromboplastin Time Prolonged", "Acute Coronary Syndrome", "Acute Kidney Injury", "Adrenal Insufficiency", "Adult Respiratory Distress Syndrome", "Agitation", "Akathisia", "Alanine Aminotransferase Increased", "Alcohol Intolerance", "Alkaline Phosphatase Increased", "Alkalosis", "Allergic Reaction", "Allergic Rhinitis", "Alopecia", "Amnesia", "Anal Fistula", "Anal Hemorrhage", "Anal Mucositis", "Anal Necrosis", "Anal Pain", "Anal Stenosis", "Anal Ulcer", "Anaphylaxis", "Anemia", "Ankle Fracture", "Anorectal Infection", "Anorexia", "Anorgasmia", "Anxiety", "Aortic Injury", "Aortic Valve Disease", "Aphonia", "Apnea", "Appendicitis", "Appendicitis Perforated", "Arachnoiditis", "Arterial Injury", "Arteritis Infective", "Arthralgia", "Arthritis", "Ascites", "Aspartate Aminotransferase Increased", "Aspiration", "Asystole", "Ataxia", "Atelectasis", "Atrial Fibrillation", "Atrial Flutter", "Atrioventricular Block Complete", "Atrioventricular Block First Degree", "Autoimmune Disorder", "Avascular Necrosis", "Azoospermia", "Back Pain", "Bile Duct Stenosis", "Biliary Anastomotic Leak", "Biliary Fistula", "Biliary Tract Infection", "Bladder Anastomotic Leak", "Bladder Infection", "Bladder Perforation", "Bladder Spasm", "Bloating", "Blood and Lymphatic System Disorders - Other", "Blood Antidiuretic Hormone Abnormal", "Blood Bilirubin Increased", "Blood Corticotrophin Decreased", "Blood Gonadotrophin Abnormal", "Blood Prolactin Abnormal", "Blurred Vision", "Body Odor", "Bone Infection", "Bone Marrow Hypocellular", "Bone Pain", "Brachial Plexopathy", "Breast Atrophy", "Breast Infection", "Breast Pain", "Bronchial Fistula", "Bronchial Infection", "Bronchial Obstruction", "Bronchial Stricture", "Bronchopleural Fistula", "Bronchopulmonary Hemorrhage", "Bronchospasm", "Bruising", "Bullous Dermatitis", "Burn", "Buttock Pain", "Capillary Leak Syndrome", "Carbon Monoxide Diffusing Capacity Decreased", "Cardiac Arrest", "Cardiac Disorders - Other", "Cardiac Troponin I Increased", "Cardiac Troponin T Increased", "Cataract", "Catheter Related Infection", "CD4 Lymphocytes Decreased", "Cecal Hemorrhage", "Cecal Infection", "Central Nervous System Necrosis", "Cerebrospinal Fluid Leakage", "Cervicitis Infection", "Cheilitis", "Chest Pain - Cardiac", "Chest Wall Pain", "Chills", "Cholecystitis", "Cholesterol High", "Chronic Kidney Disease", "Chylothorax", "Cognitive Disturbance", "Colitis", "Colonic Fistula", "Colonic Hemorrhage", "Colonic Obstruction", "Colonic Perforation", "Colonic Stenosis", "Colonic Ulcer", "Concentration Impairment", "Conduction Disorder", "Confusion", "Congenital, Familial and Genetic Disorders - Other", "Conjunctivitis", "Conjunctivitis Infective", "Constipation", "Constrictive Pericarditis", "Corneal Infection", "Corneal Ulcer", "Cough", "CPK Increased", "Cranial Nerve Infection", "Creatinine Increased", "Cushingoid", "Cystitis Noninfective", "Cytokine Release Syndrome", "Death Neonatal", "Death NOS", "Dehydration", "Delayed Orgasm", "Delayed Puberty", "Delirium", "Delusions", "Dental Caries", "Depressed Level of Consciousness", "Depression", "Dermatitis Radiation", "Device Related Infection", "Diarrhea", "Disseminated Intravascular Coagulation", "Dizziness", "Dry Eye", "Dry Mouth", "Dry Skin", "Duodenal Fistula", "Duodenal Hemorrhage", "Duodenal Infection", "Duodenal Obstruction", "Duodenal Perforation", "Duodenal Stenosis", "Duodenal Ulcer", "Dysarthria", "Dysesthesia", "Dysgeusia", "Dysmenorrhea", "Dyspareunia", "Dyspepsia", "Dysphagia", "Dysphasia", "Dyspnea", "Ear and Labyrinth Disorders - Other", "Ear Pain", "Edema Cerebral", "Edema Face", "Edema Limbs", "Edema Trunk", "Ejaculation Disorder", "Ejection Fraction Decreased", "Electrocardiogram QT Corrected Interval Prolonged", "Encephalitis Infection", "Encephalomyelitis Infection", "Encephalopathy", "Endocarditis Infective", "Endocrine Disorders - Other", "Endophthalmitis", "Enterocolitis", "Enterocolitis Infectious", "Enterovesical Fistula", "Epistaxis", "Erectile Dysfunction", "Erythema Multiforme", "Erythroderma", "Esophageal Anastomotic Leak", "Esophageal Fistula", "Esophageal Hemorrhage", "Esophageal Infection", "Esophageal Necrosis", "Esophageal Obstruction", "Esophageal Pain", "Esophageal Perforation", "Esophageal Stenosis", "Esophageal Ulcer", "Esophageal Varices Hemorrhage", "Esophagitis", "Euphoria", "Exostosis", "External Ear Inflammation", "External Ear Pain", "Extraocular Muscle Paresis", "Extrapyramidal Disorder", "Eye Disorders - Other", "Eye Infection", "Eye Pain", "Eyelid Function Disorder", "Facial Muscle Weakness", "Facial Nerve Disorder", "Facial Pain", "Fall", "Fallopian Tube Anastomotic Leak", "Fallopian Tube Obstruction", "Fallopian Tube Perforation", "Fallopian Tube Stenosis", "Fat Atrophy", "Fatigue", "Febrile Neutropenia", "Fecal Incontinence", "Female Genital Tract Fistula", "Feminization Acquired", "Fetal Death", "Fetal Growth Retardation", "Fever", "Fibrinogen Decreased", "Fibrosis Deep Connective Tissue", "Flank Pain", "Flashing Lights", "Flatulence", "Floaters", "Flu Like Symptoms", "Flushing", "Forced Expiratory Volume Decreased", "Fracture", "Gait Disturbance", "Gallbladder Fistula", "Gallbladder Infection", "Gallbladder Necrosis", "Gallbladder Obstruction", "Gallbladder Pain", "Gallbladder Perforation", "Gastric Anastomotic Leak", "Gastric Fistula", "Gastric Hemorrhage", "Gastric Necrosis", "Gastric Perforation", "Gastric Stenosis", "Gastric Ulcer", "Gastritis", "Gastroesophageal Reflux Disease", "Gastrointestinal Anastomotic Leak", "Gastrointestinal Disorders - Other", "Gastrointestinal Fistula", "Gastrointestinal Pain", "Gastrointestinal Stoma Necrosis", "Gastroparesis", "General Disorders and Administration Site Conditions - Other", "Generalized Muscle Weakness", "Genital Edema", "GGT Increased", "Gingival Pain", "Glaucoma", "Glossopharyngeal Nerve Disorder", "Glucose Intolerance", "Growth Accelerated", "Growth Hormone Abnormal", "Growth Suppression", "Gum Infection", "Gynecomastia", "Hallucinations", "Haptoglobin Decreased", "Head Soft Tissue Necrosis", "Headache", "Hearing Impaired", "Heart Failure", "Hematoma", "Hematosalpinx", "Hematuria", "Hemoglobin Increased", "Hemoglobinuria", "Hemolysis", "Hemolytic Uremic Syndrome", "Hemorrhoidal Hemorrhage", "Hemorrhoids", "Hepatic Failure", "Hepatic Hemorrhage", "Hepatic Infection", "Hepatic Necrosis", "Hepatic Pain", "Hepatitis Viral", "Hepatobiliary Disorders - Other", "Hiccups", "Hip Fracture", "Hirsutism", "Hoarseness", "Hot Flashes", "Hydrocephalus", "Hypercalcemia", "Hyperglycemia", "Hyperhidrosis", "Hyperkalemia", "Hypermagnesemia", "Hypernatremia", "Hyperparathyroidism", "Hypersomnia", "Hypertension", "Hyperthyroidism", "Hypertrichosis", "Hypertriglyceridemia", "Hyperuricemia", "Hypoalbuminemia", "Hypocalcemia", "Hypoglossal Nerve Disorder", "Hypoglycemia", "Hypohidrosis", "Hypokalemia", "Hypomagnesemia", "Hyponatremia", "Hypoparathyroidism", "Hypophosphatemia", "Hypotension", "Hypothermia", "Hypothyroidism", "Hypoxia", "Ileal Fistula", "Ileal Hemorrhage", "Ileal Obstruction", "Ileal Perforation", "Ileal Stenosis", "Ileal Ulcer", "Ileus", "Immune System Disorders - Other", "Infections and Infestations - Other", "Infective Myositis", "Infusion Related Reaction", "Infusion Site Extravasation", "Injection Site Reaction", "Injury to Carotid Artery", "Injury to Inferior Vena Cava", "Injury to Jugular Vein", "Injury to Superior Vena Cava", "Injury, Poisoning and Procedural Complications - Other", "INR Increased", "Insomnia", "Intestinal Stoma Leak", "Intestinal Stoma Obstruction", "Intestinal Stoma Site Bleeding", "Intra-Abdominal Hemorrhage", "Intracranial Hemorrhage", "Intraoperative Arterial Injury", "Intraoperative Breast Injury", "Intraoperative Cardiac Injury", "Intraoperative Ear Injury", "Intraoperative Endocrine Injury", "Intraoperative Gastrointestinal Injury", "Intraoperative Head and Neck Injury", "Intraoperative Hemorrhage", "Intraoperative Hepatobiliary Injury", "Intraoperative Musculoskeletal Injury", "Intraoperative Neurological Injury", "Intraoperative Ocular Injury", "Intraoperative Renal Injury", "Intraoperative Reproductive Tract Injury", "Intraoperative Respiratory Injury", "Intraoperative Skin Injury", "Intraoperative Splenic Injury", "Intraoperative Urinary Injury", "Intraoperative Venous Injury", "Investigations - Other", "Iron Overload", "Irregular Menstruation", "Irritability", "Ischemia Cerebrovascular", "IVth Nerve Disorder", "Jejunal Fistula", "Jejunal Hemorrhage", "Jejunal Obstruction", "Jejunal Perforation", "Jejunal Stenosis", "Jejunal Ulcer", "Joint Effusion", "Joint Infection", "Joint Range of Motion Decreased", "Joint Range of Motion Decreased Cervical Spine", "Joint Range of Motion Decreased Lumbar Spine", "Keratitis", "Kidney Anastomotic Leak", "Kidney Infection", "Kyphosis", "Lactation Disorder", "Large Intestinal Anastomotic Leak", "Laryngeal Edema", "Laryngeal Fistula", "Laryngeal Hemorrhage", "Laryngeal Inflammation", "Laryngeal Mucositis", "Laryngeal Obstruction", "Laryngeal Stenosis", "Laryngitis", "Laryngopharyngeal Dysesthesia", "Laryngospasm", "Left Ventricular Systolic Dysfunction", "Lethargy", "Leukemia Secondary to Oncology Chemotherapy", "Leukocytosis", "Leukoencephalopathy", "Libido Decreased", "Libido Increased", "Lip Infection", "Lip Pain", "Lipase Increased", "Lipohypertrophy", "Localized Edema", "Lordosis", "Lower Gastrointestinal Hemorrhage", "Lung Infection", "Lymph Gland Infection", "Lymph Leakage", "Lymph Node Pain", "Lymphedema", "Lymphocele", "Lymphocyte Count Decreased", "Lymphocyte Count Increased", "Malabsorption", "Malaise", "Mania", "Mediastinal Hemorrhage", "Mediastinal Infection", "Memory Impairment", "Meningismus", "Meningitis", "Menopause", "Menorrhagia", "Metabolism and Nutrition Disorders - Other", "Middle Ear Inflammation", "Mitral Valve Disease", "Mobitz (Type) II Atrioventricular Block", "Mobitz Type I", "Movements Involuntary", "Mucosal Infection", "Mucositis Oral", "Multi-Organ Failure", "Muscle Weakness Left-Sided", "Muscle Weakness Lower Limb", "Muscle Weakness Right-Sided", "Muscle Weakness Trunk", "Muscle Weakness Upper Limb", "Musculoskeletal and Connective Tissue Disorders - Other", "Musculoskeletal Deformity", "Myalgia", "Myelitis", "Myelodysplastic Syndrome", "Myocardial Infarction", "Myocarditis", "Myositis", "Nail Discoloration", "Nail Infection", "Nail Loss", "Nail Ridging", "Nasal Congestion", "Nausea", "Neck Edema", "Neck Pain", "Neck Soft Tissue Necrosis", "Neoplasms Benign, Malignant and Unspecified (Incl Cysts and Polyps) - Other", "Nervous System Disorders - Other", "Neuralgia", "Neutrophil Count Decreased", "Night Blindness", "Nipple Deformity", "Non-Cardiac Chest Pain", "Nystagmus", "Obesity", "Obstruction Gastric", "Oculomotor Nerve Disorder", "Olfactory Nerve Disorder", "Oligospermia", "Optic Nerve Disorder", "Oral Cavity Fistula", "Oral Dysesthesia", "Oral Hemorrhage", "Oral Pain", "Osteonecrosis of Jaw", "Osteoporosis", "Otitis Externa", "Otitis Media", "Ovarian Hemorrhage", "Ovarian Infection", "Ovarian Rupture", "Ovulation Pain", "Pain", "Pain in Extremity", "Pain of Skin", "Palmar-Plantar Erythrodysesthesia Syndrome", "Palpitations", "Pancreas Infection", "Pancreatic Anastomotic Leak", "Pancreatic Duct Stenosis", "Pancreatic Enzymes Decreased", "Pancreatic Fistula", "Pancreatic Hemorrhage", "Pancreatic Necrosis", "Pancreatitis", "Papilledema", "Papulopustular Rash", "Paresthesia", "Paronychia", "Paroxysmal Atrial Tachycardia", "Pelvic Floor Muscle Weakness", "Pelvic Infection", "Pelvic Pain", "Pelvic Soft Tissue Necrosis", "Penile Infection", "Penile Pain", "Perforation Bile Duct", "Pericardial Effusion", "Pericardial Tamponade", "Pericarditis", "Perineal Pain", "Periodontal Disease", "Periorbital Edema", "Periorbital Infection", "Peripheral Ischemia", "Peripheral Motor Neuropathy", "Peripheral Nerve Infection", "Peripheral Sensory Neuropathy", "Peritoneal Infection", "Peritoneal Necrosis", "Personality Change", "Phantom Pain", "Pharyngeal Anastomotic Leak", "Pharyngeal Fistula", "Pharyngeal Hemorrhage", "Pharyngeal Mucositis", "Pharyngeal Necrosis", "Pharyngeal Stenosis", "Pharyngitis", "Pharyngolaryngeal Pain", "Phlebitis", "Phlebitis Infective", "Photophobia", "Photosensitivity", "Platelet Count Decreased", "Pleural Effusion", "Pleural Hemorrhage", "Pleural Infection", "Pleuritic Pain", "Pneumonitis", "Pneumothorax", "Portal Hypertension", "Portal Vein Thrombosis", "Postnasal Drip", "Postoperative Hemorrhage", "Postoperative Thoracic Procedure Complication", "Precocious Puberty", "Pregnancy, Puerperium and Perinatal Conditions - Other", "Premature Delivery", "Premature Menopause", "Presyncope", "Proctitis", "Productive Cough", "Prolapse of Intestinal Stoma", "Prolapse of Urostomy", "Prostate Infection", "Prostatic Hemorrhage", "Prostatic Obstruction", "Prostatic Pain", "Proteinuria", "Pruritus", "Psychiatric Disorders - Other", "Psychosis", "Pulmonary Edema", "Pulmonary Fibrosis", "Pulmonary Fistula", "Pulmonary Hypertension", "Pulmonary Valve Disease", "Purpura", "Pyramidal Tract Syndrome", "Radiation Recall Reaction (Dermatologic)", "Radiculitis", "Rash Acneiform", "Rash Maculo-Papular", "Rash Pustular", "Rectal Anastomotic Leak", "Rectal Fistula", "Rectal Hemorrhage", "Rectal Mucositis", "Rectal Necrosis", "Rectal Obstruction", "Rectal Pain", "Rectal Perforation", "Rectal Stenosis", "Rectal Ulcer", "Recurrent Laryngeal Nerve Palsy", "Renal and Urinary Disorders - Other", "Renal Calculi", "Renal Colic", "Renal Hemorrhage", "Reproductive System and Breast Disorders - Other", "Respiratory Failure", "Respiratory, Thoracic and Mediastinal Disorders - Other", "Restlessness", "Restrictive Cardiomyopathy", "Retinal Detachment", "Retinal Tear", "Retinal Vascular Disorder", "Retinoic Acid Syndrome", "Retinopathy", "Retroperitoneal Hemorrhage", "Reversible Posterior Leukoencephalopathy Syndrome", "Rhinitis Infective", "Right Ventricular Dysfunction", "Salivary Duct Inflammation", "Salivary Gland Fistula", "Salivary Gland Infection", "Scalp Pain", "Scleral Disorder", "Scoliosis", "Scrotal Infection", "Scrotal Pain", "Seizure", "Sepsis", "Seroma", "Serum Amylase Increased", "Serum Sickness", "Sick Sinus Syndrome", "Sinus Bradycardia", "Sinus Disorder", "Sinus Pain", "Sinus Tachycardia", "Sinusitis", "Skin and Subcutaneous Tissue Disorders - Other", "Skin Atrophy", "Skin Hyperpigmentation", "Skin Hypopigmentation", "Skin Induration", "Skin Infection", "Skin Ulceration", "Sleep Apnea", "Small Intestinal Anastomotic Leak", "Small Intestinal Mucositis", "Small Intestinal Obstruction", "Small Intestinal Perforation", "Small Intestinal Stenosis", "Small Intestine Infection", "Small Intestine Ulcer", "Sneezing", "Social Circumstances - Other", "Soft Tissue Infection", "Soft Tissue Necrosis Lower Limb", "Soft Tissue Necrosis Upper Limb", "Somnolence", "Sore Throat", "Spasticity", "Spermatic Cord Anastomotic Leak", "Spermatic Cord Hemorrhage", "Spermatic Cord Obstruction", "Spinal Fracture", "Spleen Disorder", "Splenic Infection", "Stenosis of Gastrointestinal Stoma", "Stevens-Johnson Syndrome", "Stoma Site Infection", "Stomach Pain", "Stomal Ulcer", "Stridor", "Stroke", "Sudden Death NOS", "Suicidal Ideation", "Suicide Attempt", "Superficial Soft Tissue Fibrosis", "Superficial Thrombophlebitis", "Superior Vena Cava Syndrome", "Supraventricular Tachycardia", "Surgical and Medical Procedures - Other", "Syncope", "Telangiectasia", "Testicular Disorder", "Testicular Hemorrhage", "Testicular Pain", "Thromboembolic Event", "Thrombotic Thrombocytopenic Purpura", "Tinnitus", "Tooth Development Disorder", "Tooth Discoloration", "Tooth Infection", "Toothache", "Toxic Epidermal Necrolysis", "Tracheal Fistula", "Tracheal Hemorrhage", "Tracheal Mucositis", "Tracheal Obstruction", "Tracheal Stenosis", "Tracheitis", "Tracheostomy Site Bleeding", "Transient Ischemic Attacks", "Treatment Related Secondary Malignancy", "Tremor", "Tricuspid Valve Disease", "Trigeminal Nerve Disorder", "Trismus", "Tumor Lysis Syndrome", "Tumor Pain", "Typhlitis", "Unequal Limb Length", "Unintended Pregnancy", "Upper Gastrointestinal Hemorrhage", "Upper Respiratory Infection", "Ureteric Anastomotic Leak", "Urethral Anastomotic Leak", "Urethral Infection", "Urinary Fistula", "Urinary Frequency", "Urinary Incontinence", "Urinary Retention", "Urinary Tract Infection", "Urinary Tract Obstruction", "Urinary Tract Pain", "Urinary Urgency", "Urine Discoloration", "Urine Output Decreased", "Urostomy Leak", "Urostomy Obstruction", "Urostomy Site Bleeding", "Urostomy Stenosis", "Urticaria", "Uterine Anastomotic Leak", "Uterine Fistula", "Uterine Hemorrhage", "Uterine Infection", "Uterine Obstruction", "Uterine Pain", "Uterine Perforation", "Uveitis", "Vaginal Anastomotic Leak", "Vaginal Discharge", "Vaginal Dryness", "Vaginal Fistula", "Vaginal Hemorrhage", "Vaginal Infection", "Vaginal Inflammation", "Vaginal Obstruction", "Vaginal Pain", "Vaginal Perforation", "Vaginal Stricture", "Vaginismus", "Vagus Nerve Disorder", "Vas Deferens Anastomotic Leak", "Vascular Access Complication", "Vascular Disorders - Other", "Vasculitis", "Vasovagal Reaction", "Venous Injury", "Ventricular Arrhythmia", "Ventricular Fibrillation", "Ventricular Tachycardia", "Vertigo", "Vestibular Disorder", "Virilization", "Visceral Arterial Ischemia", "Vital Capacity Abnormal", "Vitreous Hemorrhage", "Voice Alteration", "Vomiting", "Vulval Infection", "Watering Eyes", "Weight Gain", "Weight Loss", "Wheezing", "White Blood Cell Decreased", "Wolff-Parkinson-White Syndrome", "Wound Complication", "Wound Dehiscence", "Wound Infection", "Wrist Fracture"

<br>Attribute Name: barretts\_esophagus\_goblet\_cells\_present
<br>Description: The yes/no/unknown indicator used to describe whether goblet cells were determined to be present in a patient diagnosed with Barrett's esophagus.
<br>Attribute of Node: follow\_up
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Yes", "No", "Unknown", "Not Reported"

<br>Attribute Name: cause\_of\_response
<br>Description: The text term used to describe the suspected cause or reason for the patient disease response.
<br>Attribute of Node: follow\_up
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: comorbidity
<br>Description: The text term used to describe a comorbidity disease, which coexists with the patient's malignant disease.
<br>Attribute of Node: follow\_up
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Acute Renal Failure", "Adenocarcinoma", "Adrenocortical Insufficiency", "Adenomatous Polyposis Coli", "Allergies", "Alpha-1 Antitrypsin", "Anemia", "Anxiety", "Arrhythmia", "Arthritis", "Asthma", "Atrial Fibrillation", "Avascular Necrosis", "Barrett's Esophagus", "Basal Cell Carcinoma", "Beckwith-Wiedemann", "Behcet's Disease", "Biliary Disorder", "Blood Clots", "Bone Fracture(s)", "Bronchitis", "Calcium Channel Blockers", "Cancer", "Cataracts", "Celiac Disease", "Cirrhosis, Unknown Etiology", "Cerebrovascular Disease", "Cholelithiasis", "Chronic Renal Failure", "Colon Polyps", "Common Variable Immunodeficiency", "Congestive Heart Failure (CHF)", "Connective Tissue Disorder", "COPD", "Coronary Artery Disease", "Crohn's Disease", "Cryptogenic Organizing Pneumonia", "Deep Vein Thrombosis / Thromboembolism", "Denys-Drash Syndrome", "Depression", "Diabetes", "Diabetes, Type II", "Diabetic Neuropathy", "Diet Controlled Diabetes", "Diverticulitis", "DVT/PE", "Dyslipidemia", "Epilepsy", "Eczema", "Epstein-Barr Virus", "Familial Adenomatous Polyposis", "Fanconi Anemia", "Fibrosis", "Gastroesophageal Reflux Disease", "GERD", "Glaucoma", "Glycogen Storage Disease", "Gout", "Gonadal Dysfunction", "Gorlin Syndrome", "H. pylori Infection", "Hashimoto's Thyroiditis", "Headache", "Heart Disease", "Hemihypertrophy", "Hemorrhagic Cystitis", "Hepatitis", "Hepatitis A Infection", "Hepatitis B Infection", "Hepatitis C Infection", "Hepatitis, Chronic", "Hereditary Non-polyposis Colon Cancer", "Herpes", "High Grade Liver Dysplastic Nodule", "HIV / AIDS", "Human Papillomavirus Infection", "HUS/TTP", "Hypercholesterolemia", "Hypercalcemia", "Hyperglycemia", "Hyperlipidemia", "Hypertension", "Hypospadias", "Hypothyroidism", "Inflammatory Bowel Disease", "Insulin Controlled Diabetes", "Interstitial Pneumontis or ARDS", "Intraductal Papillary Mucinous Neoplasm", "Iron Overload", "Ischemic Heart Disease", "ITP", "Joint Replacement", "Kidney Disease", "Liver Cirrhosis (Liver Disease)", "Liver Toxicity (Non-Infectious)", "Li-Fraumeni Syndrome", "Low Grade Liver Dysplastic Nodule", "Lupus", "Lynch Syndrome", "MAI", "Myasthenia Gravis", "Myocardial Infarction", "Neuroendocrine Tumor", "Nonalcoholic Steatohepatitis", "Obesity", "Organ transplant (site)", "Osteoarthritis", "Osteoporosis or Osteopenia", "Other", "Other Cancer Within 5 Years", "Other Nonmalignant Systemic Disease", "Other Pulmonary Complications", "Pancreatitis", "Pain (Various)", "Peptic Ulcer (Ulcer)", "Peripheral Neuropathy", "Peripheral Vascular Disease", "Peutz-Jeghers Disease", "Pregnancy in Patient or Partner", "Primary Sclerosing Cholangitis", "Psoriasis", "Pulmonary Fibrosis", "Pulmonary Hemorrhage", "Renal Failure (Requiring Dialysis)", "Renal Dialysis", "Renal Insufficiency", "Rheumatologic Disease", "Rheumatoid Arthritis", "Rubinstein-Taybi Syndrome", "Sarcoidosis", "Seizure", "Sleep apnea", "Smoking", "Steatosis", "Stroke", "Transient Ischemic Attack", "Tuberculosis", "Turcot Syndrome", "Tyrosinemia", "Ulcerative Colitis", "Wagr Syndrome", "Unknown", "Not Reported"

<br>Attribute Name: comorbidity\_method\_of\_diagnosis
<br>Description: The text term used to describe the method used to diagnose the patient's comorbidity disease.
<br>Attribute of Node: follow\_up
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Histology", "Pathology", "Radiology", "Unknown", "Not Reported"

<br>Attribute Name: contact\_type
<br>Description: Need Vocabulary
<br>Attribute of Node: follow\_up
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: date\_of\_last\_contact
<br>Description: Need Vocabulary
<br>Attribute of Node: follow\_up
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: days\_to\_adverse\_event
<br>Description: Number of days between the date used for index and the date of the patient's adverse event.
<br>Attribute of Node: follow\_up
<br>Required: false
<br>Type: integer
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: days\_to\_comorbidity
<br>Description: Number of days between the date used for index and the date the patient was diagnosed with a comorbidity.
<br>Attribute of Node: follow\_up
<br>Required: false
<br>Type: integer
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: days\_to\_follow\_up
<br>Description: Number of days between the date used for index and the date of the patient's last follow-up appointment or contact.
<br>Attribute of Node: follow\_up
<br>Required: false
<br>Type: integer
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: days\_to\_progression\_free
<br>Description: Number of days between the date used for index and the date the patient's disease was formally confirmed as progression-free.
<br>Attribute of Node: follow\_up
<br>Required: false
<br>Type: integer
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: diabetes\_treatment\_type
<br>Description: Text term used to describe the types of treatment used to manage diabetes.
<br>Attribute of Node: follow\_up
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Alpha-Glucosidase Inhibitor", "Biguanide", "Diet", "Injected Insulin", "Insulin", "Oral Hypoglycemic", "Sulfonylurea", "Thiazolidinedione", "Other", "Unknown", "Not Reported"

<br>Attribute Name: disease\_response
<br>Description: Code assigned to describe the patient's response or outcome to the disease.
<br>Attribute of Node: follow\_up
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "AJ-Adjuvant Therapy", "BED-Biochemical Evidence of Disease", "CPD-Clinical Progression", "CR-Complete Response", "CRU-Complete Response Unconfirmed", "DU-Disease Unchanged", "IMR-Immunoresponse", "IPD-Immunoprogression", "MR-Minimal/Marginal response", "MX-Mixed Response", "Non-CR/Non-PD-Non-CR/Non-PD", "NPB-No Palliative Benefit", "NR-No Response", "PA-Palliative Therapy", "PB-Palliative Benefit", "PD-Progressive Disease", "PDM-Persistent Distant Metastasis", "PLD-Persistent Locoregional Disease", "PPD-Pseudoprogression", "PR-Partial Response", "PSR-Pseudoresponse", "RD-Responsive Disease", "RP-Response", "RPD-Radiographic Progressive Disease", "sCR-Stringent Complete Response", "SD-Stable Disease", "SPD-Surgical Progression", "TE-Too Early", "TF-Tumor Free", "VGPR-Very Good Partial Response", "WT-With Tumor", "Unknown", "Not Reported"

<br>Attribute Name: dlco\_ref\_predictive\_percent
<br>Description: The value, as a percentage of predicted lung volume, measuring the amount of carbon monoxide detected in a patient's lungs.
<br>Attribute of Node: follow\_up
<br>Required: false
<br>Type: number
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: document\_number
<br>Description: Need Vocabulary
<br>Attribute of Node: follow\_up
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: ecog\_performance\_status
<br>Description: The ECOG functional performance status of the patient/participant.
<br>Attribute of Node: follow\_up
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "0", "1", "2", "3", "4", "5", "Unknown", "Not Reported"

<br>Attribute Name: explain\_unknown\_status
<br>Description: Need Vocabulary
<br>Attribute of Node: follow\_up
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: fev1\_fvc\_post\_bronch\_percent
<br>Description: Percentage value to represent result of Forced Expiratory Volume in 1 second (FEV1) divided by the Forced Vital Capacity (FVC) post-bronchodilator.
<br>Attribute of Node: follow\_up
<br>Required: false
<br>Type: number
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: fev1\_fvc\_pre\_bronch\_percent
<br>Description: Percentage value to represent result of Forced Expiratory Volume in 1 second (FEV1) divided by the Forced Vital Capacity (FVC) pre-bronchodilator.
<br>Attribute of Node: follow\_up
<br>Required: false
<br>Type: number
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: fev1\_ref\_post\_bronch\_percent
<br>Description: The percentage comparison to a normal value reference range of the volume of air that a patient can forcibly exhale from the lungs in one second post-bronchodilator.
<br>Attribute of Node: follow\_up
<br>Required: false
<br>Type: number
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: fev1\_ref\_pre\_bronch\_percent
<br>Description: The percentage comparison to a normal value reference range of the volume of air that a patient can forcibly exhale from the lungs in one second pre-bronchodilator.
<br>Attribute of Node: follow\_up
<br>Required: false
<br>Type: number
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: hepatitis\_sustained\_virological\_response
<br>Description: The yes/no/unknown indicator used to describe whether the patient received treatment for a risk factor the patient had at the time of or prior to their diagnosis.
<br>Attribute of Node: follow\_up
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Yes", "No", "Unknown", "Not Reported"

<br>Attribute Name: karnofsky\_performance\_status
<br>Description: Text term used to describe the classification used of the functional capabilities of a person.
<br>Attribute of Node: follow\_up
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "0", "10", "20", "30", "40", "50", "60", "70", "80", "90", "100", "Unknown", "Not Reported"

<br>Attribute Name: pancreatitis\_onset\_year
<br>Description: Numeric value to represent the year that the patient was diagnosed with clinical chronic pancreatitis.
<br>Attribute of Node: follow\_up
<br>Required: false
<br>Type: integer
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: patient\_status
<br>Description: Need Vocabulary
<br>Attribute of Node: follow\_up
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: physical\_exam\_changes
<br>Description: Need Vocabulary
<br>Attribute of Node: follow\_up
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: physical\_exam\_performed
<br>Description: A boolean variable stating whether or not a physical exam was performed.
<br>Attribute of Node: follow\_up
<br>Required: false
<br>Type: boolean
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: progression\_or\_recurrence\_anatomic\_site
<br>Description: The text term used to describe the anatomic site of the progressive or recurrent disease.
<br>Attribute of Node: follow\_up
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Abdomen, NOS", "Abdominal esophagus", "Accessory sinus, NOS", "Acoustic nerve", "Adrenal gland, NOS", "Ampulla of Vater", "Anal canal", "Anterior 2/3 of tongue, NOS", "Anterior floor of mouth", "Anterior mediastinum", "Anterior surface of epiglottis", "Anterior wall of bladder", "Anterior wall of nasopharynx", "Anus, NOS", "Aortic body and other paraganglia", "Appendix", "Ascending colon", "Autonomic nervous system, NOS", "Axillary tail of breast", "Base of tongue, NOS", "Bladder neck", "Bladder, NOS", "Blood", "Body of pancreas", "Body of penis", "Body of stomach", "Bone marrow", "Bone of limb, NOS", "Bone, NOS", "Bones of skull and face and associated joints", "Border of tongue", "Brain stem", "Brain, NOS", "Branchial cleft", "Breast, NOS", "Broad ligament", "Cardia, NOS", "Carotid body", "Cauda equina", "Cecum", "Central portion of breast", "Cerebellum, NOS", "Cerebral meninges", "Cerebrum", "Cervical esophagus", "Cervix uteri", "Choroid", "Ciliary body", "Cloacogenic zone", "Colon, NOS", "Commissure of lip", "Conjunctiva", "Connective, subcutaneous and other soft tissues of abdomen", "Connective, subcutaneous and other soft tissues of head, face, and neck", "Connective, subcutaneous and other soft tissues of lower limb and hip", "Connective, subcutaneous and other soft tissues of pelvis", "Connective, subcutaneous and other soft tissues of thorax", "Connective, subcutaneous and other soft tissues of trunk, NOS", "Connective, subcutaneous and other soft tissues of upper limb and shoulder", "Connective, subcutaneous and other soft tissues, NOS", "Cornea, NOS", "Corpus uteri", "Cortex of adrenal gland", "Cranial nerve, NOS", "Craniopharyngeal duct", "Descended testis", "Descending colon", "Dome of bladder", "Dorsal surface of tongue, NOS", "Duodenum", "Endocervix", "Endocrine gland, NOS", "Endometrium", "Epididymis", "Esophagus, NOS", "Ethmoid sinus", "Exocervix", "External ear", "External lip, NOS", "External lower lip", "External upper lip", "Extrahepatic bile duct", "Eye, NOS", "Eyelid", "Fallopian tube", "Female genital tract, NOS", "Floor of mouth, NOS", "Frontal lobe", "Frontal sinus", "Fundus of stomach", "Fundus uteri", "Gallbladder", "Gastric antrum", "Gastrointestinal tract, NOS", "Glans penis", "Glottis", "Greater curvature of stomach, NOS", "Gum, NOS", "Hard palate", "Head of pancreas", "Head, face or neck, NOS", "Heart", "Hematopoietic system, NOS", "Hepatic flexure of colon", "Hypopharyngeal aspect of aryepiglottic fold", "Hypopharynx, NOS", "Ileum", "Ill-defined sites within respiratory system", "Intestinal tract, NOS", "Intra-abdominal lymph nodes", "Intrahepatic bile duct", "Intrathoracic lymph nodes", "Islets of Langerhans", "Isthmus uteri", "Jejunum", "Kidney, NOS", "Labium majus", "Labium minus", "Lacrimal gland", "Laryngeal cartilage", "Larynx, NOS", "Lateral floor of mouth", "Lateral wall of bladder", "Lateral wall of nasopharynx", "Lateral wall of oropharynx", "Lesser curvature of stomach, NOS", "Lingual tonsil", "Lip, NOS", "Liver", "Long bones of lower limb and associated joints", "Long bones of upper limb, scapula and associated joints", "Lower gum", "Lower limb, NOS", "Lower lobe, lung", "Lower third of esophagus", "Lower-inner quadrant of breast", "Lower-outer quadrant of breast", "Lung, NOS", "Lymph node, NOS", "Lymph nodes of axilla or arm", "Lymph nodes of head, face and neck", "Lymph nodes of inguinal region or leg", "Lymph nodes of multiple regions", "Main bronchus", "Major salivary gland, NOS", "Male genital organs, NOS", "Mandible", "Maxillary sinus", "Meckel diverticulum", "Mediastinum, NOS", "Medulla of adrenal gland", "Meninges, NOS", "Middle ear", "Middle lobe, lung", "Middle third of esophagus", "Mouth, NOS", "Mucosa of lip, NOS", "Mucosa of lower lip", "Mucosa of upper lip", "Myometrium", "Nasal cavity", "Nasopharynx, NOS", "Nervous system, NOS", "Nipple", "Occipital lobe", "Olfactory nerve", "Optic nerve", "Orbit, NOS", "Oropharynx, NOS", "Other ill-defined sites", "Other specified parts of female genital organs", "Other specified parts of male genital organs", "Other specified parts of pancreas", "Ovary", "Overlapping lesion of accessory sinuses", "Overlapping lesion of bladder", "Overlapping lesion of bones, joints and articular cartilage", "Overlapping lesion of bones, joints and articular cartilage of limbs", "Overlapping lesion of brain", "Overlapping lesion of brain and central nervous system", "Overlapping lesion of breast", "Overlapping lesion of cervix uteri", "Overlapping lesion of colon", "Overlapping lesion of connective, subcutaneous and other soft tissues", "Overlapping lesion of corpus uteri", "Overlapping lesion of digestive system", "Overlapping lesion of endocrine glands and related structures", "Overlapping lesion of esophagus", "Overlapping lesion of eye and adnexa", "Overlapping lesion of female genital organs", "Overlapping lesion of floor of mouth", "Overlapping lesion of heart, mediastinum and pleura", "Overlapping lesion of hypopharynx", "Overlapping lesion of ill-defined sites", "Overlapping lesion of larynx", "Overlapping lesion of lip", "Overlapping lesion of lip, oral cavity and pharynx", "Overlapping lesion of lung", "Overlapping lesion of major salivary glands", "Overlapping lesion of male genital organs", "Overlapping lesion of nasopharynx", "Overlapping lesion of other and unspecified parts of mouth", "Overlapping lesion of palate", "Overlapping lesion of pancreas", "Overlapping lesion of penis", "Overlapping lesion of peripheral nerves and autonomic nervous system", "Overlapping lesion of rectum, anus and anal canal", "Overlapping lesion of respiratory system and intrathoracic organs", "Overlapping lesion of retroperitoneum and peritoneum", "Overlapping lesion of skin", "Overlapping lesion of small intestine", "Overlapping lesion of stomach", "Overlapping lesion of tongue", "Overlapping lesion of tonsil", "Overlapping lesion of urinary organs", "Overlapping lesion of vulva", "Overlapping lesions of oropharynx", "Palate, NOS", "Pancreas, NOS", "Pancreatic duct", "Parametrium", "Parathyroid gland", "Paraurethral gland", "Parietal lobe", "Parotid gland", "Pelvic bones, sacrum, coccyx and associated joints", "Pelvic lymph nodes", "Pelvis, NOS", "Penis, NOS", "Peripheral nerves and autonomic nervous system of abdomen", "Peripheral nerves and autonomic nervous system of head, face, and neck", "Peripheral nerves and autonomic nervous system of lower limb and hip", "Peripheral nerves and autonomic nervous system of pelvis", "Peripheral nerves and autonomic nervous system of thorax", "Peripheral nerves and autonomic nervous system of trunk, NOS", "Peripheral nerves and autonomic nervous system of upper limb and shoulder", "Peritoneum, NOS", "Pharynx, NOS", "Pineal gland", "Pituitary gland", "Placenta", "Pleura, NOS", "Postcricoid region", "Posterior mediastinum", "Posterior wall of bladder", "Posterior wall of hypopharynx", "Posterior wall of nasopharynx", "Posterior wall of oropharynx", "Prepuce", "Prostate gland", "Pylorus", "Pyriform sinus", "Rectosigmoid junction", "Rectum, NOS", "Renal pelvis", "Reticuloendothelial system, NOS", "Retina", "Retromolar area", "Retroperitoneum", "Rib, sternum, clavicle and associated joints", "Round ligament", "Scrotum, NOS", "Short bones of lower limb and associated joints", "Short bones of upper limb and associated joints", "Sigmoid colon", "Skin of lip, NOS", "Skin of lower limb and hip", "Skin of other and unspecified parts of face", "Skin of scalp and neck", "Skin of trunk", "Skin of upper limb and shoulder", "Skin, NOS", "Small intestine, NOS", "Soft palate, NOS", "Specified parts of peritoneum", "Spermatic cord", "Sphenoid sinus", "Spinal cord", "Spinal meninges", "Spleen", "Splenic flexure of colon", "Stomach, NOS", "Subglottis", "Sublingual gland", "Submandibular gland", "Superior wall of nasopharynx", "Supraglottis", "Tail of pancreas", "Temporal lobe", "Testis, NOS", "Thoracic esophagus", "Thorax, NOS", "Thymus", "Thyroid gland", "Tongue, NOS", "Tonsil, NOS", "Tonsillar fossa", "Tonsillar pillar", "Trachea", "Transverse colon", "Trigone of bladder", "Undescended testis", "Unknown primary site", "Upper gum", "Upper limb, NOS", "Upper lobe, lung", "Upper respiratory tract, NOS", "Upper third of esophagus", "Upper-inner quadrant of breast", "Upper-outer quadrant of breast", "Urachus", "Ureter", "Ureteric orifice", "Urethra", "Urinary system, NOS", "Uterine adnexa", "Uterus, NOS", "Uvula", "Vagina, NOS", "Vallecula", "Ventral surface of tongue, NOS", "Ventricle, NOS", "Vertebral column", "Vestibule of mouth", "Vulva, NOS", "Waldeyer ring", "Biliary tract, NOS", "Cheek mucosa", "Clitoris", "Overlapping lesion of biliary tract", "Unknown", "Not Reported"

<br>Attribute Name: progression\_or\_recurrence\_type
<br>Description: The text term used to describe the type of progressive or recurrent disease or relapsed disease.
<br>Attribute of Node: follow\_up
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Biochemical", "Distant", "Local", "Regional", "Unknown", "Not Reported"

<br>Attribute Name: reflux\_treatment\_type
<br>Description: Text term used to describe the types of treatment used to manage gastroesophageal reflux disease (GERD).
<br>Attribute of Node: follow\_up
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Antacids", "H2 Blockers", "Medically Treated", "No Treatment", "Not Applicable", "Not Reported", "Proton Pump Inhibitors", "Surgically Treated", "Unknown"

<br>Attribute Name: risk\_factor
<br>Description: The text term used to describe a risk factor the patient had at the time of or prior to their diagnosis.
<br>Attribute of Node: follow\_up
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Alcohol Consumption", "Alcoholic Liver Disease", "Allergy, Animal, NOS", "Allergy, Ant", "Allergy, Bee", "Allergy, Cat", "Allergy, Dairy or Lactose", "Allergy, Dog", "Allergy, Eggs", "Allergy, Food, NOS", "Allergy, Fruit", "Allergy, Meat", "Allergy, Mold or Dust", "Allergy, Nuts", "Allergy, Processed Foods", "Allergy, Seafood", "Allergy, Wasp", "Alpha-1 Antitrypsin Deficiency", "Autoimmune Atrophic Chronic Gastritis", "Barrett's Esophagus", "Beckwith-Wiedemann", "Behcet's Disease", "Cancer", "Cholelithiasis", "Chronic Hepatitis", "Cirrhosis", "Colon Polyps", "Common variable immune deficiency (CVID)", "Denys-Drash Syndrome", "Diabetes, NOS", "Diabetes, Type I", "Diabetes, Type II", "Diet", "Diverticulitis", "Endometriosis", "Endosalpingiosis", "Eczema", "Epstein-Barr Virus", "Familial Adenomatous Polyposis", "Fanconi Anemia", "Fibrosis", "Gastric Polyp(s)", "Gilbert's Syndrome", "Gorlin Syndrome", "Hashimoto's Thyroiditis", "Hay Fever", "Headache", "Helicobacter Pylori-Associated Gastritis", "Hematologic Disorder, NOS", "Hemihypertrophy", "Hemochromatosis", "Hepatic Encephalopathy", "Hepatitis B Infection", "Hepatitis C Infection", "Hepatitis, NOS", "High Grade Dysplasia", "HIV", "Human Papillomavirus Infection", "Hypospadias", "Intestinal Metaplasia", "Iron Overload", "Li-Fraumeni Syndrome", "Low Grade Dysplasia", "Lymphocytic Thyroiditis", "Lynch Syndrome", "Myasthenia Gravis", "Nonalcoholic Fatty Liver Disease", "Nonalcoholic Steatohepatitis", "Obesity", "Oral Contraceptives", "Pancreatitis", "Parasitic Disease of Biliary Tract", "Primary Sclerosing Cholangitis", "Recurrent Pyogenic Cholangitis", "Reflux Disease", "Rheumatoid Arthritis", "Rubinstein-Taybi Syndrome", "Sarcoidosis", "Seizure", "Sensory Changes", "Serous tubal intraepithelial carcinoma (STIC)", "Steatosis", "Tattoo", "Thyroid Nodular Hyperplasia", "Tobacco, NOS", "Tobacco, Smokeless", "Tobacco, Smoking", "Turcot Syndrome", "Undescended Testis", "Vision Changes", "Wagr Syndrome", "Unknown", "Not Reported"

<br>Attribute Name: risk\_factor\_treatment
<br>Description: The yes/no/unknown indicator used to describe whether the patient received treatment for a risk factor the patient had at the time of or prior to their diagnosis.
<br>Attribute of Node: follow\_up
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Yes", "No", "Unknown", "Not Reported"

<br>Attribute Name: treatment\_since\_last\_contact
<br>Description: None
<br>Attribute of Node: follow\_up
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: viral\_hepatitis\_serologies
<br>Description: Text term that describes the kind of serological laboratory test used to determine the patient's hepatitus status.
<br>Attribute of Node: follow\_up
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "HBV Core Antibody", "HBV DNA", "HBV Genotype", "HBV Surface Antibody", "HCV Genotype", "Hepatitis B Surface Antigen", "Hepatitis C Antibody", "Hepatitis C Virus RNA", "Unknown", "Not Reported"

<br>Attribute Name: stratification\_factor\_id
<br>Description: A unique id assigned by the data commons to the stratification\_factor node.
<br>Attribute of Node: stratification\_factor
<br>Required: true
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: grouped\_recurrence\_score
<br>Description: Grouped RS (derived from RS) Used as a stratification factor for randomizations during the later portion of the study, and included as a stratification factor for all randomized cases for stratified analyses in the paper
<br>Attribute of Node: stratification\_factor
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "0-5", "6-10", "11-15", "16-20", "21-25", "26-30", "31-35", "36-40", "41-50", "51-100"

<br>Attribute Name: stratification\_code
<br>Description: Combined stratification variable used for stratified comparison of randomized arms.
<br>Attribute of Node: stratification\_factor
<br>Required: false
<br>Type: integer
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: menopausal\_status\_stratification
<br>Description: Menopausal Status Stratification (reported during registration).
<br>Attribute of Node: stratification\_factor
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Postmenopausal", "Pre/Peri Menopausal"

<br>Attribute Name: planned\_chemotherapy\_stratification
<br>Description: Type of Planned Chemo Stratification (reported during registration).
<br>Attribute of Node: stratification\_factor
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Taxane containing regimen", "Non-Taxane regimen", "Not Applicable"

<br>Attribute Name: planned\_radiotherapy\_stratification
<br>Description: Type of Planned RT (reported during registration)
<br>Attribute of Node: stratification\_factor
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "Whole breast, no boost", "Whole breast with boost", "Partial breast", "None Planned"

<br>Attribute Name: tumor\_size\_stratification
<br>Description: Tumor Size Stratification (reported during registration)
<br>Attribute of Node: stratification\_factor
<br>Required: false
<br>Type: string
<br>Constraints: Of Enumeration
<br>Enumeration: "<= 2.0 cm", "> 2.0 cm"

<br>Attribute Name: cross\_reference\_id
<br>Description: The unique id of the object in cross referencing database that is linked to the study subject.
<br>Attribute of Relationship: cross\_referenced\_at
<br>Required: true
<br>Type: string
<br>Constraints: None
<br>Enumeration: None

<br>Attribute Name: cross\_reference\_url
<br>Description: The url the object in cross referencing database that is linked to the study subject.
<br>Attribute of Relationship: cross\_referenced\_at
<br>Required: false
<br>Type: string
<br>Constraints: None
<br>Enumeration: None


