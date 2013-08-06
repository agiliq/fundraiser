

function validate(){
	
	var frm = document.frmTransaction;
	var aName = Array();
	aName['account_id'] = 'Account ID';
	aName['reference_no'] = 'Reference No';
	aName['amount'] = 'Amount';
	aName['description'] = 'Description';
	aName['name'] = 'Billing Name';
	aName['address'] = 'Billing Address';
	aName['city'] = 'Billing City';
	aName['state'] = 'Billing State';
	aName['postal_code'] = 'Billing Postal Code';
	aName['country'] = 'Billing Country';
	aName['email'] = 'Billing Email';
	aName['phone'] = 'Billing Phone Number';
	aName['return_url']='Return URL';
	// aName['ship_name']='Shipping Name';
	// aName['ship_address']='Shipping Address';
	// aName['ship_city']='Shipping City';
	// aName['ship_state']='Shipping State';
	// aName['ship_postal_code']='Shipping Postal code';
	// aName['ship_country']='Shipping Country';
	// aName['ship_phone']='Shipping Phone';

	for(var i = 0; i < frm.elements.length ; i++){
		if((frm.elements[i].value.length == 0)||(frm.elements[i].value=="Select Country"))
		    {
				    if((frm.elements[i].name=='country')||(frm.elements[i].name=="ship_country"))
					     alert("Select the " + aName[frm.elements[i].name]);
					else
					     alert("Enter the " + aName[frm.elements[i].name]);
				    frm.elements[i].focus();
				    return false;
			}
			if(frm.elements[i].name=='account_id')
			    {
			
			        if(!validateNumeric(frm.elements[i].value))
			           {
							alert("Account Id must be NUMERIC");
							frm.elements[i].focus();
							return false;
						}
			    }
			
			if(frm.elements[i].name=='amount')
			    {
				   if(!validateNumeric(frm.elements[i].value))
				      {
					      alert("Amount should be NUMERIC");
						  frm.elements[i].focus();
						  return false;
					   }
				}

			if((frm.elements[i].name=='postal_code')||(frm.elements[i].name == 'ship_postal_code'))
			     {
			         if(!validateNumeric(frm.elements[i].value))
			           {
					     alert("Postal code should be NUMERIC");
						 frm.elements[i].focus();
						return false;
					   }
				 }	
			
			if((frm.elements[i].name=='phone')||(frm.elements[i].name =='ship_phone'))
			    {
					if(!validateNumeric(frm.elements[i].value))
					{
						alert("Enter a Valid CONTACT NUMBER");
						frm.elements[i].focus();
						return false;
					}
				}		
    	
    
	
		if((frm.elements[i].name == 'name')||(frm.elements[i].name == 'ship_name'))
		{
		
			if(validateNumeric(frm.elements[i].value))
			  {
					alert("Name should be a string");
					frm.elements[i].focus();
					return false;
			  }
		}
		
				
		if(frm.elements[i].name=='ship_postal_code'){
			if(!validateNumeric(frm.elements[i].value)){
					alert("Postal code should be NUMERIC");
			frm.elements[i].focus();
			return false;
			}
			}		
    
			
							
		if(frm.elements[i].name == 'email'){
				if(!validateEmail(frm.elements[i].value)){
					alert("Invalid input for " + aName[frm.elements[i].name]);
					frm.elements[i].focus();
					return false;
				}		
			}
			
	}  
	return true;
}

	function validateNumeric(numValue){
		if (!numValue.toString().match(/^[-]?\d*\.?\d*$/)) 
				return false;
		return true;		
	}

function validateEmail(email) {
    //Validating the email field
    var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
	//"
    if (! email.match(re)) {
        return (false);
    }
    return(true);
}


Array.prototype.inArray = function (value)
// Returns true if the passed value is found in the
// array.  Returns false if it is not.
{
    var i;
    for (i=0; i < this.length; i++) {
        // Matches identical (===), not just similar (==).
        if (this[i] === value) {
            return true;
        }
    }
    return false;
};
