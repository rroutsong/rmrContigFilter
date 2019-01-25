/*
A KBase module: rmrContigFilter
This sample module contains one small method that filters contigs.
*/

module rmrContigFilter {
    typedef structure {
        string report_name;
        string report_ref;
    } ReportResults;

	typedef string data_obj_ref;
	
	typedef structure {
		string output_workspace;
		data_obj_ref assembly_input_ref;
		int min_length;
		int max_length;
    	string report_ref;
        string report_name;
	} rmrContigFiltermaxinput;

	typedef string assembly_ref;
	
	typedef structure {
		assembly_ref output_assembly_ref;
		string report_name;
        string report_ref;
	} ReportResultsmax;

    /*
        Example app which filters contigs in an assembly using both a minimum contig length
    */
    funcdef run_rmrContigFilter(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;

    /*
        New app which filters contigs in an assembly using both a minimum and a maximum contig length
    */
    funcdef run_rmrContigFilter_max(rmrContigFiltermaxinput params) returns (ReportResultsmax output) authentication required;
};
