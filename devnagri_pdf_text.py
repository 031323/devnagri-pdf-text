import re

class Font:
    def __init__(self, sncikanam):
        vidih = open(sncikanam).read()
        self.id_aksrnam = {int(s.split('"')[1]): s.split('"')[3]  for s in re.findall(r'<GlyphID id=.*/>', vidih)}
        self.aksrnam_id = {s.split('"')[3]: int(s.split('"')[1])  for s in re.findall(r'<GlyphID id=.*/>', vidih)}
        self.aksrnam_unicode = {s.split('"')[3]: chr(int(s.split('"')[1][2:], 16)) for s in re.findall(r'<map code=.*/>', vidih)}

        self.adesh_aksrnam = dict()
        for s in re.findall(r'<Substitution in=.*/>', vidih):
            for adesh in s.split('"')[3].split(','):
                self.adesh_aksrnam[adesh] = s.split('"')[1]

        self.aksrnam_dhatvh = dict()
        for s in re.findall(r'<LigatureSet.*?</LigatureSet>', vidih, re.DOTALL):
            prtmdatuh = s.split('"')[1]
            for t in re.findall(r'<Ligature components=.*/>', s):
                self.aksrnam_dhatvh[t.split('"')[3]] = [prtmdatuh] + t.split('"')[1].split(',')

        print([a for a in self.aksrnam_id.keys() if not a in self.aksrnam_unicode.keys() and not a in self.aksrnam_dhatvh.keys()])

        #self.pscimah = set([s.split('"')[1] for s in re.findall(r'<psName name=.*/>', vidih)])

    def id_unicode(self, id, prkriya = False):
        if type(id) == list:
            idn = []
            i = 0
            while i < len(id):
                j = i + 1
                #while j < len(id) and self.id_aksrnam[id[j]] in self.pscimah:
                #    idn.append(id[j])
                #    j += 1
                idn.append(id[i])
                i = j
            return ''.join([self.id_unicode(i, prkriya) for i in idn])

        aksrnam = self.id_aksrnam[id]
        if aksrnam in self.aksrnam_unicode.keys():
            if prkriya:
                print(aksrnam)
            return self.aksrnam_unicode[aksrnam]
        #if aksrnam in self.adesh_aksrnam.keys():
        #    print('adesh: ' + aksrnam + ' > ' + self.adesh_aksrnam[aksrnam])
        #    return self.id_unicode(self.aksrnam_id[self.adesh_aksrnam[aksrnam]], prkriya)
        if aksrnam in self.aksrnam_dhatvh.keys():
            if prkriya:
                print('धात॑वः ' + aksrnam + ' > ' + ' + '.join(self.aksrnam_dhatvh[aksrnam]))
            return self.id_unicode([self.aksrnam_id[datuh] for datuh in self.aksrnam_dhatvh[aksrnam]], prkriya)
        return ''