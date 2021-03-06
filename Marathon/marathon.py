import csv, time
from sorting_algorithm import merge_sort,quick_sort,heap_sort
class MarathonRunner:
    """A class to store the data of each marathon runner."""

    def __init__(self,Dict:dict):
        """
        Construct a MarathonRunner object.

        Parameters:
        -----------
        Dict : dict
            Dictionary with keys 
            'Start NR', 
            'Vorname', 'Name',
            'Geschlecht', 'Zeit'
        """
        self.Id = Dict['Start NR']
        self.FirstName = Dict['Vorname']
        self.LastName = Dict['Name']
        self.Time = time.strptime(Dict['Zeit'],"%H:%M:%S")
        self.Sex = Dict['Geschlecht']

    def __le__(self,other):
        return self.Time <= other.Time

    def __gt__(self,other):
        return not self<=other
    
    def __eq__(self,other):
        return self<=other and other<=self

    def __ge__(self,other):
        return other<=self and not self==other
    
    def __lt__(self,other):
        return not self>=other

    def __str__(self):
        return f"{self.FirstName} {self.LastName}"
    
    def __repr__(self):
        return f"{self.Id},{self.LastName},{self.FirstName},{time.strftime('%H:%M:%S',self.Time)}"

def read_file_and_print_winners(filename,sorting_function):
    """
    Read given csv file and print winners of the race.
    Sorting is done via sorting_function.
    """
    with open(filename,'r',encoding="utf8") as file:
        data = csv.DictReader(file,delimiter=';')
        lst = [MarathonRunner(row) for row in data]
        sorted_lst = sorting_function(lst)
        # Find Winner
        winner = sorted_lst[0]
        # Find best Male and Female
        best_m = [r for r in sorted_lst if r.Sex == 'm'][0]
        best_w = [r for r in sorted_lst if r.Sex == 'w'][0]
        print(f"GesamtsiegerIn: {winner}")
        print(f"Sieger Herren:  {best_m}")
        print(f"Siegerin Damen: {best_w}")
        print("LäuferInnen mit Laufzeit zwischen 2,5 und 3 Stunden:")
        for r in sorted_lst:
            if r.Time>=time.strptime("2:30","%H:%M") and r.Time<=time.strptime("3:00","%H:%M"):
                print(f" {r.Id:>4s} {r.FirstName:15s} {r.LastName:15s} {time.strftime('%H:%M:%S',r.Time)}")

if __name__ == '__main__':
    # Read the file 'marathon.csv' and process its contents
    #read_file_and_print_winners('marathon.csv',merge_sort)
    #read_file_and_print_winners('marathon.csv',quick_sort)    
    read_file_and_print_winners('marathon.csv',heap_sort)    