from pubtator import PubTator2Anndoc

# Define entity classes here
# entity_classes = {'Gene': 'e_1', 'FamilyName': 'e_2', 'DomainMotif': 'e_3', 'Species': 'e_4'}
entity_class = {}

# Define input file
input_file = '.'

pub2anndoc = PubTator2Anndoc(entity_classes)
pub2anndoc.parse(input_file)
