# FFIEC ArcGIS Tools

## Features

This project is intended as an immediately usable resource in an ArcGIS Pro environment that allows users to perform common FFIEC/CRA/Compliance workflows within ArcGIS using FFIEC data. This toolset serves as a bridge of sorts that enables seemless integration of FFIEC data and spatial analyses that are frequently used for reporting and evaluation in compliance workflows. This toolbox is designed to work against the [FFIEC Census Tracts layer package](https://www.arcgis.com/home/item.html?id=148cb8590c714bcf9e1962ec6a404735) available for download in [ArcGIS Online](https://www.arcgis.com/index.html). 

* **[Extract FFIEC Columns to New Feature Class](https://github.com/djarrard/ffiec_arcgis_tools/blob/main/Tool%20Documentation.md#extract-ffiec-columns-to-new-feature-class)** - The FFIEC Census Tracts layer package includes over 1200 columns translated from the FFIEC Flat File. This tool allows the user to intelligently specify a selction of fields and extract them, along with the Census Tract geographies, to a new Feature Class. This is useful for creating more wieldable data structures for publishing to web services or downstream analysis where every original FFIEC column is simply not needed. 

## Instructions and Notes

1. Download the repository ZIP file
2. Extract the ZIP file to the desired folder
3. If necessary, in your ArcGIS Pro project, use the Catalog view to add a connection to the folder containing the extracted repository.
4. In the Catalog view, expand the _FFIEC Tools.pyt_ toolbox.
5. Double-click a tool to launch it.

## Requirements

1. ArcGIS Pro 3.0 or higher. Lower versions may work but have not been tested. Please submit an issue if you have issues specific to versions of ArcGIS Pro.
2. The Geoprocessing tools used in the toolbox only require a Basic license of ArcGIS Pro. No extensions are used. Standard and Advanced licenses are supported, but not required.
3. This toolbox will not work in ArcMap, and no development efforts will be made to make a compatible version.

## Issues

If there are bugs/issues with the toolbox that prevent usage or create incorrect results, please let me know by submitting an issue. I am also open to expanding the toolbox to include other use cases that expand capabilities and compatibility with compliance workflows. Please feel free to submit enhancement requests along those lines.

## Contributing

I follow the Esri Github guidelines for contributing. Please see [guidelines for contributing](https://github.com/esri/contributing).

## Licensing

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at


   http://www.apache.org/licenses/LICENSE-2.0


Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.


A copy of the license is available in the repository.
