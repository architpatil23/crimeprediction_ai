from django import forms

district_choices=[
('CENTRAL','Sohna Road'),
('EASTERN','Golf Course Road'),
('WESTERN','Sector 29'),
('SOUTHERN','MG Road'),
('NORTHERN','Cyber City'),
('NORTHEASTERN','Civil Lines'),
('NORTHWESTERN','Palam Vihar'),
('SOUTHEASTERN','DLF Phase 1'),
('SOUTHWESTERN','Galleria'),
]
hour_choices= [tuple([x,x]) for x in range(0,24)]
hour_choices.append(['All','All']);
day_choices= [
('Monday','Monday'),
('Tuesday','Tuesday'),
('Wednesday','Wednesday'),
('Thursday','Thursday'),
('Friday','Friday'),
('Saturday','Saturday'),
('Sunday','Sunday'),
('All','Weekly'),
]
class CrimeForm(forms.Form):
	dist = forms.CharField(label='Area:', widget=forms.Select(choices=district_choices))
	nbd = forms.CharField(label='Neighbourhood:')
	hour = forms.CharField(label='Hour:', widget=forms.Select(choices=hour_choices))
	day = forms.CharField(label='Day:', widget=forms.Select(choices=day_choices), required=False)  
	#filename ADD
	filename=forms.CharField(label='Uploaded Filename:', required=False)  