# -*- coding: utf-8 -*-

class Retriever(object):
    def __init__(self):
        self.data_fi = []
        self.data_se = []
        self.data_dk = []
        self.data_no = []
        self.datamap_fi = {}
        self.datamap_se = {}
        self.datamap_dk = {}
        self.datamap_no = {}


    def __index(self, suggestions):
        data = []
        datamap = {}
        suggestions = open(suggestions).readlines()
        for i in suggestions:
            i = i.strip()
            data.append(i)
            datamap[i] = i
            for e in range(len(i)):
                if i[e] == ' ':
                    data.append(i[e+1:])
                    datamap[i[e+1:]] = i
        data = list(set(data))
        return data, datamap

    def index(self, suggestions):
        self.data_fi, self.datamap_fi = self.__index('/Users/hongyusu/Codes/nova/autofill/ai/nr/data_fi')
        self.data_se, self.datamap_se = self.__index('/Users/hongyusu/Codes/nova/autofill/ai/nr/data_se')
        self.data_dk, self.datamap_dk = self.__index('/Users/hongyusu/Codes/nova/autofill/ai/nr/data_dk')
        self.data_no, self.datamap_no = self.__index('/Users/hongyusu/Codes/nova/autofill/ai/nr/data_no')


    def search(self, country, language, prefix):
        r = []
        if country == 'fi' and language == 'fi':
            for proposal in self.data_fi:
                if proposal.startswith(prefix):
                    r.append(self.datamap_fi[proposal])
        if country == 'se' and language == 'sv':
            for proposal in self.data_se:
                if proposal.startswith(prefix):
                    r.append(self.datamap_se[proposal])
        if country == 'dk' and language == 'da':
            for proposal in self.data_dk:
                if proposal.startswith(prefix):
                    r.append(self.datamap_dk[proposal])
        if country == 'no' and language == 'no':
            for proposal in self.data_no:
                if proposal.startswith(prefix):
                    r.append(self.datamap_no[proposal])

        return {'res':r}


if __name__ == '__main__':
    retriever = Retriever()
    retriever.index('')
    print(retriever.search('fi','fi','haluan nä'))
