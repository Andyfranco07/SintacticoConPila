class Grammar:
    def __init__(self):
        self.terminals = {'var', 'int', 'float', 'string', '=', '{', '}', '(', ')', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
        self.non_terminals = {'S', 'I', 'V', 'F', 'T', 'G', 'N', 'R', 'O', 'P', 'L'}
        self.productions = {
            'S': ['I', 'V', 'F'],
            'I': ['{'],
            'V': ['var', 'T', 'G'],
            'T': ['int', 'float', 'string'],
            'G': ['N', '=', 'O'],
            'N': ['L', 'R'],
            'R': ['L', 'R', 'vacio'],
            'O': ['takeData', 'P'],
            'P': ['(', ')'],
            'F': ['}'],
            'L': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        }
