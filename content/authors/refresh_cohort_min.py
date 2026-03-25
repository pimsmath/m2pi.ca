from jinja2 import Environment, FileSystemLoader, select_autoescape
import os
import pandas as pd

YEAR=2025

df = pd.read_excel(
        '/Users/iana/OneDrive - The University Of British Columbia/Shared/Programs/Mentorship/M2PI/2025/2025M2PICertificates.xlsx')

env = Environment(
    loader=FileSystemLoader("."),
    autoescape=select_autoescape()
)

user_template = env.get_template('_index.md.j2')

def get_affiliation_url(name):
    affiliation_urls = {
        'https://ualberta.ca': ['University of Alberta', 'The University of Alberta'],
        'https://ubc.ca': ['University of British Columbia', 'The University of British Columbia'],
        'https://ucalgary.ca': ['University of Calgary', 'The University of Calgary'],
        'https://uleth.ca' : ['University of Lethbridge', 'The University of Lethbridge'],
        'https://umanitoba.ca': ['University of Manitoba', 'The University of Manitoba'],
        'https://uregina.ca' : ['University of Regina', 'The University of Regina'],
        'https://usask.ca' : ['University of Saskatchewan', 'The University of Regina'],
        'https://sfu.ca' : ['Simon Fraser University'],
        'https://uvic.ca' : ['University of Victoria', 'The University of Victoria'],
        'https://uw.edu' : ['University of Washington', 'The University of Washington'],
        'https://brocku.ca' : ['Brock University'],
        'https://uottawa.ca': ['University of Ottawa', 'The University of Ottawa'],
        'https://unbc.ca': ['University of Northern British Columbia'],
    }
    for k, l in affiliation_urls.items():
        if name in l:
            return k
    return ''


for index, user in df.iterrows():
    context = {
      'name': user['name'],
      'username': user['username'],
      'affiliation': user['affiliation'],
      'affiliation_url': get_affiliation_url(user['affiliation']),
      'role': '',
      'team': user['team'],
      'year': YEAR,
      'certificate': True,
      'm2pi_edition': 'M2PI2025',
      'date': '2025-05-27T09:00:00-08:00',
      'issued': 'true',
    }
    ifname = f"{user['username']}/_index.md"
    print(ifname)
    if os.path.isfile(ifname):
        print(f"Would skip {user['name']}")
    else:
        with open(ifname, 'w', encoding='utf-8') as f:
            f.write(user_template.render(context))
