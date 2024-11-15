import csv
import sys

from util import Node, StackFrontier, QueueFrontier

# Maps names to a set of corresponding person_ids
names = {}

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
people = {}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
movies = {}


def load_data(directory):
    """
    Load data from CSV files into memory.
    """
    # Load people
    with open(f"{directory}/people.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set()
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])

    # Load movies
    with open(f"{directory}/movies.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }

    # Load stars
    with open(f"{directory}/stars.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                people[row["person_id"]]["movies"].add(row["movie_id"])
                movies[row["movie_id"]]["stars"].add(row["person_id"])
            except KeyError:
                pass


def main():
    if len(sys.argv) > 2:
        sys.exit("Usage: python degrees.py [directory]")
    directory = sys.argv[1] if len(sys.argv) == 2 else "large"

    # Load data from files into memory
    print("Loading data...")
    load_data(directory)
    print("Data loaded.")

    source = person_id_for_name(input("Name: "))
    if source is None:
        sys.exit("Person not found.")
    target = person_id_for_name(input("Name: "))
    if target is None:
        sys.exit("Person not found.")

    path = shortest_path(source, target)

    if path is None:
        print("Not connected.")
    else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        path = [(None, source)] + path
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")


def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.

    If no possible path, returns None.

    I'm getting source (id for origin) and target (id for target)
    """
    #sets up the stuff, i.e. frontier (queue for breadth first search)
    #sets the goal,explored, and start
    frontier = QueueFrontier()
    start = Node(state=source, parent=None, action=None)
    frontier.add(start)
    explored = set()
    print(target)

    while True:

        #Nodes are composed of states, parents, and actions
        #states = person id
        #actions = movie id
        #parents = last person id

        #if the frontier is empty there is no solution, so return none
        if frontier.empty():
            return None
        
        #removes inital node
        print("removes node")
        newNode = frontier.remove()

        #neighbors for person returns (movie id, person id)
        
        #adds nodes to the frontier and checks
        for _ in range(len(neighbors_for_person(newNode.state))):

            #gets aspects of current state analyzed
            movieId = list(neighbors_for_person(newNode.state))[_][0]
            personId = list(neighbors_for_person(newNode.state))[_][1]

            #if solution return solution
            if isSolution(personId, target):
                # TODO write the code to check if they match
                #I hate myself so much i did all the code right, but I messe dup the last function and wasted like a day gooddamnist
                raise Exception("yeah, we got it boys")
                returnSolution(Node(state = personId, parent=newNode, action=movieId))
            
            #if in explored, don't add to the frontier
            elif not(inExplored(explored, personId, movieId)):  
                #if not solution and not in explored add to frontier
                frontier.add(Node(state=personId, parent=newNode, action=movieId))
                #if not in explored add to explored to avoid overlap
        
        explored.add(newNode.state)
        print(f"added {newNode.state}")
        #adds the explored node to explored to avoid backtracking
        #I'm inputting the nodes more than once oopsies again agagaga maybe is checking solution

def inExplored(explored, personId, movieId):
    #TODO is bugged needs fixed not correctly identifiying or adding
    """
    Checks if input is also in explored
    """
    for _ in range(len(explored)):
        if personId == list(explored)[_]:
            print(f"{personId} is {list(explored)[_]}")
            return True
    print(f"{personId} isn't in explored")
    return False

def isSolution(dubious, target):
    """
    Checks if input is the solution
    """
    if dubious == target:
        return True
    return False

def returnSolution(solution):
    """
    returns the solution in the format requested
    """
    #note to self: actions are the movies
    #parents are the previous node?
    WHOOOO = []
    YEAH = []
    mrNode = solution
    while True:
        if mrNode.parent == None:
            break
        WHOOOO.append(mrNode.parent)
        YEAH.append(mrNode.action)
        #hold on, check if node parents are set to a node and not the person ID should work?
        mrNode = mrNode.parent


    WHOOOO.reverse()
    YEAH.reverse()
    bigMan = []
    for _ in range(len(YEAH)):
        bigMan.append((WHOOOO[_].state, YEAH[_]))
    return bigMan



    

def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    person_ids = list(names.get(name.lower(), set()))
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print(f"Which '{name}'?")
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
        try:
            person_id = input("Intended Person ID: ")
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        return None
    else:
        return person_ids[0]


def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """
    
    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
    return neighbors


if __name__ == "__main__":
    main()
