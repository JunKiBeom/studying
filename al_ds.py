from genericpath import isfile
from operator import truediv
from tkinter.tix import Tree


def linear_search(array, value):  # 정렬된 배열의 선형 검색 / O(N)
    for i in array:       # 배열의 모든 원소를 순회한다.
        if i==value:      # 원하는 값을 찾으면 반환한다.
            return value  # return i 도 가능
        elif i>value:     # 찾고 있던 값보다 큰 원소에 도달하면 루프를 일찍 종료 (정렬이 되어있기 때문)
            return None


def binaray_search(array, value):    # 이진 검색 / O(log N)
    # 찾으려는 값이 있을 수 있는 상한선과 하한선을 정한다. 최초의 상한선은 배열의 첫번째 값, 하한선은 마지막 값
    lower_bound = 0
    upper_bound = len(array) - 1

    while lower_bound <= upper_bound:
        midpoint = (upper_bound + lower_bound) / 2  # 상한선과 하한선의 중간값
        value_at_midpoint = array[midpoint]
        
        # 중간 지점의 값이 찾고 있던 값이면 검색 끝, 
        # 그렇지 않으면 더 클지 작을지 추측한 바에 따라 상한선이나 하한선을 바꾼다.
        if value < value_at_midpoint:
            upper_bound = midpoint - 1
        elif value > value_at_midpoint:
            lower_bound = midpoint + 1
        elif value == value_at_midpoint:
            return midpoint
    return None


def bubble_sort(array):  # 버블 정렬 / O(N^2)
    unsorted_until_index = len(array) - 1  # 정렬되지 않은 인덱스 기록
    sorted = False  # 배열의 정렬 여부 기록

    while not sorted:
        sorted = True  # Pass through Check
        for i in range(unsorted_until_index):
            if array[i] > array[i+1]:
                sorted = False  # 교환이 이루어지면 정렬이 안되어 있는 상태라는 것
                array[i], array[i+1] = array[i+1], array[i]
        unsorted_until_index = unsorted_until_index - 1


def hasDuplicaateeValue(array):
    # O(N^2)
    steps = 0
    for i in range(len(array)):
        for j in range (len(array)):
            steps+=1
            if i!=j and array[i] == array[j]:
                return True
    return False

    # O(N)
    '''steps = 0
    existingNumbers = []
    for i in range(len(array)):
        steps+=1
        try:
            if existingNumbers[array[i]] == None:
                pass
            else:
                return True
        except IndexError:
                existingNumbers.append(1)
    return False'''


def selection_sort(array):  # 선택 정렬 / O(N^2)
    for i in range(len(array)):
        lowestNumberIndex = i
        for j in range(len(array)):
            if (array[j] < array[lowestNumberIndex]):
                lowestNumberIndex = j
        if lowestNumberIndex!=i:
            array[i], array[lowestNumberIndex] = array[lowestNumberIndex], array[i]
    
    return array


def insertion_sort(array):  # 삽입 정렬 / O(N^2)
    for i in range(1,len(array)):
        position = i
        temp = array[i]

        while position > 0 and  array[position - 1] > temp:
            array[position] = array[position - 1]
            position = position-1
        
        array[position] = temp


# 리스트를 이용한 스택 구현
class Stack:
    def __init__(self):
        self.Stack = []

    def isEmpty(self):
        if len(self.Stack) == 0:
            return True
        else:
            return False

    def push(self, data):
        self.Stack.append(data)
        print("Push", data)

    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
            return None
        else:
            print("Pop", self.Stack[-1])
            return self.Stack.pop()

    def top(self):
        if self.isEmpty():
            print("Stack is Empty")
            return None
        else:
            print("Top", self.Stack[-1])
            return self.Stack[-1]

    def clear(self):
        self.Stack.__init__()

    def print(self):
        print(self.Stack)


# 단방향 링크드 리스트 아용한 스택 구현
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedStack:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print("Push", data)

    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
            return None
        else:
            pop = self.head.data
            self.head = self.head.next
            print("Pop", pop)
            return pop

    def top(self):
        if self.isEmpty():
            print("Stack is Empty")
            return None
        else:
            return self.head.data


# 리스트를 이용한 큐 구현
class Queue:
    def __init__(self):
        self.Queue = []

    def isEmpty(self):
        if len(self.Queue) == 0:
            return True
        else:
            return False

    def enqueue(self, data):
        print("Enqueue", data)
        self.Queue.append(data)

    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
            return None
        else:
            dequeue = self.Queue[0]
            self.Queue = self.Queue[1:]
            print("Dequeue", dequeue)
            return dequeue

    def peek(self):
        if self.isEmpty():
            print("Queue is Empty")
            return None
        else:
            peek = self.Queue[0]
            return peek


# 단방향 링킄드 리스트 이용해 큐 구현
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        if self.front is None:
            return True
        else:
            return False

    def enqueue(self, data):
        new_node = Node(data)

        if self.isEmpty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
            return None
        else:
            dequeued = self.front
            self.front = self.front.next

        if self.front is None:
            self.rear = None
        return dequeued

    def peek(self):
        if self.isEmpty():
            print("Queue is Empty")
            return None
        else:
            return self.front.data