---
sort: 5
title: Bento TailoRx Data Dictionary
---

# Bento TailoRx Data Dictionary

## Introduction

The Bento Core Data Model supports the Bento software framework that has been developed to stand up data sharing platforms for clinical trials and research programs. Modern clinical trials and research programs generate large volumes of complex biomedical data types. To address this complexity the Bento Core Data model uses a graph structure to model a clinical trial workflow. Key trial entities are modelled as *node types*, while the association between nodes are explicitly modelled as *relationship types*. 

The Bento Core Data Model has been extended to fit the TAILORx clinical data set. The extended model, also called the **BENTO_TAILORx** data model, comprises of 20 node types and 37 relationship types that are listed in the section **BENTO_TAILORx Node Types** and **Table 1**, respectively. Both nodes and relationships store data attributes in the form of properties. These data attributes are listed in the section **BENTO_TAILORx Attribute Types**. The BENTO_TAILORx graph data model has been implemented in Neo4J, a commercial graph database platform.

 

## BENTO_TAILORx Node Types

1. **Institution:** An established society, corporation, foundation or other organization founded and united for a specific purpose, e.g. for health-related research; also used to refer to a building or buildings occupied or used by such organization.

 

2. **Program:** A broad framework of goals to be achieved.

 

3. **Project:** Any specifically defined piece of work that is undertaken or attempted to meet a single requirement.

 

4. **Study:** A detailed examination, analysis, or critical inspection of a subject designed to discover facts about it.

 

5. **Study Subject:** A matter or an individual that is observed, analyzed, examined, investigated, experimented upon, or/and treated in the course of a particular study.

 

6. **Cross Reference Database:** A data repository that cross-references a study subject.

 

7. **Sample:** Any material sample taken from a biological entity for testing, diagnostic, propagation, treatment or research purposes, including a sample obtained from a living organism or taken from the biological object after halting of all its life functions. Sample can contain one or more components including but not limited to cellular molecules, cells, tissues, organs, body fluids, embryos, and body excretory products. The preferred name of this node type in the NCI Metathesaurus is "Biospecimen".

 

8. **Fraction:** A part, a fragment of a whole.

 

9. **Analyte:** The sample or material being subjected to analysis.

 

10. **Aliquot:** Pertaining to a portion of the whole; any one of two or more samples of something, of the same volume or weight.

 

11. **Laboratory Procedure:** Any procedure that involves testing or manipulating a sample of blood, urine, or other body substance in a laboratory setting.

 

12. **Report:** A short textual account; having provided a short account.

 

13. **File:** A set of related records (either written or electronic) kept together.

 

14. **Demographic Data:** Aspects of individuals or groups of individuals in a study, including basic descriptive information like age and sex.

 

15. **Exposure:** The act of subjecting someone or something to an influencing experience.

 

16. **Family Medical History:** A record of a patient's background regarding health and disease events of blood relatives. A patient's family medical history may be important in diagnosing existing conditions.

 

17. **Therapeutic Procedure:** An action or administration of therapeutic agents to produce an effect that is intended to alter or stop a pathologic process.

 

18. **Diagnosis:** The investigation, analysis and recognition of the presence and nature of disease, condition, or injury from expressed signs and symptoms; also, the scientific determination of any kind; the concise results of such an investigation.

 

19. **Follow-up:** The process by which information about the health status of an individual is obtained after a study has officially closed; an activity that continues something that has already begun or that repeats something that has already been done.

 

20. **Stratification Factor:** Selected pre-treatment factor(s) by which patients are segregated to assure equal balance of these factors before randomization to the intervention arms of a clinical protocol.
