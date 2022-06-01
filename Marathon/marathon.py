import csv

##########################################################
# Merges two lists lo,hi using the comparator function leq
def merge(lo,hi,leq):
    lst = []
    i,j = 0,0
    while i < len(lo) and j < len(hi):
        if leq(lo[i],hi[j]):
            lst.append(lo[i])
            i += 1
        else:
            lst.append(hi[j])
            j += 1
    return lst + lo[i:] + hi[j:]

##################################################
# Mergesorts lst using the comparator function leq
# Runtime O(n*log(n))
# Space Overhead O(n) since out of place
# The sorting algorithm is stable i.e. preserves 
# relative index of equal elements.
def merge_sort(lst, leq):
    if len(lst) <= 1:
        return lst
    return merge(
        merge_sort(lst[:len(lst)//2],leq),
        merge_sort(lst[len(lst)//2:],leq),
        leq)

#################################################
# Return the time in seconds from a given csv-row
def get_time(row):
    time_str = row['Zeit']
    time_tpl = time_str.split(':')
    return int(time_tpl[0])*3600 + int(time_tpl[1])*60 + int(time_tpl[2])

###################################################################
# Find the first element in a sorted list that meets the predicate.
# Returns None if no such element is present
def best_in_subset(sorted_lst,predicate):
    i = 0
    while i < len(sorted_lst) and not predicate(sorted_lst[i]):
        i += 1
    if i < len(sorted_lst):
        return sorted_lst[i]
    return None

####################################################
# Read given csv file and print winners of the race.
def read_file_and_print_winners(filename):
    with open(filename,'r',encoding="utf8") as file:
        data = csv.DictReader(file,delimiter=';')
        lst = list(data)
        sorted_lst = merge_sort(
            lst,
            lambda a,b: get_time(a)<=get_time(b))
        winner = best_in_subset(sorted_lst,lambda r: True)
        best_male = best_in_subset(sorted_lst,lambda r: r['Geschlecht']=='m')
        best_female = best_in_subset(sorted_lst,lambda r: r['Geschlecht']=='w')
        print(f"GesamtsiegerIn: {winner['Vorname']} {winner['Name']}")
        print(f"Sieger Herren: {best_male['Vorname']} {best_male['Name']}")
        print(f"Siegerin Damen: {best_female['Vorname']} {best_female['Name']}")

##############
# Main program
if __name__ == '__main__':
    read_file_and_print_winners('./Marathon/marathon.csv')