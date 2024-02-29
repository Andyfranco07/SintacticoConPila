from grammar import Grammar
from tablita import PredictTable

class PDA:
    def __init__(self, grammar, tablita):
        self.grammar = grammar
        self.tablita = tablita

    def process_input(self, input_string):
        stack = ['$']
        input_string = input_string.replace(" ", "")  
        input_string += '$'  
        input_pointer = 0
        stack_trace = [] 

        stack.append('S')

        while True:
            X = stack[-1]  
            a = input_string[input_pointer]  
            print("Cadena de entrada:", input_string[input_pointer:]) 
            print("Pila:", stack)
            print("Símbolo en la pila (X):", X)
            print("Símbolo apuntado en la cadena (a):", a)
            stack_trace.append((input_string[input_pointer:], stack.copy()))

            if a == '$':
                print("Fin de la cadena.")
                if X == '$':
                    stack.pop() 
                    return stack_trace
                else:
                    print("Error: La cadena ha sido consumida pero la pila no está vacía.")
                    return False

            if X == 'V' and a == 'v' and input_string[input_pointer+1] == 'a' and input_string[input_pointer+2] == 'r':
                stack.pop()  
                production = self.tablita.table['V']['var']  
                if production is not None:
                    for symbol in reversed(production):
                        stack.append(symbol)
                        print("Pila:", stack)
                        
                input_pointer += 3
                stack.pop()  
                continue  

            if X == 'T' and a == 'i' and input_string[input_pointer+1] == 'n' and input_string[input_pointer+2] == 't':
                    stack.pop()  
                    production = self.tablita.table['T']['int']  
                    if production is not None:
                        for symbol in reversed(production):
                            stack.append(symbol)
                            print("Pila:", stack)
                    input_pointer += 3
                    stack.pop() 
                    continue  

            elif X == 'T' and a == 'f' and input_string[input_pointer+1] == 'l' and input_string[input_pointer+2] == 'o' and input_string[input_pointer+3] == 'a' and input_string[input_pointer+4] == 't':
                        stack.pop()  
                        production = self.tablita.table['T']['float']  
                        if production is not None:
                            for symbol in reversed(production):
                                stack.append(symbol)
                                print("Pila:", stack)
                        input_pointer += 5
                        stack.pop()  
                        continue  
                
            elif X == 'T' and a == 's' and input_string[input_pointer+1] == 't' and input_string[input_pointer+2] == 'r' and input_string[input_pointer+3] == 'i' and input_string[input_pointer+4] == 'n' and input_string[input_pointer+5] == 'g':
                        stack.pop()  
                        production = self.tablita.table['T']['string']  
                        if production is not None:
                            for symbol in reversed(production):
                                stack.append(symbol)
                                print("Pila:", stack)
                        input_pointer += 6
                        stack.pop()  
                        continue  
                
            elif X == 'O' and a == 't' and input_string[input_pointer+1] == 'a' and input_string[input_pointer+2] == 'k' and input_string[input_pointer+3] == 'e' and input_string[input_pointer+4] == 'D' and input_string[input_pointer+5] == 'a' and input_string[input_pointer+6] == 't' and input_string[input_pointer+7] == 'a':
                    stack.pop()  
                    production = self.tablita.table['O']['takeData']  
                    if production is not None:
                        for symbol in reversed(production):
                            stack.append(symbol)
                            print("Pila:", stack)
                    input_pointer += 8
                    stack.pop()  
                    continue  
            
            elif a.isalpha():
                if X == 'L':
                    if input_string[input_pointer] in self.tablita.table['L']['a...z']:
                        stack.pop() 
                        stack.append(input_string[input_pointer])
                        input_pointer += 1
                        stack.pop()
                    else:
                        return False
                else:
                    production = self.tablita.table[X]['a...z']
                    if production is not None:
                        stack.pop()
                        for symbol in reversed(production):
                            stack.append(symbol)
                    else:
                        return False
                continue  


            if X in self.grammar.terminals:
                if X == a:
                    stack.pop()
                    input_pointer += 1
                else:
                    return False  
            else:  
                production = self.tablita.table[X][a]

                if production == ['vacio']:
                    stack.pop()  
                else:
                    stack.pop()  
                    if production is not None:
                        for symbol in reversed(production):
                            stack.append(symbol)
                    else:
                        return False

    def is_valid(self, input_string):
        return self.process_input(input_string)

grammar = Grammar()
tablita = PredictTable()

pda = PDA(grammar, tablita)
