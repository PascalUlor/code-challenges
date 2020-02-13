"""So what I need is your approach to solving the contact similarity problem.
Say we have a group of 1,000 people.  Each with 700 to 900 phone contacts each.
We need to figure out those with contact similarity above 30%. Meaning,
we don't want any two people to have more than 30% similarity in their contact
lists.
This will involve you simulating contacts by writing a script to:

1) Generate contacts for each of the 1k people. Remember, contact list size
varies from 700 to 900.

2) Your generation script should randomly allow for duplication of contacts
across each person.
This duplication can be anything between 10 to 50%.
After that, you can then come up with the algo for filtering out the sets with
above 30% similarity."""


import random


class Queue:
    def __init__(self):
        self.storage = []

    def enqueue(self, value):
        self.storage.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.storage.pop(0)
        else:
            return None

    def size(self):
        return len(self.storage)


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.contacts = {}

    def addContacts(self, userID, contactID):
        # ensure users don't have themselves in their contact
        if userID == contactID:
            return False
        elif contactID in self.contacts[userID] or userID in self.contacts[contactID]:
            return False
        else:
            self.contacts[userID].add(contactID)
            self.contacts[contactID].add(userID)
            return True

    def addUser(self, name):
        self.lastID += 1
        self.users[self.lastID] = User(name)
        self.contacts[self.lastID] = set()

    def populateContacts(self, numUsers, avgContacts):
        # reset graph
        self.lastID = 0
        self.users = {}
        self.contacts = {}

        # Add users
        # loop over a range of 0 to numUsers
        for i in range(numUsers):
            # add user to the graph
            self.addUser(f"User {i + 1}")

        # contacts

        # get the target contacts via (numUsers * avgContacts)
        targetContacts = (numUsers * avgContacts)
        # set counter for total number of contacts
        totalContacts = 0
        # set a counter for collisions
        collisions = 0

        # while total contacts is less than the target contacts
        while totalContacts < targetContacts:
            # set userID to a random number between 1 and the lastID
            userID = random.randint(1, self.lastID)
            # set contactID to a random number between 1 and the lastID
            contactID = random.randint(1, self.lastID)
            # if the return of add contact of userID and contactID is true
            if self.addContacts(userID, contactID):
                # increment total friendships
                totalContacts += 2
            # otherwise
            else:
                # increment collisions
                collisions += 1
        # print collision
        print(f"COLLISIONS: {collisions}")

    def getAllSocialPaths(self, userID):
        visited = {}
        # create a queue
        q = Queue()
        # enqueue the user id as a list
        q.enqueue([userID])

        # while queue is not empty
        while q.size() > 0:
            # dequeue to path variable
            path = q.dequeue()
            # set new user id to the last item in path
            newUserID = path[-1]

            # check if the new user id is not in the visited structure
            if newUserID not in visited:
                # set the new user ids path in visited
                visited[newUserID] = path

                # loop over each contact id in the contacts at the index of new user id
                for contactID in self.contacts[newUserID]:
                    # check that the contact id is not in visited
                    if contactID not in visited:
                        # create a copy of the path
                        new_path = list(path)
                        # append the contact id to the copy of the path
                        new_path.append(contactID)
                        # enqueue the copy of the path
                        q.enqueue(new_path)

        # return the visited data structure
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    numUsers = 1000
    avgContacts = 800
    # sg.populateContacts(numUsers, avgContacts)

    sg.populateContacts(numUsers, avgContacts)

    connections = sg.getAllSocialPaths(1)
    print(f"Users in extended contact list: {len(connections) - 1}")

    total_sp = 0

    for userID in connections:
        total_sp += len(connections[userID])

    print(f"Average length of contacts: {total_sp / len(connections)}")
    print(sg.contacts)
    # print(connections)
