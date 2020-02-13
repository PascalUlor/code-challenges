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


class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.contact_list = []
        self.user = {}

    def addUser(self, name, contacts):
        self.lastID += 1
        self.contact_list.append({name : list(set(contacts))})

    def populateContacts(self, numUsers, avgContacts):
        # reset graph
        self.lastID = 0
        self.users = {}
        # Add users
        targetContacts = avgContacts
        # set counter for total number of contacts
        totalContacts = 0
        contacts = []
        # loop over a range of 0 to numUsers
        for i in range(numUsers):
            totalContacts = 0
            contacts = []
            while totalContacts < targetContacts:
                # set contactID to a random number between 1 and the lastID
                contactID = random.randint(1, avgContacts << i)
                # if the return of add contact of userID and contactID is true
                contacts.append(contactID)
                # increment total friendships
                totalContacts += 1
            # add user to the graph
            if len(contacts) == totalContacts:
                self.addUser(i + 1, contacts)
                contacts = []


def get_off_set(user_contacts):
    off_set = []
    for i in user_contacts:
        if list(i.keys())[0] not in off_set:
            for j in range(0, len(user_contacts)-1):
                if (list(i.keys())[0] != list(user_contacts[j].keys())[0]):
                    join = list(i.values())[0] + user_contacts[j].get(list(user_contacts[j].keys())[0])
                    set(join)
                    per = (len(list(i.values())[0]) * 30)//100
                    if (len(join) - len(set(join)) > per):
                        off_set.append(list(i.keys())[0])
                        off_set.append(list(user_contacts[j].keys())[0])
                else:
                    continue
    return off_set


if __name__ == '__main__':
    sg = SocialGraph()
    numUsers = 10
    avgContacts = 9

    sg.populateContacts(numUsers, avgContacts)

    print(sg.contact_list)

    print(get_off_set(sg.contact_list))