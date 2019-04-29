from collections import OrderedDict
from unittest import TestCase

import pyjsonnlp
import pytest
from pyjsonnlp import validation

from spacyjsonnlp import SpacyPipeline, get_model
from . import mocks

text = "Autonomous cars from the countryside of France shift insurance liability toward manufacturers. People are afraid that they will crash."


class TestSpacy(TestCase):
    def test_process(self):
        pyjsonnlp.__version__ = '0.1'
        actual = SpacyPipeline.process(text, spacy_model='en', coreferences=False, constituents=False)
        expected = OrderedDict([('meta', OrderedDict([('DC.conformsTo', '0.1'), ('DC.created', '2019-01-25T17:04:34'), ('DC.date', '2019-01-25T17:04:34')])), ('documents', {1: OrderedDict([('meta', OrderedDict([('DC.conformsTo', '0.1'), ('DC.source', 'SpaCy 2.1.3'), ('DC.created', '2019-01-25T17:04:34'), ('DC.date', '2019-01-25T17:04:34'), ('DC.language', 'en')])), ('id', 1), ('text', 'Autonomous cars from the countryside of France shift insurance liability toward manufacturers. People are afraid that they will crash.'), ('tokenList', {1: {'id': 1, 'text': 'Autonomous', 'lemma': 'autonomous', 'xpos': 'JJ', 'upos': 'ADJ', 'entity_iob': 'O', 'characterOffsetBegin': 0, 'characterOffsetEnd': 10, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'No', 'Alpha': 'Yes', 'Degree': 'Pos', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'Yes'}, 'shape': 'Xxxxx'}, 2: {'id': 2, 'text': 'cars', 'lemma': 'car', 'xpos': 'NNS', 'upos': 'NOUN', 'entity_iob': 'O', 'characterOffsetBegin': 11, 'characterOffsetEnd': 15, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'No', 'Alpha': 'Yes', 'Number': 'Plur', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'Yes'}, 'shape': 'xxxx'}, 3: {'id': 3, 'text': 'from', 'lemma': 'from', 'xpos': 'IN', 'upos': 'ADP', 'entity_iob': 'O', 'characterOffsetBegin': 16, 'characterOffsetEnd': 20, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'Yes', 'Alpha': 'Yes', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'Yes'}, 'shape': 'xxxx'}, 4: {'id': 4, 'text': 'the', 'lemma': 'the', 'xpos': 'DT', 'upos': 'DET', 'entity_iob': 'O', 'characterOffsetBegin': 21, 'characterOffsetEnd': 24, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'Yes', 'Alpha': 'Yes', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'Yes'}, 'shape': 'xxx'}, 5: {'id': 5, 'text': 'countryside', 'lemma': 'countryside', 'xpos': 'NN', 'upos': 'NOUN', 'entity_iob': 'O', 'characterOffsetBegin': 25, 'characterOffsetEnd': 36, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'No', 'Alpha': 'Yes', 'Number': 'Sing', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'Yes'}, 'shape': 'xxxx'}, 6: {'id': 6, 'text': 'of', 'lemma': 'of', 'xpos': 'IN', 'upos': 'ADP', 'entity_iob': 'O', 'characterOffsetBegin': 37, 'characterOffsetEnd': 39, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'Yes', 'Alpha': 'Yes', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'Yes'}, 'shape': 'xx'}, 7: {'id': 7, 'text': 'France', 'lemma': 'France', 'xpos': 'NNP', 'upos': 'PROPN', 'entity_iob': 'B', 'characterOffsetBegin': 40, 'characterOffsetEnd': 46, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'No', 'Alpha': 'Yes', 'NounType': 'Prop', 'Number': 'Sing', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'Yes'}, 'shape': 'Xxxxx', 'entity': 'GPE'}, 8: {'id': 8, 'text': 'shift', 'lemma': 'shift', 'xpos': 'NN', 'upos': 'NOUN', 'entity_iob': 'O', 'characterOffsetBegin': 47, 'characterOffsetEnd': 52, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'No', 'Alpha': 'Yes', 'Number': 'Sing', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'Yes'}, 'shape': 'xxxx'}, 9: {'id': 9, 'text': 'insurance', 'lemma': 'insurance', 'xpos': 'NN', 'upos': 'NOUN', 'entity_iob': 'O', 'characterOffsetBegin': 53, 'characterOffsetEnd': 62, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'No', 'Alpha': 'Yes', 'Number': 'Sing', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'Yes'}, 'shape': 'xxxx'}, 10: {'id': 10, 'text': 'liability', 'lemma': 'liability', 'xpos': 'NN', 'upos': 'NOUN', 'entity_iob': 'O', 'characterOffsetBegin': 63, 'characterOffsetEnd': 72, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'No', 'Alpha': 'Yes', 'Number': 'Sing', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'Yes'}, 'shape': 'xxxx'}, 11: {'id': 11, 'text': 'toward', 'lemma': 'toward', 'xpos': 'IN', 'upos': 'ADP', 'entity_iob': 'O', 'characterOffsetBegin': 73, 'characterOffsetEnd': 79, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'Yes', 'Alpha': 'Yes', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'Yes'}, 'shape': 'xxxx'}, 12: {'id': 12, 'text': 'manufacturers', 'lemma': 'manufacturer', 'xpos': 'NNS', 'upos': 'NOUN', 'entity_iob': 'O', 'characterOffsetBegin': 80, 'characterOffsetEnd': 93, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'No', 'Alpha': 'Yes', 'Number': 'Plur', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'No'}, 'shape': 'xxxx'}, 13: {'id': 13, 'text': '.', 'lemma': '.', 'xpos': '.', 'upos': 'PUNCT', 'entity_iob': 'O', 'characterOffsetBegin': 93, 'characterOffsetEnd': 94, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'No', 'Alpha': 'No', 'PunctType': 'Peri', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'Yes'}}, 14: {'id': 14, 'text': 'People', 'lemma': 'People', 'xpos': 'NNS', 'upos': 'NOUN', 'entity_iob': 'O', 'characterOffsetBegin': 94, 'characterOffsetEnd': 100, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'No', 'Alpha': 'Yes', 'Number': 'Plur', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'Yes'}, 'shape': 'Xxxxx'}, 15: {'id': 15, 'text': 'are', 'lemma': 'be', 'xpos': 'VBP', 'upos': 'VERB', 'entity_iob': 'O', 'characterOffsetBegin': 101, 'characterOffsetEnd': 104, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'Yes', 'Alpha': 'Yes', 'VerbForm': 'Fin', 'Tense': 'Pres', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'Yes'}, 'shape': 'xxx'}, 16: {'id': 16, 'text': 'afraid', 'lemma': 'afraid', 'xpos': 'JJ', 'upos': 'ADJ', 'entity_iob': 'O', 'characterOffsetBegin': 105, 'characterOffsetEnd': 111, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'No', 'Alpha': 'Yes', 'Degree': 'Pos', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'Yes'}, 'shape': 'xxxx'}, 17: {'id': 17, 'text': 'that', 'lemma': 'that', 'xpos': 'IN', 'upos': 'ADP', 'entity_iob': 'O', 'characterOffsetBegin': 112, 'characterOffsetEnd': 116, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'Yes', 'Alpha': 'Yes', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'Yes'}, 'shape': 'xxxx'}, 18: {'id': 18, 'text': 'they', 'lemma': '-PRON-', 'xpos': 'PRP', 'upos': 'PRON', 'entity_iob': 'O', 'characterOffsetBegin': 117, 'characterOffsetEnd': 121, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'Yes', 'Alpha': 'Yes', 'PronType': 'Prs', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'Yes'}, 'shape': 'xxxx'}, 19: {'id': 19, 'text': 'will', 'lemma': 'will', 'xpos': 'MD', 'upos': 'VERB', 'entity_iob': 'O', 'characterOffsetBegin': 122, 'characterOffsetEnd': 126, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'Yes', 'Alpha': 'Yes', 'VerbType': 'Mod', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'Yes'}, 'shape': 'xxxx'}, 20: {'id': 20, 'text': 'crash', 'lemma': 'crash', 'xpos': 'VB', 'upos': 'VERB', 'entity_iob': 'O', 'characterOffsetBegin': 127, 'characterOffsetEnd': 132, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'No', 'Alpha': 'Yes', 'VerbForm': 'Inf', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'No'}, 'shape': 'xxxx'}, 21: {'id': 21, 'text': '.', 'lemma': '.', 'xpos': '.', 'upos': 'PUNCT', 'entity_iob': 'O', 'characterOffsetBegin': 132, 'characterOffsetEnd': 133, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'No', 'Alpha': 'No', 'PunctType': 'Peri', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'No'}}}), ('clauses', {1: {'id': 1, 'sentenceId': 2, 'clauseType': 'complement', 'tokens': [17, 18, 19, 20], 'root': [20], 'mainVerb': {'head': 20, 'semantic': [20], 'phrase': [17, 18, 19, 20]}, 'subject': {'head': 18, 'semantic': [18], 'phrase': [18]}, 'compound': False, 'complex': False, 'transitivity': 'intransitive', 'negated': False, 'parentClauseId': 2}, 2: {'id': 2, 'sentenceId': 2, 'clauseType': 'matrix', 'tokens': [14, 15, 16, 21], 'root': [15], 'mainVerb': {'head': 15, 'semantic': [15], 'phrase': [14, 15, 16, 17, 18, 19, 20, 21]}, 'subject': {'head': 14, 'semantic': [14], 'phrase': [14]}, 'compound': False, 'complex': True, 'negated': False}}), ('sentences', {1: {'id': 1, 'tokenFrom': 1, 'tokenTo': 14, 'tokens': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 'root': [2], 'compound': False, 'complex': False, 'negated': False}, 2: {'id': 2, 'tokenFrom': 14, 'tokenTo': 22, 'tokens': [14, 15, 16, 17, 18, 19, 20, 21], 'root': [15], 'mainVerb': {'head': 15, 'semantic': [15], 'phrase': [14, 15, 16, 17, 18, 19, 20, 21]}, 'subject': {'head': 14, 'semantic': [14], 'phrase': [14]}, 'compound': False, 'complex': True, 'negated': False}}), ('dependencies', [{'style': 'universal', 'arcs': {1: [{'sentenceId': 1, 'label': 'amod', 'governor': 2, 'dependent': 1}], 2: [{'sentenceId': 1, 'label': 'root', 'governor': 0, 'dependent': 2}], 3: [{'sentenceId': 1, 'label': 'prep', 'governor': 2, 'dependent': 3}], 4: [{'sentenceId': 1, 'label': 'det', 'governor': 5, 'dependent': 4}], 5: [{'sentenceId': 1, 'label': 'pobj', 'governor': 3, 'dependent': 5}], 6: [{'sentenceId': 1, 'label': 'prep', 'governor': 5, 'dependent': 6}], 7: [{'sentenceId': 1, 'label': 'compound', 'governor': 10, 'dependent': 7}], 8: [{'sentenceId': 1, 'label': 'compound', 'governor': 9, 'dependent': 8}], 9: [{'sentenceId': 1, 'label': 'compound', 'governor': 10, 'dependent': 9}], 10: [{'sentenceId': 1, 'label': 'pobj', 'governor': 6, 'dependent': 10}], 11: [{'sentenceId': 1, 'label': 'prep', 'governor': 10, 'dependent': 11}], 12: [{'sentenceId': 1, 'label': 'pobj', 'governor': 11, 'dependent': 12}], 13: [{'sentenceId': 1, 'label': 'punct', 'governor': 2, 'dependent': 13}], 14: [{'sentenceId': 2, 'label': 'nsubj', 'governor': 15, 'dependent': 14}], 15: [{'sentenceId': 2, 'label': 'root', 'governor': 0, 'dependent': 15}], 16: [{'sentenceId': 2, 'label': 'acomp', 'governor': 15, 'dependent': 16}], 17: [{'sentenceId': 2, 'label': 'mark', 'governor': 20, 'dependent': 17}], 18: [{'sentenceId': 2, 'label': 'nsubj', 'governor': 20, 'dependent': 18}], 19: [{'sentenceId': 2, 'label': 'aux', 'governor': 20, 'dependent': 19}], 20: [{'sentenceId': 2, 'label': 'ccomp', 'governor': 16, 'dependent': 20}], 21: [{'sentenceId': 2, 'label': 'punct', 'governor': 15, 'dependent': 21}]}}]), ('expressions', [{'id': 1, 'type': 'NP', 'head': 2, 'dependency': 'root', 'tokens': [1, 2]}, {'id': 2, 'type': 'NP', 'head': 5, 'dependency': 'pobj', 'tokens': [4, 5]}, {'id': 3, 'type': 'NP', 'head': 10, 'dependency': 'pobj', 'tokens': [7, 8, 9, 10]}])])})])
        assert actual == expected, actual

    def test_process_coref(self):
        pyjsonnlp.__version__ = '0.1'
        actual = SpacyPipeline.process(text, spacy_model='en', coreferences=True, constituents=False)
        expected = OrderedDict([('meta', OrderedDict([('DC.conformsTo', '0.1'), ('DC.created', '2019-01-25T17:04:34'), ('DC.date', '2019-01-25T17:04:34')])), ('documents', {1: OrderedDict([('meta', OrderedDict([('DC.conformsTo', '0.1'), ('DC.source', 'SpaCy 2.1.3'), ('DC.created', '2019-01-25T17:04:34'), ('DC.date', '2019-01-25T17:04:34'), ('DC.language', 'en')])), ('id', 1), ('text', 'Autonomous cars from the countryside of France shift insurance liability toward manufacturers. People are afraid that they will crash.'), ('tokenList', {1: {'id': 1, 'text': 'Autonomous', 'lemma': 'autonomous', 'xpos': 'JJ', 'upos': 'ADJ', 'entity_iob': 'O', 'characterOffsetBegin': 0, 'characterOffsetEnd': 10, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'No', 'Alpha': 'Yes', 'Degree': 'Pos', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'Yes'}, 'shape': 'Xxxxx'}, 2: {'id': 2, 'text': 'cars', 'lemma': 'car', 'xpos': 'NNS', 'upos': 'NOUN', 'entity_iob': 'O', 'characterOffsetBegin': 11, 'characterOffsetEnd': 15, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'No', 'Alpha': 'Yes', 'Number': 'Plur', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'Yes'}, 'shape': 'xxxx'}, 3: {'id': 3, 'text': 'from', 'lemma': 'from', 'xpos': 'IN', 'upos': 'ADP', 'entity_iob': 'O', 'characterOffsetBegin': 16, 'characterOffsetEnd': 20, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'Yes', 'Alpha': 'Yes', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'Yes'}, 'shape': 'xxxx'}, 4: {'id': 4, 'text': 'the', 'lemma': 'the', 'xpos': 'DT', 'upos': 'DET', 'entity_iob': 'O', 'characterOffsetBegin': 21, 'characterOffsetEnd': 24, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'Yes', 'Alpha': 'Yes', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'Yes'}, 'shape': 'xxx'}, 5: {'id': 5, 'text': 'countryside', 'lemma': 'countryside', 'xpos': 'NN', 'upos': 'NOUN', 'entity_iob': 'O', 'characterOffsetBegin': 25, 'characterOffsetEnd': 36, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'No', 'Alpha': 'Yes', 'Number': 'Sing', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'Yes'}, 'shape': 'xxxx'}, 6: {'id': 6, 'text': 'of', 'lemma': 'of', 'xpos': 'IN', 'upos': 'ADP', 'entity_iob': 'O', 'characterOffsetBegin': 37, 'characterOffsetEnd': 39, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'Yes', 'Alpha': 'Yes', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'Yes'}, 'shape': 'xx'}, 7: {'id': 7, 'text': 'France', 'lemma': 'France', 'xpos': 'NNP', 'upos': 'PROPN', 'entity_iob': 'B', 'characterOffsetBegin': 40, 'characterOffsetEnd': 46, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'No', 'Alpha': 'Yes', 'NounType': 'Prop', 'Number': 'Sing', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'Yes'}, 'shape': 'Xxxxx', 'entity': 'GPE'}, 8: {'id': 8, 'text': 'shift', 'lemma': 'shift', 'xpos': 'NN', 'upos': 'NOUN', 'entity_iob': 'O', 'characterOffsetBegin': 47, 'characterOffsetEnd': 52, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'No', 'Alpha': 'Yes', 'Number': 'Sing', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'Yes'}, 'shape': 'xxxx'}, 9: {'id': 9, 'text': 'insurance', 'lemma': 'insurance', 'xpos': 'NN', 'upos': 'NOUN', 'entity_iob': 'O', 'characterOffsetBegin': 53, 'characterOffsetEnd': 62, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'No', 'Alpha': 'Yes', 'Number': 'Sing', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'Yes'}, 'shape': 'xxxx'}, 10: {'id': 10, 'text': 'liability', 'lemma': 'liability', 'xpos': 'NN', 'upos': 'NOUN', 'entity_iob': 'O', 'characterOffsetBegin': 63, 'characterOffsetEnd': 72, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'No', 'Alpha': 'Yes', 'Number': 'Sing', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'Yes'}, 'shape': 'xxxx'}, 11: {'id': 11, 'text': 'toward', 'lemma': 'toward', 'xpos': 'IN', 'upos': 'ADP', 'entity_iob': 'O', 'characterOffsetBegin': 73, 'characterOffsetEnd': 79, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'Yes', 'Alpha': 'Yes', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'Yes'}, 'shape': 'xxxx'}, 12: {'id': 12, 'text': 'manufacturers', 'lemma': 'manufacturer', 'xpos': 'NNS', 'upos': 'NOUN', 'entity_iob': 'O', 'characterOffsetBegin': 80, 'characterOffsetEnd': 93, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'No', 'Alpha': 'Yes', 'Number': 'Plur', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'No'}, 'shape': 'xxxx'}, 13: {'id': 13, 'text': '.', 'lemma': '.', 'xpos': '.', 'upos': 'PUNCT', 'entity_iob': 'O', 'characterOffsetBegin': 93, 'characterOffsetEnd': 94, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'No', 'Alpha': 'No', 'PunctType': 'Peri', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'Yes'}}, 14: {'id': 14, 'text': 'People', 'lemma': 'People', 'xpos': 'NNS', 'upos': 'NOUN', 'entity_iob': 'O', 'characterOffsetBegin': 94, 'characterOffsetEnd': 100, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'No', 'Alpha': 'Yes', 'Number': 'Plur', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'Yes'}, 'shape': 'Xxxxx'}, 15: {'id': 15, 'text': 'are', 'lemma': 'be', 'xpos': 'VBP', 'upos': 'VERB', 'entity_iob': 'O', 'characterOffsetBegin': 101, 'characterOffsetEnd': 104, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'Yes', 'Alpha': 'Yes', 'VerbForm': 'Fin', 'Tense': 'Pres', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'Yes'}, 'shape': 'xxx'}, 16: {'id': 16, 'text': 'afraid', 'lemma': 'afraid', 'xpos': 'JJ', 'upos': 'ADJ', 'entity_iob': 'O', 'characterOffsetBegin': 105, 'characterOffsetEnd': 111, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'No', 'Alpha': 'Yes', 'Degree': 'Pos', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'Yes'}, 'shape': 'xxxx'}, 17: {'id': 17, 'text': 'that', 'lemma': 'that', 'xpos': 'IN', 'upos': 'ADP', 'entity_iob': 'O', 'characterOffsetBegin': 112, 'characterOffsetEnd': 116, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'Yes', 'Alpha': 'Yes', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'Yes'}, 'shape': 'xxxx'}, 18: {'id': 18, 'text': 'they', 'lemma': '-PRON-', 'xpos': 'PRP', 'upos': 'PRON', 'entity_iob': 'O', 'characterOffsetBegin': 117, 'characterOffsetEnd': 121, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'Yes', 'Alpha': 'Yes', 'PronType': 'Prs', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'Yes'}, 'shape': 'xxxx'}, 19: {'id': 19, 'text': 'will', 'lemma': 'will', 'xpos': 'MD', 'upos': 'VERB', 'entity_iob': 'O', 'characterOffsetBegin': 122, 'characterOffsetEnd': 126, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'Yes', 'Alpha': 'Yes', 'VerbType': 'Mod', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'Yes'}, 'shape': 'xxxx'}, 20: {'id': 20, 'text': 'crash', 'lemma': 'crash', 'xpos': 'VB', 'upos': 'VERB', 'entity_iob': 'O', 'characterOffsetBegin': 127, 'characterOffsetEnd': 132, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'No', 'Alpha': 'Yes', 'VerbForm': 'Inf', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'No'}, 'shape': 'xxxx'}, 21: {'id': 21, 'text': '.', 'lemma': '.', 'xpos': '.', 'upos': 'PUNCT', 'entity_iob': 'O', 'characterOffsetBegin': 132, 'characterOffsetEnd': 133, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'No', 'Alpha': 'No', 'PunctType': 'Peri', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'No'}}}), ('clauses', {1: {'id': 1, 'sentenceId': 2, 'clauseType': 'complement', 'tokens': [17, 18, 19, 20], 'root': [20], 'mainVerb': {'head': 20, 'semantic': [20], 'phrase': [17, 18, 19, 20]}, 'subject': {'head': 18, 'semantic': [18], 'phrase': [18]}, 'compound': False, 'complex': False, 'transitivity': 'intransitive', 'negated': False, 'parentClauseId': 2}, 2: {'id': 2, 'sentenceId': 2, 'clauseType': 'matrix', 'tokens': [14, 15, 16, 21], 'root': [15], 'mainVerb': {'head': 15, 'semantic': [15], 'phrase': [14, 15, 16, 17, 18, 19, 20, 21]}, 'subject': {'head': 14, 'semantic': [14], 'phrase': [14]}, 'compound': False, 'complex': True, 'negated': False}}), ('sentences', {1: {'id': 1, 'tokenFrom': 1, 'tokenTo': 14, 'tokens': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 'root': [2], 'compound': False, 'complex': False, 'negated': False}, 2: {'id': 2, 'tokenFrom': 14, 'tokenTo': 22, 'tokens': [14, 15, 16, 17, 18, 19, 20, 21], 'root': [15], 'mainVerb': {'head': 15, 'semantic': [15], 'phrase': [14, 15, 16, 17, 18, 19, 20, 21]}, 'subject': {'head': 14, 'semantic': [14], 'phrase': [14]}, 'compound': False, 'complex': True, 'negated': False}}), ('dependencies', [{'style': 'universal', 'arcs': {1: [{'sentenceId': 1, 'label': 'amod', 'governor': 2, 'dependent': 1}], 2: [{'sentenceId': 1, 'label': 'root', 'governor': 0, 'dependent': 2}], 3: [{'sentenceId': 1, 'label': 'prep', 'governor': 2, 'dependent': 3}], 4: [{'sentenceId': 1, 'label': 'det', 'governor': 5, 'dependent': 4}], 5: [{'sentenceId': 1, 'label': 'pobj', 'governor': 3, 'dependent': 5}], 6: [{'sentenceId': 1, 'label': 'prep', 'governor': 5, 'dependent': 6}], 7: [{'sentenceId': 1, 'label': 'compound', 'governor': 10, 'dependent': 7}], 8: [{'sentenceId': 1, 'label': 'compound', 'governor': 9, 'dependent': 8}], 9: [{'sentenceId': 1, 'label': 'compound', 'governor': 10, 'dependent': 9}], 10: [{'sentenceId': 1, 'label': 'pobj', 'governor': 6, 'dependent': 10}], 11: [{'sentenceId': 1, 'label': 'prep', 'governor': 10, 'dependent': 11}], 12: [{'sentenceId': 1, 'label': 'pobj', 'governor': 11, 'dependent': 12}], 13: [{'sentenceId': 1, 'label': 'punct', 'governor': 2, 'dependent': 13}], 14: [{'sentenceId': 2, 'label': 'nsubj', 'governor': 15, 'dependent': 14}], 15: [{'sentenceId': 2, 'label': 'root', 'governor': 0, 'dependent': 15}], 16: [{'sentenceId': 2, 'label': 'acomp', 'governor': 15, 'dependent': 16}], 17: [{'sentenceId': 2, 'label': 'mark', 'governor': 20, 'dependent': 17}], 18: [{'sentenceId': 2, 'label': 'nsubj', 'governor': 20, 'dependent': 18}], 19: [{'sentenceId': 2, 'label': 'aux', 'governor': 20, 'dependent': 19}], 20: [{'sentenceId': 2, 'label': 'ccomp', 'governor': 16, 'dependent': 20}], 21: [{'sentenceId': 2, 'label': 'punct', 'governor': 15, 'dependent': 21}]}}]), ('coreferences', [{'id': 0, 'representative': {'tokens': [14], 'head': 14}, 'referents': [{'tokens': [18], 'head': 18}]}]), ('expressions', [{'id': 1, 'type': 'NP', 'head': 2, 'dependency': 'root', 'tokens': [1, 2]}, {'id': 2, 'type': 'NP', 'head': 5, 'dependency': 'pobj', 'tokens': [4, 5]}, {'id': 3, 'type': 'NP', 'head': 10, 'dependency': 'pobj', 'tokens': [7, 8, 9, 10]}])])})])
        assert actual == expected, actual

    def test_process_coref_single(self):
        pyjsonnlp.__version__ = '0.1'
        actual = SpacyPipeline.process("I am a cat.", spacy_model='en', coreferences=True, constituents=False)
        expected = OrderedDict([('meta', OrderedDict([('DC.conformsTo', '0.1'), ('DC.created', '2019-01-25T17:04:34'), ('DC.date', '2019-01-25T17:04:34')])), ('documents', {1: OrderedDict([('meta', OrderedDict([('DC.conformsTo', '0.1'), ('DC.source', 'SpaCy 2.1.3'), ('DC.created', '2019-01-25T17:04:34'), ('DC.date', '2019-01-25T17:04:34'), ('DC.language', 'en')])), ('id', 1), ('text', 'I am a cat.'), ('tokenList', {1: {'id': 1, 'text': 'I', 'lemma': '-PRON-', 'xpos': 'PRP', 'upos': 'PRON', 'entity_iob': 'O', 'characterOffsetBegin': 0, 'characterOffsetEnd': 1, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'Yes', 'Alpha': 'Yes', 'PronType': 'Prs', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'Yes'}, 'shape': 'X'}, 2: {'id': 2, 'text': 'am', 'lemma': 'be', 'xpos': 'VBP', 'upos': 'VERB', 'entity_iob': 'O', 'characterOffsetBegin': 2, 'characterOffsetEnd': 4, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'Yes', 'Alpha': 'Yes', 'VerbForm': 'Fin', 'Tense': 'Pres', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'Yes'}, 'shape': 'xx'}, 3: {'id': 3, 'text': 'a', 'lemma': 'a', 'xpos': 'DT', 'upos': 'DET', 'entity_iob': 'O', 'characterOffsetBegin': 5, 'characterOffsetEnd': 6, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'Yes', 'Alpha': 'Yes', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'Yes'}, 'shape': 'x'}, 4: {'id': 4, 'text': 'cat', 'lemma': 'cat', 'xpos': 'NN', 'upos': 'NOUN', 'entity_iob': 'O', 'characterOffsetBegin': 7, 'characterOffsetEnd': 10, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'No', 'Alpha': 'Yes', 'Number': 'Sing', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'No'}, 'shape': 'xxx'}, 5: {'id': 5, 'text': '.', 'lemma': '.', 'xpos': '.', 'upos': 'PUNCT', 'entity_iob': 'O', 'characterOffsetBegin': 10, 'characterOffsetEnd': 11, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'No', 'Alpha': 'No', 'PunctType': 'Peri', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'No'}}}), ('sentences', {1: {'id': 1, 'tokenFrom': 1, 'tokenTo': 6, 'tokens': [1, 2, 3, 4, 5], 'root': [2], 'mainVerb': {'head': 2, 'semantic': [2], 'phrase': [1, 2, 3, 4, 5]}, 'subject': {'head': 1, 'semantic': [1], 'phrase': [1]}, 'compound': False, 'complex': False, 'transitivity': 'intransitive', 'negated': False}}), ('dependencies', [{'style': 'universal', 'arcs': {1: [{'sentenceId': 1, 'label': 'nsubj', 'governor': 2, 'dependent': 1}], 2: [{'sentenceId': 1, 'label': 'root', 'governor': 0, 'dependent': 2}], 3: [{'sentenceId': 1, 'label': 'det', 'governor': 4, 'dependent': 3}], 4: [{'sentenceId': 1, 'label': 'attr', 'governor': 2, 'dependent': 4}], 5: [{'sentenceId': 1, 'label': 'punct', 'governor': 2, 'dependent': 5}]}}]), ('expressions', [{'id': 1, 'type': 'NP', 'head': 4, 'dependency': 'attr', 'tokens': [3, 4]}])])})])
        assert actual == expected, actual

    def test_constituents(self):
        pyjsonnlp.__version__ = '0.1'
        actual = SpacyPipeline.process(text, spacy_model='en', coreferences=False, constituents=True)
        expected = OrderedDict([('meta', OrderedDict([('DC.conformsTo', '0.1'), ('DC.created', '2019-01-25T17:04:34'), ('DC.date', '2019-01-25T17:04:34')])), ('documents', {1: OrderedDict([('meta', OrderedDict([('DC.conformsTo', '0.1'), ('DC.source', 'SpaCy 2.1.3'), ('DC.created', '2019-01-25T17:04:34'), ('DC.date', '2019-01-25T17:04:34'), ('DC.language', 'en')])), ('id', 1), ('text', 'Autonomous cars from the countryside of France shift insurance liability toward manufacturers. People are afraid that they will crash.'), ('tokenList', {1: {'id': 1, 'text': 'Autonomous', 'lemma': 'autonomous', 'xpos': 'JJ', 'upos': 'ADJ', 'entity_iob': 'O', 'characterOffsetBegin': 0, 'characterOffsetEnd': 10, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'No', 'Alpha': 'Yes', 'Degree': 'Pos', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'Yes'}, 'shape': 'Xxxxx'}, 2: {'id': 2, 'text': 'cars', 'lemma': 'car', 'xpos': 'NNS', 'upos': 'NOUN', 'entity_iob': 'O', 'characterOffsetBegin': 11, 'characterOffsetEnd': 15, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'No', 'Alpha': 'Yes', 'Number': 'Plur', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'Yes'}, 'shape': 'xxxx'}, 3: {'id': 3, 'text': 'from', 'lemma': 'from', 'xpos': 'IN', 'upos': 'ADP', 'entity_iob': 'O', 'characterOffsetBegin': 16, 'characterOffsetEnd': 20, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'Yes', 'Alpha': 'Yes', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'Yes'}, 'shape': 'xxxx'}, 4: {'id': 4, 'text': 'the', 'lemma': 'the', 'xpos': 'DT', 'upos': 'DET', 'entity_iob': 'O', 'characterOffsetBegin': 21, 'characterOffsetEnd': 24, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'Yes', 'Alpha': 'Yes', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'Yes'}, 'shape': 'xxx'}, 5: {'id': 5, 'text': 'countryside', 'lemma': 'countryside', 'xpos': 'NN', 'upos': 'NOUN', 'entity_iob': 'O', 'characterOffsetBegin': 25, 'characterOffsetEnd': 36, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'No', 'Alpha': 'Yes', 'Number': 'Sing', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'Yes'}, 'shape': 'xxxx'}, 6: {'id': 6, 'text': 'of', 'lemma': 'of', 'xpos': 'IN', 'upos': 'ADP', 'entity_iob': 'O', 'characterOffsetBegin': 37, 'characterOffsetEnd': 39, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'Yes', 'Alpha': 'Yes', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'Yes'}, 'shape': 'xx'}, 7: {'id': 7, 'text': 'France', 'lemma': 'France', 'xpos': 'NNP', 'upos': 'PROPN', 'entity_iob': 'B', 'characterOffsetBegin': 40, 'characterOffsetEnd': 46, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'No', 'Alpha': 'Yes', 'NounType': 'Prop', 'Number': 'Sing', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'Yes'}, 'shape': 'Xxxxx', 'entity': 'GPE'}, 8: {'id': 8, 'text': 'shift', 'lemma': 'shift', 'xpos': 'VBP', 'upos': 'VERB', 'entity_iob': 'O', 'characterOffsetBegin': 47, 'characterOffsetEnd': 52, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'No', 'Alpha': 'Yes', 'VerbForm': 'Fin', 'Tense': 'Pres', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'Yes'}, 'shape': 'xxxx'}, 9: {'id': 9, 'text': 'insurance', 'lemma': 'insurance', 'xpos': 'NN', 'upos': 'NOUN', 'entity_iob': 'O', 'characterOffsetBegin': 53, 'characterOffsetEnd': 62, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'No', 'Alpha': 'Yes', 'Number': 'Sing', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'Yes'}, 'shape': 'xxxx'}, 10: {'id': 10, 'text': 'liability', 'lemma': 'liability', 'xpos': 'NN', 'upos': 'NOUN', 'entity_iob': 'O', 'characterOffsetBegin': 63, 'characterOffsetEnd': 72, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'No', 'Alpha': 'Yes', 'Number': 'Sing', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'Yes'}, 'shape': 'xxxx'}, 11: {'id': 11, 'text': 'toward', 'lemma': 'toward', 'xpos': 'IN', 'upos': 'ADP', 'entity_iob': 'O', 'characterOffsetBegin': 73, 'characterOffsetEnd': 79, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'Yes', 'Alpha': 'Yes', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'Yes'}, 'shape': 'xxxx'}, 12: {'id': 12, 'text': 'manufacturers', 'lemma': 'manufacturer', 'xpos': 'NNS', 'upos': 'NOUN', 'entity_iob': 'O', 'characterOffsetBegin': 80, 'characterOffsetEnd': 93, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'No', 'Alpha': 'Yes', 'Number': 'Plur', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'No'}, 'shape': 'xxxx'}, 13: {'id': 13, 'text': '.', 'lemma': '.', 'xpos': '.', 'upos': 'PUNCT', 'entity_iob': 'O', 'characterOffsetBegin': 93, 'characterOffsetEnd': 94, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'No', 'Alpha': 'No', 'PunctType': 'Peri', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'Yes'}}, 14: {'id': 14, 'text': 'People', 'lemma': 'People', 'xpos': 'NNS', 'upos': 'NOUN', 'entity_iob': 'O', 'characterOffsetBegin': 94, 'characterOffsetEnd': 100, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'No', 'Alpha': 'Yes', 'Number': 'Plur', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'Yes'}, 'shape': 'Xxxxx'}, 15: {'id': 15, 'text': 'are', 'lemma': 'be', 'xpos': 'VBP', 'upos': 'VERB', 'entity_iob': 'O', 'characterOffsetBegin': 101, 'characterOffsetEnd': 104, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'Yes', 'Alpha': 'Yes', 'VerbForm': 'Fin', 'Tense': 'Pres', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'Yes'}, 'shape': 'xxx'}, 16: {'id': 16, 'text': 'afraid', 'lemma': 'afraid', 'xpos': 'JJ', 'upos': 'ADJ', 'entity_iob': 'O', 'characterOffsetBegin': 105, 'characterOffsetEnd': 111, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'No', 'Alpha': 'Yes', 'Degree': 'Pos', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'Yes'}, 'shape': 'xxxx'}, 17: {'id': 17, 'text': 'that', 'lemma': 'that', 'xpos': 'IN', 'upos': 'ADP', 'entity_iob': 'O', 'characterOffsetBegin': 112, 'characterOffsetEnd': 116, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'Yes', 'Alpha': 'Yes', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'Yes'}, 'shape': 'xxxx'}, 18: {'id': 18, 'text': 'they', 'lemma': '-PRON-', 'xpos': 'PRP', 'upos': 'PRON', 'entity_iob': 'O', 'characterOffsetBegin': 117, 'characterOffsetEnd': 121, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'Yes', 'Alpha': 'Yes', 'PronType': 'Prs', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'Yes'}, 'shape': 'xxxx'}, 19: {'id': 19, 'text': 'will', 'lemma': 'will', 'xpos': 'MD', 'upos': 'VERB', 'entity_iob': 'O', 'characterOffsetBegin': 122, 'characterOffsetEnd': 126, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'Yes', 'Alpha': 'Yes', 'VerbType': 'Mod', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'Yes'}, 'shape': 'xxxx'}, 20: {'id': 20, 'text': 'crash', 'lemma': 'crash', 'xpos': 'VB', 'upos': 'VERB', 'entity_iob': 'O', 'characterOffsetBegin': 127, 'characterOffsetEnd': 132, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'No', 'Alpha': 'Yes', 'VerbForm': 'Inf', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'No'}, 'shape': 'xxxx'}, 21: {'id': 21, 'text': '.', 'lemma': '.', 'xpos': '.', 'upos': 'PUNCT', 'entity_iob': 'O', 'characterOffsetBegin': 132, 'characterOffsetEnd': 133, 'lang': 'en', 'features': {'Overt': 'Yes', 'Stop': 'No', 'Alpha': 'No', 'PunctType': 'Peri', 'Foreign': 'No'}, 'misc': {'SpaceAfter': 'No'}}}), ('clauses', {1: {'id': 1, 'sentenceId': 2, 'clauseType': 'complement', 'tokens': [17, 18, 19, 20], 'root': [20], 'mainVerb': {'head': 20, 'semantic': [20], 'phrase': [17, 18, 19, 20]}, 'subject': {'head': 18, 'semantic': [18], 'phrase': [18]}, 'compound': False, 'complex': False, 'transitivity': 'intransitive', 'negated': False, 'parentClauseId': 2}, 2: {'id': 2, 'sentenceId': 2, 'clauseType': 'matrix', 'tokens': [14, 15, 16, 21], 'root': [15], 'mainVerb': {'head': 15, 'semantic': [15], 'phrase': [14, 15, 16, 17, 18, 19, 20, 21]}, 'subject': {'head': 14, 'semantic': [14], 'phrase': [14]}, 'compound': False, 'complex': True, 'negated': False}}), ('sentences', {1: {'id': 1, 'tokenFrom': 1, 'tokenTo': 14, 'tokens': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 'root': [2], 'compound': False, 'complex': False, 'negated': False}, 2: {'id': 2, 'tokenFrom': 14, 'tokenTo': 22, 'tokens': [14, 15, 16, 17, 18, 19, 20, 21], 'root': [15], 'mainVerb': {'head': 15, 'semantic': [15], 'phrase': [14, 15, 16, 17, 18, 19, 20, 21]}, 'subject': {'head': 14, 'semantic': [14], 'phrase': [14]}, 'compound': False, 'complex': True, 'negated': False}}), ('dependencies', [{'style': 'universal', 'arcs': {1: [{'sentenceId': 1, 'label': 'amod', 'governor': 2, 'dependent': 1}], 2: [{'sentenceId': 1, 'label': 'root', 'governor': 0, 'dependent': 2}], 3: [{'sentenceId': 1, 'label': 'prep', 'governor': 2, 'dependent': 3}], 4: [{'sentenceId': 1, 'label': 'det', 'governor': 5, 'dependent': 4}], 5: [{'sentenceId': 1, 'label': 'pobj', 'governor': 3, 'dependent': 5}], 6: [{'sentenceId': 1, 'label': 'prep', 'governor': 5, 'dependent': 6}], 7: [{'sentenceId': 1, 'label': 'compound', 'governor': 10, 'dependent': 7}], 8: [{'sentenceId': 1, 'label': 'compound', 'governor': 9, 'dependent': 8}], 9: [{'sentenceId': 1, 'label': 'compound', 'governor': 10, 'dependent': 9}], 10: [{'sentenceId': 1, 'label': 'pobj', 'governor': 6, 'dependent': 10}], 11: [{'sentenceId': 1, 'label': 'prep', 'governor': 10, 'dependent': 11}], 12: [{'sentenceId': 1, 'label': 'pobj', 'governor': 11, 'dependent': 12}], 13: [{'sentenceId': 1, 'label': 'punct', 'governor': 2, 'dependent': 13}], 14: [{'sentenceId': 2, 'label': 'nsubj', 'governor': 15, 'dependent': 14}], 15: [{'sentenceId': 2, 'label': 'root', 'governor': 0, 'dependent': 15}], 16: [{'sentenceId': 2, 'label': 'acomp', 'governor': 15, 'dependent': 16}], 17: [{'sentenceId': 2, 'label': 'mark', 'governor': 20, 'dependent': 17}], 18: [{'sentenceId': 2, 'label': 'nsubj', 'governor': 20, 'dependent': 18}], 19: [{'sentenceId': 2, 'label': 'aux', 'governor': 20, 'dependent': 19}], 20: [{'sentenceId': 2, 'label': 'ccomp', 'governor': 16, 'dependent': 20}], 21: [{'sentenceId': 2, 'label': 'punct', 'governor': 15, 'dependent': 21}]}}]), ('constituents', [{'sentenceId': 1, 'labeledBracketing': '(ROOT (S (NP (NP (JJ Autonomous) (NNS cars)) (PP (IN from) (NP (NP (DT the) (NN countryside)) (PP (IN of) (NP (NNP France)))))) (VP (VBP shift) (NP (NN insurance) (NN liability)) (PP (IN toward) (NP (NNS manufacturers)))) (. .)))'}, {'sentenceId': 2, 'labeledBracketing': '(ROOT (S (NP (NNS People)) (VP (VBP are) (ADJP (JJ afraid) (SBAR (IN that) (S (NP (PRP they)) (VP (MD will) (VP (VB crash))))))) (. .)))'}]), ('expressions', [{'id': 1, 'type': 'NP', 'head': 2, 'dependency': 'root', 'tokens': [1, 2]}, {'id': 2, 'type': 'NP', 'head': 5, 'dependency': 'pobj', 'tokens': [4, 5]}, {'id': 3, 'type': 'NP', 'head': 10, 'dependency': 'pobj', 'tokens': [7, 8, 9, 10]}])])})])
        assert actual == expected, actual

    def test_model_not_found(self):
        with pytest.raises(ModuleNotFoundError):
            get_model('martian_core', False, False)

    def test_validation(self):
        assert validation.is_valid(SpacyPipeline.process(text, spacy_model='en', coreferences=True))
