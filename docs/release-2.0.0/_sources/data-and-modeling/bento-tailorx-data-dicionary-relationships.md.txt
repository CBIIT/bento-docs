# Relationships among Bento TailoRx node types

Relationships among BENTO_TAILORx node types. Listed are relationships that connect node types in the BENTO_TAILORx conceptual data model, the source and destination nodes for each relationship, and the multiplicity of each relationship.

|     Relationship               |     Source                    |     Destination                 |     Multiplicity    |
|--------------------------------|-------------------------------|---------------------------------|---------------------|
|     of_institution             |     program                   |     institution                 |     many_to_many    |
|     of_program                 |     project                   |     program                     |     many_to_many    |
|     of_program                 |     study                     |     program                     |     many_to_many    |
|     of_program                 |     study_subject             |     program                     |     many_to_many    |
|     of_program                 |     laboratory_procedure      |     program                     |     many_to_many    |
|     cross_referenced_at        |     study_subject             |     cross_reference_database    |     many_to_many    |
|     of_project                 |     study_subject             |     project                     |     many_to_many    |
|     of_study                   |     study_subject             |     study                       |     many_to_many    |
|     of_study_subject           |     sample                    |     study_subject               |     many_to_one     |
|     of_sample                  |     fraction                  |     sample                      |     many_to_one     |
|     of_fraction                |     analyte                   |     fraction                    |     many_to_one     |
|     of_analyte                 |     aliquot                   |     analyte                     |     many_to_one     |
|     of_sample                  |     analyte                   |     sample                      |     many_to_one     |
|     processed_by               |     aliquot                   |     laboratory_procedure        |     many_to_many    |
|     processed_by               |     analyte                   |     laboratory_procedure        |     many_to_many    |
|     processed_by               |     fraction                  |     laboratory_procedure        |     many_to_many    |
|     processed_by               |     sample                    |     laboratory_procedure        |     many_to_many    |
|     of_sample                  |     report                    |     sample                      |     one_to_one      |
|     of_fraction                |     report                    |     fraction                    |     one_to_one      |
|     of_analyte                 |     report                    |     analyte                     |     one_to_one      |
|     of_aliquot                 |     report                    |     aliquot                     |     one_to_one      |
|     of_laboratory_procedure    |     report                    |     laboratory_procedure        |     one_to_one      |
|     of_study_subject           |     demographic_data          |     study_subject               |     one_to_one      |
|     of_study_subject           |     exposure                  |     study_subject               |     one_to_one      |
|     of_study_subject           |     family_medical_history    |     study_subject               |     one_to_one      |
|     of_study_subject           |     file                      |     study_subject               |     many_to_one     |
|     of_sample                  |     file                      |     sample                      |     many_to_one     |
|     of_laboratory_procedure    |     file                      |     laboratory_procedure        |     many_to_one     |
|     of_study                   |     file                      |     study                       |     many_to_one     |
|     of_project                 |     file                      |     project                     |     many_to_one     |
|     of_program                 |     file                      |     program                     |     many_to_one     |
|     of_diagnosis               |     file                      |     diagnosis                   |     many_to_one     |
|     of_diagnosis               |     therapeutic_procedure     |     diagnosis                   |     many_to_one     |
|     of_diagnosis               |     follow_up                 |     diagnosis                   |     many_to_one     |
|     of_study_subject           |     diagnosis                 |     study_subject               |     many_to_one     |
|     of_study_subject           |     stratification_factor     |     study_subject               |     one_to_one      |
|     of_study_subject           |     follow_up                 |     study_subject               |     many_to_one     |
