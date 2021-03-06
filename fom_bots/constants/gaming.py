from typing import List

GAMER_TAGS = {
    'jordan': {
        'gamertag': 'XxDaewoo_LanosxX',
        'console': 'psn',
        'groupme_id': '5733418'
    },
    'branden': {
        'gamertag': 'HebrewHammer012',
        'console': 'psn',
        'groupme_id': '11197971'
    },
    'drew': {
        'gamertag': 'DrewP1014',
        'console': 'xbl',
        'groupme_id': '12475716'
    },
    'tom': {
        'gamertag': 'tstahle174',
        'console': 'psn',
        'groupme_id': '11201297'
    },
    'horn': {
        'gamertag': 'hornhub',
        'console': 'psn',
        'groupme_id': '11166971'
    },
    'lroll': {
        'gamertag': 'Rollyfingers002',
        'console': 'psn',
        'groupme_id': '5733441'
    },
    'shayne': {
        'gamertag': 'WolfBayne34',
        'console': 'psn',
        'groupme_id': '5531014'
    },
    'ruke': {
        'gamertag': 'Ruke J',
        'console': 'xbl',
        'groupme_id': '29798276'
    },
    'tyler': {
        'gamertag': 'smileyguys_1624',
        'console': 'psn',
        'groupme_id': '5824702'
    },
    'michael': {
        'gamertag': 'mooore27',
        'console': 'psn',
        'groupme_id': '16942747'
    },
    'josh': {
        'gamertag': 'jGilla_94',
        'console': 'psn',
        'groupme_id': '6202937'
    },
    'mike': {
        'gamertag': 'HMickman',
        'console': 'psn',
        'groupme_id': '11166935'
    }
}


def _build_profile_dict(users: List[str]) -> dict:
    out = {}
    for user in users:
        out[user] = GAMER_TAGS[user]
    return out


def _build_id_list(users: List[str]) -> List[str]:
    out = []
    for user in users:
        out.append(GAMER_TAGS[user]['groupme_id'])
    return out


COD_PROFILES = _build_profile_dict([
    'jordan', 'branden', 'drew', 'tom',
    'horn', 'lroll', 'shayne', 'ruke',
    'tyler', 'michael'
])

FIFA_PROFILES = _build_profile_dict([
    'branden', 'tom', 'lroll',
    'shayne', 'michael', 'josh',
    'mike'
])

PGA_PROFILES = _build_profile_dict([
    'branden', 'lroll', 'shayne', 'horn',
    'josh', 'tyler', 'ruke', 'tom'
])

QC_FOM = _build_id_list([
    'shayne', 'horn', 'tyler', 'ruke',
    'tom', 'drew', 'jordan'
])
