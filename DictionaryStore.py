from Properties import Properties
from FileHelper import FileHelper
from gensim import corpora, matutils


class DictionaryStory:
    def __init__(self):
        self.dictionary: corpora.Dictionary = None
        self.properties: Properties = Properties()
        self.labels = []
        self.features = []
        self.__build_dictionary()

    def __get_array_of_words(self, type: str):
        file_path = self.properties.get_data_path_of_type(type)
        text = FileHelper.read_from_file(file_path)
        return [word for word in text.split()]

    def __build_dictionary(self):
        if self.dictionary is not None:
            return

        print('build_dictionary...')
        dict_words = []

        for type in self.properties.get_types():
            arr = self.__get_array_of_words(type)
            dict_words.append(arr)

        self.dictionary = corpora.Dictionary(dict_words)

    def get_dense(self, type: str):
        words = self.__get_array_of_words(type)
        vec = self.dictionary.doc2bow(words)
        dense = list(matutils.corpus2dense([vec], num_terms=len(self.dictionary)).T[0])
        return dense

    def __build_data_set(self):
        print('__build_data_set')
        for type in self.properties.get_types():
            feature = self.get_dense(type)
            self.labels.append(type)
            self.features.append(feature)

    def get_label_and_data(self):
        self.__build_data_set()
        return self.labels, self.features