# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = []
        self.elems_dict = {}

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def read_query2(self, query):
        return Query(query.split())

    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            # self.write_chain(cur for cur in reversed(self.elems)
            #             if self._hash_func(cur) == query.ind)
            if query.ind in self.elems_dict:
                self.write_chain(reversed(self.elems_dict[query.ind]))
            else:
                print('')
                
        else:
            hashValue = self._hash_func(query.s)
            foundHash = hashValue in self.elems_dict
            
            if query.type == "find":
                if foundHash:
                    tmp_list = self.elems_dict[hashValue]
                    self.write_search_result(query.s in tmp_list)
                else:
                    self.write_search_result(False)
                    
            elif query.type == 'add':
                if foundHash and query.s not in self.elems_dict[hashValue]:
                    self.elems_dict[hashValue].append(query.s)
                
                elif foundHash == False:
                    self.elems_dict[hashValue]= [query.s]
            else:
                if foundHash and query.s in self.elems_dict[hashValue]:
                    self.elems_dict[hashValue].remove(query.s)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

        # for i in range(len(test_list3)):
        #     self.process_query(self.read_query2(test_list3[i]))

if __name__ == '__main__':
    
    # test_list =[
    #     'add world',
    #     'add HellO',
    #     'check 4',
    #     'find World',
    #     'find world','del world',
    #     'check 4',
    #     'del HellO',
    #     'add luck',
    #     'add GooD',
    #     'check 2',
    #     'del good' 
    # ]

    # test_list2 = [
    #     'add test',
    #      'add test',
    #      'find test',
    #      'del test',
    #      'find test',
    #      'find Test',
    #      'add Test',
    #      'find Test' 
    # ]

    # test_list3 = [
    #     'check 0', 'find help', 'add help', 'add del', 'add add', 'find add', 'find del', 'del del', 'find del', 'check 0', 'check 1', 'check 2' 
    # ]

    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
