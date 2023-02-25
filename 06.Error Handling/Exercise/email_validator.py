class NameTooShortError(Exception):
    """The name is shorter or equal to 4"""
    pass


class MustContainAtSymbolError(Exception):
    """The email doesn't contain '@' """
    pass


class InvalidDomainError(Exception):
    """Domain is different than (.com, .bg, .org, .net)"""
    pass


domains = ["com", "bg", "org", "net"]

email = input()

while email != "End":

    if len(email.split("@")[0]) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    if email.split(".")[-1] not in domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")

    email = input()
