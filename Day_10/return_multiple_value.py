def format_name(f_name,l_name):
	if f_name=="" or l_name=="":
		return "Provide some valid inputs"
	formatted_f_name = f_name.title();
	formatted_l_name = l_name.title();
	return f"{formatted_f_name} {formatted_l_name}"


name_format = format_name("sachin","jose")
print(name_format)
print(format_name("",""))