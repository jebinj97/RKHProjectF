$(function(){
var countryOptions;
var stateOptions;
var districtOptions;
var sectorOptions;
var schemeOptions;
	$.getJSON('/static/data/countries.json',function(result){
		$.each(result, function(i,country) {
			//<option value='countrycode'>contryname</option>
			countryOptions+="<option value='"
			+country.code+
			"'>"
			+country.name+
			"</option>";
			 });
			 $('#country').html(countryOptions);
	});
	$("#country").change(function(){
	if($(this).val()=="IN"){
			$.getJSON('/static/data/indianStates.json',function(result){
			$.each(result, function(stateCode,stateName) {
				//<option value='stateCode'>stateName</option>
				stateOptions+="<option value='"
				+stateCode+
				"'>"
				+stateName+
				"</option>";
				 });
				 $('#state').html(stateOptions);
			});
		}
	});

	$("#state").change(function(){
	if($(this).val()=="KL"){
			$.getJSON('/static/data/MHDistricts.json',function(result){
			$.each(result, function(i,district) {
				//<option value='districtName'>districtName</option>
				districtOptions+="<option value='"+district.name+"'>"
				+district.name+
				"</option>";
				 });
				 $('#district').html(districtOptions);
			});
		}
	});
	$.getJSON('/static/data/sector.json',function(result){
		$.each(result, function(i,sector) {
			sectorOptions+="<option value='"
			+sector.code+
			"'>"
			+sector.name+
			"</option>";
			 });
			 $('#sector').html(sectorOptions);
	});
	$("#sector").change(function(){
		if($(this).val()=="E"){
				$.getJSON('/static/data/education.json',function(result){
				$.each(result, function(schemeCode,schemeName) {
					//<option value='stateCode'>stateName</option>
					schemeOptions+="<option value='"
					+schemeCode+
					"'>"
					+schemeName+
					"</option>";
					 });
					 $('#scheme').html(schemeOptions);
				});
			}
		});
		$("#sector").change(function(){
			if($(this).val()=="H"){
					$.getJSON('/static/data/housing.json',function(result){
					$.each(result, function(schemeCode,schemeName) {
						//<option value='stateCode'>stateName</option>
						schemeOptions+="<option value='"
						+schemeCode+
						"'>"
						+schemeName+
						"</option>";
						 });
						 $('#scheme').html(schemeOptions);
					});
				}
			});
			$("#sector").change(function(){
				schemeOptions="-";
				if($(this).val()=="M"){
						$.getJSON('/static/data/medical.json',function(result){
						$.each(result, function(schemeCode,schemeName) {
							//<option value='stateCode'>stateName</option>
							schemeOptions+="<option value='"
							+schemeCode+
							"'>"
							+schemeName+
							"</option>";
							 });
							 $('#scheme').html(schemeOptions);
						});
					}
				});
				$("#sector").change(function(){
					schemeOptions="-";
					if($(this).val()=="L"){
							$.getJSON('/static/data/land.json',function(result){
							$.each(result, function(schemeCode,schemeName) {
								//<option value='stateCode'>stateName</option>
								schemeOptions+="<option value='"
								+schemeCode+
								"'>"
								+schemeName+
								"</option>";
								 });
								 $('#scheme').html(schemeOptions);
							});
						}
					});
					$("#sector").change(function(){
						schemeOptions="-";
						if($(this).val()=="W"){
								$.getJSON('/static/data/water.json',function(result){
								$.each(result, function(schemeCode,schemeName) {
									//<option value='stateCode'>stateName</option>
									schemeOptions+="<option value='"
									+schemeCode+
									"'>"
									+schemeName+
									"</option>";
									 });
									 $('#scheme').html(schemeOptions);
								});
							}
						});
						$("#sector").change(function(){
							schemeOptions="-";
							if($(this).val()=="F"){
									$.getJSON('/static/data/finance.json',function(result){
									$.each(result, function(schemeCode,schemeName) {
										//<option value='stateCode'>stateName</option>
										schemeOptions+="<option value='"
										+schemeCode+
										"'>"
										+schemeName+
										"</option>";
										 });
										 $('#scheme').html(schemeOptions);
									});
								}
							});
		});
