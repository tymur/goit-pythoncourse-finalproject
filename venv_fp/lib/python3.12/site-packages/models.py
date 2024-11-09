class Note:
    def __init__(self, title, content, tags=None):
        self.title = title
        self.content = content
        self.tags = tags if tags else []

    def edit_title(self, new_title):
        self.title = new_title

    def edit_content(self, new_content):
        self.content = new_content

    def edit_tags(self, new_tags):
        self.tags = new_tags


class Contact:
    def __init__(self, name, address, phone, email, birthday):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        self.birthday = birthday

    def edit_name(self, new_name):
        self.name = new_name

    def edit_address(self, new_address):
        self.address = new_address

    def edit_phone(self, new_phone):
        self.phone = new_phone

    def edit_email(self, new_email):
        self.email = new_email

    def edit_birthday(self, new_birthday):
        self.birthday = new_birthday
