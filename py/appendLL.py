
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
#construtor da linkedList
class LinkedList:
    def __init__(self, value):
        #crio o nó inicial
        new_node = Node(value)
        #defino a head, como o nó criado
        self.head = new_node
        #defino a tail, como o nó criado
        self.tail = new_node
        #defino o comprimento da lista
        self.length = 1
#função de imprimir
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
#função de append
    def append(self, value):
        new_node = Node(value)
        #caso não existe nós
        if self.head is None:
            self.tail = new_node
            self.head = new_node
        else:
            #se existirem nós, o novo nó adicionado é Tail
            #o ponteiro de tail é o novo nó
            self.tail.next = new_node
            #como temos o ponteiro no novo nó, podemos defini-lo como Tail
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        #se o comprimento for 0 ou a head foi nenhuma inicialmente
        if self.length == 0 or self.head == None:
            return None

        #temp = variavel que vai até a tail
        temp = self.head
        #pre = variavel que ficará 1 "atras" permitindo segurar outros ponteiros
        pre = self.head

        #se temp tiver um nó apos ele
        while temp.next is not None:
            #pre é temp
            pre = temp
            #temp é o nó na frente dele
            temp = temp.next
            #dessa forma, podemos fazer com que pre fique sempre 1 atras de temp
        #self é a variavel pre, que é o penultimo item da lista
        self.tail = pre
        #e o elemento depois de pre, é None, excluindo o ponteiro, logo, perdendo o nó
        self.tail.next = None
        #Decrementar o comprimento!
        self.length -= 1

        #se o comprimento for 0, apos tentaremos o Loop
        if self.length == 0:
            self.head = None
            self.tail = None

        return temp

    def prepend(self, value):
        #cria novo nó com o valor
        new_node = Node(value)
        #pergunta se temos pelo menos 1 no, se não, aponta head e tail, para o nó novo
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        #se temos mais de 1 ano
        else:
            #aponta o ponteiro do novo nó pra head
            new_node.next = self.head
            #aponta head pro novo nó, tornando ele o começo da lista
            self.head = new_node
        #AUMENTE O TAMANHO DA LISTA
        self.length += 1
        return True   

    def popfirst(self):
        if self.length == 0:
            return None
        #precisamos segurar o node para exclui-lo
        temp = self.head
        #apontamos a head para o proximo nó, usando o ponteiro 
        self.head = self.head.next
        #excluimos o ponteiro que conectava o nó na lista que queriamos excluir apartir do .next do temp
        temp.next = None
        #Diminui o tamanho da lista
        self.length -= 1
        if self.length == 0:
            temp = self.head
            self.tail = None
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        # if index < 0 or index > self.length:
        #     return None
        # temp = self.head
        # for _ in range(index):
        #     temp = temp.next
        # temp.value = value
        # return True
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append()
        
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.popfirst()
        if index == self.length:
            return self.pop()
        
        prev = self.get(index - 1)
        temp = prev.next
        #Não usar funções para ponteiros acessaveis, isso aumenta MUITO a eficiencia do codigo
        
        prev.next = temp.next
        temp.next = None
        self.length+=1
        return temp

    def reverse(self):
        prev = None
        temp = self.head
        after = temp.next
        for _ in range(self.length):
            #after deve estar sempre 1 a frente de temp
            after = temp.next
            #temp deve apontar para o de tras
            temp.next = prev
            #o de tras deve seguir temp
            prev = temp
            #temp deve se tornar o da frente(after)
            temp = after


my_linked_list = LinkedList(0)

my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)


print(my_linked_list.get(2))
my_linked_list.set_value(2, 10)
print(my_linked_list.get(2))