
import json
import fileinput

import re
import json
import fileinput
import json
import time

import csv

import operator 

from collections import Counter
import stop_words
import string

emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""
 
regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
 
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]
    
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
 
def tokenize(s):
    return tokens_re.findall(s)
 
def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    tokens = [x.lower() for x in tokens]
    return tokens

 
x=[]
y=[]
stop=['rally',
 'death',
 'custody',
 'arrest',
 'injustice',
 'violence',
 'revenge',
 'incident',
 'anger',
 'protestors',
 u'turmoil',
 u'riot',
 u'question',
 u'objection',
 u'dissent',
 u'assembly',
 u'convocation',
 u'session',
 u'convention',
 u'meet',
 u'ruination',
 u'decease',
 u'downfall',
 u'dissolution',
 u'repose',
 u'guardianship',
 u'protection',
 u'care',
 u'keeping',
 u'management',
 u'capture',
 u'incarceration',
 u'imprisonment',
 u'detention',
 u'restraining',
 u'inequity',
 u'wrongdoing',
 u'violation',
 u'discrimination',
 u'oppression',
 u'rampage',
 u'disturbance',
 u'brutality',
 u'clash',
 u'confusion',
 u'retribution',
 u'attack',
 u'vengeance',
 u'reprisal',
 u'counterblow',
 u'episode',
 u'circumstance',
 u'scene',
 u'matter',
 u'event',
 u'annoyance',
 u'acrimony',
 u'impatience',
 u'enmity',
 u'rage',
 u'militant',
 u'dissident',
 u'activist',
 u'anxiety',
 u'strife',
 u'brawl',
 u'uproar',
 u'query',
 u'investigation',
 u'inquiry',
 u'questioning',
 u'inquisition',
 u'criticism',
 u'grievance',
 u'exception',
 u'rejection',
 u'displeasure',
 u'discord',
 u'disunity',
 u'resistance',
 u'dissension',
 u'gathering',
 u'crowd',
 u'cluster',
 u'huddle',
 u'council',
 u'confab',
 u'conference',
 u'conclave',
 u'congress',
 u'turnout',
 u'discussion',
 u'term',
 u'period',
 u'hearing',
 u'meeting',
 u'show',
 u'right',
 u'fair',
 u'fit',
 u'reconciled',
 u'appropriate',
 u'undoing',
 u'wrack',
 u'liquidation',
 u'extinction',
 u'curtains',
 u'dying',
 u'departure',
 u'quietus',
 u'breakdown',
 u'collapse',
 u'debacle',
 u'deterioration',
 u'divorce',
 u'partition',
 u'disintegration',
 u'division',
 u'divorcement',
 u'inactivity',
 u'stillness',
 u'quietude',
 u'renewal',
 u'quietness',
 u'safekeeping',
 u'watch',
 u'trust',
 u'shelter',
 u'preservation',
 u'stability',
 u'conservation',
 u'safety',
 u'responsibility',
 u'load',
 u'encumbrance',
 u'distress',
 u'foreboding',
 u'observance',
 u'charge',
 u'executive',
 u'administration',
 u'board',
 u'authority',
 u'head',
 u'apprehension',
 u'taking',
 u'confiscation',
 u'seizure',
 u'confinement',
 u'captivity',
 u'restraint',
 u'isolation',
 u'quarantine',
 u'delay',
 u'forbidding',
 u'governing',
 u'restrictive',
 u'coercive',
 u'constraining',
 u'unfairness',
 u'wrong',
 u'misbehavior',
 u'crime',
 u'misdeed',
 u'malpractice',
 u'encroachment',
 u'negligence',
 u'infringement',
 u'infraction',
 u'misdemeanor',
 u'intolerance',
 u'favoritism',
 u'bigotry',
 u'prejudice',
 u'dictatorship',
 u'maltreatment',
 u'cruelty',
 u'despotism',
 u'binge',
 u'orgy',
 u'frenzy',
 u'uprising',
 u'shock',
 u'explosion',
 u'fracas',
 u'savagery',
 u'inhumanity',
 u'barbarity',
 u'barbarism',
 u'rift',
 u'crash',
 u'melee',
 u'bewilderment',
 u'embarrassment',
 u'turbulence',
 u'distraction',
 u'comeuppance',
 u'retaliation',
 u'compensation',
 u'raid',
 u'intrusion',
 u'onslaught',
 u'offensive',
 u'return',
 u'requital',
 u'counteraction',
 u'reciprocation',
 u'chapter',
 u'installment',
 u'experience',
 u'thing',
 u'case',
 u'status',
 u'accident',
 u'occurrence',
 u'fate',
 u'scenery',
 u'picture',
 u'set',
 u'theater',
 u'material',
 u'element',
 u'body',
 u'individual',
 u'affair',
 u'crisis',
 u'ceremony',
 u'story',
 u'discontent',
 u'exasperation',
 u'pique',
 u'frustration',
 u'animosity',
 u'ill will',
 u'belligerence',
 u'bitterness',
 u'rancor',
 u'nervousness',
 u'eagerness',
 u'excitement',
 u'antagonism',
 u'hostility',
 u'madness',
 u'furor',
 u'temper',
 u'fury',
 u'militaristic',
 u'vigorous',
 u'assertive',
 u'belligerent',
 u'bellicose',
 u'discordant',
 u'sectarian',
 u'nonconformist',
 u'heretical',
 u'heterodox',
 u'revolutionary',
 u'advocate',
 u'opponent',
 u'restlessness',
 u'suffering',
 u'uncertainty',
 u'squabble',
 u'warfare',
 u'argument',
 u'ruckus',
 u'flap',
 u'reservation',
 u'search',
 u'survey',
 u'review',
 u'probe',
 u'audit',
 u'study',
 u'examination',
 u'inquest',
 u'inquiring',
 u'catechism',
 u'interrogation',
 u'trial',
 u'third degree',
 u'comment',
 u'assessment',
 u'critique',
 u'opinion',
 u'hardship',
 u'sorrow',
 u'resentment',
 u'grief',
 u'omission',
 u'exclusion',
 u'barring',
 u'expulsion',
 u'veto',
 u'elimination',
 u'repudiation',
 u'turndown',
 u'distaste',
 u'disapproval',
 u'umbrage',
 u'tumult',
 u'dissonance',
 u'disharmony',
 u'harshness',
 u'jangle',
 u'divergence',
 u'divergency',
 u'severance',
 u'intransigence',
 u'support',
 u'refusal',
 u'fight',
 u'fuss',
 u'wrangle',
 u'function',
 u'throng',
 u'group',
 u'horde',
 u'sellout',
 u'people',
 u'chunk',
 u'batch',
 u'collection',
 u'band',
 u'bundle',
 u'mess',
 u'gang',
 u'committee',
 u'ring',
 u'dialogue',
 u'chat',
 u'chitchat',
 u'palaver',
 u'forum',
 u'consultation',
 u'seminar',
 u'interview',
 u'powwow',
 u'society',
 u'union',
 u'attendance',
 u'number',
 u'deliberation',
 u'exchange',
 u'phrase',
 u'style',
 u'word',
 u'name',
 u'language',
 u'span',
 u'stretch',
 u'season',
 u'age',
 u'perception',
 u'extent',
 u'faculty',
 u'reach',
 u'effect',
 u'showdown',
 u'contest',
 u'competition',
 u'pageant',
 u'parade',
 u'appearance',
 u'program',
 u'good',
 u'legal',
 u'honest',
 u'legitimate',
 u'civil',
 u'sincere',
 u'unbiased',
 u'lawful',
 u'proper',
 u'wise',
 u'capable',
 u'able',
 u'apt',
 u'prepared',
 u'regulated',
 u'accustomed',
 u'resigned',
 u'adapted',
 u'adjusted',
 u'relevant',
 u'useful',
 u'convenient',
 u'applicable',
 u'miscalculation',
 u'disgrace',
 u'decimate',
 u'torment',
 u'wreck',
 u'ruin',
 u'trash',
 u'eradication',
 u'removal',
 u'withdrawal',
 u'clearance',
 u'annihilation',
 u'destruction',
 u'obsolescence',
 u'exit',
 u'bitter end',
 u'end of the line',
 u'doomed',
 u'fading',
 u'moribund',
 u'decaying',
 u'sinking',
 u'retirement',
 u'flight',
 u'evacuation',
 u'escape',
 u'clincher',
 u'overthrow',
 u'coup de grace',
 u'final blow',
 u'overcoming',
 u'disruption',
 u'mishap',
 u'failure',
 u'neurosis',
 u'catastrophe',
 u'devastation',
 u'disaster',
 u'decline',
 u'devaluation',
 u'slump',
 u'degradation',
 u'depreciation',
 u'breakup',
 u'split',
 u'separation',
 u'annulment',
 u'barrier',
 u'segregation',
 u'apportionment',
 u'putrefaction',
 u'demoralization',
 u'fragmentation',
 u'decentralization',
 u'distribution',
 u'selection',
 u'disunion',
 u'disjuncture',
 u'detachment',
 u'sluggishness',
 u'stagnation',
 u'lethargy',
 u'torpor',
 u'dormancy',
 u'hush',
 u'tranquility',
 u'calmness',
 u'serenity',
 u'doldrums',
 u'placidness',
 u'dispassion',
 u'rebirth',
 u'revival',
 u'rejuvenation',
 u'regeneration',
 u'resumption',
 u'calm',
 u'refuge',
 u'assurance',
 u'certainty',
 u'timepiece',
 u'chronometer',
 u'wristwatch',
 u'stopwatch',
 u'ticker',
 u'faith',
 u'confidence',
 u'expectation',
 u'hope',
 u'positiveness',
 u'shed',
 u'sanctuary',
 u'dwelling',
 u'house',
 u'hut',
 u'storage',
 u'conservancy',
 u'security',
 u'strength',
 u'cohesion',
 u'balance',
 u'control',
 u'supervision',
 u'freedom',
 u'immunity',
 u'duty',
 u'power',
 u'importance',
 u'goods',
 u'capacity',
 u'weight',
 u'haul',
 u'albatross',
 u'saddle',
 u'irritation',
 u'unhappiness',
 u'shame',
 u'pang',
 u'affliction',
 u'premonition',
 u'dread',
 u'prognostic',
 u'adherence',
 u'acknowledgment',
 u'compliance',
 u'fulfillment',
 u'celebration',
 u'complaint',
 u'indictment',
 u'allegation',
 u'stink',
 u'gripe',
 u'managerial',
 u'ruling',
 u'controlling',
 u'managing',
 u'government',
 u'agency',
 u'legislation',
 u'rule',
 u'panel',
 u'strip',
 u'plank',
 u'timber',
 u'slat',
 u'jurisdiction',
 u'force',
 u'pizzazz',
 u'prime',
 u'champion',
 u'principal',
 u'leading',
 u'premier',
 u'alarm',
 u'disquiet',
 u'mistrust',
 u'misgiving',
 u'catching',
 u'pandemic',
 u'communicative',
 u'contagious',
 u'expansive',
 u'appropriation',
 u'expropriation',
 u'arrogation',
 u'stroke',
 u'illness',
 u'convulsion',
 u'repression',
 u'jail',
 u'bondage',
 u'slavery',
 u'restriction',
 u'constraint',
 u'self-restraint',
 u'moderation',
 u'solitude',
 u'desolation',
 u'remoteness',
 u'seclusion',
 u'sequestration',
 u'stoppage',
 u'lag',
 u'setback',
 u'moratorium',
 u'postponement',
 u'sinister',
 u'threatening',
 u'menacing',
 u'frightening',
 u'grim',
 u'administrative',
 u'dominant',
 u'ascendant',
 u'antagonistic',
 u'confining',
 u'opposed',
 u'prohibitive',
 u'prohibitory',
 u'bullying',
 u'violent',
 u'forced',
 u'forceful',
 u'intimidating',
 u'inhibit',
 u'bind',
 u'necessitate',
 u'curb',
 u'constrict',
 u'malfeasance',
 u'untrue',
 u'inaccurate',
 u'mistaken',
 u'unsound',
 u'bad',
 u'impropriety',
 u'immorality',
 u'insubordination',
 u'transgression',
 u'lawlessness',
 u'felony',
 u'peccadillo',
 u'carelessness',
 u'dereliction',
 u'invasion',
 u'inroad',
 u'trespass',
 u'disregard',
 u'oversight',
 u'neglect',
 u'laxity',
 u'lapse',
 u'error',
 u'offense',
 u'criminality',
 u'dogmatism',
 u'narrow-mindedness',
 u'nepotism',
 u'partisanship',
 u'racism',
 u'bias',
 u'sexism',
 u'tyranny',
 u'authoritarianism',
 u'totalitarianism',
 u'autocracy',
 u'fascism',
 u'injury',
 u'abuse',
 u'torture',
 u'malice',
 u'blind',
 u'carousal',
 u'fling',
 u'spree',
 u'indulgence',
 u'surfeit',
 u'fever',
 u'burst',
 u'revolution',
 u'upheaval',
 u'revolt',
 u'rebellion',
 u'impact',
 u'consternation',
 u'bump',
 u'outbreak',
 u'blast',
 u'detonation',
 u'outburst',
 u'depravity',
 u'atrocity',
 u'vulgarity',
 u'viciousness',
 u'breach',
 u'flaw',
 u'fissure',
 u'gap',
 u'sound',
 u'smash',
 u'din',
 u'tussle',
 u'scuffle',
 u'perplexity',
 u'surprise',
 u'discombobulation',
 u'daze',
 u'dilemma',
 u'chagrin',
 u'unease',
 u'bluster',
 u'interruption',
 u'complication',
 u'aberration',
 u'due',
 u'recompense',
 u'just deserts',
 u'punishment',
 u'eye for an eye',
 u'redress',
 u'settlement',
 u'payoff',
 u'wage',
 u'fee',
 u'break-in',
 u'sortie',
 u'sweep',
 u'imposition',
 u'interference',
 u'incursion',
 u'blitz',
 u'onset',
 u'assault',
 u'distasteful',
 u'obnoxious',
 u'embarrassing',
 u'rude',
 u'abhorrent',
 u'arrival',
 u'entry',
 u'rebound',
 u'restoration',
 u'recovery',
 u'counterpoise',
 u'interchange',
 u'barter',
 u'member',
 u'affiliate',
 u'branch',
 u'portion',
 u'payment',
 u'repayment',
 u'training',
 u'maturity',
 u'practice',
 u'understanding',
 u'wisdom',
 u'point',
 u'information',
 u'piece',
 u'bin',
 u'crate',
 u'crib',
 u'wallet',
 u'sheath',
 u'dignity',
 u'prominence',
 u'place',
 u'stature',
 u'position',
 u'calamity',
 u'hazard',
 u'existence',
 u'incidence',
 u'instance',
 u'destiny',
 u'chance',
 u'future',
 u'decor',
 u'furnishings',
 u'terrain',
 u'setting',
 u'landscape',
 u'impression',
 u'photograph',
 u'copy',
 u'art',
 u'description',
 u'firm',
 u'bent',
 u'stated',
 u'specified',
 u'rooted',
 u'arena',
 u'opera house',
 u'room',
 u'theatre',
 u'cinema',
 u'actual',
 u'perceptible',
 u'substantial',
 u'appreciable',
 u'earthly',
 u'fundamental',
 u'item',
 u'component',
 u'detail',
 u'frame',
 u'carcass',
 u'shaft',
 u'embodiment',
 u'figure',
 u'respective',
 u'singular',
 u'personal',
 u'sole',
 u'lone',
 u'project',
 u'transaction',
 u'proceeding',
 u'crunch',
 u'emergency',
 u'pressure',
 u'service',
 u'version',
 u'fantasy',
 u'fable',
 u'biography',
 u'uneasiness',
 u'regret',
 u'provocation',
 u'tiff']


fl = open("graph.csv","w")
wr = csv.writer(fl)
# f is the file pointer to the JSON data set
for line in fileinput.input("BAL-4.0.json"):
    terms_hash=[]
    row=[]
    tweet = json.loads(line)
    
    terms_hash = [term for term in preprocess(tweet['text']) if term in stop]
    
    freq = len(terms_hash)
    tym = tweet['created_at']
    
    row.append(tym)
    row.append(freq)
    if freq > 0 :
        print freq
        print terms_hash
        print tweet['text']
        #time.sleep(1)
    wr.writerows([row])     
    
fl.close()    


    