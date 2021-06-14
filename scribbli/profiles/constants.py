class RoleChoices(object):
    Guest = 0
    User = 1
    Moderator = 2
    Admin = 3

    @staticmethod
    def as_choices():
        return (
            (RoleChoices.Guest, "Guest"),
            (RoleChoices.User, "User"),
            (RoleChoices.Moderator, "Moderator"),
            (RoleChoices.Admin, "Admin"),
        )
