from bai1 import Node
from bai1 import Problem

table = {
    '#1': ['#2','#1','#1','#5'],
    '#2': ['#2','#3','#4','#2'],
    '#3': ['#5','#1','#6','#3'],
    '#4': ['#4','#4','#4','#6'],
    '#5': ['#5','#5','#6','#5'],
    '#6': ['#7','#6','#6','#6'],
    '#7': ['#7','#4','#7','#2']
}

def solution(node):
    solution = []
    while(True):
        if (node._parent):
            solution.append(node._status)
            node = node._parent
        else:
            solution.append(node._status)
            break
        
    return solution

def expand(node,problem):
    successors = []
    for i in problem._space[node._status]:
        n = Node(i)
        n._parent = node
        successors.append(n)
        
    return successors
    
        

def bsf(problem,initial,target):
    # hàng đợi
    fringe = []
    fringe.append(initial)
    
    # mảng các trạng thái đã xét
    closed = []
    
    while(len(fringe)):
        n = fringe.pop(0)
        
        if n in closed:
            continue
        else:
            closed.append(n)
        
            if(n._status in target):
                return solution(n)
            
            if(expand(n, problem)):
                fringe.extend(expand(n, problem))
            
    return 'No Solution'
        
    
def main():
    # vấn đề
    problem = Problem('#1', 
                      ['#7'],
                      ['a','b','c','d'],
                      ['#1','#2','#3','#4','#5','#6','#7'],
                      'BFS',
                      table)
    
    # giải quyết vấn đề bằng tìm kiếm
    if (problem._strategy == 'BFS'):
        solution = bsf(problem, Node(problem._initial), problem._target)
        solution.reverse()
        print(solution)
  
     

    #ham chuyen giai phap thanh hanh dong 
    def convert_solution_to_actions(solution):
        actions = []
        for i in range(len(solution) - 1):
            current_state = solution[i]
            next_state = solution[i + 1]
            action_index = table[current_state].index(next_state)  
            action = chr(ord('a') + action_index)
            actions.append(action)
        return actions
    
    actions = convert_solution_to_actions(solution)
    print(actions)
        

if __name__ == '__main__':
    main()
  