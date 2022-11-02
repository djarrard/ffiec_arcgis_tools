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

## Enrich Customer Portfolio with FFIEC Data

### Description
Associates FFIEC attributes to a customer dataset

### Usage
Use this tool to enrich an existing geocoded customer dataset with variables from the FFIEC. This tool is intended to be used the output of the Build FFIEC Feature Class tool. It accomplishes the join using the spatial relationship between the individual customer points and the census tract that it intersects.

### Parameters

Parameter | Description
-----------| -----------
Customer Point Layer | The input ArcGIS point layer representing the portfolio you wish to enrich. This input MUST be a point layer. If your customers are not yet geocoded, you will need to [geocode your customer table](https://pro.arcgis.com/en/pro-app/latest/tool-reference/geocoding/geocode-addresses.htm) first.
FFIEC Tracts Layer | The input tracts layer containing the fields you wish to join. Use the _Build FFIEC Feature Class_ tool to create this layer, and then use the output of that tool as input to this one.
Field Selection Mode | The input tracts layer containing the fields you wish to join. Use the Build FFIEC Feature Class tool to create this layer, and then use the output of that tool as input to this one.<br><br><ul><li><b>Join All Fields from the FFIEC Layer</b>- this option will join all available fields in the input tracts layer to the customer points.</li><li><b>Manually Select Fields</b> - this option will join all available fields in the input tracts layer to the customer points.</li></ul>
FFIEC Fields to Join (contextual) | This parameter is only available when the Field Selection Mode parameter is set to "Manually Select Fields". Use this parameter to select the individual fields you wish to join from the tracts layer to the customer layer.
Output Customer Feature Class | Specify the output location and desired name of the result layer.

### Requirements and Resources
