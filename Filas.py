# Nó da Fila
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Fila
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

# Inclusão de elementos na fila    
    def enqueue (self, value):
        new_node = Node (value)

        if self.front == None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

# Remoção de elementos na fila
    def dequeue (self):
        if self.front == None:
            raise Exception ("Queue is empty")
        temp = self.front
        self.front = self.front.next
        if self.front == None:
            self.rear = None
            return temp.value

# Acessa o primeiro elemento da fila
    def peek (self):
        if self.front == None:
            raise Exception ("Queue is empty")
        return self.front.value

#Verifica se a fila está vazia (este teste deve ser feito após os outros testas das filas)
    def is_empty (self):
        return self.front == None

# Exibe a fila
    def display_queue (self):
        current = self.front
        while current != None:
            print (current.value, end="")
            current = current.next

# Teste da fila
q = Queue ()

q.enqueue (10)
q.enqueue (20)
q.enqueue (30)
q.enqueue (40)

# Exibe a fila
# q.display_queue ()

q.display_queue ()

q.peek ()

q.dequeue ()

q.is_empty ()

# Preciso aprender como fazer o teste por meio de inserção de células ou não conseguirei testar a fila
# como faço para inserir células no Python?
# Simples(basta criar um código com extensão ipynb)