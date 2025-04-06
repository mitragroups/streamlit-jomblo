class Member:
    def __init__(self, nama):
        self.name = nama
        self.is_active = True

    def deactivate(self):
        self.is_active = False
        
    def activate(self):
        self.is_active = True

class Jomblo:
    def __init__(self, nama):
        self.name = nama
        self.gender = []
        self.age = []
        self.members = []
        pass
    
    def register_member(self, member: Member):
        self.members.append(member)
        
    def get_active_members(self):
        active_members = []
        for member in self.members:
            if member.is_active:
                active_members.append(member)
                
        return active_members