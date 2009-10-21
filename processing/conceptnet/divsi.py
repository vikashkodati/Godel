import sys
sys.path.append('data/conceptnet/')
from csc.util.persist import get_picklecached_thing
from csc.conceptnet4.models import Concept
from csc.conceptnet4.analogyspace import conceptnet_2d_from_db
from csc.nl import get_nl
import csc

from utils.memoize import persistent_memoize
from utils.debug import *

def svd_loaded(function):
    def wrap(*args):
        instance = args[0]
        if instance.svd == None:
            instance.svd = instance.load_svd()

        return function(*args)
    return wrap

class DivsiHelper:
    def __init__(self):
        self.EuroNL = get_nl('en')
        
    def byFeatureTag(self, universal_sentence):
        for x in universal_sentence.features:
            tag, left, right = x
            yield {'tag':tag, 'l':left, 'r':right}
            
    def interestingTags(self, univ_sentence):
        iTags = ['_subj', '_obj', '_predadj']
        for eachTag in self.byFeatureTag(univ_sentence):
            if eachTag['tag'] in iTags:
                concept = self.Conceptable(eachTag)
                if concept:
                    yield concept
                
    def Conceptable(self, tag):
        if self.EuroNL.is_stopword(tag['l']):
            return False
        if self.EuroNL.is_stopword(tag['r']):
            return False
        if self.EuroNL.is_blacklisted(tag['l']):
            return False
        if self.EuroNL.is_blacklisted(tag['r']):
            return False

        L   = self.EuroNL.normalize(tag['l'])
        R   = self.EuroNL.normalize(tag['r'])
        Tag = self.EuroNL.normalize(tag['tag'])
        return {'l':L, 'r':R, 'tag':Tag}
    
class Divsi:
    svd = None
    def __init__(self):
        self.helper = DivsiHelper()
        self.cnet_normalized = conceptnet_2d_from_db('en').normalized()
        self.analogySpace = self.cnet_normalized.svd()
        self.EN_NL = get_nl('en')

    def load_svd(self, k=100):
        svd = self.tensor.svd(k=k)
        return svd

    
    def concept_similarity(self, universal_word):
        for interesting in self.helper.interestingTags(universal_word):
            try:
                left = self.analogySpace.weighted_u[interesting['l'],:]
                right = self.analogySpace.weighted_u[interesting['r'],:]
                similar = left.hat() * right.hat()
                debug(similar, prefix='L:%s R:%s' % (interesting['l'], interesting['r']))
            except:
                pass
            
            

            


    
    
