from tkinter import messagebox
class Set:
    def __init__(self, elements, name=None):
        if name:
            self.name = name
        self.elements = elements

    def __str__(self):
        return "Name: {} | Elements: {}".format(self.name, self.elements)


def cart_product(sets,set_ids):
    """obtains which sets to calculate from and prints cartesian product"""
    #set_ids = input("Enter set names separated by a comma (,)").split(",")
    calc_sets = []
    for id in set_ids:
        for set in sets:
            if set.name == id:
                calc_sets.append(set)
    if len(calc_sets) == 0:
        messagebox.showinfo("Missing Sets","None of those sets were found")
        return ""
    for x in range(len(set_ids)-1):
        results = []
        set1 = calc_sets[0]
        set2 = calc_sets[1]
        for element1 in set1.elements:
            for element2 in set2.elements:
                to_add = []
                for y in range(x+1):
                    to_add.append(element1[y])
                to_add.append(element2)
                results.append(to_add)
        calc_sets = calc_sets[1:]
        calc_sets[0] = Set(results, name=str(x))
    result_string = "{"
    for result in results:
        #print(str(result).replace("[", "{").replace("]", "}"), end=",")
        result_string += str(result).replace("[", "{").replace("]", "}")
    result_string += "}"
    return result_string