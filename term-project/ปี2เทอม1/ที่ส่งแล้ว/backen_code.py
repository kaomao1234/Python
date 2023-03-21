
class Lnode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Hnode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.info = {'สถานะ': 'ว่าง'}
        self.left = left
        self.right = right


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def add(self, data):
        if self.head == None:
            self.head = Lnode(data)
        else:
            self.__add__(self.head, data)

    def __add__(self, node: Lnode, data):
        if node.next == None:
            node.next = Lnode(data)
        else:
            self.__add__(node.next, data)

    def delete(self, key):
        for i in range(self.__count_node__(self.head, key)):
            if self.head.data == key:
                self.head = self.head.next
            else:
                self.__delete__(self.head, key)

    def __delete__(self, node: Lnode, key):
        # [setattr(node,'next',node.next.next) if node.next.data == key else self.__delete__(node.next,key)]
        if node.next.data == key:
            node.next = node.next.next
        else:
            self.__delete__(node.next, key)

    def display(self):
        self.__disp__(self.head)

    def __disp__(self, node):
        if node == None:
            print(None)
        else:
            print(node.data, end=' ---> ')
            self.__disp__(node.next)

    def __count_node__(self, node, key, c=0):
        if node == None:
            return c
        elif node.data == key:
            c += 1
        return self.__count_node__(node.next, key, c)

    def reset_node(self):
        self.head = None


class BinaryHeap:
    def __init__(self, head=None):
        self.head = head
        self.path_value = 0

    def way_arrow(self, plot_point=None, list_of_direct=None):#todo กำหนดเส้นทางของNode
        if plot_point == None and list_of_direct == None:
            return self.way_arrow(self.path_value, [])
        elif plot_point >= 2:
            plot_point //= 2
            list_of_direct.append(plot_point)
            return self.way_arrow(plot_point, list_of_direct)
        else:
            return list_of_direct[::-1]

    def full_stat(self, data):
        self._full_stat_(self.head,data)

    def get_node_info(self, data):
        lst = []
        self.__get_node_info__(self.head, data, lst)
        return lst[0]

    def __get_node_info__(self, node: Hnode, data, lst):
        if node != None:
            if node.data == data:
                lst.append(node.info)
            self.__get_node_info__(node.left, data, lst)
            self.__get_node_info__(node.right, data, lst)

    def insert(self, data):
        if self.head == None:
            self.head = Hnode(data)
            self.path_value += 1
        else:
            if self.search(data) == False:
                self.path_value += 1
                self.__insert__(self.head, data)
                print(data,'==>',self.way_arrow())
            else:
                print("{} is already in heap.".format(data))

    def __insert__(self, node: Hnode, data, idx=1):
        get_plot_direction = self.way_arrow()
        put_direction = self.path_value % 2
        if idx == len(get_plot_direction):
            newnode = Hnode(data)
            if node.left == None and put_direction == 0:
                node.left = newnode
            elif node.right == None and put_direction != 0:
                node.right = newnode
        else:
            if get_plot_direction[idx] % 2 == 0:
                self.__insert__(node.left, data, idx+1)
            elif get_plot_direction[idx] % 2 != 0:
                self.__insert__(node.right, data, idx+1)

    def search(self, data):
        proof = []
        self.__search__(self.head, data, proof)
        return True in proof

    def __search__(self, node, key, proof: list):
        if node != None:
            if node.data == key:
                proof.append(True)
            self.__search__(node.left, key, proof)
            self.__search__(node.right, key, proof)

    def __del_last_node__(self, node: Hnode, idx=1):
        get_plot_direction = self.way_arrow()
        if idx == len(get_plot_direction):
            temp = ''
            if node.right == None:
                temp = node.left.data
                node.left = None
            else:
                temp = node.right.data
                node.right = None
            return temp
        else:
            path_sym = get_plot_direction[idx]
            if path_sym % 2 == 0:
                return self.__del_last_node__(node.left, idx+1)
            else:
                return self.__del_last_node__(node.right, idx+1)

    def __delete(self, node, key):
        if node != None:
            if node.data == key:
                node.data = self.__del_last_node__(self.head)
            else:
                self.__delete(node.left, key)
                self.__delete(node.right, key)

    def update_info_node(self, data, info: dict):
        self._update_info_node_(self.head, data, info)

    def delete(self, key):
        self.__delete(self.head, key)

    def reset_node(self):
        self.head = None
        self.path_value = 0

    def _full_stat_(self, node, data):
        if node != None:
            if node.data == data:
                node.info['สถานะ'] = 'ไม่ว่าง'
            self._full_stat_(node.left, data)
            self._full_stat_(node.right, data)

    def _update_info_node_(self, node, data, info: dict):
        if node != None:
            if node.data == data:
                node.info.update(info)
            self._update_info_node_(node.left, data, info)
            self._update_info_node_(node.right, data, info)
obj = BinaryHeap()
for i in range(0, 10):
    obj.insert(i)
# pprint()
