# Tool Documentation

This file serves as documentation for the tools in the python toolbox. The metadata for each individual tool has been populated, and these same documentation concepts are accessible in the tool tips for each tool. Though efforts will be made to ensure both sets are synchronized, this page will represent the most up-to-date documentation for the individual tools.

## Extract FFIEC Columns to New Feature Class

### Description

Allows for the extraction of specific columns and column ranges to a new feature class.

### Usage

The raw FFIEC dataset contains 1,212 columns. In the process of creating web resources, performing analyses, or simply managing geospatial resources, some may find that the full dataset is not necessary. This tools allows for the simple extraction of FFIEC fields to a new Census Tracts feature class.

### Parameters

Parameter | Description
-----------| -----------
FFIEC Layer | The tracts feature class that contains the FFIEC columns and census tract geographies. For best results, use the extracted [FFIEC Census Tracts Layer Package (August 26, 2022 release) Layer Package](https://www.arcgis.com/home/item.html?id=148cb8590c714bcf9e1962ec6a404735) as input.
FFIEC Column Indexex to Extract | Use this parameter to specify which fields from the FFIEC data file you want present within the output. The parameter can use a series of individual field index references along with ranges. For example, an input of "1-50, 75, 89, 100-110" would be interpreted to pull the matching fields from the dataset and isolate them into a new feature class. The field indexes correspond with [File/Definitions Dictionary spreadsheet](https://www.ffiec.gov/Census/Census_Flat_Files/FFIEC_Census_File_Definitions_26AUG22.xlsx) available from the FFIEC Website. 
Output Feature Class | The output feature class to be created by the tool.

### Requirements and Resources

* FFIEC 2022 Census Tracts Feature Class - https://www.arcgis.com/home/item.html?id=148cb8590c714bcf9e1962ec6a404735
