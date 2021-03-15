from knowledge_base import *


class LogicalAgent():

    def __init__(self, KB):
        self.KB = KB

    # TODO
    def bottom_up(self):
        ''' Implements the botton up proof strategy and returns all the logical consequence odf the KB
        Returns:
            A list with all the logical consequences of KB
        '''
        logical_list = []

        for ask in self.KB.askables:
            if ask not in logical_list:
                x = True if input(f'Is {ask.atom} true (y or n)? ') == 'y' else False

                if x:
                    logical_list.append(ask.atom)

        while True:
            select = False
            for clause in self.KB.clauses:
                if clause.head not in logical_list and (all(map(lambda x: x in logical_list, clause.body))):
                    logical_list.append(clause.head)
                    select = True
            if select == False:
                break
        return logical_list

    # TODO
    def top_down(self, query):
        '''Implements the top down proof strategy. Given a query (the atom that it wants to prove)
        it returns True if the query is a consequence of the knowledge base.
        Args:
            querry: The atom that should be proved
        Returns:
            True if the query is a logical consequence of KB, False otherwise
        '''
        to_prove = query

        while to_prove != []:
            findClause = False

            for statement in self.KB.statements:
                if isinstance(statement, Clause):
                    if statement.head == to_prove[0]:
                        to_prove.pop(0)
                        to_prove = statement.body + to_prove
                        findClause = True
                        break

                if isinstance(statement, Askable):
                    if statement.atom == to_prove[0]:
                        x = True if input(f'atom {statement.atom} is true (y or n)? ') == 'y' else False
                        if x:
                            to_prove.pop(0)
                            findClause = True
                            break

            if findClause == False:
                return False

        return True

    # TODO
    def explain(self, g):
        '''Implements the process of abductions. It tries to explain the atoms  in the list g using
         the assumable in KB.
        Args:
            g: A set of atoms that should be explained
        Returns:
            A list of explanation for the atoms in g
        '''


        explanation_list = []
        for statement in self.KB.statements:
            if isinstance(statement, Assumable):
                explanation_list.append((statement.atom, [statement.atom]))
        for clause in self.KB.clauses:
            if all(map(lambda x: (x, ...) in explanation_list, clause.body)):
                explanation_list.append((clause.head, [x[1] for x in explanation_list if x[0] in clause.body]))

        return explanation_list