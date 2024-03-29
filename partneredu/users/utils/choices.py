ORGANIZATION_TYPES = {
    "Corporation",
    "Nonprofit organization",
    "Government agency",
    "Educational institution",
    "Hospital",
    "Retail store",
    "Manufacturing company",
    "Financial institution",
    "Technology company",
    "Consulting firm",
    "Law firm",
    "Research institute",
    "Media company",
    "Advertising agency",
    "Real estate agency",
    "Restaurant",
    "Hotel",
    "Transportation company",
    "Construction company",
    "Pharmaceutical company",
    "Insurance company",
    "Energy company",
    "Telecommunications company",
    "Startup",
    "Charity",
    "Foundation",
    "University",
    "College",
    "School",
    "Hospitality company",
    "Healthcare provider",
    "Software company",
    "Bank",
    "Credit union",
    "Brokerage firm",
    "Investment firm",
    "Venture capital firm",
    "Fitness center",
    "Sports team",
    "Museum",
    "Library",
    "Art gallery",
    "Music venue",
    "Theater",
    "Tourism board",
    "Chamber of commerce",
    "Trade association",
    "Professional association",
    "Social club",
    "Environmental organization",
    "Animal shelter",
    "Legal aid organization",
    "Community center",
    "Food bank",
    "Religious institution",
    "Youth organization",
    "Senior center",
    "Arts organization",
    "Cultural center",
    "Trade union",
    "Labor union",
    "Professional society",
    "Franchise",
    "Social service agency",
    "Political party",
    "Government contractor",
    "Military organization",
    "Volunteer organization",
    "Cooperative",
    # Additional types of organizations
    "Internet company",
    "Software development firm",
    "E-commerce platform",
    "Retail chain",
    "Fashion brand",
    "Automobile manufacturer",
    "Aerospace company",
    "Shipping company",
    "Logistics company",
    "Food delivery service",
    "Beverage company",
    "Consumer goods company",
    "Pharmaceutical laboratory",
    "Healthcare system",
    "Dental clinic",
    "Legal consultancy",
    "Human resources agency",
    "Talent agency",
    "Marketing agency",
    "Public relations firm",
    "Event management company",
    "Travel agency",
    "Tour operator",
    "Amusement park",
    "Gaming company",
    "Film studio",
    "Television network",
    "Web hosting company",
    "Domain registrar",
    "Social media platform",
    "Streaming service",
    "Video game developer",
    "Animation studio",
    "Software as a Service (SaaS) provider",
    "Cloud computing company",
    "Cybersecurity firm",
    "Artificial intelligence company",
    "Biotechnology company",
    "Medical device manufacturer",
    "Fitness equipment manufacturer",
    "Professional sports league",
    "Athletic apparel brand",
    "Fine arts school",
    "Performing arts school",
    "Language school",
    "Test prep company",
    "Career counseling center",
    "Tutoring service",
    "Online learning platform",
    "Public policy institute",
    "Think tank",
    "Laboratory",
    "Medical clinic",
    "Healthcare consultancy",
    "Financial advisory firm",
    "Wealth management firm",
    "Hedge fund",
    "Private equity firm",
}

# data scrapped from TDSB's 2021-2022 course choices
# https://www.tdsb.on.ca/Portals/0/docs/Choices%202021-22.pdf
COURSE_OPTIONS = [
    ("Exploring & Creating the Arts", "AEA3O1"),
    ("Integrated Arts", "ALC1O1"),
    ("Dramatic Arts", "ADA1O"),
    ("Drama", "ADA4E"),
    ("Dramatic Arts - Music Theatre", "ADB1O"),
    ("Drama in the Community", "ADC1O"),
    ("Dramatic Arts - Production", "ADD1O"),
    ("Dramatic Arts - Film/Video", "ADV1O"),
    ("Director’s Craft", "ADF3M"),
    ("Dramatic Arts - Acting/Improvisation", "ADG3M"),
    ("Dramatic Arts - Playwriting/Theatre Development", "ADP3M"),
    ("Canadian Theatre", "ADT3M"),
    ("Music", "AMU1O"),
    ("Music - Vocal/Choral", "AMV1O"),
    ("Media Arts", "ASM2O"),
    ("Dance", "ATC1O"),
    ("Dances", "ATX3M"),
    ("Dance - Ballet", "ATB1O"),
    ("Dance - Composition", "ATD1O"),
    ("Dance - African", "ATF1O"),
    ("Dance - Jazz", "ATJ1O"),
    ("Dance - Caribbean", "ATK1O"),
    ("Dance - Modern", "ATM1O"),
    ("Dance - Performance Practice", "ATP1O"),
    ("Dance – Northern European/Asian", "ATE1O"),
    ("Dance – English/Irish/Scottish", "ATG1O"),
    ("Dance – History Development", "ATH1O"),
    ("Dance – Indian/South Central Asian", "ATI1O"),
    ("Dance – Central & South American", "ATL1O"),
    ("Dance – Aboriginal Peoples (N.A.)", "ATN1O"),
    ("Dance – Pacific Rim", "ATO1O"),
    ("Dance –Hip Hop", "ATR1O"),
    ("Dance – Social", "ATS1O"),
    ("Dance – Tap", "ATT1O"),
    ("Dance –Music/Theatre", "ATU1O"),
    ("Dance – Med/Mid East", "ATW1O"),
    ("Dance – French", "ATX1O"),
    ("Dance – World Cultures", "ATZ1O"),
    ("Visual Arts", "AVI1O"),
    ("Visual Arts - Crafts", "AWA1O"),
    ("Visual Arts - Ceramics", "AWC1O"),
    ("Visual Arts - Visual Design", "AWD1O"),
    ("Visual Arts - Information/Consumer Design", "AWE1O"),
    ("Visual Arts - Industrial Design", "AWF1O"),
    ("Visual Arts - Environmental Design", "AWG1O"),
    ("Visual Arts - Interior Design", "AWH1O"),
    ("Visual Arts - Fashion & Textile Design", "AWI1O"),
    ("Visual Arts - Stage Design", "AWJ1O"),
    ("Visual Arts - Illustration", "AWK1O"),
    ("Visual Arts - Drawing", "AWL1O"),
    ("Visual Arts - Drawing and Painting", "AWM1O"),
    ("Visual Arts - Painting", "AWN1O"),
    ("Visual Arts - Printmaking", "AWO1O"),
    ("Visual Arts - Sculpture", "AWP1O"),
    ("Visual Arts - Photography", "AWQ1O"),
    ("Visual Arts - Film/Video", "AWR1O"),
    ("Visual Arts - Digital Media", "AWS1O"),
    ("Visual Arts - Non-Traditional", "AWT1O"),
    ("Visual Arts - Cultural/Historical Studies", "AWU1O"),
    ("Financial Accounting Fundamentals", "BAF3M"),
    ("Accounting Essentials", "BAI3E"),
    ("Accounting for a Small Business", "BAN4E"),
    ("Financial Accounting Princ", "BAT4M"),
    ("International Business Essentials", "BBB4E"),
    ("International Business Fundamentals", "BBB4M"),
    ("Introduction to Business", "BBI1O"),
    ("Entrepreneurship: The Venture", "BDI3C"),
    ("Entrepreneurship: The Enterprising Person", "BDP3O"),
    ("Entrepreneurship: Venture Planning in an Electronic Age", "BDV4C"),
    ("Marketing: Goods, Services, Events", "BMI3C"),
    ("Marketing: Retail and Service", "BMX3E"),
    ("Business Leadership: Becoming a Manager", "BOG4E"),
    ("Business Leadership: Management Fundamentals", "BOH4M"),
    ("Information and Communication Technology: The Digital Environment", "BTA3O"),
    ("Information and Communication Technology in Business", "BTT1O"),
    ("Information and Communication Technology: Multimedia Solutions", "BTX4C"),
    ("Information and Communication Technology in the Workplace", "BTX4E"),
    ("Issues in Canadian Geography", "CGC1D"),
    ("Regional Geography", "CGD3M"),
    ("Forces of Nature: Physical Processes and Disasters", "CGF3M"),
    ("Travel and Tourism: A Geographic Perspective", "CGG3O"),
    ("Spatial Technologies in Action", "CGO4M"),
    ("Living in a Sustainable World", "CGR4E"),
    ("The Environment and Resource Management", "CGR4M"),
    ("Introduction to Spatial Technologies", "CGT3O"),
    ("World Geography: Urban Patterns and Population Issues", "CGU4M"),
    ("World Issues: A Geographic Analysis", "CGW4C"),
    ("American History", "CHA3U"),
    ("Canadian History since World War I", "CHC2D"),
    ("Origins and Citizenship: The History of a Canadian Ethnic Group", "CHE3O"),
    ("Genocide and Crimes Against Humanity", "CHG3B"),
    ("Canada: History, Identity, and Culture", "CHI4U"),
    ("Adventures in World History", "CHM4E"),
    ("World History since 1900: Global and Regional Interactions", "CHT3O"),
    ("Civics and Citizenship", "CHV2O"),
    ("World History to the End of the Fifteenth Century", "CHW3M"),
    ("World History since the Fifteenth Century", "CHY4C"),
    ("Analysing Current Economic Issues", "CIA4U"),
    ("Making Personal Economic Choices", "CIC4E"),
    ("The Individual and the Economy", "CIE3M"),
    ("Legal Studies", "CLN4C"),
    ("Canadian and International Law", "CLN4U"),
    ("Understanding Everyday Law in Canada", "CLU3E"),
    ("Understanding Canadian Law", "CLU3M"),
    ("Politics in Action: Making Change", "CPC3O"),
    ("Canadian and International Politics", "CPW4U"),
    ("Ancient Greek", "LVGBD"),
    ("Latin", "LVLBD"),
    ("Classical Civilization", "LVV4U"),
    ("Albanian", "LBABD"),
    ("Amharic", "LDCBD"),
    ("Arabic", "LYABD"),
    ("Armenian", "LYRBD"),
    ("Ashanti", "LDABD"),
    ("Career Studies", "GLC2O"),
    ("Discovering the Workplace", "GLD2O"),
    ("Learning Strategies", "GLE1O"),
    ("Advanced Learning Strategies", "GLE3O"),
    ("Navigating the Workplace", "GLN4O"),
    ("Learning Strategies I - Skills for Success in Secondary School", "GLS1O"),
    ("Advanced Learning Strategies: Skills for Success After Secondary School", "GLS4O"),
    ("Leadership and Peer Support", "GPP3O"),
    ("Designing Your Future", "GWL3O"),
    ("Healthy Living and Outdoor Activities", "PAD1O"),
    ("Healthy Living and Personal and Fitness Activities", "PAF1O"),
    ("Healthy Living and Individual and Small Group Activities", "PAI1O"),
    ("Healthy Living and Large Group Activities", "PAL1O"),
    ("Healthy Living and Aquatics Activities", "PAQ1O"),
    ("Healthy Living and Rhythm and Movement Activities", "PAR1O"),
    ("Recreation and Healthy and Active Living Leadership", "PLF4M"),
    ("Healthy Active Living Education", "PPL1O"),
    ("Health for Life", "PPZ3C"),
    ("Interdisciplinary Studies", "IDC3O"),
    ("Foundations for College Mathematics", "MAP4C"),
    ("Foundations for College Mathematics", "MBF3C"),
    ("Functions and Applications", "MCF3M"),
    ("Functions", "MCR3U"),
    ("Mathematics for College Technology", "MCT4C"),
    ("Calculus and Vectors", "MCV4U"),
    ("Mathematics of Data Management", "MDM4U"),
    ("Clothing", "HNL2O"),
    ("Raising Healthy Children", "HPC3O"),
    ("Working with School-Age Children and Adolescents", "HPD4C"),
    ("Working with Infants and young Children", "HPW3C"),
    ("World Religions and Belief Traditions in Daily Life", "HRF3O"),
    ("World Religions and Belief Traditions: Perspectives, Issues, and Challenges", "HRT3M"),
    ("Challenge and Change in Society", "HSB4U"),
    ("World Cultures", "HSC4M"),
    ("Equity, Diversity, and Social Justice", "HSE3E"),
    ("Gender Studies", "HSG3M"),
    ("Introduction to Anthropology, Psychology, and Sociology", "HSP3C"),
    ("Philosophy: The Big Questions", "HZB3M"),
    ("Philosophy: Questions and Theories", "HZT4U"),
    ("Exploring Technologies", "TIJ1O"),
    ("Exploring Communications Technology", "TGJ1O"),
    ("Communications Technology", "TGJ2O"),
    ("Print and Graphic Communications", "TGG3M"),
    ("Interactive New Media and Animation", "TGI3M"),
    ("Photography and Digital Imaging", "TGP3M"),
    ("Radio, Audio and Sound Production", "TGR3M"),
    ("TV, Video and Movie Production", "TGV3M"),
    ("Agriculture", "THG3E"),
    ("Horticulture", "THH3E"),
    ("Landscape Construction & Maintenance", "THL3E"),
    ("Forestry", "THO3E"),
    ("Horticulture Management & Science", "THS3M"),
    ("Exploring Hairstyling and Aesthetics", "TXJ1O"),
    ("Hairstyling and Aesthetics", "TXJ2O"),
    ("Aesthetics", "TXA3E"),
    ("Hairstyling", "TXH3E"),
    ("Child Development and Gerontology", "TOJ4C"),
    ("Exploring Health Care", "TPJ1O"),
    ("Health Care", "TPJ2O"),
    ("Dental Services", "TPD3M"),
    ("Laboratory Services", "TPL3M"),
    ("Nursing/Medical Services", "TPM3M"),
    ("Pharmacy Services", "TPP3M"),
    ("Therapy Services", "TPT3M"),
    ("Exploring Hospitality and Tourism", "TFJ1O"),
    ("Hospitality and Tourism", "TFJ2O"),
    ("Hospitality and Tourism", "TFJ3C"),
    ("Exploring Transportation Technology", "TTJ1O"),
    ("Transportation Technology", "TTJ2O"),
    ("Transportation Technology: Motive Power", "TTJ3C"),
    ("Transportation Technology: Vehicle Ownership", "TTJ3O"),
    ("Transportation Technology: Power Management", "TTJ4C"),
    ("Transportation Technology: Vehicle Maintenance", "TTJ4E"),
    ("Auto Service", "TTA3C"),
    ("Auto Body", "TTB3C"),
    ("Heavy Duty & Agricultural Equipment", "TTH3C"),
    ("Light Aircraft", "TTL3C"),
    ("Small Engine & Recreational", "TTS3C"),
    ("Truck and Coach", "TTT3C"),
]
COURSE_OPTIONS = [(course[1], course[0]) for course in COURSE_OPTIONS]


POSITIONS = [
    ("Chief Executive Officer", "CEO"),
    ("Chief Operating Officer", "COO"),
    ("Chief Financial Officer", "CFO"),
    ("Chief Technology Officer", "CTO"),
    ("Chief Marketing Officer", "CMO"),
    ("Chief Human Resources Officer", "CHRO"),
    ("Chief Information Officer", "CIO"),
    ("Chief Security Officer", "CSO"),
    ("Chief Legal Officer", "CLO"),
    ("Chief Communications Officer", "CCO"),
    ("Vice President of Operations", "VP Operations"),
    ("Vice President of Finance", "VP Finance"),
    ("Vice President of Marketing", "VP Marketing"),
    ("Vice President of Sales", "VP Sales"),
    ("Vice President of Human Resources", "VP HR"),
    ("Vice President of Engineering", "VP Engineering"),
    ("Vice President of Product Management", "VP Product"),
    ("Director of Operations", "Director Operations"),
    ("Director of Finance", "Director Finance"),
    ("Director of Marketing", "Director Marketing"),
    ("Director of Sales", "Director Sales"),
    ("Director of Human Resources", "Director HR"),
    ("Director of Engineering", "Director Engineering"),
    ("Director of Product Management", "Director Product"),
    ("Finance Manager", "Finance Manager"),
    ("Marketing Manager", "Marketing Manager"),
    ("Sales Manager", "Sales Manager"),
    ("Human Resources Manager", "HR Manager"),
    ("Engineering Manager", "Engineering Manager"),
    ("Product Manager", "Product Manager"),
    ("Operations Manager", "Operations Manager"),
    ("Accountant", "Accountant"),
    ("Financial Analyst", "Financial Analyst"),
    ("Marketing Specialist", "Marketing Specialist"),
    ("Sales Representative", "Sales Representative"),
    ("Human Resources Specialist", "HR Specialist"),
    ("Software Engineer", "Software Engineer"),
    ("Systems Engineer", "Systems Engineer"),
    ("Network Engineer", "Network Engineer"),
    ("Frontend Developer", "Frontend Developer"),
    ("Backend Developer", "Backend Developer"),
    ("Full Stack Developer", "Full Stack Developer"),
    ("UX/UI Designer", "UX/UI Designer"),
    ("Product Designer", "Product Designer"),
    ("Project Manager", "Project Manager"),
    ("Business Analyst", "Business Analyst"),
    ("Data Analyst", "Data Analyst"),
    ("Operations Analyst", "Operations Analyst"),
    ("Quality Assurance Analyst", "QA Analyst"),
    ("Customer Success Manager", "Customer Success Manager"),
    ("Technical Support Specialist", "Technical Support Specialist"),
    ("Systems Administrator", "Systems Administrator"),
    ("Database Administrator", "Database Administrator"),
    ("Network Administrator", "Network Administrator"),
    ("Information Security Analyst", "Information Security Analyst"),
    ("Legal Counsel", "Legal Counsel"),
    ("Corporate Communications Manager", "Corporate Communications Manager"),
    ("Public Relations Specialist", "PR Specialist"),
    ("Content Writer", "Content Writer"),
    ("Social Media Manager", "Social Media Manager"),
    ("Recruiter", "Recruiter"),
    ("Talent Acquisition Specialist", "Talent Acquisition Specialist"),
    ("Training and Development Manager", "Training and Development Manager"),
    ("Compensation and Benefits Manager", "Compensation and Benefits Manager"),
    ("Facilities Manager", "Facilities Manager"),
    ("Logistics Coordinator", "Logistics Coordinator"),
    ("Procurement Specialist", "Procurement Specialist"),
    ("Supply Chain Manager", "Supply Chain Manager"),
    ("Warehouse Manager", "Warehouse Manager"),
    ("Customer Service Manager", "Customer Service Manager"),
    ("Call Center Supervisor", "Call Center Supervisor"),
    ("Operations Supervisor", "Operations Supervisor"),
    ("Inventory Control Specialist", "Inventory Control Specialist"),
    ("Safety Coordinator", "Safety Coordinator"),
    ("Compliance Officer", "Compliance Officer"),
    ("Environmental Health and Safety Manager", "EHS Manager"),
    ("Internal Auditor", "Internal Auditor"),
    ("Risk Manager", "Risk Manager"),
    ("Legal Assistant", "Legal Assistant"),
    ("Executive Assistant", "Executive Assistant"),
    ("Administrative Assistant", "Administrative Assistant"),
    ("Office Manager", "Office Manager"),
    ("Receptionist", "Receptionist"),
    ("Data Scientist", "Data Scientist"),
    ("Machine Learning Engineer", "ML Engineer"),
    ("Artificial Intelligence Specialist", "AI Specialist"),
    ("Cybersecurity Analyst", "Cybersecurity Analyst"),
    ("Penetration Tester", "Penetration Tester"),
    ("Security Operations Center (SOC) Analyst", "SOC Analyst"),
    ("Incident Responder", "Incident Responder"),
    ("Digital Forensic Analyst", "Digital Forensic Analyst"),
    ("Cloud Architect", "Cloud Architect"),
    ("DevOps Engineer", "DevOps Engineer"),
    ("Site Reliability Engineer", "SRE"),
    ("IT Manager", "IT Manager"),
    ("IT Administrator", "IT Administrator"),
    ("IT Support Specialist", "IT Support Specialist"),
    ("Help Desk Technician", "Help Desk Technician"),
    ("Desktop Support Engineer", "Desktop Support Engineer"),
    ("Network Technician", "Network Technician"),
    ("Telecommunications Specialist", "Telecom Specialist"),
    ("Database Developer", "Database Developer"),
    ("UI/UX Developer", "UI/UX Developer"),
    ("Game Developer", "Game Developer"),
    ("Mobile App Developer", "Mobile App Developer"),
    ("Web Developer", "Web Developer"),
    ("E-commerce Manager", "E-commerce Manager"),
    ("Digital Marketing Manager", "Digital Marketing Manager"),
    ("Content Marketing Specialist", "Content Marketing Specialist"),
    ("SEO Specialist", "SEO Specialist"),
    ("PPC Specialist", "PPC Specialist"),
    ("Email Marketing Specialist", "Email Marketing Specialist"),
    ("Brand Manager", "Brand Manager"),
    ("Event Coordinator", "Event Coordinator"),
    ("Public Relations Manager", "PR Manager"),
    ("Community Manager", "Community Manager"),
    ("Influencer Marketing Manager", "Influencer Marketing Manager"),
    ("Sales Operations Manager", "Sales Operations Manager"),
    ("Channel Sales Manager", "Channel Sales Manager"),
    ("Account Manager", "Account Manager"),
    ("Technical Account Manager", "Technical Account Manager"),
    ("Business Development Representative", "BDR"),
    ("Sales Engineer", "Sales Engineer"),
    ("Channel Partner Manager", "Channel Partner Manager"),
    ("Account Executive", "Account Executive"),
    ("Sales Trainer", "Sales Trainer"),
    ("Sales Operations Analyst", "Sales Operations Analyst"),
    ("Customer Success Specialist", "Customer Success Specialist"),
    ("Customer Experience Manager", "Customer Experience Manager"),
    ("Customer Support Specialist", "Customer Support Specialist"),
    ("User Experience Researcher", "UX Researcher"),
    ("Market Research Analyst", "Market Research Analyst"),
    ("Operations Research Analyst", "Operations Research Analyst"),
]

POSITIONS = [(position[1], position[0]) for position in POSITIONS]
