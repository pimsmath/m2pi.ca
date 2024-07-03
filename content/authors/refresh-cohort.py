from jinja2 import Environment, FileSystemLoader, select_autoescape

import pandas as pd
import segno

YEAR = 2024

env = Environment(
    loader=FileSystemLoader("."),
    autoescape=select_autoescape()
)
user_template = env.get_template('_index.md.j2')

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
}

cols = {
    17: 'name',
    18: 'affiliation',
    19: 'role',
    20: 'team',
    21: 'degree_name1',
    22: 'degree_name2',
    23: 'degree_name3',
    24: 'degree_institution1',
    25: 'degree_institution2',
    26: 'degree_institution3',
    27: 'interest1',
    28: 'interest2',
    29: 'interest3',
    30: 'interest4',
    31: 'interest5',
    32: 'interest6',
    33: 'interest7',
    34: 'interest8',
    35: 'interest9',
    36: 'interest10',
    37: 'social1',
    38: 'social2',
    39: 'social3',
    40: 'social4',
    45: 'bio',
}

social_services = {
    'linkedin'     : {'icon': 'linkedin', 'icon_pack': 'fab'},
    'google'       : {'icon': 'google-scholar', 'icon_pack': 'ai'},
    'github'       : {'icon': 'github', 'icon_pack': 'fab'},
    'researchgate' : {'icon': 'researchgate', 'icon_pack': 'ai'},
    'youtube'      : {'icon': 'youtube', 'icon_pack': 'fab'},
}


fellows = pd.read_csv(
  '~/Downloads/m2piprofile-2024.csv',
  skiprows=3,
  usecols=cols.keys(),
  names=cols.values()
)

fellows_obj = fellows.select_dtypes('object')
fellows[fellows_obj.columns] = fellows_obj.apply(lambda x: x.str.strip())

for index, user in fellows.iterrows():

    affiliation = affiliation_url = ''
    affiliation_found = False
    for k, v in affiliation_urls.items():
        if user['affiliation'] in v:
            affiliation =  v[0]
            affiliation_url = k
            affiliation_found=True
    if not affiliation_found:
        print(f"Didn't find affiliation {user['affiliation']} for {user['name']}")

    courses = []
    if user['degree_name1'] == user['degree_name1']:
        courses.append({'name': user['degree_name1'], 'institution': user['degree_institution1']})
    if user['degree_name2'] == user['degree_name2']:
        courses.append({'name': user['degree_name2'], 'institution': user['degree_institution2']})
    if user['degree_name3'] == user['degree_name3']:
        courses.append({'name': user['degree_name3'], 'institution': user['degree_institution3']})

    interests = [user[f'interest{x}'] for x in list(range(1, 11)) if user[f'interest{x}'] == user[f'interest{x}']]


    socials = []
    for social in [user[f'social{i}'] for i in range(1, 5)]:
        if pd.notna(social):
            socialFound = False
            for site, details in social_services.items():
                if site in social:
                    socialFound = True 
                    socials.append({'icon': details['icon'], 'icon_pack': details['icon_pack'], 'link': social })
            if not socialFound:
                print(f"Didn't find: {social}")

    context = {
        'name' : user['name'],
        'username': (user['name'][0] + ''.join(user['name'].split()[-1:])).lower(),
        'affiliation': affiliation,
        'affiliation_url': affiliation_url,
        'role': user['role'],
        'team': user['team'],
        'courses': courses,
        'interests': interests,
        'socials': socials,
        'bio': user['bio'] if pd.notna(user['bio']) else '',
        'cert': {
            'file': f"./{YEAR}/cert.pdf",
            'img': f"./{YEAR}/cert.png",
            'title': f"M2PI{YEAR}",
            'date': '2024-06-26T10:00:00-07:00',
            'issued': 'true',
        },
    }

    with open(f"{context['username']}_index.md", 'w', encoding='utf-8') as f:
        f.write(user_template.render(context))

    cert_url = f"https://m2pi.ca/authors/{context['username']}/cert"
    qr = segno.make(cert_url)
    qr.save(f"{context['username']}_qr.png", scale=10, border=4)
