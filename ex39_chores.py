#chores
from collections import OrderedDict

morning = ['Make Bed',
'Open blinds and curtains',
'10 minute tidy of common areas']

afternoon = ['Dishes',
'10 min tidy of bedrooms and bathrooms',
'Take out trash/recycling',
'Wipe down counters',
'Quick sweep']

week_1 = ["""Take inventory or pantry & 
linen closet for needed
home goods, toiletry supplies, etc.
""", """Review calendar for events""", 
"""Plan upcoming meals""", 
"""Misc. household admin. management"""]

week_2 = ['Wipe down appliances'
, 'Dishwash parts as needed']

full_fridge_cleanse = ['Wipe down counters',
'Discard any expired goods',
'Sanitize doors and handles']

week_3 = ['Full Fidge Cleanse',full_fridge_cleanse]

yearly_chore={'January':"Jan stuff",
'February': "Feb stuff", 'March':"March stuff",
'April':"April stuff", 'May':"May stuff",
 'June':"June stuff", 'July':'July stuff', 
 'August':'Aug stuff', 'September':'Sept stuff',
 'October':'Oct stuff', 'November':'Nov stuff',
 'December': 'Dec stuff'}

monthly_chore = {'Week 1':week_1, 'Week 2':week_2, 'Week 3':week_3, 'Week 4': yearly_chore}

weekly = OrderedDict({'Sunday':'No chores today - call your Mom!',
'Monday':'Laundry',
'Tuesday':monthly_chore,
'Wednesday':'Vacuum',
'Thursday':'Bathrooms',
'Friday':'Dust/polish/windows',
'Saturday':'Catch up'})


for k,v in yearly_chore.items():
	moy=k
	print("Your daily chore list:")
	print('%s:\n'% k)
	for k,v in monthly_chore.items():
		wk = k
		wk_list = v
		print('%s:\n' % k)
		for k, v in weekly.items():
			dow=k
			print('%s:\n' % k)
			if dow != 'Tuesday':
				print('\t%s'% v)
			else:
				for i in wk_list:
					print('\n\t%s'% i)
				if wk != 'Week 4':
					print('%s'% monthly_chore[wk])
				else:
					print('%s' % yearly_chore[moy])