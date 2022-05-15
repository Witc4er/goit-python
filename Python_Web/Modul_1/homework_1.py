import json
import pickle
from abc import ABCMeta, abstractmethod


class SerializationInterface(metaclass=ABCMeta):

    @abstractmethod
    def read_file(self, path_file):
        """Retrieve data from the input source"""
        return

    @abstractmethod
    def write_file(self, data, path_file):
        """Save data object to the output"""
        return


class SerializationJson(SerializationInterface):

    def read_file(self, path_file):
        return json.load(path_file)

    def write_file(self, data, path_file):
        return json.dump(data, path_file)


class SerializationBin(SerializationInterface):

    def read_file(self, path_file):
        return pickle.load(path_file)

    def write_file(self, data, path_file):
        return pickle.dump(data, path_file)


if __name__ == '__main__':
    SerializationBin()