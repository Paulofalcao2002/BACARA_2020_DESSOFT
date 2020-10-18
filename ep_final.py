# EP - Design de Software
# Equipe: Lorena Budin e Paulo Falcão
# Data: 18/10/2020

import random
import os

#dicionário contendo o baralho original
baralho = {"A de espadas": 1, "A de copas": 1, "A de paus": 1, "A de ouros": 1,
                  "2 de espadas": 2, "2 de copas": 2, "2 de paus": 2, "2 de ouros": 2,
                  "3 de espadas": 3, "3 de copas": 3, "3 de paus": 3, "3 de ouros": 3,
                  "4 de espadas": 4, "4 de copas": 4, "4 de paus": 4, "4 de ouros": 4,
                  "5 de espadas": 5, "5 de copas": 5, "5 de paus": 5, "5 de ouros": 5,
                  "6 de espadas": 6, "6 de copas": 6, "6 de paus": 6, "6 de ouros": 6,
                  "7 de espadas": 7, "7 de copas": 7, "7 de paus": 7, "7 de ouros": 7,
                  "8 de espadas": 8, "8 de copas": 8, "8 de paus": 8, "8 de ouros": 8,
                  "9 de espadas": 9, "9 de copas": 9, "9 de paus": 9, "9 de ouros": 9,
                  "10 de espadas": 10, "10 de copas": 10, "10 de paus": 10, "10 de ouros": 10,
                  "Rainha de espadas": 0, "Rainha de copas": 0, "Rainha de paus": 0, "Rainha de ouros": 0,
                  "Valete de espadas": 0, "Valete de copas": 0, "Valete de paus": 0, "Valete de ouros": 0,
                  "Rei de espadas": 0, "Rei de copas": 0, "Rei de paus": 0, "Rei de ouros": 0}