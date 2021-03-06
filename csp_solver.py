import copy

backtrack_counter = 0
failure_counter = 0
def backtracking_search(csp):
    backtrack_counter = 0
    """This functions starts the CSP solver and returns the found
    solution.
    """
    # Make a so-called "deep copy" of the dictionary containing the
    # domains of the CSP variables. The deep copy is required to
    # ensure that any changes made to 'assignment' does not have any
    # side effects elsewhere.
    assignment = copy.deepcopy(csp.domains)

    # Run AC-3 on all constraints in the CSP, to weed out all of the
    # values that are not arc-consistent to begin with
    ac_3(csp, assignment, csp.get_all_arcs())
    # Call backtrack with the partial assignment 'assignment'
    return backtrack(csp, assignment)



def backtrack(csp, assignment):
    global backtrack_counter
    global failure_counter
    backtrack_counter += 1

    """The function 'Backtrack' from the pseudocode in the
    textbook.

    The function is called recursively, with a partial assignment of
    values 'assignment'. 'assignment' is a dictionary that contains
    a list of all legal values for the variables that have *not* yet
    been decided, and a list of only a single value for the
    variables that *have* been decided.

    When all of the variables in 'assignment' have lists of length
    one, i.e. when all variables have been assigned a value, the
    function should return 'assignment'. Otherwise, the search
    should continue. When the function 'inference' is called to run
    the AC-3 algorithm, the lists of legal values in 'assignment'
    should get reduced as AC-3 discovers illegal values.

    IMPORTANT: For every iteration of the for-loop in the
    pseudocode, you need to make a deep copy of 'assignment' into a
    new variable before changing it. Every iteration of the for-loop
    should have a clean slate and not see any traces of the old
    assignments and inferences that took place in previous
    iterations of the loop.
    """

    #First checking if we have a solution
    if isSolution(assignment):
        print("Calls to backtrack:", backtrack_counter)
        print("Search returned a failure:", failure_counter, "times")
        return assignment

    #Selecting a variable to assign a value
    variable = select_unassigned_variable(csp, assignment)

    #The search begins
    for value in assignment[variable]:
        temp = assignment                                   #Making sure we kan "undo" our choices if the search needs to backtrack
        assignment = copy.deepcopy(assignment)              #Copying to make sure backtracking is proper
        assignment[variable] = [value]                      #Assigning the choosen variable with the first value in its domain
        if(ac_3(csp, assignment, csp.get_all_arcs())):      #Using ac-3 algorithm to make the search faster
            result = backtrack(csp, assignment)             #Going deeper in the search tree
            if result is not None:                          #Have we reached a dead end?
                return result

        assignment = temp                                   #We have to backtrack

    failure_counter += 1
    return None



#Simple checker to see if we have a solution
def isSolution(assignment):
    if assignment is None:
        return False
    return all(len(value) == 1 for value in assignment.values())


def select_unassigned_variable(csp, assignment):
    """The function 'Select-Unassigned-Variable' from the pseudocode
    in the textbook. Should return the name of one of the variables
    in 'assignment' that have not yet been decided, i.e. whose list
    of legal values has a length greater than one.
    """
    for variable in csp.variables:
        if len(assignment[variable]) > 1:
            return variable



def ac_3(csp, assignment, arcs):
    """The function 'AC-3' from the pseudocode in the textbook.
    'assignment' is the current partial assignment, that contains
    the lists of legal values for each undecided variable. 'queue'
    is the initial queue of arcs that should be visited.
    """
    arc_queue = arcs

    while arc_queue:
        current_arc = arc_queue.pop(0)
        from_node = current_arc[0]
        to_node = current_arc[1]
        if revise(csp ,assignment, from_node, to_node):
            if len(assignment[from_node]) == 0: #There is no possible solution within this domain
                return False

            #If we did a change to currents domain, we need to look at all the arcs from that node again
            for neigbour_node in csp.get_all_neighboring_arcs(from_node):
                if neigbour_node[0] != to_node:
                    arc_queue.append((neigbour_node[0],from_node))

    return True

def revise(csp, assignment, i, j):
    """The function 'Revise' from the pseudocode in the textbook.
    'assignment' is the current partial assignment, that contains
    the lists of legal values for each undecided variable. 'i' and
    'j' specifies the arc that should be visited. If a value is
    found in variable i's domain that doesn't satisfy the constraint
    between i and j, the value should be deleted from i's list of
    legal values in 'assignment'.
    """
    did_revise = False
    for from_node_value in assignment[i]:
        found_valid_pair = False # using bool to check if we find a valid
        for to_node_value in assignment[j]:
            test_pair = (from_node_value, to_node_value)
            if j == i:
                continue

            if test_pair in csp.constraints[i][j]:
                found_valid_pair = True # We can only remove from domain if we hav NO valid pairs, so finding just one is enough

        # The bread and butter of the ac-3; No pair of values for the two nodes holds and we have to remove that value from the nodes domain
        if not found_valid_pair:
            assignment[i].remove(from_node_value)
            did_revise = True

    return did_revise