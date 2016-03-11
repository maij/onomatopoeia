#!/usr/bin/env python2.7

from audio_vars import *
from collections import namedtuple

# Creating a data type to have named values in dict.
ipa_val = namedtuple('ipa_val', 'unicode file_path')

# IPA Pulmonic consonant constructors
places              = ['labial', 'coronal', 'dorsal', 'laryngeal']
sublabial_places    = ['bilabial', 'labio-dental', 'linguo-labial']
subcoronal_places   = ['linguo-labial', 'dental', 'alveolar', 'palato-alveolar', 'retroflex', 'alveolo-palatal']
subdorsal_places    = ['alveolo-palatal', 'palatal', 'velar', 'uvular']
sublaryngeal_places = ['uvular','pharyngeal', 'epiglottal', 'glottal']

manners             = ['nasal', 'stop', 'sibilant-affricate', 'non-sibilant-affricate', 'sibilant-fricative',
                       'non-sibilant-fricative', 'approximant', 'flap', 'trill', 'lateral-affricate',
                       'lateral-fricative', 'lateral-approximant', 'lateral-flap']
# IPA Non-pulmonic consonants
simple_clicks       = []
other_clicks        = []
implosives          = []
ejectives           = []

# IPA Co-articulated consonants
continuants         = []
occlusives          = []

pulmonic_consonants = {
    ('labial'   ,'bilabial'     ,'nasal'                     ):ipa_val(u'\u006D\u0325', audio_path + 'l_b__n'   + audio_ext),
    ('labial'   ,'labio-dental' ,'nasal'                     ):ipa_val(u'\u0271\u030A'      , audio_path + 'l_ld_n'   + audio_ext),
    ('labial'   ,'linguo-labial','nasal'                     ):ipa_val(u'\u0000'      , audio_path + 'l_ll_n'   + audio_ext),
                                                                                      
    ('labial'   ,'bilabial'     ,'stop'                      ):ipa_val(u'\u0000'      , audio_path + 'l_b__s'   + audio_ext),
    ('labial'   ,'labio-dental' ,'stop'                      ):ipa_val(u'\u0000'      , audio_path + 'l_ld_s'   + audio_ext),
    ('labial'   ,'linguo-labial','stop'                      ):ipa_val(u'\u0000'      , audio_path + 'l_ll_s'   + audio_ext),
                                                                                      
    ('labial'   ,'bilabial'     ,'sibilant-affricative'      ):ipa_val(u'\u0000'      , audio_path + 'l_b__sa'  + audio_ext),
    ('labial'   ,'labio-dental' ,'sibilant-affricative'      ):ipa_val(u'\u0000'      , audio_path + 'l_ld_sa'  + audio_ext),
    ('labial'   ,'linguo-labial','sibilant-affricative'      ):ipa_val(u'\u0000'      , audio_path + 'l_ll_sa'  + audio_ext),
    ('labial'   ,'bilabial'     ,'non-sibilant-affricative'  ):ipa_val(u'\u0000'      , audio_path + 'l_b__nsa' + audio_ext),
    ('labial'   ,'labio-dental' ,'non-sibilant-affricative'  ):ipa_val(u'\u0000'      , audio_path + 'l_ld_nsa' + audio_ext),
    ('labial'   ,'linguo-labial','non-sibilant-affricative'  ):ipa_val(u'\u0000'      , audio_path + 'l_ll_nsa' + audio_ext),
    ('labial'   ,'bilabial'     ,'approximant'               ):ipa_val(u'\u0000'      , audio_path + 'l_b__a'   + audio_ext),
    ('labial'   ,'labio-dental' ,'approximant'               ):ipa_val(u'\u0000'      , audio_path + 'l_ld_a'   + audio_ext),
    ('labial'   ,'linguo-labial','approximant'               ):ipa_val(u'\u0000'      , audio_path + 'l_ll_a'   + audio_ext),
    ('labial'   ,'bilabial'     ,'flap'                      ):ipa_val(u'\u0000'      , audio_path + 'l_b__f'   + audio_ext),
    ('labial'   ,'labio-dental' ,'flap'                      ):ipa_val(u'\u0000'      , audio_path + 'l_ld_f'   + audio_ext),
    ('labial'   ,'linguo-labial','flap'                      ):ipa_val(u'\u0000'      , audio_path + 'l_ll_f'   + audio_ext),
    ('labial'   ,'bilabial'     ,'trill'                     ):ipa_val(u'\u0000'      , audio_path + 'l_b__t'   + audio_ext),
    ('labial'   ,'labio-dental' ,'trill'                     ):ipa_val(u'\u0000'      , audio_path + 'l_ld_t'   + audio_ext),
    ('labial'   ,'linguo-labial','trill'                     ):ipa_val(u'\u0000'      , audio_path + 'l_ll_t'   + audio_ext),
    ('labial'   ,'bilabial'     ,'lateral-affricate'         ):ipa_val(u'\u0000'      , audio_path + 'l_b__laf' + audio_ext),
    ('labial'   ,'labio-dental' ,'lateral-affricate'         ):ipa_val(u'\u0000'      , audio_path + 'l_ld_laf' + audio_ext),
    ('labial'   ,'linguo-labial','lateral-affricate'         ):ipa_val(u'\u0000'      , audio_path + 'l_ll_laf' + audio_ext),
    ('labial'   ,'bilabial'     ,'lateral-fricative'         ):ipa_val(u'\u0000'      , audio_path + 'l_b__lfr' + audio_ext),
    ('labial'   ,'labio-dental' ,'lateral-fricative'         ):ipa_val(u'\u0000'      , audio_path + 'l_ld_lfr' + audio_ext),
    ('labial'   ,'linguo-labial','lateral-fricative'         ):ipa_val(u'\u0000'      , audio_path + 'l_ll_lfr' + audio_ext),
    ('labial'   ,'bilabial'     ,'lateral-approximant'       ):ipa_val(u'\u0000'      , audio_path + 'l_b__lap' + audio_ext),
    ('labial'   ,'labio-dental' ,'lateral-approximant'       ):ipa_val(u'\u0000'      , audio_path + 'l_ld_lap' + audio_ext),
    ('labial'   ,'linguo-labial','lateral-approximant'       ):ipa_val(u'\u0000'      , audio_path + 'l_ll_lap' + audio_ext),
    ('labial'   ,'bilabial'     ,'lateral-flap'              ):ipa_val(u'\u0000'      , audio_path + 'l_b__lfl' + audio_ext),
    ('labial'   ,'labio-dental' ,'lateral-flap'              ):ipa_val(u'\u0000'      , audio_path + 'l_ld_lfl' + audio_ext),
    ('labial'   ,'linguo-labial','lateral-flap'              ):ipa_val(u'\u0000'      , audio_path + 'l_ll_lfl' + audio_ext),
                                                                                      
                                                                                      
    ('coronal'  ,'linguo-labial'  ,'nasal'                   ):ipa_val(u'\u0000'      , audio_path + 'l_b__sa'  + audio_ext),
    ('coronal'  ,'dental'         ,'nasal'                   ):ipa_val(u'\u0000'      , audio_path + 'l_ld_sa'  + audio_ext),
    ('coronal'  ,'alveolar'       ,'nasal'                   ):ipa_val(u'\u0000'      , audio_path + 'l_ll_sa'  + audio_ext),
    ('coronal'  ,'palato-alveolar','nasal'                   ):ipa_val(u'\u0000'      , audio_path + 'l_b__nsa' + audio_ext),
    ('coronal'  ,'retroflex'      ,'nasal'                   ):ipa_val(u'\u0000'      , audio_path + 'l_ld_nsa' + audio_ext),
    ('coronal'  ,'alveolo-palatal','nasal'                   ):ipa_val(u'\u0000'      , audio_path + 'l_ll_nsa' + audio_ext),
    ('coronal'  ,'linguo-labial'  ,'stop'                    ):ipa_val(u'\u0000'      , audio_path + 'l_b__a'   + audio_ext),
    ('coronal'  ,'dental'         ,'stop'                    ):ipa_val(u'\u0000'      , audio_path + 'l_ld_a'   + audio_ext),
    ('coronal'  ,'alveolar'       ,'stop'                    ):ipa_val(u'\u0000'      , audio_path + 'l_ll_a'   + audio_ext),
    ('coronal'  ,'palato-alveolar','stop'                    ):ipa_val(u'\u0000'      , audio_path + 'l_b__f'   + audio_ext),
    ('coronal'  ,'retroflex'      ,'stop'                    ):ipa_val(u'\u0000'      , audio_path + 'l_ld_f'   + audio_ext),
    ('coronal'  ,'alveolo-palatal','stop'                    ):ipa_val(u'\u0000'      , audio_path + 'l_ll_f'   + audio_ext),
    ('coronal'  ,'linguo-labial'  ,'sibilant-affricate'      ):ipa_val(u'\u0000'      , audio_path + 'l_b__t'   + audio_ext),
    ('coronal'  ,'dental'         ,'sibilant-affricate'      ):ipa_val(u'\u0000'      , audio_path + 'l_ld_t'   + audio_ext),
    ('coronal'  ,'alveolar'       ,'sibilant-affricate'      ):ipa_val(u'\u0000'      , audio_path + 'l_ll_t'   + audio_ext),
    ('coronal'  ,'palato-alveolar','sibilant-affricate'      ):ipa_val(u'\u0000'      , audio_path + 'l_b__laf' + audio_ext),
    ('coronal'  ,'retroflex'      ,'sibilant-affricate'      ):ipa_val(u'\u0000'      , audio_path + 'l_ld_laf' + audio_ext),
    ('coronal'  ,'alveolo-palatal','sibilant-affricate'      ):ipa_val(u'\u0000'      , audio_path + 'l_ll_laf' + audio_ext),
    ('coronal'  ,'linguo-labial'  ,'non-sibilant-affricate'  ):ipa_val(u'\u0000'      , audio_path + 'l_b__lfr' + audio_ext),
    ('coronal'  ,'dental'         ,'non-sibilant-affricate'  ):ipa_val(u'\u0000'      , audio_path + 'l_ld_lfr' + audio_ext),
    ('coronal'  ,'alveolar'       ,'non-sibilant-affricate'  ):ipa_val(u'\u0000'      , audio_path + 'l_ll_lfr' + audio_ext),
    ('coronal'  ,'palato-alveolar','non-sibilant-affricate'  ):ipa_val(u'\u0000'      , audio_path + 'l_b__lap' + audio_ext),
    ('coronal'  ,'retroflex'      ,'non-sibilant-affricate'  ):ipa_val(u'\u0000'      , audio_path + 'l_ld_lap' + audio_ext),
    ('coronal'  ,'alveolo-palatal','non-sibilant-affricate'  ):ipa_val(u'\u0000'      , audio_path + 'l_ll_lap' + audio_ext),
    ('coronal'  ,'linguo-labial'  ,'non-sibilant-fricative'  ):ipa_val(u'\u0000'      , audio_path + 'l_b__lfl' + audio_ext),
    ('coronal'  ,'dental'         ,'non-sibilant-fricative'  ):ipa_val(u'\u0000'      , audio_path + 'l_ld_lfl' + audio_ext),
    ('coronal'  ,'alveolar'       ,'non-sibilant-fricative'  ):ipa_val(u'\u0000'      , audio_path + 'l_ll_lfl' + audio_ext),
    ('coronal'  ,'palato-alveolar','non-sibilant-fricative'  ):ipa_val(u'\u0000'      , audio_path + 'l_b__sa'  + audio_ext),
    ('coronal'  ,'retroflex'      ,'non-sibilant-fricative'  ):ipa_val(u'\u0000'      , audio_path + 'l_ld_sa'  + audio_ext),
    ('coronal'  ,'alveolo-palatal','non-sibilant-fricative'  ):ipa_val(u'\u0000'      , audio_path + 'l_ll_sa'  + audio_ext),
    ('coronal'  ,'linguo-labial'  ,'approximant'             ):ipa_val(u'\u0000'      , audio_path + 'l_b__nsa' + audio_ext),
    ('coronal'  ,'dental'         ,'approximant'             ):ipa_val(u'\u0000'      , audio_path + 'l_ld_nsa' + audio_ext),
    ('coronal'  ,'alveolar'       ,'approximant'             ):ipa_val(u'\u0000'      , audio_path + 'l_ll_nsa' + audio_ext),
    ('coronal'  ,'palato-alveolar','approximant'             ):ipa_val(u'\u0000'      , audio_path + 'l_b__a'   + audio_ext),
    ('coronal'  ,'retroflex'      ,'approximant'             ):ipa_val(u'\u0000'      , audio_path + 'l_ld_a'   + audio_ext),
    ('coronal'  ,'alveolo-palatal','approximant'             ):ipa_val(u'\u0000'      , audio_path + 'l_ll_a'   + audio_ext),
    ('coronal'  ,'linguo-labial'  ,'flap'                    ):ipa_val(u'\u0000'      , audio_path + 'l_b__f'   + audio_ext),
    ('coronal'  ,'dental'         ,'flap'                    ):ipa_val(u'\u0000'      , audio_path + 'l_ld_f'   + audio_ext),
    ('coronal'  ,'alveolar'       ,'flap'                    ):ipa_val(u'\u0000'      , audio_path + 'l_ll_f'   + audio_ext),
    ('coronal'  ,'palato-alveolar','flap'                    ):ipa_val(u'\u0000'      , audio_path + 'l_b__t'   + audio_ext),
    ('coronal'  ,'retroflex'      ,'flap'                    ):ipa_val(u'\u0000'      , audio_path + 'l_ld_t'   + audio_ext),
    ('coronal'  ,'alveolo-palatal','flap'                    ):ipa_val(u'\u0000'      , audio_path + 'l_ll_t'   + audio_ext),
    ('coronal'  ,'linguo-labial'  ,'trill'                   ):ipa_val(u'\u0000'      , audio_path + 'l_b__laf' + audio_ext),
    ('coronal'  ,'dental'         ,'trill'                   ):ipa_val(u'\u0000'      , audio_path + 'l_ld_laf' + audio_ext),
    ('coronal'  ,'alveolar'       ,'trill'                   ):ipa_val(u'\u0000'      , audio_path + 'l_ll_laf' + audio_ext),
    ('coronal'  ,'palato-alveolar','trill'                   ):ipa_val(u'\u0000'      , audio_path + 'l_b__lfr' + audio_ext),
    ('coronal'  ,'retroflex'      ,'trill'                   ):ipa_val(u'\u0000'      , audio_path + 'l_ld_lfr' + audio_ext),
    ('coronal'  ,'alveolo-palatal','trill'                   ):ipa_val(u'\u0000'      , audio_path + 'l_ll_lfr' + audio_ext),
    ('coronal'  ,'linguo-labial'  ,'lateral-affricate'       ):ipa_val(u'\u0000'      , audio_path + 'l_b__lap' + audio_ext),
    ('coronal'  ,'dental'         ,'lateral-affricate'       ):ipa_val(u'\u0000'      , audio_path + 'l_ld_lap' + audio_ext),
    ('coronal'  ,'alveolar'       ,'lateral-affricate'       ):ipa_val(u'\u0000'      , audio_path + 'l_ll_lap' + audio_ext),
    ('coronal'  ,'palato-alveolar','lateral-affricate'       ):ipa_val(u'\u0000'      , audio_path + 'l_b__lfl' + audio_ext),
    ('coronal'  ,'retroflex'      ,'lateral-affricate'       ):ipa_val(u'\u0000'      , audio_path + 'l_ld_lfl' + audio_ext),
    ('coronal'  ,'alveolo-palatal','lateral-affricate'       ):ipa_val(u'\u0000'      , audio_path + 'l_ll_lfl' + audio_ext),
    ('coronal'  ,'linguo-labial'  ,'lateral-fricative'       ):ipa_val(u'\u0000'      , audio_path + 'l_b__sa'  + audio_ext),
    ('coronal'  ,'dental'         ,'lateral-fricative'       ):ipa_val(u'\u0000'      , audio_path + 'l_ld_sa'  + audio_ext),
    ('coronal'  ,'alveolar'       ,'lateral-fricative'       ):ipa_val(u'\u0000'      , audio_path + 'l_ll_sa'  + audio_ext),
    ('coronal'  ,'palato-alveolar','lateral-fricative'       ):ipa_val(u'\u0000'      , audio_path + 'l_b__nsa' + audio_ext),
    ('coronal'  ,'retroflex'      ,'lateral-fricative'       ):ipa_val(u'\u0000'      , audio_path + 'l_ld_nsa' + audio_ext),
    ('coronal'  ,'alveolo-palatal','lateral-fricative'       ):ipa_val(u'\u0000'      , audio_path + 'l_ll_nsa' + audio_ext),
    ('coronal'  ,'linguo-labial'  ,'lateral-approximant'     ):ipa_val(u'\u0000'      , audio_path + 'l_b__a'   + audio_ext),
    ('coronal'  ,'dental'         ,'lateral-approximant'     ):ipa_val(u'\u0000'      , audio_path + 'l_ld_a'   + audio_ext),
    ('coronal'  ,'alveolar'       ,'lateral-approximant'     ):ipa_val(u'\u0000'      , audio_path + 'l_ll_a'   + audio_ext),
    ('coronal'  ,'palato-alveolar','lateral-approximant'     ):ipa_val(u'\u0000'      , audio_path + 'l_b__f'   + audio_ext),
    ('coronal'  ,'retroflex'      ,'lateral-approximant'     ):ipa_val(u'\u0000'      , audio_path + 'l_ld_f'   + audio_ext),
    ('coronal'  ,'alveolo-palatal','lateral-approximant'     ):ipa_val(u'\u0000'      , audio_path + 'l_ll_f'   + audio_ext),
    ('coronal'  ,'linguo-labial'  ,'lateral-flap'            ):ipa_val(u'\u0000'      , audio_path + 'l_b__t'   + audio_ext),
    ('coronal'  ,'dental'         ,'lateral-flap'            ):ipa_val(u'\u0000'      , audio_path + 'l_ld_t'   + audio_ext),
    ('coronal'  ,'alveolar'       ,'lateral-flap'            ):ipa_val(u'\u0000'      , audio_path + 'l_ll_t'   + audio_ext),
    ('coronal'  ,'palato-alveolar','lateral-flap'            ):ipa_val(u'\u0000'      , audio_path + 'l_b__laf' + audio_ext),
    ('coronal'  ,'retroflex'      ,'lateral-flap'            ):ipa_val(u'\u0000'      , audio_path + 'l_ld_laf' + audio_ext),
    ('coronal'  ,'alveolo-palatal','lateral-flap'            ):ipa_val(u'\u0000'      , audio_path + 'l_ll_laf' + audio_ext),
                                                                                      
                                                                                      
    ('dorsal'   ,'alveolo-palatal','nasal'                   ):ipa_val(u'\u0000'      , audio_path + 'l_ll_lfr' + audio_ext),
    ('dorsal'   ,'palatal'        ,'nasal'                   ):ipa_val(u'\u0000'      , audio_path + 'l_b__lap' + audio_ext),
    ('dorsal'   ,'velar'          ,'nasal'                   ):ipa_val(u'\u0000'      , audio_path + 'l_ld_lap' + audio_ext),
    ('dorsal'   ,'uvular'         ,'nasal'                   ):ipa_val(u'\u0000'      , audio_path + 'l_ll_lap' + audio_ext),
    ('dorsal'   ,'alveolo-palatal','stop'                    ):ipa_val(u'\u0000'      , audio_path + 'l_b__lfl' + audio_ext),
    ('dorsal'   ,'palatal'        ,'stop'                    ):ipa_val(u'\u0000'      , audio_path + 'l_ld_lfl' + audio_ext),
    ('dorsal'   ,'velar'          ,'stop'                    ):ipa_val(u'\u0000'      , audio_path + 'l_ll_lfl' + audio_ext),
    ('dorsal'   ,'uvular'         ,'stop'                    ):ipa_val(u'\u0000'      , audio_path + 'l_ll_lfr' + audio_ext),
    ('dorsal'   ,'alveolo-palatal','sibilant-affricative'    ):ipa_val(u'\u0000'      , audio_path + 'l_b__lap' + audio_ext),
    ('dorsal'   ,'palatal'        ,'sibilant-affricative'    ):ipa_val(u'\u0000'      , audio_path + 'l_ld_lap' + audio_ext),
    ('dorsal'   ,'velar'          ,'sibilant-affricative'    ):ipa_val(u'\u0000'      , audio_path + 'l_ll_lap' + audio_ext),
    ('dorsal'   ,'uvular'         ,'sibilant-affricative'    ):ipa_val(u'\u0000'      , audio_path + 'l_b__lfl' + audio_ext),
    ('dorsal'   ,'alveolo-palatal','non-sibilant-affricative'):ipa_val(u'\u0000'      , audio_path + 'l_ld_lfl' + audio_ext),
    ('dorsal'   ,'palatal'        ,'non-sibilant-affricative'):ipa_val(u'\u0000'      , audio_path + 'l_ll_lfl' + audio_ext),
    ('dorsal'   ,'velar'          ,'non-sibilant-affricative'):ipa_val(u'\u0000'      , audio_path + 'l_ll_lfr' + audio_ext),
    ('dorsal'   ,'uvular'         ,'non-sibilant-affricative'):ipa_val(u'\u0000'      , audio_path + 'l_b__lap' + audio_ext),
    ('dorsal'   ,'alveolo-palatal','approximant'             ):ipa_val(u'\u0000'      , audio_path + 'l_ld_lap' + audio_ext),
    ('dorsal'   ,'palatal'        ,'approximant'             ):ipa_val(u'\u0000'      , audio_path + 'l_ll_lap' + audio_ext),
    ('dorsal'   ,'velar'          ,'approximant'             ):ipa_val(u'\u0000'      , audio_path + 'l_b__lfl' + audio_ext),
    ('dorsal'   ,'uvular'         ,'approximant'             ):ipa_val(u'\u0000'      , audio_path + 'l_ld_lfl' + audio_ext),
    ('dorsal'   ,'alveolo-palatal','flap'                    ):ipa_val(u'\u0000'      , audio_path + 'l_ll_lfl' + audio_ext),
    ('dorsal'   ,'palatal'        ,'flap'                    ):ipa_val(u'\u0000'      , audio_path + 'l_ll_lfr' + audio_ext),
    ('dorsal'   ,'velar'          ,'flap'                    ):ipa_val(u'\u0000'      , audio_path + 'l_b__lap' + audio_ext),
    ('dorsal'   ,'uvular'         ,'flap'                    ):ipa_val(u'\u0000'      , audio_path + 'l_ld_lap' + audio_ext),
    ('dorsal'   ,'alveolo-palatal','trill'                   ):ipa_val(u'\u0000'      , audio_path + 'l_ll_lap' + audio_ext),
    ('dorsal'   ,'palatal'        ,'trill'                   ):ipa_val(u'\u0000'      , audio_path + 'l_b__lfl' + audio_ext),
    ('dorsal'   ,'velar'          ,'trill'                   ):ipa_val(u'\u0000'      , audio_path + 'l_ld_lfl' + audio_ext),
    ('dorsal'   ,'uvular'         ,'trill'                   ):ipa_val(u'\u0000'      , audio_path + 'l_ll_lfl' + audio_ext),
    ('dorsal'   ,'alveolo-palatal','lateral-affricate'       ):ipa_val(u'\u0000'      , audio_path + 'l_ll_lfr' + audio_ext),
    ('dorsal'   ,'palatal'        ,'lateral-affricate'       ):ipa_val(u'\u0000'      , audio_path + 'l_b__lap' + audio_ext),
    ('dorsal'   ,'velar'          ,'lateral-affricate'       ):ipa_val(u'\u0000'      , audio_path + 'l_ld_lap' + audio_ext),
    ('dorsal'   ,'uvular'         ,'lateral-affricate'       ):ipa_val(u'\u0000'      , audio_path + 'l_ll_lap' + audio_ext),
    ('dorsal'   ,'alveolo-palatal','lateral-fricative'       ):ipa_val(u'\u0000'      , audio_path + 'l_b__lfl' + audio_ext),
    ('dorsal'   ,'palatal'        ,'lateral-fricative'       ):ipa_val(u'\u0000'      , audio_path + 'l_ld_lfl' + audio_ext),
    ('dorsal'   ,'velar'          ,'lateral-fricative'       ):ipa_val(u'\u0000'      , audio_path + 'l_ll_lfl' + audio_ext),
    ('dorsal'   ,'uvular'         ,'lateral-fricative'       ):ipa_val(u'\u0000'      , audio_path + 'l_ll_lfr' + audio_ext),
    ('dorsal'   ,'alveolo-palatal','lateral-approximant'     ):ipa_val(u'\u0000'      , audio_path + 'l_b__lap' + audio_ext),
    ('dorsal'   ,'palatal'        ,'lateral-approximant'     ):ipa_val(u'\u0000'      , audio_path + 'l_ld_lap' + audio_ext),
    ('dorsal'   ,'velar'          ,'lateral-approximant'     ):ipa_val(u'\u0000'      , audio_path + 'l_ll_lap' + audio_ext),
    ('dorsal'   ,'uvular'         ,'lateral-approximant'     ):ipa_val(u'\u0000'      , audio_path + 'l_b__lfl' + audio_ext),
    ('dorsal'   ,'alveolo-palatal','lateral-flap'            ):ipa_val(u'\u0000'      , audio_path + 'l_ld_lfl' + audio_ext),
    ('dorsal'   ,'palatal'        ,'lateral-flap'            ):ipa_val(u'\u0000'      , audio_path + 'l_ll_lfl' + audio_ext),
    ('dorsal'   ,'velar'          ,'lateral-flap'            ):ipa_val(u'\u0000'      , audio_path + 'l_ld_lfl' + audio_ext),
    ('dorsal'   ,'uvular'         ,'lateral-flap'            ):ipa_val(u'\u0000'      , audio_path + 'l_ll_lfl' + audio_ext),
                                                                                      
                                                                                      
    ('laryngeal','uvular'    ,'nasal'                        ):ipa_val(u'\u0000'      , audio_path + 'l_ll_lfr' + audio_ext),
    ('laryngeal','epiglottal','nasal'                        ):ipa_val(u'\u0000'      , audio_path + 'l_b__lap' + audio_ext),
    ('laryngeal','glottal'   ,'nasal'                        ):ipa_val(u'\u0000'      , audio_path + 'l_ld_lap' + audio_ext),
    ('laryngeal','uvular'    ,'stop'                         ):ipa_val(u'\u0000'      , audio_path + 'l_ll_lap' + audio_ext),
    ('laryngeal','epiglottal','stop'                         ):ipa_val(u'\u0000'      , audio_path + 'l_b__lfl' + audio_ext),
    ('laryngeal','glottal'   ,'stop'                         ):ipa_val(u'\u0000'      , audio_path + 'l_ld_lfl' + audio_ext),
    ('laryngeal','uvular'    ,'sibilant-affricative'         ):ipa_val(u'\u0000'      , audio_path + 'l_ll_lfl' + audio_ext),
    ('laryngeal','epiglottal','sibilant-affricative'         ):ipa_val(u'\u0000'      , audio_path + 'l_ll_lfr' + audio_ext),
    ('laryngeal','glottal'   ,'sibilant-affricative'         ):ipa_val(u'\u0000'      , audio_path + 'l_b__lap' + audio_ext),
    ('laryngeal','uvular'    ,'non-sibilant-affricative'     ):ipa_val(u'\u0000'      , audio_path + 'l_ld_lap' + audio_ext),
    ('laryngeal','epiglottal','non-sibilant-affricative'     ):ipa_val(u'\u0000'      , audio_path + 'l_ll_lap' + audio_ext),
    ('laryngeal','glottal'   ,'non-sibilant-affricative'     ):ipa_val(u'\u0000'      , audio_path + 'l_b__lfl' + audio_ext),
    ('laryngeal','uvular'    ,'approximant'                  ):ipa_val(u'\u0000'      , audio_path + 'l_ld_lfl' + audio_ext),
    ('laryngeal','epiglottal','approximant'                  ):ipa_val(u'\u0000'      , audio_path + 'l_ll_lfl' + audio_ext),
    ('laryngeal','glottal'   ,'approximant'                  ):ipa_val(u'\u0000'      , audio_path + 'l_ll_lfr' + audio_ext),
    ('laryngeal','uvular'    ,'flap'                         ):ipa_val(u'\u0000'      , audio_path + 'l_b__lap' + audio_ext),
    ('laryngeal','epiglottal','flap'                         ):ipa_val(u'\u0000'      , audio_path + 'l_ld_lap' + audio_ext),
    ('laryngeal','glottal'   ,'flap'                         ):ipa_val(u'\u0000'      , audio_path + 'l_ll_lap' + audio_ext),
    ('laryngeal','uvular'    ,'trill'                        ):ipa_val(u'\u0000'      , audio_path + 'l_b__lfl' + audio_ext),
    ('laryngeal','epiglottal','trill'                        ):ipa_val(u'\u0000'      , audio_path + 'l_ld_lfl' + audio_ext),
    ('laryngeal','glottal'   ,'trill'                        ):ipa_val(u'\u0000'      , audio_path + 'l_ll_lfl' + audio_ext),
    ('laryngeal','uvular'    ,'lateral-affricate'            ):ipa_val(u'\u0000'      , audio_path + 'l_ll_lfr' + audio_ext),
    ('laryngeal','epiglottal','lateral-affricate'            ):ipa_val(u'\u0000'      , audio_path + 'l_b__lap' + audio_ext),
    ('laryngeal','glottal'   ,'lateral-affricate'            ):ipa_val(u'\u0000'      , audio_path + 'l_ld_lap' + audio_ext),
    ('laryngeal','uvular'    ,'lateral-fricative'            ):ipa_val(u'\u0000'      , audio_path + 'l_ll_lap' + audio_ext),
    ('laryngeal','epiglottal','lateral-fricative'            ):ipa_val(u'\u0000'      , audio_path + 'l_b__lfl' + audio_ext),
    ('laryngeal','glottal'   ,'lateral-fricative'            ):ipa_val(u'\u0000'      , audio_path + 'l_ld_lfl' + audio_ext),
    ('laryngeal','uvular'    ,'lateral-approximant'          ):ipa_val(u'\u0000'      , audio_path + 'l_ll_lfl' + audio_ext),
    ('laryngeal','epiglottal','lateral-approximant'          ):ipa_val(u'\u0000'      , audio_path + 'l_ll_lfr' + audio_ext),
    ('laryngeal','glottal'   ,'lateral-approximant'          ):ipa_val(u'\u0000'      , audio_path + 'l_b__lap' + audio_ext),
    ('laryngeal','uvular'    ,'lateral-flap'                 ):ipa_val(u'\u0000'      , audio_path + 'l_ld_lap' + audio_ext),
    ('laryngeal','epiglottal','lateral-flap'                 ):ipa_val(u'\u0000'      , audio_path + 'l_ll_lap' + audio_ext),
    ('laryngeal','glottal'   ,'lateral-flap'                 ):ipa_val(u'\u0000'      , audio_path + 'l_b__lfl' + audio_ext)
}


vowels = {
    ('front'     ,'close'     ):ipa_val(u'\u0000', audio_path + 'v_f_c' + audio_ext),
    ('front'     ,'near-close'):ipa_val(u'\u0000', audio_path + 'v_f_nc' + audio_ext),
    ('front'     ,'close-mid' ):ipa_val(u'\u0000', audio_path + 'v_f_cm' + audio_ext),
    ('front'     ,'mid'       ):ipa_val(u'\u0000', audio_path + 'v_f_m' + audio_ext),
    ('front'     ,'open-mid'  ):ipa_val(u'\u0000', audio_path + 'v_f_om' + audio_ext),
    ('front'     ,'near-open' ):ipa_val(u'\u0000', audio_path + 'v_f_no' + audio_ext),
    ('front'     ,'open'      ):ipa_val(u'\u0000', audio_path + 'v_f_o' + audio_ext),

    ('near-front','close'     ):ipa_val(u'\u0000', audio_path + 'l_ld_lfl' + audio_ext),
    ('near-front','near-close'):ipa_val(u'\u0000', audio_path + 'l_ll_lfl' + audio_ext),
    ('near-front','close-mid' ):ipa_val(u'\u0000', audio_path + 'l_ld_lfl' + audio_ext),
    ('near-front','mid'       ):ipa_val(u'\u0000', audio_path + 'l_ld_lfl' + audio_ext),
    ('near-front','open-mid'  ):ipa_val(u'\u0000', audio_path + 'l_ld_lfl' + audio_ext),
    ('near-front','near-open' ):ipa_val(u'\u0000', audio_path + 'l_ld_lfl' + audio_ext),
    ('near-front','open'      ):ipa_val(u'\u0000', audio_path + 'l_ld_lfl' + audio_ext),

    ('central'   ,'close'     ):ipa_val(u'\u0000', audio_path + 'l_ld_lfl' + audio_ext),
    ('central'   ,'near-close'):ipa_val(u'\u0000', audio_path + 'l_ld_lfl' + audio_ext),
    ('central'   ,'close-mid' ):ipa_val(u'\u0000', audio_path + 'l_ld_lfl' + audio_ext),
    ('central'   ,'mid'       ):ipa_val(u'\u0000', audio_path + 'l_ld_lfl' + audio_ext),
    ('central'   ,'open-mid'  ):ipa_val(u'\u0000', audio_path + 'l_ld_lfl' + audio_ext),
    ('central'   ,'near-open' ):ipa_val(u'\u0000', audio_path + 'l_ld_lfl' + audio_ext),
    ('central'   ,'open'      ):ipa_val(u'\u0000', audio_path + 'l_ld_lfl' + audio_ext),

    ('near-back' ,'close'     ):ipa_val(u'\u0000', audio_path + 'l_ld_lfl' + audio_ext),
    ('near-back' ,'near-close'):ipa_val(u'\u0000', audio_path + 'l_ld_lfl' + audio_ext),
    ('near-back' ,'close-mid' ):ipa_val(u'\u0000', audio_path + 'l_ld_lfl' + audio_ext),
    ('near-back' ,'mid'       ):ipa_val(u'\u0000', audio_path + 'l_ld_lfl' + audio_ext),
    ('near-back' ,'open-mid'  ):ipa_val(u'\u0000', audio_path + 'l_ld_lfl' + audio_ext),
    ('near-back' ,'near-open' ):ipa_val(u'\u0000', audio_path + 'l_ld_lfl' + audio_ext),
    ('near-back' ,'open'      ):ipa_val(u'\u0000', audio_path + 'l_ld_lfl' + audio_ext),

    ('back'      ,'close'     ):ipa_val(u'\u0000', audio_path + 'l_ld_lfl' + audio_ext),
    ('back'      ,'near-close'):ipa_val(u'\u0000', audio_path + 'l_ld_lfl' + audio_ext),
    ('back'      ,'close-mid' ):ipa_val(u'\u0000', audio_path + 'l_ld_lfl' + audio_ext),
    ('back'      ,'mid'       ):ipa_val(u'\u0000', audio_path + 'l_ld_lfl' + audio_ext),
    ('back'      ,'open-mid'  ):ipa_val(u'\u0000', audio_path + 'l_ld_lfl' + audio_ext),
    ('back'      ,'near-open' ):ipa_val(u'\u0000', audio_path + 'l_ld_lfl' + audio_ext),
    ('back'      ,'open'      ):ipa_val(u'\u0000', audio_path + 'l_ld_lfl' + audio_ext),
}


print('Using IPA_primitives.')
#ipa_temp = ipa_val(u'\u0000', 'this is a string')
#print(ipa_temp)
#print(ipa_temp[1])
for key in pulmonic_consonants.keys():
    print("{key} => {char}".format(key=key, char=pulmonic_consonants[key][0]))
    #print(key + ' => ' + pulmonic_consonants[key])[1])
