
from experta import *
import pandas as pd
class journal(Fact):
    name = Field(str,mandatory=True)
    research = Field(str,mandatory=True)
    keyword = Field(str,mandatory=True)
    conference_ranking = Field(str,mandatory=True)
    impact_factor = Field(float,mandatory=True)
research_list = ['Agricultural and Biological Sciences','Arts and Humanities','Biochemistry,genitics and molecular biology','Bussiness,Management and Accounting','Chemical engineering','Chemistry','Computer Science','Decision Sciences','Dentistry','Earth and Planetary sciences','Economics,econometrics and Finance','Energy','Engineering','Environmental Science','Health professions','Immunology and microbiology','Material Sciences','Mathematics','Medicine','Multidisciplinary','Neuroscience','Nursing','Pharmacology,Toxicology and Pharmaceutics','Physics and Astronomy','Psychology','Social Sciences','Veterinary']
for i in research_list:
    print(i + '\n')
research_area = input('Enter research area\n')
keyword_u = input("Enter Keyword\n")
research_area = research_area.lower().strip()
keyword_u = keyword_u.lower().strip()
conference_ranking = input("Enter preferred Conference ranking\n")

#df = pd.read_csv('know.csv')

xl = []
xl_r = []
xd = []
xd_r = []
class start(KnowledgeEngine):
#yield journal(name='',research='',keyword='',conference_ranking='',impact_factor=)
    @DefFacts(order=0)
    def declare_journal(self):
        yield journal(name='American Forests',research='agricultural and biological sciences',keyword='forests',conference_ranking='Q4',impact_factor=10.3)
        yield journal(name='Molecular Biology and Evolution',research='agricultural and biological sciences',keyword='molecular biology',conference_ranking='Q1',impact_factor=8.612)
        yield journal(name='Trends in Ecology and Evolution',research='agricultural and biological sciences',keyword='ecology',conference_ranking='Q1',impact_factor=6.86)
        yield journal(name='Nature Plants',research='agricultural and biological sciences',keyword='plants',conference_ranking='Q1',impact_factor=5.517)
        yield journal(name='Fisheries Oceanography',research='agricultural and biological sciences',keyword='fisheries',conference_ranking='Q2',impact_factor=11.23)
        yield journal(name='Journal of Insect Physiology',research='agricultural and biological sciences',keyword='Insects',conference_ranking='Q2',impact_factor=5.67)
        yield journal(name='Photosynthesis Research',research='agricultural and biological sciences',keyword='photosynthesis',conference_ranking='Q2',impact_factor=7.8)
        yield journal(name='Journal of Wildlife Management', research='agricultural and biological sciences', keyword='wildlife', conference_ranking='Q3', impact_factor=1.45)
        yield journal(name='Current Zoology',research='agricultural and biological sciences',keyword='zoology',conference_ranking='Q3',impact_factor=4.56)
        yield journal(name='Food and Function',research='agricultural and biological sciences',keyword='food',conference_ranking='Q4',impact_factor=6.7)
        yield journal(name='Psychological Bulletin', research='arts and humanities', keyword='Psychology', conference_ranking='Q1', impact_factor=5.6)
        yield journal(name='Journal of Communication',research='arts and humanities',keyword='communication',conference_ranking='Q1',impact_factor=6.7)
        yield journal(name='Applied Linguistics',research='arts and humanities',keyword='linguistics',conference_ranking='Q2',impact_factor=8.90)
        yield journal(name='Gender and Society',research='arts and humanities',keyword='gender',conference_ranking='Q2',impact_factor=5.6)
        yield journal(name='Ethics',research='arts and humanities',keyword='ethics',conference_ranking='Q2',impact_factor=3.2)
        yield journal(name='Evolution and Human Behavior',research='arts and humanities',keyword='evolution',conference_ranking='Q3',impact_factor=2.31)
        yield journal(name='Cultural Anthropology',research='arts and humanities',keyword='anthropology',conference_ranking='Q3',impact_factor=9.876)
        yield journal(name='Journal of Literacy Research',research='arts and humanities',keyword='literacy',conference_ranking='Q3',impact_factor=0.456)
        yield journal(name='The Journal of Philosophy',research='arts and humanities',keyword='philosophy',conference_ranking='Q4',impact_factor=1.67)
        yield journal(name='Intelligence',research='arts and humanities',keyword='intelligence',conference_ranking='Q4',impact_factor=9.1)
        yield journal(name='Nature Reviews Cancer',research='biochemistry,genetics and molecular biology',keyword='cancer',conference_ranking='Q1',impact_factor=8.45)
        yield journal(name='Nature Biotechnology',research='biochemistry,genetics and molecular biology',keyword='biotechnology',conference_ranking='Q1',impact_factor=1.234)
        yield journal(name='Cell Metabolism',research='biochemistry,genetics and molecular biology',keyword='cell metabolism',conference_ranking='Q1',impact_factor=7.54)
        yield journal(name='Genome Biology',research='biochemistry,genetics and molecular biology',keyword='genome',conference_ranking='Q2',impact_factor=1.45)
        yield journal(name='Cell Stem Cell',research='biochemistry,genetics and molecular biology',keyword='stem cell',conference_ranking='Q2',impact_factor=4.56)
        yield journal(name='Nucleic Acids Research',research='biochemistry,genetics and molecular biology',keyword='nucleic acids',conference_ranking='Q2',impact_factor=7.65)
        yield journal(name='Cell Systems',research='biochemistry,genetics and molecular biology',keyword='cell',conference_ranking='Q3',impact_factor=3.45)
        yield journal(name='Annals of the Rheumatic Diseases',research='biochemistry,genetics and molecular biology',keyword='rheumatic diseases',conference_ranking='Q3',impact_factor=5.67)
        yield journal(name='Chem',research='biochemistry,genetics and molecular biology',keyword='chem',conference_ranking='Q4',impact_factor=3.21)
        yield journal(name='Nature Reviews Endocrinology',research='biochemistry,genetics and molecular biology',keyword='Endocrinology',conference_ranking = 'Q4',impact_factor=3.412)
        yield journal(name='Journal of Finance',research='business,management and accounting',keyword='finance',conference_ranking='Q1',impact_factor=2.34)
        yield journal(name='Journal of Labor Economics',research='business,management and accounting',keyword='labor economics',conference_ranking='Q1',impact_factor=6.789)
        yield journal(name='Journal of Marketing',research='business,management and accounting',keyword='marketing',conference_ranking='Q1',impact_factor=9.78)
        yield journal(name='Journal of Consumer Research',research='business,management and accounting',keyword ='consumer',conference_ranking='Q2',impact_factor=3.23)
        yield journal(name='Journal of Accounting Research',research='business,management and accounting',keyword='accounting',conference_ranking='Q2',impact_factor=6.56)
        yield journal(name='Journal of Management',research='business,management and accounting',keyword='management',conference_ranking='Q2',impact_factor=7.89)
        yield journal(name='Organization Science',research='business,management and accounting',keyword='organization',conference_ranking='Q3',impact_factor=2.34)
        yield journal(name='Journal of Human Resources',research='business,management and accounting',keyword='human resources',conference_ranking='Q3',impact_factor=4.5)
        yield journal(name='Leadership Quarterly',research='business,management and accounting',keyword='leadership',conference_ranking='Q4',impact_factor=6.7)
        yield journal(name='Journal of Consumer Psychology',research='business,management and accounting',keyword='consumer psychology',conference_ranking='Q4',impact_factor=3.21)
        yield journal(name='Nature Nanotechnology',research='chemical engineering',keyword='nanotechnology',conference_ranking='Q1',impact_factor=1.234)
        yield journal(name='Nature Catalysis',research='chemical engineering',keyword='catalysis',conference_ranking='Q1',impact_factor=5.67)
        yield journal(name='Journal of Catalysis',research='chemical engineering',keyword='catalysis',conference_ranking ='Q1',impact_factor=3.45)
        yield journal(name='Food Hydrocolloids',research='chemical engineering',keyword='hydrocolloids',conference_ranking='Q2',impact_factor=2.345)
        yield journal(name='Biofabrication',research='chemical engineering',keyword='biofabrication',conference_ranking='Q2',impact_factor=4.5)
        yield journal(name='Combustion and Flame',research='chemical engineering',keyword='combustion',conference_ranking='Q2',impact_factor=3.456)
        yield journal(name='Corrosion Science',research='chemical engineering',keyword='corrosion',conference_ranking='Q3',impact_factor=6.78)
        yield journal(name='Fuel',research='chemical engineering',keyword='fuel',conference_ranking='Q3',impact_factor=3.45)
        yield journal(name='Ultrasonics Sonochemistry',research='chemical engineering',keyword='sonochemistry',conference_ranking='Q4',impact_factor=7.89)
        yield journal(name='2D Materials',research='chemistry',keyword='materials',conference_ranking='Q1',impact_factor=8.9)
        yield journal(name='Progress in Surface Science',research='chemistry',keyword='Surface Science',conference_ranking='Q1',impact_factor=0.345)
        yield journal(name='Biosensors and Bioelectronics',research='chemistry',keyword='bioelectronics',conference_ranking='Q2',impact_factor=2.34)
        yield journal(name='Progress in Nuclear Magnetic Resonance Spectroscopy',research='chemistry',keyword=' nuclear magnetic resonance',conference_ranking='Q2',impact_factor=9.8)
        yield journal(name='Carbon',research='chemistry',keyword='carbon',conference_ranking='Q3',impact_factor=5.67)
        yield journal(name='Macromolecules',research='chemistry',keyword='macromolecules',conference_ranking='Q3',impact_factor=9.8)
        yield journal(name='Mass Spectrometry Reviews',research='chemistry',keyword='spectrometry',conference_ranking='Q3',impact_factor=4.56)
        yield journal(name='Desalination',research='chemistry',keyword='desalination',conference_ranking='Q4',impact_factor=8.9)
        yield journal(name='Journal of Energy Chemistry',research='chemistry',keyword='energy',conference_ranking='Q4',impact_factor=7.65)
        yield journal(name='Polymer Reviews',research='chemistry',keyword='polymer',conference_ranking='Q4',impact_factor=3.213)
        yield journal(name='Vaccine', research='veterinary', keyword='vaccine', conference_ranking='Q1',
                      impact_factor=1.45)
        yield journal(name='GeroScience', research='veterinary', keyword='geroscience', conference_ranking='Q2',
                      impact_factor=1.585)
        yield journal(name='Veterinary Microbiology', research='veterinary', keyword='microbiology',
                      conference_ranking='Q1', impact_factor=1.138)
        yield journal(name='Animal Nutrition', research='veterinary', keyword='nutrition', conference_ranking='Q1',
                      impact_factor=1.45)
        yield journal(name='Veterinary Microbiology', research='veterinary', keyword='microbiology',
                      conference_ranking='Q3', impact_factor=1.215)
        yield journal(name='Parasite', research='veterinary', keyword='parasite', conference_ranking='Q1',
                      impact_factor=1.45)
        yield journal(name='Veterinary Parasitology', research='veterinary', keyword='parasitology',
                      conference_ranking='Q3', impact_factor=0.45)
        yield journal(name='Veterinary Surgery', research='veterinary', keyword='surgery', conference_ranking='Q2',
                      impact_factor=1.19)
        yield journal(name='Mycopathologia', research='veterinary', keyword='mycopathologia', conference_ranking='Q4',
                      impact_factor=0.217)
        yield journal(name='Veterinary Dermatology', research='veterinary', keyword='dermatology',
                      conference_ranking='Q4', impact_factor=1.15)

        yield journal(name='Nature Climate Change', research='social sciences', keyword='climate',
                      conference_ranking='Q1', impact_factor=2.125)
        yield journal(name='Annual Review of Criminology', research='social sciences', keyword='criminology',
                      conference_ranking='Q1', impact_factor=1.012)
        yield journal(name='Global Environmental Change', research='social sciences', keyword='environment',
                      conference_ranking='Q1', impact_factor=2.41)
        yield journal(name='Journal of Politics', research='social sciences', keyword='politics',
                      conference_ranking='Q2', impact_factor=1.34)
        yield journal(name='Annual Review of Sociology', research='social sciences', keyword='sociology',
                      conference_ranking='Q2', impact_factor=1.83)
        yield journal(name='World Bank Research Observer', research='social sciences', keyword='world bank',
                      conference_ranking='Q2', impact_factor=1.14)
        yield journal(name='Journal of Advertising', research='social sciences', keyword='advertising',
                      conference_ranking='Q3', impact_factor=1.001)
        yield journal(name='Journal of Service Research', research='social sciences', keyword='service',
                      conference_ranking='Q3', impact_factor=0.23)
        yield journal(name='Transportation Research', research='social sciences', keyword='transportation',
                      conference_ranking='Q4', impact_factor=0.26)
        yield journal(name='Tobacco Control', research='social sciences', keyword='tobacco', conference_ranking='Q4',
                      impact_factor=1.89)

        yield journal(name='Annual Review of Psychology', research='psychology', keyword='psychology',
                      conference_ranking='Q1', impact_factor=2.221)
        yield journal(name='Trends in Cognitive Sciences', research='psychology', keyword='cognitive',
                      conference_ranking='Q1', impact_factor=0.141)
        yield journal(name='Leadership Quarterly', research='psychology', keyword='leadership', conference_ranking='Q1',
                      impact_factor=1.899)
        yield journal(name='Nature Human Behaviour', research='psychology', keyword='human behaviour',
                      conference_ranking='Q2', impact_factor=1.098)
        yield journal(name='Human Communication Research', research='psychology', keyword='communication',
                      conference_ranking='Q2', impact_factor=2.249)
        yield journal(name='Cognitive Psychology', research='psychology', keyword='cognitive', conference_ranking='Q3',
                      impact_factor=1.284)
        yield journal(name='Political Psychology', research='psychology', keyword='political', conference_ranking='Q3',
                      impact_factor=1.923)
        yield journal(name='Journal of Personality', research='psychology', keyword='personality',
                      conference_ranking='Q4', impact_factor=0.354)
        yield journal(name='Depression and Anxiety', research='psychology', keyword='depression',
                      conference_ranking='Q1', impact_factor=1.29)
        yield journal(name='Emotion', research='psychology', keyword='emotion', conference_ranking='Q2',
                      impact_factor=1.55)

        yield journal(name='Reviews of Modern Physics', research='physics and astronomy', keyword='modern physics',
                      conference_ranking='Q1', impact_factor=1.058)
        yield journal(name='Nature Nanotechnology', research='physics and astronomy', keyword='nanotechnology',
                      conference_ranking='Q1', impact_factor=1.35)
        yield journal(name='Nature Materials', research='physics and astronomy', keyword='materials',
                      conference_ranking='Q1', impact_factor=0.652)
        yield journal(name='Advances in Physics', research='physics and astronomy', keyword='physics',
                      conference_ranking='Q2', impact_factor=1.649)
        yield journal(name='Nature Photonics', research='physics and astronomy', keyword='photonics',
                      conference_ranking='Q2', impact_factor=1.208)
        yield journal(name='Living Reviews in Relativity', research='physics and astronomy', keyword='relativity',
                      conference_ranking='Q2', impact_factor=2.45)
        yield journal(name='Nature Electronics', research='physics and astronomy', keyword='electronics',
                      conference_ranking='Q3', impact_factor=0.789)
        yield journal(name='Advances in Optics and Photonics', research='physics and astronomy', keyword='optics',
                      conference_ranking='Q3', impact_factor=1.115)
        yield journal(name='ACS Photonics', research='physics and astronomy', keyword='photonics',
                      conference_ranking='Q4', impact_factor=1.02)
        yield journal(name='Nature Astronomy', research='physics and astronomy', keyword='astronomy',
                      conference_ranking='Q4', impact_factor=0.34)

        yield journal(name='Diabetes Care', research='nursing', keyword='diabetes', conference_ranking='Q1',
                      impact_factor=1.78)
        yield journal(name='Annual Review of Nutrition', research='nursing', keyword='nutrition',
                      conference_ranking='Q1', impact_factor=1.029)
        yield journal(name='International Journal of Obesity', research='nursing', keyword='obesity',
                      conference_ranking='Q1', impact_factor=2.38)
        yield journal(name='Journal of Cancer Survivorship', research='nursing', keyword='cancer',
                      conference_ranking='Q2', impact_factor=0.245)
        yield journal(name='Current Opinion in Lipidology', research='nursing', keyword='lipidology',
                      conference_ranking='Q3', impact_factor=1.28)
        yield journal(name='Global Heart', research='nursing', keyword='heart', conference_ranking='Q4',
                      impact_factor=1.013)
        yield journal(name='Appetite', research='nursing', keyword='appetite', conference_ranking='Q4',
                      impact_factor=0.94)
        yield journal(name='Nutrients', research='nursing', keyword='nutrients', conference_ranking='Q2',
                      impact_factor=1.13)
        yield journal(name='Nutrition and Metabolism', research='nursing', keyword='metabolism',
                      conference_ranking='Q3', impact_factor=2.258)
        yield journal(name='Journal of Aging and Health', research='nursing', keyword='aging', conference_ranking='Q2',
                      impact_factor=1.483)

        yield journal(name='Neuron', research='neuroscience', keyword='neuron', conference_ranking='Q1',
                      impact_factor=1.320)
        yield journal(name='Progress in Retinal and Eye Research', research='neuroscience', keyword='eye',
                      conference_ranking='Q1', impact_factor=1.03)
        yield journal(name='Nature Reviews Neurology', research='neuroscience', keyword='neurology',
                      conference_ranking='Q1', impact_factor=1.013)
        yield journal(name='Ageing Research Reviews', research='neuroscience', keyword='ageing',
                      conference_ranking='Q2', impact_factor=1.359)
        yield journal(name='Pain', research='neuroscience', keyword='pain', conference_ranking='Q2', impact_factor=1.39)
        yield journal(name='Epilepsia', research='neuroscience', keyword='epilepsia', conference_ranking='Q2',
                      impact_factor=2.145)
        yield journal(name='Human Brain Mapping', research='neuroscience', keyword='brain', conference_ranking='Q3',
                      impact_factor=2.28)
        yield journal(name='Cortex', research='neuroscience', keyword='cortex', conference_ranking='Q3',
                      impact_factor=0.318)
        yield journal(name='Multiple Sclerosis', research='neuroscience', keyword='sclerosis', conference_ranking='Q4',
                      impact_factor=1.44)
        yield journal(name='Journal of Neurochemistry', research='neuroscience', keyword='neurochemistry',
                      conference_ranking='Q4', impact_factor=1.92)

        yield journal(name='Nature', research='multidisciplinary', keyword='nature', conference_ranking='Q1',
                      impact_factor=1.29)
        yield journal(name='Science', research='multidisciplinary', keyword='science', conference_ranking='Q1',
                      impact_factor=1.321)
        yield journal(name='Fractals', research='multidisciplinary', keyword='fractals', conference_ranking='Q1',
                      impact_factor=1.11)
        yield journal(name='Applied Network Science', research='multidisciplinary', keyword='network',
                      conference_ranking='Q2', impact_factor=1.349)
        yield journal(name='Theology and Science', research='multidisciplinary', keyword='theology',
                      conference_ranking='Q2', impact_factor=2.292)
        yield journal(name='Resonance', research='multidisciplinary', keyword='resonance', conference_ranking='Q2',
                      impact_factor=0.38)
        yield journal(name='Data in Brief', research='multidisciplinary', keyword='data', conference_ranking='Q3',
                      impact_factor=1.944)
        yield journal(name='New Scientist', research='multidisciplinary', keyword='scientist', conference_ranking='Q3',
                      impact_factor=1.832)
        yield journal(name='Research Journal of Applied Sciences', research='multidisciplinary',
                      keyword='applied sciences', conference_ranking='Q4', impact_factor=1.852)
        yield journal(name='Synthesiology', research='multidisciplinary', keyword='synthesiology',
                      conference_ranking='Q4', impact_factor=1.822)

        yield journal(name='Nature Reviews Genetics', research='medicine', keyword='genetics', conference_ranking='Q1',
                      impact_factor=0.294)
        yield journal(name='Nature Reviews Cancer', research='medicine', keyword='cancer', conference_ranking='Q1',
                      impact_factor=0.491)
        yield journal(name='Nature Reviews Immunology', research='medicine', keyword='immunology',
                      conference_ranking='Q1', impact_factor=1.592)
        yield journal(name='The Lancet', research='medicine', keyword='lancet', conference_ranking='Q2',
                      impact_factor=1.39)
        yield journal(name='Nature Reviews Microbiology', research='medicine', keyword='microbiology',
                      conference_ranking='Q2', impact_factor=1.93)
        yield journal(name='Immunity', research='medicine', keyword='immunity', conference_ranking='Q3',
                      impact_factor=1.011)
        yield journal(name='Cancer Cell', research='medicine', keyword='cancer', conference_ranking='Q3',
                      impact_factor=1.49)
        yield journal(name='Nature Reviews Clinical Oncology', research='medicine', keyword='oncology',
                      conference_ranking='Q4', impact_factor=2.384)
        yield journal(name='Genome Research', research='medicine', keyword='genome', conference_ranking='Q4',
                      impact_factor=1.99)
        yield journal(name='European Urology', research='medicine', keyword='urology', conference_ranking='Q4',
                      impact_factor=0.47)

        yield journal(name='Nature Reviews Drug Discovery', research='pharmacology, toxicology and pharmaceutics',
                      keyword='drug', conference_ranking='Q1', impact_factor=1.395)
        yield journal(name='Molecular Therapy', research='pharmacology, toxicology and pharmaceutics',
                      keyword='molecular', conference_ranking='Q1', impact_factor=2.859)
        yield journal(name='Protein & Cell', research='pharmacology, toxicology and pharmaceutics', keyword='protein',
                      conference_ranking='Q1', impact_factor=0.29)
        yield journal(name='Environmental Pollution', research='pharmacology, toxicology and pharmaceutics',
                      keyword='pollution', conference_ranking='Q2', impact_factor=0.273)
        yield journal(name='Expert Review of Vaccines', research='pharmacology, toxicology and pharmaceutics',
                      keyword='vaccines', conference_ranking='Q2', impact_factor=2.29)
        yield journal(name='Antiviral Research', research='pharmacology, toxicology and pharmaceutics',
                      keyword='antiviral', conference_ranking='Q2', impact_factor=0.497)
        yield journal(name='Human Genomics', research='pharmacology, toxicology and pharmaceutics', keyword='genomics',
                      conference_ranking='Q3', impact_factor=1.37)
        yield journal(name='Antibiotics', research='pharmacology, toxicology and pharmaceutics', keyword='antibiotics',
                      conference_ranking='Q3', impact_factor=1.392)
        yield journal(name='Toxins', research='pharmacology, toxicology and pharmaceutics', keyword='toxins',
                      conference_ranking='Q4', impact_factor=1.45)
        yield journal(name='Alcohol and Alcoholism', research='pharmacology, toxicology and pharmaceutics',
                      keyword='alcohol', conference_ranking='Q4', impact_factor=1.22)

        yield journal(name='Annual Review of Astronomy and Astrophysics', research='earth and planetary sciences',
                      keyword='astronomy', conference_ranking='Q1', impact_factor=12.954)
        yield journal(name='Reviews of Geophysics', research='earth and planetary sciences', keyword='geophysics',
                      conference_ranking='Q1', impact_factor=12.954)
        yield journal(name='Annual Review of Marine Science', research='earth and planetary sciences', keyword='marine',
                      conference_ranking='Q1', impact_factor=7.193)
        yield journal(name='Living Reviews in Solar Physics', research='earth and planetary sciences',
                      keyword='solar physics', conference_ranking='Q1', impact_factor=9.3545)
        yield journal(name='Physics of the Dark Universe', research='earth and planetary sciences',
                      keyword='dark universe', conference_ranking='Q2', impact_factor=1.459)
        yield journal(name='Journal of Applied Meteorology and Climatology', research='earth and planetary sciences',
                      keyword='meteorology', conference_ranking='Q2', impact_factor=1.367)
        yield journal(name='Advances in Atmospheric Sciences', research='earth and planetary sciences',
                      keyword='atmospheric', conference_ranking='Q3', impact_factor=0.554)
        yield journal(name='Planetary and Space Science', research='earth and planetary sciences', keyword='planetary',
                      conference_ranking='Q3', impact_factor=0.438)
        yield journal(name='Journal of the Geothermal Research Society of Japan',
                      research='earth and planetary sciences', keyword='geothermal', conference_ranking='Q4',
                      impact_factor=0.157)
        yield journal(name='Observatory', research='earth and planetary sciences', keyword='observatory',
                      conference_ranking='Q4', impact_factor=0.128)

        yield journal(name='Journal of Political Economy', research='economics,econometrics and finance',
                      keyword='political economics', conference_ranking='Q1', impact_factor=17.138)
        yield journal(name='Journal of Finance', research='economics,econometrics and finance', keyword='finance',
                      conference_ranking='Q1', impact_factor=7.228)
        yield journal(name='Econometrica', research='economics,econometrics and finance', keyword='econometrica',
                      conference_ranking='Q1', impact_factor=5.876)
        yield journal(name='Review of Financial Studies', research='economics,econometrics and finance',
                      keyword='financial studies', conference_ranking='Q2', impact_factor=1.108)
        yield journal(name='Journal of Labor Economics', research='economics,econometrics and finance', keyword='labor',
                      conference_ranking='Q2', impact_factor=1.236)
        yield journal(name='Journal of Marketing', research='economics,econometrics and finance', keyword='marketing',
                      conference_ranking='Q3', impact_factor=0.918)
        yield journal(name='Journal of Accounting Research', research='economics,econometrics and finance',
                      keyword='accounting', conference_ranking='Q3', impact_factor=0.778)
        yield journal(name='Journal of Management', research='economics,econometrics and finance', keyword='management',
                      conference_ranking='Q3', impact_factor=0.568)
        yield journal(name='IMF Economic Review', research='economics,econometrics and finance', keyword='imf',
                      conference_ranking='Q4', impact_factor=0.138)
        yield journal(name='World Bank Research Observer', research='economics,econometrics and finance',
                      keyword='world bank', conference_ranking='Q4', impact_factor=0.180)

        yield journal(name='Nature Energy', research='energy', keyword='nature energy', conference_ranking='Q1',
                      impact_factor=21.228)
        yield journal(name='Nano Energy', research='energy', keyword='nano', conference_ranking='Q1',
                      impact_factor=14.228)
        yield journal(name='Applied Energy', research='energy', keyword='applied energy', conference_ranking='Q1',
                      impact_factor=5.244)
        yield journal(name='Energy Conversion and Management', research='energy', keyword='energy conversion',
                      conference_ranking='Q2', impact_factor=2.008)
        yield journal(name='Energy Policy', research='energy', keyword='energy policy', conference_ranking='Q2',
                      impact_factor=1.228)
        yield journal(name='Applied Thermal Engineering', research='energy', keyword='thermal', conference_ranking='Q3',
                      impact_factor=1.428)
        yield journal(name='Fuel', research='energy', keyword='fuel', conference_ranking='Q3', impact_factor=1.998)
        yield journal(name='Biofuel Research Journal', research='energy', keyword='biofuel', conference_ranking='Q3',
                      impact_factor=1.228)
        yield journal(name='Solar Energy', research='energy', keyword='solar', conference_ranking='Q4',
                      impact_factor=7.228)
        yield journal(name='Geothermics', research='energy', keyword='geothermics', conference_ranking='Q4',
                      impact_factor=0.328)
        yield journal(name='Biomass and Bioenergy', research='energy', keyword='biomass', conference_ranking='Q4',
                      impact_factor=0.018)

        yield journal(name='Nature Nanotechnology', research='engineering', keyword='nanotechnology',
                      conference_ranking='Q1', impact_factor=14.277)
        yield journal(name='Cement and Concrete Research', research='engineering', keyword='cement',
                      conference_ranking='Q1', impact_factor=14.225)
        yield journal(name='Research Policy', research='engineering', keyword='research', conference_ranking='Q2',
                      impact_factor=4.114)
        yield journal(name='IEEE Geoscience and Remote Sensing Magazine', research='engineering', keyword='geoscience',
                      conference_ranking='Q2', impact_factor=6.618)
        yield journal(name='International Journal of Robotics Research', research='engineering', keyword='robotics',
                      conference_ranking='Q2', impact_factor=5.923)
        yield journal(name='2D Materials', research='engineering', keyword='2d', conference_ranking='Q3',
                      impact_factor=1.258)
        yield journal(name='International Journal of Plasticity', research='engineering', keyword='plasticity',
                      conference_ranking='Q3', impact_factor=1.098)
        yield journal(name='Progress in Aerospace Sciences', research='engineering', keyword='aerospace',
                      conference_ranking='Q3', impact_factor=1.128)
        yield journal(name='Chemical Engineering Journal', research='engineering', keyword='chemical',
                      conference_ranking='Q4', impact_factor=0.555)
        yield journal(name='Biofabrication', research='engineering', keyword='biofabrication', conference_ranking='Q4',
                      impact_factor=0.325)
        yield journal(name='Rock Mechanics and Rock Engineering', research='engineering', keyword='rock',
                      conference_ranking='Q4', impact_factor=0.228)

        yield journal(name='Fungal Diversity', research='environmental science', keyword='fungal',
                      conference_ranking='Q1', impact_factor=15.555)
        yield journal(name='Nature Climate Change', research='environmental science', keyword='climate',
                      conference_ranking='Q1', impact_factor=10.027)
        yield journal(name='Methods in Ecology and Evolution', research='environmental science', keyword='ecology',
                      conference_ranking='Q1', impact_factor=9.327)
        yield journal(name='Fish and Fisheries', research='environmental science', keyword='fish',
                      conference_ranking='Q2', impact_factor=4.628)
        yield journal(name='Conservation Biology', research='environmental science', keyword='biology',
                      conference_ranking='Q2', impact_factor=5.636)
        yield journal(name='Ecosystem Services', research='environmental science', keyword='ecosystem',
                      conference_ranking='Q2', impact_factor=7.833)
        yield journal(name='Cryosphere', research='environmental science', keyword='cryosphere',
                      conference_ranking='Q3', impact_factor=1.928)
        yield journal(name='Geobiology', research='environmental science', keyword='', conference_ranking='Q3',
                      impact_factor=1.210)
        yield journal(name='Green Chemistry', research='environmental science', keyword='green chemistry',
                      conference_ranking='Q4', impact_factor=0.100)
        yield journal(name='Organization and Environment', research='environmental science', keyword='organization',
                      conference_ranking='Q4', impact_factor=0.511)

        yield journal(name='Journal of Physiology', research='health professions', keyword='physiology',
                      conference_ranking='Q1', impact_factor=16.937)
        yield journal(name='Diabetes Technology and Therapeutics', research='health professions', keyword='diabetes',
                      conference_ranking='Q1', impact_factor=11.980)
        yield journal(name='Journal of Learning Disabilities', research='health professions', keyword='disabilities',
                      conference_ranking='Q1', impact_factor=8.511)
        yield journal(name='Ear and Hearing', research='health professions', keyword='hearing', conference_ranking='Q2',
                      impact_factor=5.004)
        yield journal(name='Spine', research='health professions', keyword='spine', conference_ranking='Q2',
                      impact_factor=6.125)
        yield journal(name='Audiology and Neurotology Extra', research='health professions', keyword='neurotology',
                      conference_ranking='Q3', impact_factor=1.533)
        yield journal(name='Journal of Physiotherapy', research='health professions', keyword='physiotherapy',
                      conference_ranking='Q3', impact_factor=1.521)
        yield journal(name='Altex', research='health professions', keyword='altex', conference_ranking='Q4',
                      impact_factor=0.500)
        yield journal(name='Histochemistry and Cell Biology', research='health professions', keyword='cell',
                      conference_ranking='Q4', impact_factor=0.981)
        yield journal(name='Applied Ergonomics', research='health professions', keyword='ergonomics',
                      conference_ranking='Q4', impact_factor=0.567)

        yield journal(name='Journal of Statistical Software', research='computer science',
                      keyword='statistical software', conference_ranking='Q1', impact_factor=1.45)
        yield journal(name='Science Robotics', research='computer science', keyword='robotics', conference_ranking='Q2',
                      impact_factor=3.75)
        yield journal(name='Molecular Systems Biology', research='computer science', keyword='systems biology',
                      conference_ranking='Q2', impact_factor=5.55)
        yield journal(name='Nature Biomedical Engineering', research='computer science',
                      keyword='biomedical engineering', conference_ranking='Q4', impact_factor=7.58)
        yield journal(name='Foundations and Trends in Machine Learning', research='computer science',
                      keyword='machine learning', conference_ranking='Q3', impact_factor=6.66)
        yield journal(name='Journal of Computer-Mediated Communication', research='computer science',
                      keyword='computer mediated communication', conference_ranking='Q1', impact_factor=2.09)
        yield journal(name='Internet and Higher Education', research='computer science', keyword='internet',
                      conference_ranking='Q4', impact_factor=3.55)
        yield journal(name='International Journal of Computer Vision', research='computer science',
                      keyword='computer vision', conference_ranking='Q3', impact_factor=8.86)
        yield journal(name='npj Quantum Information', research='computer science', keyword='quantum',
                      conference_ranking='Q1', impact_factor=4.45)
        yield journal(name='IEEE Communications Magazine', research='computer science', keyword='ieee communication',
                      conference_ranking='Q2', impact_factor=7.69)
        yield journal(name='Annals of Mathematics', research='decision sciences', keyword='mathematics',
                      conference_ranking='Q1', impact_factor=4.67)
        yield journal(name='Management Science', research='decision sciences', keyword='management',
                      conference_ranking='Q2', impact_factor=6.77)
        yield journal(name='Organizational Research Methods', research='decision sciences', keyword='research methods',
                      conference_ranking='Q3', impact_factor=2.22)
        yield journal(name='Annals of Statistics', research='decision sciences', keyword='statistics',
                      conference_ranking='Q4', impact_factor=3.34)
        yield journal(name='Journal of the American Statistical Association', research='decision sciences',
                      keyword='american statistical association', conference_ranking='Q2', impact_factor=6.55)
        yield journal(name='Journal of Operations Management', research='decision sciences',
                      keyword='operations management', conference_ranking='Q4', impact_factor=7.88)
        yield journal(name='Structural Equation Modeling', research='decision sciences', keyword='equation modelling',
                      conference_ranking='Q2', impact_factor=9.99)
        yield journal(name='Annals of Probability', research='decision sciences', keyword='probability',
                      conference_ranking='Q3', impact_factor=4.78)
        yield journal(name='R Journal', research='decision sciences', keyword='r', conference_ranking='Q1',
                      impact_factor=5.46)
        yield journal(name='Research Policy', research='decision sciences', keyword='policy', conference_ranking='Q3',
                      impact_factor=3.67)
        yield journal(name='Periodontology 2000', research='dentistry', keyword='periodontology',
                      conference_ranking='Q1', impact_factor=1.78)
        yield journal(name='Journal of Clinical Periodontology', research='dentistry',
                      keyword='clinical periodontology', conference_ranking='Q2', impact_factor=6.87)
        yield journal(name='Clinical Oral Implants Research', research='dentistry', keyword='oral implants',
                      conference_ranking='Q3', impact_factor=4.87)
        yield journal(name='Journal of Dental Research', research='dentistry', keyword='dental research',
                      conference_ranking='Q4', impact_factor=5.55)
        yield journal(name='Dental Materials', research='dentistry', keyword='materials', conference_ranking='Q2',
                      impact_factor=7.77)
        yield journal(name='Oral Oncology', research='dentistry', keyword='oncology', conference_ranking='Q4',
                      impact_factor=4.44)
        yield journal(name='Journal of Dentistry', research='dentistry', keyword='dentist', conference_ranking='Q2',
                      impact_factor=6.67)
        yield journal(name='Journal of Endodontics', research='dentistry', keyword='endodontics',
                      conference_ranking='Q3', impact_factor=8.99)
        yield journal(name='Operative Dentistry', research='dentistry', keyword='operative', conference_ranking='Q1',
                      impact_factor=9.67)
        yield journal(name='Caries Research', research='dentistry', keyword='caries', conference_ranking='Q4',
                      impact_factor=8.69)
        yield journal(name='Nature Reviews Immunology', research='immunology and microbiology', keyword='nature',
                      conference_ranking='Q1', impact_factor=3.87)
        yield journal(name='Annual Review of Immunology', research='immunology and microbiology',
                      keyword='annual review', conference_ranking='Q3', impact_factor=2.29)
        yield journal(name='Nature Reviews Microbiology', research='immunology and microbiology',
                      keyword='nature microbiology', conference_ranking='Q2', impact_factor=5.25)
        yield journal(name='Nature Biotechnology', research='immunology and microbiology', keyword='biotechnology',
                      conference_ranking='Q2', impact_factor=8.44)
        yield journal(name='Immunity', research='immunology and microbiology', keyword='immune',
                      conference_ranking='Q3', impact_factor=6.98)
        yield journal(name='Clinical Microbiology Reviews', research='immunology and microbiology',
                      keyword='microbiology reviews', conference_ranking='Q1', impact_factor=1.99)
        yield journal(name='Cell Host and Microbe', research='immunology and microbiology', keyword='host and microbe',
                      conference_ranking='Q3', impact_factor=1.90)
        yield journal(name='EMBO Journal', research='immunology and microbiology', keyword='embo',
                      conference_ranking='Q4', impact_factor=7.76)
        yield journal(name='The Lancet HIV', research='immunology and microbiology', keyword='hiv',
                      conference_ranking='Q1', impact_factor=9.67)
        yield journal(name='Blood', research='immunology and microbiology', keyword='blood', conference_ranking='Q3',
                      impact_factor=4.21)
        yield journal(name='Nature Energy', research='materials science', keyword='energy', conference_ranking='Q2',
                      impact_factor=1.56)
        yield journal(name='Nature Nanotechnology', research='materials science', keyword='nanotechnology',
                      conference_ranking='Q1', impact_factor=4.33)
        yield journal(name='Nature Materials', research='materials science', keyword='materials',
                      conference_ranking='Q3', impact_factor=7.77)
        yield journal(name='Nature Photonics', research='materials science', keyword='photonics',
                      conference_ranking='Q4', impact_factor=7.88)
        yield journal(name='Advanced Energy Materials', research='materials science', keyword='energy materials',
                      conference_ranking='Q1', impact_factor=6.55)
        yield journal(name='Nano Futures', research='materials science', keyword='nano', conference_ranking='Q1',
                      impact_factor=2.56)
        yield journal(name='Progress in Materials Science', research='materials science', keyword='progress',
                      conference_ranking='Q4', impact_factor=8.00)
        yield journal(name='ACS Energy Letters', research='materials science', keyword='energy letters',
                      conference_ranking='Q2', impact_factor=7.00)
        yield journal(name='Nature Electronics', research='materials science', keyword='electronics',
                      conference_ranking='Q3', impact_factor=2.02)
        yield journal(name='Chem', research='materials science', keyword='chem', conference_ranking='Q1',
                      impact_factor=2.00)
        yield journal(name='Publications Mathématiques', research='mathematics', keyword='publications',
                      conference_ranking='Q1', impact_factor=5.00)
        yield journal(name='Annals of Mathematics', research='mathematics', keyword='annals', conference_ranking='Q2',
                      impact_factor=6.06)
        yield journal(name='Inventiones Mathematicae', research='mathematics', keyword='inventiones',
                      conference_ranking='Q3', impact_factor=7.77)
        yield journal(name='Acta Mathematica', research='mathematics', keyword='acta', conference_ranking='Q4',
                      impact_factor=4.00)
        yield journal(name='Springer Monographs in Mathematics', research='mathematics', keyword='springer monogarphs',
                      conference_ranking='Q1', impact_factor=1.98)
        yield journal(name='Duke Mathematical Journal', research='mathematics', keyword='duke', conference_ranking='Q2',
                      impact_factor=6.11)
        yield journal(name='Acta Numerica', research='mathematics', keyword='numerica', conference_ranking='Q3',
                      impact_factor=3.33)
        yield journal(name='SIAM Review', research='mathematics', keyword='siam', conference_ranking='Q4',
                      impact_factor=8.99)
        yield journal(name='Structural Equation Modeling', research='mathematics', keyword='equation modeling',
                      conference_ranking='Q1', impact_factor=5.55)
        yield journal(name='Geometry and Topology', research='mathematics', keyword='topology', conference_ranking='Q2',
                      impact_factor=6.96)
    @Rule((journal(name = MATCH.x,research=L(research_area) , conference_ranking=L(conference_ranking),impact_factor=MATCH.y)))
    def print(self,x,y):
        if(len(xl) == 0):
            xl.append(x)
            xl_r.append(y)
        else:
            if(xl_r[0] < y):
                xl.pop()
                xl_r.pop()
                xl.append(x)
                xl_r.append(y)
        #print(x)

    @Rule((journal(name=MATCH.x,research=L(research_area) ,keyword=L(keyword_u), conference_ranking=L(conference_ranking), impact_factor=MATCH.y)))
    def pr(self,x,y):
        if (len(xd) == 0):
            xd.append(x)
            xd_r.append(y)
        else:
            if (xd_r[0] < y):
                xd.pop()
                xd_r.pop()
                xd.append(x)
                xd_r.append(y)

engine = start()
engine.reset()
engine.run()
if(len(xd) != 0):
    print("You should get "+xd.pop())
elif(len(xl)!=0):
    print("You should get "+xl.pop())
else:
    print("No matches found")

