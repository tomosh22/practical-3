from tkinter import messagebox


class Set:
    def __init__(self, elements, name=None):
        if name:
            self.name = name
        self.elements = elements

    def __str__(self):
        return "Name: {} | Elements: {}".format(self.name, self.elements)


def cart_product(sets, set_ids):
    """obtains which sets to calculate from and returns cartesian product"""

    # determining which sets have been passed through in set_ids
    calc_sets = []
    for id in set_ids:
        for set in sets:
            if set.name == id:
                calc_sets.append(set)

    # error if no sets have been appended to calc_sets, indicates user error
    if len(calc_sets) == 0:
        messagebox.showinfo("Missing Sets", "None of those sets were found")
        return ""

    # will need loop x-1 number of times when x is number of sets in calc_sets
    # eg need to loop 3 times if there are 4 sets in calc_sets
    for x in range(len(set_ids) - 1):

        # results contains all the sets included in the cartesian product
        # results will contain a number of arrays, each representing a set
        results = []

        # calculate cartesian product of first 2 sets in calc_sets
        set1 = calc_sets[0]
        set2 = calc_sets[1]

        for element1 in set1.elements:
            for element2 in set2.elements:

                # to_add represents the current set
                to_add = []

                # adds all combinations of element1 and element2 to to_add and appends the result to results
                for y in range(x + 1):
                    to_add.append(element1[y])
                to_add.append(element2)
                results.append(to_add)

        # the newly calculated cartesian product becomes another set to be iterated through
        calc_sets = calc_sets[1:]
        calc_sets[0] = Set(results, name=str(x))

    result_string = "{"
    for result in results:
        # python represents arrays with [ and ] but sets are represented with { and }
        result_string += str(result).replace("[", "{").replace("]", "}")
    result_string += "}"
    return result_string
