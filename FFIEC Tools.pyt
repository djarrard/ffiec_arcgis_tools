import arcpy


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = "toolbox"

        # List of tool classes associated with this toolbox
        self.tools = [extract_ffiec_columns, enrich_portfolio]


class Tool(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Tool"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = None
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        return

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return

class extract_ffiec_columns(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Extract FFIEC Columns to New Feature Class"
        self.description = "Allows for the easy extraction of specific FFIEC Columns"
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        ffiecLayer = arcpy.Parameter(
            displayName = "FFIEC Layer",
            name = "ffiecLayer",
            datatype = ["DEFeatureClass","GPFeatureLayer"],
            parameterType = "Required",
            direction = "Input")

        ffiecFields = arcpy.Parameter(
            displayName = "FFIEC Columns Indexes to Extract",
            name = "ffiecFields",
            datatype = "GPString",
            parameterType = "Required",
            direction = "Input")

        outFC = arcpy.Parameter(
            displayName = "Output Feature Class",
            name = "outFC",
            datatype = "GPFeatureLayer",
            parameterType = "Required",
            direction = "Output")
        params = [ffiecLayer, ffiecFields, outFC]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""     
        
        return 

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""

        parameters[0].clearMessage()
        fields = arcpy.ListFields(parameters[0].valueAsText)
        ffiec_fields = []
        for field in fields:
            if "ffiec_" in field.name:
                ffiec_fields.append(field.name)
        data = len(ffiec_fields)
        if data == 0:
            parameters[0].setErrorMessage("This layer contains no columns with an 'ffiec_' prefix in the field name. This tool is designed to work against columns that have an 'ffiec_' prefix. The original layer for which this tool was designed can be downloaded here: https://www.arcgis.com/home/item.html?id=148cb8590c714bcf9e1962ec6a404735")
        elif data != 1212:
            parameters[0].setWarningMessage(f"It appears that this layer does not contain the full 1,212 FFIEC columns in the original dataset for which this tool was designed (it contains {data} FFIEC columns). Though this tool may continue to work, bear in mind that the index ranges may need to be modified to work with this input.")

        parameters[1].clearMessage()
        if parameters[1].altered:
            parameters[1].clearMessage()
            element_list = parameters[1].valueAsText.split(",")
            field_list = []
            try:
                for item in element_list:
                        if "-" in item:
                            field_range = item.split("-")
                            start = int(field_range[0])
                            end = int(field_range[1]) + 1
                            for field in list(range(start,end)): 
                                field_list.append(field)
                        else:
                            field_list.append(int(item))
            except:
                parameters[1].setErrorMessage("The string contains an invalid entry. Entries must be numeric, comma-delimited, and may contain discreet values and ranges (e.g. '1-25, 50, 70-80, 100'.backups")
            string_error = False
            ffiec_fields = [f"ffiec_{x}" for x in field_list]
            fc_fields = [field.name for field in fields]
            for field in ffiec_fields:
                if field not in fc_fields:
                    string_error = True
            if string_error:
                parameters[1].setErrorMessage("The field list string contains a value that does not exist in the FFIEC Layer referenced")
            duplicates = [num for num in ffiec_fields if ffiec_fields.count(num) > 1]
            if len(duplicates) > 1:
                parameters[1].setErrorMessage("The field list string is specified in a way where a single field is specified more than once")
                
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        in_layer = parameters[0].valueAsText
        fields = parameters[1].valueAsText
        out_fc = parameters[2].valueAsText

        element_list = fields.split(",")
        field_list = []
        for item in element_list:
                if "-" in item:
                    field_range = item.split("-")
                    start = int(field_range[0])
                    end = int(field_range[1]) + 1
                    for field in list(range(start,end)): 
                        field_list.append(field)
                else:
                    field_list.append(int(item))

        ffiec_fields = [f"ffiec_{x}" for x in field_list]

        fc_fields = [f.name for f in arcpy.ListFields(in_layer) if "ffiec_" not in f.name]
        remove_list = ["objectid", "shape", "shape_length", "shape_area"]
        fc_fields = [item for item in fc_fields if item.lower() not in remove_list]
        final_list = fc_fields + ffiec_fields
        arcpy.AddMessage(f"Columns to be retained: {final_list}")

        fms = arcpy.FieldMappings()

        for field in final_list:
            fm = arcpy.FieldMap()
            fm.addInputField(in_layer, field)
            fms.addFieldMap(fm)

        
        arcpy.AddMessage("Field mappings generated")
        arcpy.conversion.FeatureClassToFeatureClass(in_layer,
                                                    os.path.dirname(out_fc),
                                                    os.path.basename(out_fc),
                                                    field_mapping = fms)
        arcpy.AddMessage("Feature Class exported")
        return

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return

class enrich_portfolio(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Enrich Customer Portfolio with FFIEC Data"
        self.description = "Transfers FFIEC attributes from a census tract layer to customer points based on spatial intersection"
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        ### portfolioLayer param[0] ###
        portfolioLayer = arcpy.Parameter(
            displayName = "Portfolio Point Layer",
            name = "portfolioLayer",
            datatype = "GPFeatureLayer",
            parameterType = "Required",
            direction = "Input")
        portfolioLayer.filter.list = ["Point"]

        ### tractsLayer param[1] ###
        tractsLayer = arcpy.Parameter(
            displayName = "FFIEC Tracts Layer",
            name = "tractsLayer",
            datatype = "GPFeatureLayer",
            parameterType = "Required",
            direction = "Input")
        tractsLayer.filter.list = ["Polygon"]

        ### fieldSelectMode param[2] ###
        fieldSelectMode = arcpy.Parameter(
            displayName = "Field Selection Mode",
            name = "fieldSelectMode",
            datatype = "GPString",
            parameterType = "Required",
            direction = "Input")

        fieldSelectMode.filter.type = "ValueList"
        fieldSelectMode.filter.list = ['Join All Fields from FFIEC Layer', 'Manually Select Fields']
        fieldSelectMode.value = "Join All Fields from FFIEC Layer"

        ### manualSelect param[3] ###
        manualSelect = arcpy.Parameter(
            displayName = "FFIEC Fields to Join",
            name = "manualSelect",
            datatype = "Field",
            parameterType = "Optional",
            multiValue = True,
            enabled = False,
            direction = "Input")

        manualSelect.parameterDependencies = [tractsLayer.name]

        ### resultLayer param[4] ###
        resultLayer = arcpy.Parameter(
            displayName = "Output Customer Feature Class",
            name = "resultLayer",
            datatype = "GPFeatureLayer",
            parameterType = "Required",
            direction = "Output")
        
        params = [portfolioLayer,tractsLayer,fieldSelectMode, manualSelect, resultLayer]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        if parameters[2].value == "Join All Fields from FFIEC Layer":
            parameters[3].enabled = False

        elif parameters[2].value == "Manually Select Fields":
            parameters[3].enabled = True
            
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""

        parameters[3].clearMessage()
        
        portfolio_fields = arcpy.ListFields(parameters[0].valueAsText)
        portfolio_fields = [field.name for field in portfolio_fields]
        join_fields = parameters[3].valueAsText
        join_fields = join_fields.split(';')
        
        conflict_flag = False
        for field in join_fields:
            if field in portfolio_fields:
                parameters[3].setErrorMessage(f"The portfolio layer already contains a field with a name that's identical to one you are trying to join from the join layer: {field}")

        return

    def execute(self, parameters, messages):
        """The source code of the tool."""

        target = parameters[0].valueAsText
        join = parameters[1].valueAsText
        mode = parameters[2].valueAsText
        out = parameters[4].valueAsText
        
        if mode == "Join All Fields from FFIEC Layer":
            arcpy.SpatialJoin_analysis(target, join, out)

        elif mode == "Manually Select Fields":
            joinList = parameters[3].valueAsText
            joinList = joinList.split(';')

            fieldmappings = arcpy.FieldMappings()
            fieldmappings.addTable(target)

            for field in joinList:
                fm = arcpy.FieldMap()
                arcpy.AddMessage(field)
                fm.addInputField(join, field)
                fieldmappings.addFieldMap(fm)

            arcpy.SpatialJoin_analysis(target, join, out,"","", fieldmappings)
        
        return


    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return
