#!/usr/bin/env python2.7

import sys
import os

audio_dir = './ogg_files/'

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

ipa_pulmonic_consonants = {
    ('labial'   ,'bilabial'     ,'nasal'                     ):u'\u0000',
    ('labial'   ,'labio-dental' ,'nasal'                     ):u'\u0000',
    ('labial'   ,'linguo-labial','nasal'                     ):u'\u0000',
    ('labial'   ,'bilabial'     ,'stop'                      ):u'\u0000',
    ('labial'   ,'labio-dental' ,'stop'                      ):u'\u0000',
    ('labial'   ,'linguo-labial','stop'                      ):u'\u0000',
    ('labial'   ,'bilabial'     ,'sibilant-affricative'      ):u'\u0000',
    ('labial'   ,'labio-dental' ,'sibilant-affricative'      ):u'\u0000',
    ('labial'   ,'linguo-labial','sibilant-affricative'      ):u'\u0000',
    ('labial'   ,'bilabial'     ,'non-sibilant-affricative'  ):u'\u0000',
    ('labial'   ,'labio-dental' ,'non-sibilant-affricative'  ):u'\u0000',
    ('labial'   ,'linguo-labial','non-sibilant-affricative'  ):u'\u0000',
    ('labial'   ,'bilabial'     ,'approximant'               ):u'\u0000',
    ('labial'   ,'labio-dental' ,'approximant'               ):u'\u0000',
    ('labial'   ,'linguo-labial','approximant'               ):u'\u0000',
    ('labial'   ,'bilabial'     ,'flap'                      ):u'\u0000',
    ('labial'   ,'labio-dental' ,'flap'                      ):u'\u0000',
    ('labial'   ,'linguo-labial','flap'                      ):u'\u0000',
    ('labial'   ,'bilabial'     ,'trill'                     ):u'\u0000',
    ('labial'   ,'labio-dental' ,'trill'                     ):u'\u0000',
    ('labial'   ,'linguo-labial','trill'                     ):u'\u0000',
    ('labial'   ,'bilabial'     ,'lateral-affricate'         ):u'\u0000',
    ('labial'   ,'labio-dental' ,'lateral-affricate'         ):u'\u0000',
    ('labial'   ,'linguo-labial','lateral-affricate'         ):u'\u0000',
    ('labial'   ,'bilabial'     ,'lateral-fricative'         ):u'\u0000',
    ('labial'   ,'labio-dental' ,'lateral-fricative'         ):u'\u0000',
    ('labial'   ,'linguo-labial','lateral-fricative'         ):u'\u0000',
    ('labial'   ,'bilabial'     ,'lateral-approximant'       ):u'\u0000',
    ('labial'   ,'labio-dental' ,'lateral-approximant'       ):u'\u0000',
    ('labial'   ,'linguo-labial','lateral-approximant'       ):u'\u0000',
    ('labial'   ,'bilabial'     ,'lateral-flap'              ):u'\u0000',
    ('labial'   ,'labio-dental' ,'lateral-flap'              ):u'\u0000',
    ('labial'   ,'linguo-labial','lateral-flap'              ):u'\u0000',


    ('coronal'  ,'linguo-labial'  ,'nasal'                   ):u'\u0000',
    ('coronal'  ,'dental'         ,'nasal'                   ):u'\u0000',
    ('coronal'  ,'alveolar'       ,'nasal'                   ):u'\u0000',
    ('coronal'  ,'palato-alveolar','nasal'                   ):u'\u0000',
    ('coronal'  ,'retroflex'      ,'nasal'                   ):u'\u0000',
    ('coronal'  ,'alveolo-palatal','nasal'                   ):u'\u0000',
    ('coronal'  ,'linguo-labial'  ,'stop'                    ):u'\u0000',
    ('coronal'  ,'dental'         ,'stop'                    ):u'\u0000',
    ('coronal'  ,'alveolar'       ,'stop'                    ):u'\u0000',
    ('coronal'  ,'palato-alveolar','stop'                    ):u'\u0000',
    ('coronal'  ,'retroflex'      ,'stop'                    ):u'\u0000',
    ('coronal'  ,'alveolo-palatal','stop'                    ):u'\u0000',
    ('coronal'  ,'linguo-labial'  ,'sibilant-affricate'      ):u'\u0000',
    ('coronal'  ,'dental'         ,'sibilant-affricate'      ):u'\u0000',
    ('coronal'  ,'alveolar'       ,'sibilant-affricate'      ):u'\u0000',
    ('coronal'  ,'palato-alveolar','sibilant-affricate'      ):u'\u0000',
    ('coronal'  ,'retroflex'      ,'sibilant-affricate'      ):u'\u0000',
    ('coronal'  ,'alveolo-palatal','sibilant-affricate'      ):u'\u0000',
    ('coronal'  ,'linguo-labial'  ,'non-sibilant-affricate'  ):u'\u0000',
    ('coronal'  ,'dental'         ,'non-sibilant-affricate'  ):u'\u0000',
    ('coronal'  ,'alveolar'       ,'non-sibilant-affricate'  ):u'\u0000',
    ('coronal'  ,'palato-alveolar','non-sibilant-affricate'  ):u'\u0000',
    ('coronal'  ,'retroflex'      ,'non-sibilant-affricate'  ):u'\u0000',
    ('coronal'  ,'alveolo-palatal','non-sibilant-affricate'  ):u'\u0000',
    ('coronal'  ,'linguo-labial'  ,'non-sibilant-fricative'  ):u'\u0000',
    ('coronal'  ,'dental'         ,'non-sibilant-fricative'  ):u'\u0000',
    ('coronal'  ,'alveolar'       ,'non-sibilant-fricative'  ):u'\u0000',
    ('coronal'  ,'palato-alveolar','non-sibilant-fricative'  ):u'\u0000',
    ('coronal'  ,'retroflex'      ,'non-sibilant-fricative'  ):u'\u0000',
    ('coronal'  ,'alveolo-palatal','non-sibilant-fricative'  ):u'\u0000',
    ('coronal'  ,'linguo-labial'  ,'approximant'             ):u'\u0000',
    ('coronal'  ,'dental'         ,'approximant'             ):u'\u0000',
    ('coronal'  ,'alveolar'       ,'approximant'             ):u'\u0000',
    ('coronal'  ,'palato-alveolar','approximant'             ):u'\u0000',
    ('coronal'  ,'retroflex'      ,'approximant'             ):u'\u0000',
    ('coronal'  ,'alveolo-palatal','approximant'             ):u'\u0000',
    ('coronal'  ,'linguo-labial'  ,'flap'                    ):u'\u0000',
    ('coronal'  ,'dental'         ,'flap'                    ):u'\u0000',
    ('coronal'  ,'alveolar'       ,'flap'                    ):u'\u0000',
    ('coronal'  ,'palato-alveolar','flap'                    ):u'\u0000',
    ('coronal'  ,'retroflex'      ,'flap'                    ):u'\u0000',
    ('coronal'  ,'alveolo-palatal','flap'                    ):u'\u0000',
    ('coronal'  ,'linguo-labial'  ,'trill'                   ):u'\u0000',
    ('coronal'  ,'dental'         ,'trill'                   ):u'\u0000',
    ('coronal'  ,'alveolar'       ,'trill'                   ):u'\u0000',
    ('coronal'  ,'palato-alveolar','trill'                   ):u'\u0000',
    ('coronal'  ,'retroflex'      ,'trill'                   ):u'\u0000',
    ('coronal'  ,'alveolo-palatal','trill'                   ):u'\u0000',
    ('coronal'  ,'linguo-labial'  ,'lateral-affricate'       ):u'\u0000',
    ('coronal'  ,'dental'         ,'lateral-affricate'       ):u'\u0000',
    ('coronal'  ,'alveolar'       ,'lateral-affricate'       ):u'\u0000',
    ('coronal'  ,'palato-alveolar','lateral-affricate'       ):u'\u0000',
    ('coronal'  ,'retroflex'      ,'lateral-affricate'       ):u'\u0000',
    ('coronal'  ,'alveolo-palatal','lateral-affricate'       ):u'\u0000',
    ('coronal'  ,'linguo-labial'  ,'lateral-fricative'       ):u'\u0000',
    ('coronal'  ,'dental'         ,'lateral-fricative'       ):u'\u0000',
    ('coronal'  ,'alveolar'       ,'lateral-fricative'       ):u'\u0000',
    ('coronal'  ,'palato-alveolar','lateral-fricative'       ):u'\u0000',
    ('coronal'  ,'retroflex'      ,'lateral-fricative'       ):u'\u0000',
    ('coronal'  ,'alveolo-palatal','lateral-fricative'       ):u'\u0000',
    ('coronal'  ,'linguo-labial'  ,'lateral-approximant'     ):u'\u0000',
    ('coronal'  ,'dental'         ,'lateral-approximant'     ):u'\u0000',
    ('coronal'  ,'alveolar'       ,'lateral-approximant'     ):u'\u0000',
    ('coronal'  ,'palato-alveolar','lateral-approximant'     ):u'\u0000',
    ('coronal'  ,'retroflex'      ,'lateral-approximant'     ):u'\u0000',
    ('coronal'  ,'alveolo-palatal','lateral-approximant'     ):u'\u0000',
    ('coronal'  ,'linguo-labial'  ,'lateral-flap'            ):u'\u0000',
    ('coronal'  ,'dental'         ,'lateral-flap'            ):u'\u0000',
    ('coronal'  ,'alveolar'       ,'lateral-flap'            ):u'\u0000',
    ('coronal'  ,'palato-alveolar','lateral-flap'            ):u'\u0000',
    ('coronal'  ,'retroflex'      ,'lateral-flap'            ):u'\u0000',
    ('coronal'  ,'alveolo-palatal','lateral-flap'            ):u'\u0000',

    ('dorsal'   ,'alveolo-palatal','nasal'                   ):u'\u0000',
    ('dorsal'   ,'palatal'        ,'nasal'                   ):u'\u0000',
    ('dorsal'   ,'velar'          ,'nasal'                   ):u'\u0000',
    ('dorsal'   ,'uvular'         ,'nasal'                   ):u'\u0000',
    ('dorsal'   ,'alveolo-palatal','stop'                    ):u'\u0000',
    ('dorsal'   ,'palatal'        ,'stop'                    ):u'\u0000',
    ('dorsal'   ,'velar'          ,'stop'                    ):u'\u0000',
    ('dorsal'   ,'uvular'         ,'stop'                    ):u'\u0000',
    ('dorsal'   ,'alveolo-palatal','sibilant-affricative'    ):u'\u0000',
    ('dorsal'   ,'palatal'        ,'sibilant-affricative'    ):u'\u0000',
    ('dorsal'   ,'velar'          ,'sibilant-affricative'    ):u'\u0000',
    ('dorsal'   ,'uvular'         ,'sibilant-affricative'    ):u'\u0000',
    ('dorsal'   ,'alveolo-palatal','non-sibilant-affricative'):u'\u0000',
    ('dorsal'   ,'palatal'        ,'non-sibilant-affricative'):u'\u0000',
    ('dorsal'   ,'velar'          ,'non-sibilant-affricative'):u'\u0000',
    ('dorsal'   ,'uvular'         ,'non-sibilant-affricative'):u'\u0000',
    ('dorsal'   ,'alveolo-palatal','approximant'             ):u'\u0000',
    ('dorsal'   ,'palatal'        ,'approximant'             ):u'\u0000',
    ('dorsal'   ,'velar'          ,'approximant'             ):u'\u0000',
    ('dorsal'   ,'uvular'         ,'approximant'             ):u'\u0000',
    ('dorsal'   ,'alveolo-palatal','flap'                    ):u'\u0000',
    ('dorsal'   ,'palatal'        ,'flap'                    ):u'\u0000',
    ('dorsal'   ,'velar'          ,'flap'                    ):u'\u0000',
    ('dorsal'   ,'uvular'         ,'flap'                    ):u'\u0000',
    ('dorsal'   ,'alveolo-palatal','trill'                   ):u'\u0000',
    ('dorsal'   ,'palatal'        ,'trill'                   ):u'\u0000',
    ('dorsal'   ,'velar'          ,'trill'                   ):u'\u0000',
    ('dorsal'   ,'uvular'         ,'trill'                   ):u'\u0000',
    ('dorsal'   ,'alveolo-palatal','lateral-affricate'       ):u'\u0000',
    ('dorsal'   ,'palatal'        ,'lateral-affricate'       ):u'\u0000',
    ('dorsal'   ,'velar'          ,'lateral-affricate'       ):u'\u0000',
    ('dorsal'   ,'uvular'         ,'lateral-affricate'       ):u'\u0000',
    ('dorsal'   ,'alveolo-palatal','lateral-fricative'       ):u'\u0000',
    ('dorsal'   ,'palatal'        ,'lateral-fricative'       ):u'\u0000',
    ('dorsal'   ,'velar'          ,'lateral-fricative'       ):u'\u0000',
    ('dorsal'   ,'uvular'         ,'lateral-fricative'       ):u'\u0000',
    ('dorsal'   ,'alveolo-palatal','lateral-approximant'     ):u'\u0000',
    ('dorsal'   ,'palatal'        ,'lateral-approximant'     ):u'\u0000',
    ('dorsal'   ,'velar'          ,'lateral-approximant'     ):u'\u0000',
    ('dorsal'   ,'uvular'         ,'lateral-approximant'     ):u'\u0000',
    ('dorsal'   ,'alveolo-palatal','lateral-flap'            ):u'\u0000',
    ('dorsal'   ,'palatal'        ,'lateral-flap'            ):u'\u0000',
    ('dorsal'   ,'velar'          ,'lateral-flap'            ):u'\u0000',
    ('dorsal'   ,'uvular'         ,'lateral-flap'            ):u'\u0000',

    ('laryngeal','uvular'    ,'nasal'                        ):u'\u0000',
    ('laryngeal','epiglottal','nasal'                        ):u'\u0000',
    ('laryngeal','glottal'   ,'nasal'                        ):u'\u0000',
    ('laryngeal','uvular'    ,'stop'                         ):u'\u0000',
    ('laryngeal','epiglottal','stop'                         ):u'\u0000',
    ('laryngeal','glottal'   ,'stop'                         ):u'\u0000',
    ('laryngeal','uvular'    ,'sibilant-affricative'         ):u'\u0000',
    ('laryngeal','epiglottal','sibilant-affricative'         ):u'\u0000',
    ('laryngeal','glottal'   ,'sibilant-affricative'         ):u'\u0000',
    ('laryngeal','uvular'    ,'non-sibilant-affricative'     ):u'\u0000',
    ('laryngeal','epiglottal','non-sibilant-affricative'     ):u'\u0000',
    ('laryngeal','glottal'   ,'non-sibilant-affricative'     ):u'\u0000',
    ('laryngeal','uvular'    ,'approximant'                  ):u'\u0000',
    ('laryngeal','epiglottal','approximant'                  ):u'\u0000',
    ('laryngeal','glottal'   ,'approximant'                  ):u'\u0000',
    ('laryngeal','uvular'    ,'flap'                         ):u'\u0000',
    ('laryngeal','epiglottal','flap'                         ):u'\u0000',
    ('laryngeal','glottal'   ,'flap'                         ):u'\u0000',
    ('laryngeal','uvular'    ,'trill'                        ):u'\u0000',
    ('laryngeal','epiglottal','trill'                        ):u'\u0000',
    ('laryngeal','glottal'   ,'trill'                        ):u'\u0000',
    ('laryngeal','uvular'    ,'lateral-affricate'            ):u'\u0000',
    ('laryngeal','epiglottal','lateral-affricate'            ):u'\u0000',
    ('laryngeal','glottal'   ,'lateral-affricate'            ):u'\u0000',
    ('laryngeal','uvular'    ,'lateral-fricative'            ):u'\u0000',
    ('laryngeal','epiglottal','lateral-fricative'            ):u'\u0000',
    ('laryngeal','glottal'   ,'lateral-fricative'            ):u'\u0000',
    ('laryngeal','uvular'    ,'lateral-approximant'          ):u'\u0000',
    ('laryngeal','epiglottal','lateral-approximant'          ):u'\u0000',
    ('laryngeal','glottal'   ,'lateral-approximant'          ):u'\u0000',
    ('laryngeal','uvular'    ,'lateral-flap'                 ):u'\u0000',
    ('laryngeal','epiglottal','lateral-flap'                 ):u'\u0000',
    ('laryngeal','glottal'   ,'lateral-flap'                 ):u'\u0000',
}


ipa_vowels = {
    ('front'     ,'close'     ):u'\u0000',
    ('front'     ,'near-close'):u'\u0000',
    ('front'     ,'close-mid' ):u'\u0000',
    ('front'     ,'mid'       ):u'\u0000',
    ('front'     ,'open-mid'  ):u'\u0000',
    ('front'     ,'near-open' ):u'\u0000',
    ('front'     ,'open'      ):u'\u0000',

    ('near-front','close'     ):u'\u0000',
    ('near-front','near-close'):u'\u0000',
    ('near-front','close-mid' ):u'\u0000',
    ('near-front','mid'       ):u'\u0000',
    ('near-front','open-mid'  ):u'\u0000',
    ('near-front','near-open' ):u'\u0000',
    ('near-front','open'      ):u'\u0000',

    ('central'   ,'close'     ):u'\u0000',
    ('central'   ,'near-close'):u'\u0000',
    ('central'   ,'close-mid' ):u'\u0000',
    ('central'   ,'mid'       ):u'\u0000',
    ('central'   ,'open-mid'  ):u'\u0000',
    ('central'   ,'near-open' ):u'\u0000',
    ('central'   ,'open'      ):u'\u0000',

    ('near-back' ,'close'     ):u'\u0000',
    ('near-back' ,'near-close'):u'\u0000',
    ('near-back' ,'close-mid' ):u'\u0000',
    ('near-back' ,'mid'       ):u'\u0000',
    ('near-back' ,'open-mid'  ):u'\u0000',
    ('near-back' ,'near-open' ):u'\u0000',
    ('near-back' ,'open'      ):u'\u0000',

    ('back'      ,'close'     ):u'\u0000',
    ('back'      ,'near-close'):u'\u0000',
    ('back'      ,'close-mid' ):u'\u0000',
    ('back'      ,'mid'       ):u'\u0000',
    ('back'      ,'open-mid'  ):u'\u0000',
    ('back'      ,'near-open' ):u'\u0000',
    ('back'      ,'open'      ):u'\u0000',
}

#print ipa_pulmonic_consonants
#print ipa_vowels

for key in ipa_pulmonic_consonants.keys():
    #print audio_dir + key[1] + '_' + key[2] + '.ogg'
    if (os.path.isfile(audio_dir + key[1] + '_' + key[2] + '.ogg')):
        print key[1] + '_' + key[2]
for key in ipa_vowels.keys():
    #print audio_dir + key[0] + '_' + key[1] + '.ogg'
    if (os.path.isfile(audio_dir + key[0] + '_' + key[1] + '.ogg')):
        print key[0] + '_' + key[1]
    #print ipa_pulmonic_consonants[key]
#for i in range(0x0000, 0xFFFF+1):
    #print u'\u{:04x}'.format(str(i).decode('utf-8'))
   # .encode('utf-8')
