from collections import OrderedDict



contacts = {

	'joe':{'phone':'234-0987','email':'abc@mail.com','address':'lagos'},

	'jane':{'phone':'234-0774','email':'ert@gmail.com','address':'benin'},

	'pat':{'phone':'234-0823','email':'xyz@gmail.com','address':'enugu'},

	'moe':{'phone':'234-0915','email':'moe@mail.com','address':'abuja'}

}

o_contacts = OrderedDict(contacts)

for i in range(len(o_contacts)):
	print(i)
 