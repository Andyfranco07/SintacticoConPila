class PredictTable:
    def __init__(self):
        self.table = {
            'S': {
                'int': None,
                'float': None,
                'string': None,
                '{': ['I', 'V', 'F'],
                'takeData': None,
                'a...z': None,
                '(': None,
                ')': None,
                '}': None,
                '=': None
            },
            'I': {
                'int': None,
                'float': None,
                'string': None,
                '{': ['{'],
                'takeData': None,
                'a...z': None,
                '(': None,
                ')': None,
                '}': None,
                '=': None
            },
            'V': {
                'int': None,
                'float': None,
                'string': None,
                'var': ['var', 'T', 'G'],
                'takeData': None,
                '{': None,
                'a...z': None,
                '(': None,
                ')': None,
                '}': None,
                '=': None
            },
            'T': {
                'int': ['int'],
                'float': ['float'],
                'string': ['string'],
                'takeData': None,
                '{': None,
                'a...z': None,
                '(': None,
                ')': None,
                '}': None,
                '=': None
            },
            'G': {
                'int': None,
                'float': None,
                'string': None,
                'a...z': ['N', '=', 'O'],
                'takeData': None,
                '{': None,
                '(': None,
                ')': None,
                '}': None,
                '=': None
            },
            'N': {
                'int': None,
                'float': None,
                'string': None,
                'a...z': ['L', 'R'],
                'takeData': None,
                '{': None,
                '(': None,
                ')': None,
                '}': None,
                '=': None
            },
            'R': {
                'int': None,
                'float': None,
                'string': None,
                'a...z': ['L', 'R'],
                'takeData': None,
                '{': None,
                '(': None,
                ')': None,
                '}': None,
                '=': ['vacio']
            },
            'O': {
                'int': None,
                'float': None,
                'string': None,
                'takeData': ['takeData', 'P'],
                '{': None,
                'a...z': None,
                '(': None,
                ')': None,
                '}': None,
                '=': None
            },
            'P': {
                'int': None,
                'float': None,
                'string': None,
                '(': ['(', ')'],
                'takeData': None,
                '{': None,
                'a...z': None,
                ')': None,
                '}': None,
                '=': None
            },
            'F': {
                'int': None,
                'float': None,
                'string': None,
                '}': ['}'],
                'takeData': None,
                '{': None,
                'a...z': None,
                '(': None,
                ')': None,
                '=': None
            },
            'L': {
                'int': None,
                'float': None,
                'string': None,
                '{': None,
                'takeData': None,
                '(': None,
                ')': None,
                '}': None,
                'a...z': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
                '=': None
            }
        }
