from pymongo import MongoClient
from bson.objectid import ObjectId
from flask import g


class Inventory:
    FALSY_DATA_ERROR = 'Dados inválidos! Insira dados válidos'
    NO_DATA_ERROR = 'Dados inexistentes! Preencha os campos'
    SUCESS_MESSAGE = 'Programa executado com sucesso!'

    @staticmethod
    def insert():
        pass

    @staticmethod
    def update():
        pass

    @staticmethod
    def delete():
        pass

    @staticmethod
    def get():
        pass