from knowledge_base import Clause, Askable, KB

class LogicalAgent():

    def __init__(self,KB: KB):
        self.KB = KB

    def bottom_up(self):
        ''' Implements the botton up proof strategy and returns all the logical consequence odf the KB
        Returns:
            A list with all the logical consequences of KB
        '''
        consequences = [] # logical consequences

        clause = self.select_clause(consequences)
        while clause is not None:
            consequences.append(clause)
            clause = self.select_clause(consequences)

        return consequences

    
    def select_clause(self, consequences):
        for st in self.KB.statements:
            if st.head in consequences:
                continue

            if isinstance(st, Askable):
                if not st.answered and st.ask():
                    return st.head
            
            else:
                if all([atom in consequences for atom in st.body]):
                    return st.head


    def top_down(self,query):
        '''Implements the top down proof strategy. Given a query (the atom that it wants to prove) 
        it returns True if the query is a consequence of the knowledge base. 
        
        Args:
            querry: The atom that should be proved
        Returns: 
            True if the query is a logical consequence of KB, False otherwise
        '''
        
        pass
    
    # TODO
    def explain(self,g):
        '''Implements the process of abductions. It tries to explain the atoms  in the list g using
         the assumable in KB.
        Args:
            g: A set of atoms that should be explained
        
        Returns:
            A list of explanation for the atoms in g
        '''
        pass