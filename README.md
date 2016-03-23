# YoRaS
Years of Rice and Salt mod for EU4
contact todd@tjgilbert.com if your interested in helping

current (3.26.2016) Split plague effected prov into 6 groups based on this chart: http://3.bp.blogspot.com/-Nrei3k9FN2k/VIIy9HbeQ9I/AAAAAAAAArs/1XHWTrNLfwM/s1600/bdeth.gif
  add event for each group:

1347.1.1 = {} # Black Death Arrives

1357.1.1 = {	base_manpower = 4 
		base_tax = 7
		base_production = 7} # 10 years into 1st Plague 
		
1367.1.1 = { 	base_manpower = 3 
		base_tax = 5
		base_production = 5} # End of 20 year Plague
		
1404.1.1 = {} # Final Death Arrives

1405.1.1 = {	owner = XXX
		controller = XXX
		citysize = 0 
		base_tax = 1 
		base_production = 1
		base_manpower = 1} # Final Death is complete

with 1340's dates matching the chart dates. 1350s and 1360s dates reduce base man/tax/prod by 33% and 66% respectively, rounded up. 1400 events are identical for all, for now. all future events are removed.

future tasks:
add in nations from the book using the dates in the text
fill in the gaps
