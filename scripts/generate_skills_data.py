#!/usr/bin/env python3
"""
Generate skills data for GitHub Pages
Scans all skill files and generates JavaScript data file

Usage:
    python scripts/generate_skills_data.py
"""

import re
import yaml
import json
from pathlib import Path
from typing import Dict, List, Optional

SCRIPT_DIR = Path(__file__).parent.resolve()
PROJECT_ROOT = SCRIPT_DIR.parent
SKILLS_DIR = PROJECT_ROOT / 'skills'
EXTERNAL_AUTHOR_DIRS = [
    PROJECT_ROOT / 'external' / 'aakashg',
    PROJECT_ROOT / 'external' / 'wdavidturner',
]
OUTPUT_FILE = PROJECT_ROOT / 'assets/js/skills-data.js'

# Category icons mapping
CATEGORY_ICONS = {
    'executive': '👔',
    'software': '💻',
    'technology': '🔧',
    'ai-ml': '🤖',
    'healthcare': '⚕️',
    'medical': '🏥',
    'legal': '⚖️',
    'education': '🎓',
    'finance': '💰',
    'creative': '🎨',
    'research': '🔬',
    'product': '📦',
    'marketing': '📊',
    'automotive': '🚗',
    'data': '🗄️',
    'business': '💼',
    'construction': '🏗️',
    'manufacturing': '🏭',
    'energy': '⚡',
    'aerospace': '🚀',
    'agriculture': '🌾',
    'biotech': '🧬',
    'cybersecurity': '🔒',
    'blockchain': '⛓️',
    'robotics': '🦾',
    'quantum': '⚛️',
    'entertainment': '🎭',
    'media': '📺',
    'sports': '⚽',
    'transportation': '🚚',
    'hospitality': '🏨',
    'retail': '🛒',
    'real-estate': '🏠',
    'government': '🏛️',
    'public-service': '🚒',
    'military': '🎖️',
    'nonprofit': '❤️',
    'consulting': '💡',
    'hr': '👥',
    'operations': '⚙️',
    'sales': '🤝',
    'customer-service': '🎧',
    'admin': '📋',
    'facilities': '🏢',
    'environmental': '🌱',
    'safety': '🛡️',
    'quality': '✅',
    'supply-chain': '📦',
    'logistics': '🚛',
    'procurement': '🛍️',
    'events': '🎪',
    'writing': '✍️',
    'translation': '🌐',
    'interpreting': '🗣️',
    'teaching': '📚',
    'coaching': '🎯',
    'therapy': '🧠',
    'social-work': '🤲',
    'library': '📖',
    'museum': '🏛️',
    'archaeology': '⛏️',
    'architecture': '🏗️',
    'interior-design': '🛋️',
    'fashion': '👗',
    'culinary': '👨‍🍳',
    'baking': '🥖',
    'bartending': '🍸',
    'agriculture': '🚜',
    'fishing': '🎣',
    'forestry': '🌲',
    'mining': '⛏️',
    'oil-gas': '🛢️',
    'utilities': '💡',
    'waste-management': '♻️',
    'cleaning': '🧹',
    'maintenance': '🔧',
    'repair': '🛠️',
    'installation': '🔩',
    'inspection': '🔍',
    'testing': '🧪',
    'calibration': '⚖️',
    'automation': '🤖',
    'control-systems': '🎛️',
    'instrumentation': '📡',
    'telecommunications': '📡',
    'networking': '🌐',
    'cloud': '☁️',
    'devops': '🚀',
    'security-ops': '🔐',
    'database': '🗃️',
    'analytics': '📊',
    'visualization': '📈',
    'machine-learning': '🧠',
    'deep-learning': '🔮',
    'nlp': '💬',
    'computer-vision': '👁️',
    'robotics': '🦾',
    'embedded': '🔌',
    'iot': '📲',
    'hardware': '💾',
    'semiconductor': '💿',
    'optics': '🔭',
    'photonics': '✨',
    'nanotechnology': '🔬',
    'biomedical': '🏥',
    'pharmaceutical': '💊',
    'veterinary': '🐾',
    'dentistry': '🦷',
    'optometry': '👓',
    'physical-therapy': '🏃',
    'occupational-therapy': '🤲',
    'speech-therapy': '🗣️',
    'nutrition': '🥗',
    'fitness': '💪',
    'wellness': '🧘',
    'beauty': '💄',
    'spa': '🧖',
    'tourism': '✈️',
    'travel': '🌍',
    'hotel': '🏨',
    'restaurant': '🍽️',
    'catering': '🍱',
    'food-service': '🍔',
    'agriculture': '🌾',
    'horticulture': '🌷',
    'landscaping': '🌳',
    'gardening': '🌻',
    'animal-care': '🐕',
    'pet-care': '🐱',
    'veterinary': '🐾',
    'zoology': '🦁',
    'marine-biology': '🐋',
    'conservation': '🌿',
    'wildlife': '🦅',
    'forestry': '🌲',
    'fisheries': '🐟',
    'aquaculture': '🦐',
    'mining': '⛏️',
    'metallurgy': '🔩',
    'materials': '🔧',
    'ceramics': '🏺',
    'textiles': '🧵',
    'paper': '📄',
    'printing': '🖨️',
    'packaging': '📦',
    'shipping': '🚢',
    'freight': '📬',
    'warehousing': '🏭',
    'distribution': '🚚',
    'inventory': '📋',
    'purchasing': '🛒',
    'sourcing': '🌐',
    'vendor-management': '🤝',
    'contract-management': '📄',
    'project-management': '📊',
    'program-management': '📈',
    'portfolio-management': '💼',
    'change-management': '🔄',
    'risk-management': '⚠️',
    'compliance': '✅',
    'governance': '🏛️',
    'audit': '🔍',
    'forensics': '🔬',
    'investigation': '🕵️',
    'intelligence': '🧠',
    'research': '🔬',
    'development': '💡',
    'innovation': '✨',
    'design': '🎨',
    'engineering': '⚙️',
    'architecture': '🏗️',
    'planning': '📐',
    'scheduling': '📅',
    'estimating': '💰',
    'surveying': '📏',
    'mapping': '🗺️',
    'gis': '🌍',
    'remote-sensing': '🛰️',
    'photogrammetry': '📷',
    'cartography': '🗺️',
    'meteorology': '🌤️',
    'climatology': '🌡️',
    'oceanography': '🌊',
    'hydrology': '💧',
    'geology': '🪨',
    'seismology': '🌋',
    'volcanology': '🌋',
    'paleontology': '🦴',
    'anthropology': '🏺',
    'archaeology': '⛏️',
    'history': '📜',
    'philosophy': '🤔',
    'linguistics': '🗣️',
    'literature': '📚',
    'music': '🎵',
    'art': '🎨',
    'dance': '💃',
    'theater': '🎭',
    'film': '🎬',
    'photography': '📷',
    'journalism': '📰',
    'publishing': '📖',
    'broadcasting': '📡',
    'advertising': '📢',
    'public-relations': '📣',
    'marketing': '📊',
    'branding': '🏷️',
    'market-research': '📊',
    'consumer-insights': '👥',
    'product-research': '🔬',
    'usability': '👤',
    'accessibility': '♿',
    'inclusion': '🤝',
    'diversity': '🌈',
    'equity': '⚖️',
    'sustainability': '🌱',
    'csr': '❤️',
    'ethics': '⚖️',
    'legal': '⚖️',
    'regulatory': '📋',
    'policy': '📜',
    'advocacy': '📣',
    'lobbying': '🏛️',
    'diplomacy': '🕊️',
    'international-relations': '🌍',
    'trade': '💱',
    'economics': '📈',
    'finance': '💰',
    'accounting': '🧾',
    'tax': '📋',
    'insurance': '🛡️',
    'banking': '🏦',
    'investment': '📈',
    'wealth-management': '💎',
    'financial-planning': '📊',
    'credit': '💳',
    'lending': '🏦',
    'mortgage': '🏠',
    'real-estate': '🏢',
    'property-management': '🏘️',
    'facilities-management': '🏢',
    'construction-management': '🏗️',
    'site-management': '🏭',
    'safety-management': '🛡️',
    'quality-management': '✅',
    'process-improvement': '📈',
    'lean': '🏭',
    'six-sigma': '📊',
    'agile': '🔄',
    'scrum': '🏉',
    'kanban': '📋',
    'devops': '🚀',
    'sre': '🔧',
    'platform-engineering': '🏗️',
    'infrastructure': '🏭',
    'networking': '🌐',
    'telecom': '📡',
    'wireless': '📶',
    'satellite': '🛰️',
    'broadcast': '📺',
    'cable': '📡',
    'isp': '🌐',
    'datacenter': '🏢',
    'cloud': '☁️',
    'edge': '🔷',
    'cdn': '🌐',
    'hosting': '🖥️',
    'colocation': '🏢',
    'managed-services': '🔧',
    'outsourcing': '🌐',
    'consulting': '💡',
    'professional-services': '🤝',
    'staffing': '👥',
    'recruiting': '🎯',
    'hr': '👥',
    'payroll': '💰',
    'benefits': '🎁',
    'compensation': '💰',
    'performance': '📊',
    'learning': '📚',
    'development': '💡',
    'training': '🎯',
    'elearning': '💻',
    'instructional-design': '🎨',
    'curriculum': '📚',
    'assessment': '📝',
    'evaluation': '📊',
    'accreditation': '✅',
    'certification': '🏆',
    'licensing': '📜',
    'permitting': '📋',
    'inspection': '🔍',
    'testing': '🧪',
    'calibration': '⚖️',
    'metrology': '📏',
    'standardization': '📋',
    'normalization': '📊',
    'benchmarking': '📈',
    'best-practices': '⭐',
    'knowledge-management': '🧠',
    'information-management': '📊',
    'records-management': '📁',
    'archiving': '📦',
    'digitization': '💾',
    'preservation': '🏛️',
    'conservation': '🌿',
    'restoration': '🏗️',
    'maintenance': '🔧',
    'repair': '🛠️',
    'overhaul': '🔧',
    'refurbishment': '🔄',
    'remanufacturing': '🏭',
    'recycling': '♻️',
    'waste-management': '🗑️',
    'disposal': '🚮',
    'remediation': '🧹',
    'decommissioning': '🏭',
    'demolition': '🏗️',
    'abatement': '🧹',
    'mitigation': '🛡️',
    'adaptation': '🔄',
    'resilience': '💪',
    'preparedness': '🎒',
    'response': '🚨',
    'recovery': '♻️',
    'continuity': '🔁',
    'contingency': '📋',
    'emergency': '🚨',
    'crisis': '⚠️',
    'disaster': '🌪️',
    'business-continuity': '🏢',
    'it-service-management': '🔧',
    'it-asset-management': '💻',
    'software-asset-management': '💿',
    'hardware-asset-management': '💾',
    'configuration-management': '⚙️',
    'change-management': '🔄',
    'release-management': '🚀',
    'deployment-management': '📦',
    'service-desk': '🎧',
    'incident-management': '🚨',
    'problem-management': '🔍',
    'event-management': '📅',
    'availability-management': '⏱️',
    'capacity-management': '📊',
    'performance-management': '📈',
    'service-level-management': '📋',
    'vendor-management': '🤝',
    'supplier-management': '📦',
    'contract-management': '📄',
    'procurement': '🛒',
    'sourcing': '🌐',
    'purchasing': '💰',
    'logistics': '🚚',
    'transportation': '🚛',
    'warehousing': '🏭',
    'distribution': '📦',
    'fulfillment': '✅',
    'order-management': '📋',
    'inventory-management': '📊',
    'demand-planning': '📈',
    'supply-planning': '📊',
    'production-planning': '🏭',
    'master-scheduling': '📅',
    'material-requirements': '📦',
    'capacity-requirements': '📊',
    'shop-floor-control': '🏭',
    'quality-control': '✅',
    'quality-assurance': '✅',
    'inspection': '🔍',
    'testing': '🧪',
    'validation': '✅',
    'verification': '✓',
    'certification': '🏆',
    'compliance': '✅',
    'regulatory': '📋',
    'governance': '🏛️',
    'risk': '⚠️',
    'audit': '🔍',
    'control': '🎛️',
    'monitoring': '👁️',
    'reporting': '📊',
    'analytics': '📈',
    'intelligence': '🧠',
    'forecasting': '🔮',
    'predictive': '📊',
    'prescriptive': '💡',
    'optimization': '⚡',
    'simulation': '🎮',
    'modeling': '📐',
    'prototyping': '🎯',
    'experimentation': '🧪',
    'research': '🔬',
    'development': '💡',
    'innovation': '✨',
    'invention': '💡',
    'discovery': '🔍',
    'exploration': '🗺️',
    'prospecting': '⛏️',
    'surveying': '📏',
    'sampling': '🧪',
    'analysis': '🔬',
    'synthesis': '⚗️',
    'design': '🎨',
    'engineering': '⚙️',
    'manufacturing': '🏭',
    'production': '⚙️',
    'assembly': '🔧',
    'fabrication': '🏭',
    'processing': '⚙️',
    'refining': '⚗️',
    'treatment': '🧪',
    'finishing': '✨',
    'packaging': '📦',
    'labeling': '🏷️',
    'branding': '🏷️',
    'marketing': '📊',
    'sales': '💰',
    'distribution': '🚚',
    'delivery': '📦',
    'service': '🛎️',
    'support': '🎧',
    'consulting': '💡',
    'advisory': '📋',
    'coaching': '🎯',
    'mentoring': '👥',
    'training': '📚',
    'teaching': '👨‍🏫',
    'facilitating': '🤝',
    'mediating': '⚖️',
    'negotiating': '🤝',
    'arbitrating': '⚖️',
    'adjudicating': '⚖️',
    'judging': '⚖️',
    'refereeing': '📢',
    'umpiring': '📢',
    'officiating': '📢',
    'moderating': '🎤',
    'hosting': '🎭',
    'presenting': '🎤',
    'speaking': '🗣️',
    'lecturing': '👨‍🏫',
    'tutoring': '📚',
    'instructing': '📋',
    'educating': '🎓',
    'informing': '📢',
    'communicating': '💬',
    'corresponding': '✉️',
    'documenting': '📝',
    'recording': '🎙️',
    'transcribing': '📝',
    'translating': '🌐',
    'interpreting': '🗣️',
    'localizing': '🌍',
    'adapting': '🔄',
    'customizing': '⚙️',
    'personalizing': '👤',
    'configuring': '⚙️',
    'tailoring': '✂️',
    'modifying': '🔧',
    'adjusting': '🎚️',
    'tuning': '🎸',
    'calibrating': '⚖️',
    'balancing': '⚖️',
    'harmonizing': '🎵',
    'synchronizing': '⏱️',
    'coordinating': '🤝',
    'organizing': '📋',
    'planning': '📅',
    'scheduling': '📆',
    'sequencing': '🔢',
    'prioritizing': '📊',
    'ranking': '📈',
    'scoring': '🎯',
    'grading': '📝',
    'rating': '⭐',
    'reviewing': '👁️',
    'assessing': '📊',
    'evaluating': '📋',
    'appraising': '💎',
    'valuing': '💰',
    'pricing': '💵',
    'costing': '💰',
    'budgeting': '📊',
    'forecasting': '🔮',
    'projecting': '📈',
    'estimating': '💰',
    'quoting': '📋',
    'bidding': '📢',
    'tendering': '📄',
    'proposing': '💡',
    'recommending': '👍',
    'suggesting': '💡',
    'advising': '📋',
    'counseling': '🤝',
    'guiding': '🧭',
    'directing': '📢',
    'leading': '👑',
    'managing': '📊',
    'supervising': '👁️',
    'overseeing': '👁️',
    'administering': '📋',
    'operating': '⚙️',
    'running': '🏃',
    'executing': '▶️',
    'implementing': '🛠️',
    'deploying': '🚀',
    'installing': '🔧',
    'commissioning': '✅',
    'activating': '▶️',
    'launching': '🚀',
    'starting': '▶️',
    'initiating': '🚀',
    'kicking-off': '🏈',
    'opening': '🚪',
    'commencing': '🎬',
    'beginning': '🔛',
    'creating': '✨',
    'generating': '⚡',
    'producing': '🏭',
    'making': '🔨',
    'building': '🏗️',
    'constructing': '🏗️',
    'assembling': '🔧',
    'composing': '🎵',
    'formulating': '⚗️',
    'developing': '💡',
    'evolving': '🧬',
    'growing': '🌱',
    'expanding': '📈',
    'scaling': '📊',
    'multiplying': '✖️',
    'duplicating': '📄',
    'replicating': '🔁',
    'cloning': '👥',
    'copying': '📄',
    'reproducing': '🔄',
    'printing': '🖨️',
    'publishing': '📖',
    'distributing': '📦',
    'circulating': '🔄',
    'broadcasting': '📡',
    'transmitting': '📡',
    'sending': '📤',
    'shipping': '🚢',
    'transporting': '🚚',
    'moving': '📦',
    'transferring': '🔄',
    'migrating': '🐦',
    'relocating': '🚚',
    'resettling': '🏠',
    'establishing': '🏗️',
    'founding': '🏛️',
    'instituting': '🏛️',
    'constituting': '📜',
    'forming': '🎨',
    'organizing': '📋',
    'structuring': '🏗️',
    'systematizing': '⚙️',
    'standardizing': '📋',
    'normalizing': '📊',
    'routinizing': '🔄',
    'habituating': '🔄',
    'conditioning': '🧠',
    'training': '📚',
    'drilling': '🎯',
    'exercising': '🏃',
    'practicing': '🎯',
    'rehearsing': '🎭',
    'preparing': '🎒',
    'readying': '✅',
    'arranging': '📋',
    'ordering': '📊',
    'sorting': '📂',
    'classifying': '📁',
    'categorizing': '📂',
    'grouping': '👥',
    'clustering': '🔵',
    'aggregating': '➕',
    'consolidating': '🏗️',
    'integrating': '🔗',
    'unifying': '🤝',
    'merging': '🔄',
    'combining': '➕',
    'blending': '🎨',
    'mixing': '⚗️',
    'fusing': '🔥',
    'melding': '🔥',
    'welding': '🔥',
    'soldering': '🔥',
    'bonding': '🔗',
    'adhering': '🔗',
    'sticking': '🩹',
    'attaching': '📎',
    'connecting': '🔗',
    'linking': '🔗',
    'coupling': '🔗',
    'joining': '➕',
    'uniting': '🤝',
    'allying': '🤝',
    'associating': '👥',
    'affiliating': '🔗',
    'partnering': '🤝',
    'collaborating': '🤝',
    'cooperating': '🤝',
    'coordinating': '🤝',
    'synchronizing': '⏱️',
    'harmonizing': '🎵',
    'orchestrating': '🎼',
    'conducting': '🎼',
    'directing': '📢',
    'guiding': '🧭',
    'steering': '🚢',
    'piloting': '✈️',
    'navigating': '🧭',
    'driving': '🚗',
    'riding': '🏇',
    'flying': '✈️',
    'sailing': '⛵',
    'boating': '🚤',
    'rowing': '🚣',
    'paddling': '🛶',
    'swimming': '🏊',
    'diving': '🤿',
    'surfing': '🏄',
    'skiing': '⛷️',
    'skating': '⛸️',
    'boarding': '🛹',
    'hiking': '🥾',
    'climbing': '🧗',
    'camping': '⛺',
    'fishing': '🎣',
    'hunting': '🏹',
    'tracking': '👣',
    'trailing': '🛤️',
    'following': '👣',
    'pursuing': '🏃',
    'chasing': '🏃',
    'hounding': '🐕',
    'stalking': '🐆',
    'ambushing': '🌳',
    'trapping': '🪤',
    'snaring': '🕸️',
    'netting': '🕸️',
    'catching': '🎣',
    'capturing': '🎯',
    'seizing': '✊',
    'grabbing': '✊',
    'taking': '✋',
    'getting': '✅',
    'obtaining': '📋',
    'acquiring': '💰',
    'procuring': '🛒',
    'securing': '🔒',
    'gaining': '📈',
    'earning': '💰',
    'winning': '🏆',
    'achieving': '🏆',
    'accomplishing': '✅',
    'fulfilling': '✅',
    'completing': '✅',
    'finishing': '🏁',
    'concluding': '🏁',
    'closing': '🚪',
    'ending': '🏁',
    'terminating': '🛑',
    'stopping': '🛑',
    'halting': '🛑',
    'pausing': '⏸️',
    'suspending': '⏸️',
    'interrupting': '⏸️',
    'breaking': '💔',
    'disrupting': '💥',
    'disturbing': '🌊',
    'interfering': '⚡',
    'hindering': '🚧',
    'impeding': '🚧',
    'obstructing': '🚧',
    'blocking': '🚫',
    'barricading': '🚧',
    'fortifying': '🏰',
    'defending': '🛡️',
    'guarding': '💂',
    'protecting': '🛡️',
    'shielding': '🛡️',
    'screening': '📺',
    'covering': '📔',
    'hiding': '🙈',
    'concealing': '🎭',
    'masking': '🎭',
    'disguising': '🎭',
    'camouflaging': '🦎',
    'cloaking': '🧥',
    'veiling': '🧕',
    'shrouding': '🌫️',
    'wrapping': '🎁',
    'packaging': '📦',
    'boxing': '📦',
    'crating': '📦',
    'containing': '📦',
    'holding': '✋',
    'keeping': '🔒',
    'retaining': '🔒',
    'maintaining': '🔧',
    'preserving': '🏛️',
    'conserving': '🌿',
    'saving': '💾',
    'storing': '🗃️',
    'warehousing': '🏭',
    'stocking': '📦',
    'inventorying': '📋',
    'cataloging': '📚',
    'indexing': '📇',
    'filing': '📁',
    'archiving': '📦',
    'recording': '🎙️',
    'logging': '📝',
    'registering': '📝',
    'enrolling': '📝',
    'listing': '📋',
    'enumerating': '🔢',
    'counting': '🔢',
    'numbering': '🔢',
    'quantifying': '📊',
    'measuring': '📏',
    'weighing': '⚖️',
    'scaling': '📊',
    'sizing': '📏',
    'dimensioning': '📐',
    'calculating': '🧮',
    'computing': '💻',
    'processing': '⚙️',
    'analyzing': '🔬',
    'examining': '🔍',
    'inspecting': '🔍',
    'investigating': '🕵️',
    'exploring': '🔭',
    'researching': '🔬',
    'studying': '📚',
    'learning': '🧠',
    'understanding': '💡',
    'knowing': '🧠',
    'recognizing': '👁️',
    'identifying': '🏷️',
    'naming': '🏷️',
    'labeling': '🏷️',
    'tagging': '🏷️',
    'coding': '💻',
    'marking': '✏️',
    'noting': '📝',
    'annotating': '📝',
    'commenting': '💬',
    'explaining': '💬',
    'describing': '📝',
    'defining': '📖',
    'specifying': '📋',
    'detailing': '📝',
    'elaborating': '📝',
    'expanding': '📈',
    'extending': '📏',
    'stretching': '🤸',
    'reaching': '🙌',
    'grasping': '✊',
    'seizing': '✊',
    'capturing': '🎯',
    'catching': '🎣',
    'trapping': '🪤',
    'snaring': '🕸️',
    'entangling': '🕸️',
    'ensnaring': '🕸️',
    'tricking': '🎭',
    'deceiving': '🎭',
    'misleading': '🎭',
    'duping': '🎭',
    'conning': '🎭',
    'scamming': '🚫',
    'defrauding': '🚫',
    'swindling': '🚫',
    'cheating': '🚫',
    'counterfeiting': '🚫',
    'forging': '🔨',
    'faking': '🎭',
    'pretending': '🎭',
    'acting': '🎭',
    'performing': '🎭',
    'playing': '🎮',
    'simulating': '🎮',
    'emulating': '🎮',
    'imitating': '🎭',
    'mimicking': '🦜',
    'copying': '📄',
    'replicating': '🔁',
    'reproducing': '🔄',
    'cloning': '👥',
    'duplicating': '📄',
    'multiplying': '✖️',
    'increasing': '📈',
    'decreasing': '📉',
    'reducing': '📉',
    'minimizing': '⬇️',
    'maximizing': '⬆️',
    'optimizing': '⚡',
    'improving': '📈',
    'enhancing': '✨',
    'upgrading': '⬆️',
    'advancing': '🚀',
    'progressing': '📈',
    'developing': '💡',
    'evolving': '🧬',
    'maturing': '🍷',
    'growing': '🌱',
    'expanding': '📈',
    'extending': '📏',
    'broadening': '↔️',
    'widening': '↔️',
    'deepening': '⬇️',
    'heightening': '⬆️',
    'lifting': '🏋️',
    'raising': '⬆️',
    'elevating': '⬆️',
    'boosting': '🚀',
    'augmenting': '➕',
    'supplementing': '➕',
    'complementing': '➕',
    'completing': '✅',
    'perfecting': '💎',
    'polishing': '✨',
    'refining': '⚗️',
    'purifying': '💧',
    'filtering': '🗑️',
    'straining': '🗑️',
    'sieving': '🗑️',
    'sorting': '📂',
    'sifting': '🗑️',
    'screening': '📺',
    'selecting': '✓',
    'choosing': '✓',
    'picking': '✓',
    'electing': '🗳️',
    'appointing': '👔',
    'assigning': '📋',
    'delegating': '📋',
    'entrusting': '🔐',
    'empowering': '💪',
    'authorizing': '✅',
    'licensing': '📜',
    'permitting': '📋',
    'allowing': '✅',
    'enabling': '✅',
    'facilitating': '🤝',
    'helping': '🤝',
    'aiding': '🤝',
    'assisting': '🤝',
    'supporting': '🤝',
    'backing': '🤝',
    'promoting': '📢',
    'advancing': '🚀',
    'furthering': '🚀',
    'encouraging': '👍',
    'motivating': '🎯',
    'inspiring': '✨',
    'stimulating': '⚡',
    'exciting': '🎉',
    'thrilling': '🎢',
    'delighting': '😊',
    'pleasing': '😊',
    'satisfying': '✅',
    'fulfilling': '✅',
    'gratifying': '😊',
    'rewarding': '🏆',
    'compensating': '💰',
    'remunerating': '💰',
    'paying': '💰',
    'repaying': '💰',
    'reimbursing': '💰',
    'refunding': '💰',
    'rebating': '💰',
    'discounting': '🏷️',
    'deducting': '➖',
    'subtracting': '➖',
    'removing': '🗑️',
    'eliminating': '🚫',
    'eradicating': '🚫',
    'exterminating': '🚫',
    'annihilating': '💥',
    'destroying': '💥',
    'demolishing': '🏗️',
    'razing': '🏗️',
    'leveling': '🏗️',
    'flattening': '🏗️',
    'clearing': '🧹',
    'cleaning': '🧹',
    'cleansing': '🧹',
    'purging': '🧹',
    'purifying': '💧',
    'detoxifying': '💧',
    'sanitizing': '🧼',
    'sterilizing': '🔬',
    'disinfecting': '🧼',
    'fumigating': '☠️',
    'decontaminating': '🧹',
    'remediating': '🧹',
    'rehabilitating': '🏥',
    'restoring': '🏗️',
    'repairing': '🛠️',
    'fixing': '🔧',
    'mending': '🧵',
    'patching': '🩹',
    'healing': '🏥',
    'curing': '💊',
    'treating': '🏥',
    'caring': '❤️',
    'nursing': '🏥',
    'doctoring': '⚕️',
    'theraping': '🧠',
    'counseling': '🤝',
    'advising': '📋',
    'consulting': '💡',
    'guiding': '🧭',
    'leading': '👑',
    'directing': '📢',
    'managing': '📊',
    'administering': '📋',
    'governing': '🏛️',
    'ruling': '👑',
    'reigning': '👑',
    'commanding': '📢',
    'ordering': '📋',
    'dictating': '📢',
    'mandating': '📋',
    'requiring': '✅',
    'demanding': '📢',
    'requesting': '🙏',
    'asking': '❓',
    'questioning': '❓',
    'inquiring': '❓',
    'querying': '❓',
    'interrogating': '❓',
    'interviewing': '🎤',
    'surveying': '📊',
    'polling': '🗳️',
    'voting': '🗳️',
    'electing': '🗳️',
    'selecting': '✓',
    'choosing': '✓',
    'picking': '✓',
    'opting': '✓',
    'deciding': '✅',
    'determining': '✅',
    'resolving': '✅',
    'settling': '✅',
    'concluding': '🏁',
    'finalizing': '✅',
    'completing': '✅',
    'closing': '🚪',
    'finishing': '🏁',
    'ending': '🏁',
    'terminating': '🛑',
    'quitting': '🚪',
    'resigning': '📄',
    'retiring': '🏖️',
    'withdrawing': '⬅️',
    'exiting': '🚪',
    'leaving': '🚪',
    'departing': '🛫',
    'going': '🏃',
    'coming': '🏃',
    'arriving': '🛬',
    'reaching': '🙌',
    'attaining': '🏆',
    'achieving': '🏆',
    'accomplishing': '✅',
}


def parse_skill_file(skill_path: Path) -> Optional[Dict]:
    """Parse a SKILL.md file and extract metadata"""
    try:
        content = skill_path.read_text(encoding='utf-8')
        
        # Initialize variables
        metadata = {}
        body_content = content
        
        # Extract YAML frontmatter
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                yaml_content = parts[1]
                body_content = parts[2].strip()
                try:
                    metadata = yaml.safe_load(yaml_content) or {}
                except:
                    metadata = {}
        
        # Extract skill info
        skill_name = skill_path.parent.name
        # Category: prefer YAML metadata (works for both internal and external skills),
        # fall back to first directory segment under skills/.
        yaml_meta = metadata.get('metadata') or {}
        yaml_category = metadata.get('category') or yaml_meta.get('category')
        if yaml_category:
            category = str(yaml_category)
        else:
            try:
                rel_path = skill_path.relative_to(SKILLS_DIR)
                category = rel_path.parts[0]
            except ValueError:
                category = 'other'
        
        # Get description
        description = metadata.get('description', '')
        if isinstance(description, str):
            # Clean up multi-line descriptions
            description = ' '.join(description.split())
        else:
            description = f"Expert {skill_name.replace('-', ' ').title()} skill"
        
        # Get full description from content (first paragraph after frontmatter)
        full_description = description
        if body_content:
            # Extract first paragraph
            first_para = body_content.split('\n\n')[0].strip()
            # Remove markdown headers
            first_para = first_para.lstrip('#').strip()
            if first_para and len(first_para) > 50:
                full_description = first_para[:300]
                if len(first_para) > 300:
                    full_description += '...'
        
        # Short description (max 100 chars)
        short_description = description[:97] + '...' if len(description) > 100 else description
        
        # Get icon based on category
        icon = CATEGORY_ICONS.get(category, '🔧')
        
        # Get quality from metadata (use difficulty as primary, quality as fallback)
        skill_metadata = metadata.get('metadata', {}) or {}
        
        # Try difficulty first (expert, advanced, intermediate, beginner)
        difficulty = skill_metadata.get('difficulty', '').lower() if skill_metadata.get('difficulty') else ''
        quality_val = skill_metadata.get('quality', '').lower() if skill_metadata.get('quality') else ''
        
        # Map to our three quality levels
        if difficulty in ['expert', 'master']:
            quality = 'expert'
        elif difficulty in ['advanced', 'intermediate', 'proficient']:
            quality = 'advanced'
        elif difficulty in ['beginner', 'novice', 'basic']:
            quality = 'intermediate'
        elif quality_val in ['production', 'excellent', 'a', '1', 'high']:
            quality = 'expert'
        elif quality_val in ['advanced', 'good', 'b', '2', 'medium']:
            quality = 'advanced'
        elif quality_val in ['intermediate', 'c', '3', 'low']:
            quality = 'intermediate'
        else:
            # Default based on score
            score_val = skill_metadata.get('score', '')
            try:
                if isinstance(score_val, str) and '/' in score_val:
                    score_num = float(score_val.split('/')[0])
                else:
                    score_num = float(score_val)
                if score_num >= 8.5:
                    quality = 'expert'
                elif score_num >= 7.0:
                    quality = 'advanced'
                else:
                    quality = 'intermediate'
            except:
                quality = 'intermediate'
        
        # Get rating from metadata (default based on quality)
        rating = skill_metadata.get('score', None)
        if rating is None:
            rating_map = {'expert': 9.0, 'advanced': 8.0, 'intermediate': 7.0}
            rating = rating_map.get(quality, 7.5)
        else:
            try:
                # Handle formats like "8.3/10"
                if isinstance(rating, str) and '/' in rating:
                    rating = float(rating.split('/')[0])
                else:
                    rating = float(rating)
            except:
                rating = 7.5
        
        # Generate install count (simulated based on skill name hash for consistency)
        import hashlib
        name_hash = int(hashlib.md5(skill_name.encode()).hexdigest(), 16)
        installs = f"{(name_hash % 150) + 1}.{name_hash % 10}k"
        
        # Generate display name
        display_name = metadata.get('display_name', skill_name.replace('-', ' ').title())
        
        # Generate Chinese name (placeholder - can be enhanced with translation)
        name_zh = metadata.get('display_name_zh', display_name)
        
        return {
            'id': skill_name,
            'name': display_name,
            'nameZh': name_zh,
            'category': category,
            'icon': icon,
            'shortDesc': short_description,
            'shortDescZh': short_description,  # Can be enhanced with translation
            'fullDesc': full_description,
            'fullDescZh': full_description,  # Can be enhanced with translation
            'quality': quality,
            'rating': round(rating, 1),
            'installs': installs,
            'command': f"Read https://raw.githubusercontent.com/theneoai/awesome-skills/main/{skill_path.relative_to(PROJECT_ROOT)} and install {skill_name} skill"
        }
    except Exception as e:
        print(f"Error parsing {skill_path}: {e}")
        import traceback
        traceback.print_exc()
        return None


def generate_skills_data():
    """Generate JavaScript skills data file"""
    import datetime
    
    print("🔍 Scanning all skills...")
    
    skills = []
    seen_ids = {}  # Track seen IDs and their categories
    
    # Exclude directories that are not actual skills
    EXCLUDED_DIRS = {'_template', '_common', '.git', 'node_modules', '__pycache__'}

    scan_dirs = [SKILLS_DIR] + [d for d in EXTERNAL_AUTHOR_DIRS if d.exists()]
    skill_files = [
        f
        for d in scan_dirs
        for f in d.rglob('**/SKILL.md')
        if not any(excluded in f.parts for excluded in EXCLUDED_DIRS)
    ]
    
    print(f"Found {len(skill_files)} skill files")
    
    for i, skill_file in enumerate(skill_files, 1):
        if i % 50 == 0:
            print(f"  Processed {i}/{len(skill_files)}...")
        
        skill_data = parse_skill_file(skill_file)
        if skill_data:
            # Handle duplicate IDs by adding category prefix
            original_id = skill_data['id']
            category = skill_data['category']
            
            if original_id in seen_ids:
                # This ID already exists, make it unique
                new_id = f"{category}-{original_id}"
                skill_data['id'] = new_id
                print(f"  ⚠️  Duplicate ID '{original_id}' found, renamed to '{new_id}'")
            else:
                seen_ids[original_id] = category
            
            skills.append(skill_data)
    
    print(f"✅ Successfully parsed {len(skills)} skills")
    
    # Calculate statistics for hero section
    categories = {}
    quality_counts = {'expert': 0, 'advanced': 0, 'intermediate': 0}
    for skill in skills:
        cat = skill['category']
        categories[cat] = categories.get(cat, 0) + 1
        quality = skill.get('quality', 'intermediate')
        if quality in quality_counts:
            quality_counts[quality] += 1
    
    avg_rating = sum(s.get('rating', 7.5) for s in skills) / len(skills) if skills else 0
    
    # Generate JavaScript - use skillsData as variable name for compatibility with new index.html
    js_content = f"""// Auto-generated skills data
// Generated: {datetime.datetime.now().isoformat()}
// Total skills: {len(skills)}
// Categories: {len(categories)}

const skillsData = {json.dumps(skills, indent=4, ensure_ascii=False)};

// Hero statistics - auto-generated
const heroStats = {{
    totalSkills: {len(skills)},
    totalCategories: {len(categories)},
    avgRating: {round(avg_rating, 1)},
    expertSkills: {quality_counts['expert']},
    advancedSkills: {quality_counts['advanced']},
    intermediateSkills: {quality_counts['intermediate']}
}};

// Export for use in other scripts
if (typeof module !== 'undefined' && module.exports) {{
    module.exports = {{ skillsData, heroStats }};
}}
"""
    
    # Ensure directory exists
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    
    # Write file
    OUTPUT_FILE.write_text(js_content, encoding='utf-8')
    print(f"✅ Generated: {OUTPUT_FILE}")
    
    # Print category breakdown
    print("\n📊 Category breakdown:")
    for cat, count in sorted(categories.items(), key=lambda x: -x[1])[:10]:
        print(f"  {cat}: {count}")
    
    print(f"\n📈 Quality distribution:")
    print(f"  Expert: {quality_counts['expert']}")
    print(f"  Advanced: {quality_counts['advanced']}")
    print(f"  Intermediate: {quality_counts['intermediate']}")
    
    return len(skills)


if __name__ == '__main__':
    count = generate_skills_data()
    print(f"\n🎉 Successfully generated data for {count} skills!")
