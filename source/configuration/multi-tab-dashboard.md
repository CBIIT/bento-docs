## To Configure tabs on Dashboard: 

1. Open `bento-frontend/src/bento/dashboardTabData.js`

2. To change Properties of tab go to `tabs` object:
- **`name`** : Text to show on tab
- **`dataField`**: specifies what data appears in the column, field must be from the GraphQL API query


3. To change style of tab go to `tabIndex` object : 
-  **`title`** : Text to shown on tab
-  **`primaryColor`** : background color when tab is selected
-  **`selectedColor`** : font color when tab is selected


4. To change Properties of table go to `table` object:
- **`dataField`** : field name in "Data" object to get values for table. 
- **`defaultSortField`**: Value must be one of the 'dataField' in columns.

- ```
  defaultSortField: '<GraphQL API query field used to sort the table.>'
  ```

- **defaultSortDirection**: Sort default column in Ascending or Descending order. 

- ```
  defaultSortDirection: '<sort order, asc|desc>',
  ```

- **buttonText**: Text to appear on Add to cart button**

- ```
  buttonText: '<Button Text>'
  ```

- **saveButtonDefaultStyle**: Style of on Add to cart button**

- ```
  saveButtonDefaultStyle: '<Button Style>'
  ```

- **ActiveSaveButtonDefaultStyle**: Style of on Add to cart button when it is active mode**

- ```
  ActiveSaveButtonDefaultStyle: '<Button Style>'
  ```

-  **DeactiveSaveButtonDefaultStyle**: Style of on Add to cart button when it is disabled mode**

- ActiveSaveButtonDefaultStyle: '<Button Style>'

- columns:

   List of Columns. Max 10 Columns. If added more than 10 columns, 

  Bento will display the first 10 columns without an error or warning message

  . The top-down order of columns will be displayed left to right on the UI. 

  - ```
    columns: [
        ...
        {
          dataField: '<GraphQL API query field returning data for this column>',
          header: '<Column Header>',
          link: '<link to be embedded in column value>'
          sort: '<sort order, asc|desc>',
          primary: true or false,
          display: true or false,
          dataFromRoot: true or false,
        },
      ...
    ]
    ```

- - - **dataField:** GraphQL API query field returning data for this column

    - **header**: Heading Text for column

    - **sort:** sort order for column

    - **primary:** applies to primary field of table like "sample_ID" or "File_ID" based on which files will be added in to cart.

    - **display:** Show or Hide column 

    - **dataFromRoot:** Get data from parent element.

    - link:

       Hyperlink to internal or external page. Field value can be injected in link dynamically using * { datafield }

      \* in link value string. 

      ```
      //Internal Link 
      link: '/arm/{dataField}',
      
      // External Link
      link: 'https://example.com/{dataField}'
      ```

 

 

5. To change Properties of tooltip go to tooltipContent object:

- **icon**: The help tip icon that appears next to the 'add button'

- ```
  icon: '<Icon Url>'
  ```

- **alt**: alt for the tooltip image **

- ```
  alt: '<Alt Text>'
  ```

-  **0,1,2**: tooltip content for first tab, second tab and third tab.

- ```
  0: '<Tooltip Message>'
  ```

 

 GraphQL Query used in the Dashboard page: 

```javascript
// GraphQL query to retrieve detailed info for a case
export const DASHBOARD_QUERY = gql`{
  numberOfPrograms
  numberOfStudies
  numberOfSubjects
  numberOfSamples
  numberOfLabProcedures
  numberOfFiles
  subjectCountByProgram{
        group
        subjects
      }
    subjectCountByStudy{
        group
        subjects
      }
    subjectCountByDiagnoses{
        group
        subjects
      }
    subjectCountByRecurrenceScore{
        group
        subjects
      }
    subjectCountByTumorSize{
        group
        subjects
      }
    subjectCountByChemotherapyRegimen{
        group
        subjects
      }
    subjectCountByTumorGrade{
        group
        subjects
      }
  subjectCountByErStatus{
        group
        subjects
      }
  subjectCountByPrStatus{
        group
        subjects
      }
  subjectCountByMenopauseStatus{
        group
        subjects
      }
  subjectCountByChemotherapyRegimen{
        group
        subjects
      }
      subjectCountByEndocrineTherapy{
    group
    subjects
  }
    armsByPrograms {
        program
        caseSize
        children {
            arm
            caseSize
            size
        }
    }  subjectOverViewPaged(first: 1000000) {
      subject_id
      program_id
      study_info
      samples
      program
      study_acronym
      diagnosis
      recurrence_score
      tumor_size
      tumor_grade
      er_status
      pr_status
      chemotherapy
      endocrine_therapy
      menopause_status
      age_at_index
      survival_time
      lab_procedures
      files{
        file_id
      }
  }
    sampleOverview {
        sample_id
        subject_id
        program
        arm
        diagnosis
        tissue_type
        tissue_composition
        sample_anatomic_site
        sample_procurement_method
        platform
        files 
    }
    
    fileOverview {
        file_id
        file_name
        association
        file_description
        file_format
        file_size
        program
        arm
        subject_id
        sample_id
        diagnosis
    }
  }`;
```
