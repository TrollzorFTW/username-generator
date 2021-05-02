def first_combination(first_name,last_name):
	combinations = []
	
	# with no delimiter
	combinations.append(first_name+last_name)
	combinations.append(first_name.lower()+last_name)
	combinations.append(first_name+last_name.lower())
	combinations.append(first_name.lower()+last_name.lower())
	
	# with dot as delimiter
	combinations.append(first_name+'.'+last_name)
	combinations.append(first_name.lower()+'.'+last_name)
	combinations.append(first_name+'.'+last_name.lower())
	combinations.append(first_name.lower()+'.'+last_name.lower())
	
	# with underline as delimiter
	combinations.append(first_name+'_'+last_name)
	combinations.append(first_name.lower()+'_'+last_name)
	combinations.append(first_name+'_'+last_name.lower())
	combinations.append(first_name.lower()+'_'+last_name.lower())	
	
	return combinations

# 1 letter for first name and full last name
def second_combination(first_name,last_name):
	combinations = []

	# with no delimiter
	combinations.append(first_name[0]+last_name)
	combinations.append(first_name[0].lower()+last_name)
	combinations.append(first_name[0]+last_name.lower())
	combinations.append(first_name[0].lower()+last_name.lower())

	# with dot as delimiter
	combinations.append(first_name[0]+'.'+last_name)
	combinations.append(first_name[0].lower()+'.'+last_name)
	combinations.append(first_name[0]+'.'+last_name.lower())
	combinations.append(first_name[0].lower()+'.'+last_name.lower())
	
	# with underline as delimiter
	combinations.append(first_name[0]+'_'+last_name)
	combinations.append(first_name[0].lower()+'_'+last_name)
	combinations.append(first_name[0]+'_'+last_name.lower())
	combinations.append(first_name[0].lower()+'_'+last_name.lower())   
	
	return combinations


# full first name and just 1 letter for last name
def third_combination(first_name,last_name):
	combinations = []

	# with no delimiter
	combinations.append(first_name+last_name[0])
	combinations.append(first_name.lower()+last_name[0])
	combinations.append(first_name+last_name[0].lower())
	combinations.append(first_name.lower()+last_name[0].lower())

	# with dot as delimiter
	combinations.append(first_name+'.'+last_name[0])
	combinations.append(first_name.lower()+'.'+last_name[0])
	combinations.append(first_name+'.'+last_name[0].lower())
	combinations.append(first_name.lower()+'.'+last_name[0].lower())
	
	# with underline as delimiter
	combinations.append(first_name+'_'+last_name[0])
	combinations.append(first_name.lower()+'_'+last_name[0])
	combinations.append(first_name+'_'+last_name[0].lower())
	combinations.append(first_name.lower()+'_'+last_name[0].lower())   
	
	return combinations

