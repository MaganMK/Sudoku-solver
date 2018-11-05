def backtracking_search():
    """This functions starts the CSP solver and returns the found
    solution.
    """
    # Make a so-called "deep copy" of the dictionary containing the
    # domains of the CSP variables. The deep copy is required to
    # ensure that any changes made to 'assignment' does not have any
    # side effects elsewhere.

    # Run AC-3 on all constraints in the CSP, to weed out all of the
    # values that are not arc-consistent to begin with

    # Call backtrack with the partial assignment 'assignment'
    pass


def backtrack(self, assignment):
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
    # TODO: IMPLEMENT THIS
    pass


def select_unassigned_variable(self, assignment):
    """The function 'Select-Unassigned-Variable' from the pseudocode
    in the textbook. Should return the name of one of the variables
    in 'assignment' that have not yet been decided, i.e. whose list
    of legal values has a length greater than one.
    """
    # TODO: IMPLEMENT THIS
    pass


def inference(self, assignment, queue):
    """The function 'AC-3' from the pseudocode in the textbook.
    'assignment' is the current partial assignment, that contains
    the lists of legal values for each undecided variable. 'queue'
    is the initial queue of arcs that should be visited.
    """
    # TODO: IMPLEMENT THIS
    pass


def revise(self, assignment, i, j):
    """The function 'Revise' from the pseudocode in the textbook.
    'assignment' is the current partial assignment, that contains
    the lists of legal values for each undecided variable. 'i' and
    'j' specifies the arc that should be visited. If a value is
    found in variable i's domain that doesn't satisfy the constraint
    between i and j, the value should be deleted from i's list of
    legal values in 'assignment'.
    """
    # TODO: IMPLEMENT THIS
    pass