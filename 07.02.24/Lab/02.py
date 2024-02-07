
# можно было бы все прикрутить к редис и bcrypt, но в задании этого не было :)
# тут просто реализация методов

class User:
    def __init__(self, user_name='', password=''):
        self.user_name = user_name
        self.password = password


class WebSite:
    def __init__(self, name, url):
        self._name = name
        self._url = url
        self._page_list = {}
        self._user: User() = None

    def set_user(self, user):
        self._user = user

    def login(self, user, password):
        if self._user.user_name == user and self._user.password == password:
            print('\nYou are successfully logged in.')
        else:
            print('\nWrong user name or password.')

    def add_page(self, caption, page):
        self._page_list[caption] = page
        print('\nPage successfully added.')

    def delete_page(self, caption):
        if caption in self._page_list:
            del self._page_list[caption]
            print(f'\nPage "{caption}" deleted')
        else:
            print(f'\nPage {caption}" not found')

    def get_webpage_info(self):
        return f'\nWEB SITE INFO: \nTotal pages {len(self._page_list)}\nList of available pages: {self._page_list}'

    def search_page_by_caption(self, caption):
        for page in self._page_list:
            if caption in page:
                print(f'\nPage "{caption}" found: {self._page_list[page].view_page_detail()}')

    def search_page_by_content(self, content):
        for page in self._page_list:
            if content in self._page_list[page]._content:
                print(f'\nPage "{content}" found: {self._page_list[page].view_page_detail()}')


class WebPage:
    def __init__(self, caption, content, publication_date):
        self._caption = caption
        self._content = content
        self._publication_date = publication_date

    def __repr__(self):
        return f'{self._caption}'

    def view_page_detail(self):
        return f'\nWEB PAGE INFO: \nPage: {self._caption}\nContent: {self._content}\nPublication date: {self._publication_date}'

    def edit_page(self):
        new_caption = input('\nEnter new caption: ')
        new_content = input('Enter new content: ')
        new_publication_date = input('Enter new publication date: ')
        self._caption = new_caption
        self._content = new_content
        self._publication_date = new_publication_date



website = WebSite('MySite', 'www.mysite.com')

page1 = WebPage('Page 1', 'Page about 1', '07.02.2024 20:00')
page2 = WebPage('Page 2', 'Page about 2', '07.02.2024 20:01')
page3 = WebPage('Page 3', 'Page about 3', '07.02.2024 20:02')

website.add_page(page1._caption, page1)
website.add_page(page2._caption, page2)
website.add_page(page3._caption, page3)

print(website.get_webpage_info())

website.delete_page(page2._caption)

print(website.get_webpage_info())

print(page1.view_page_detail())

website.search_page_by_caption('1')

website.search_page_by_content('about 1')

page1.edit_page()

user = User('test', 'test')

website.set_user(user)

user_name = input('\nEnter user name: ')

password = input('Enter user password: ')

website.login(user_name, password)

menu = '''
    MENU:
1 - Create website
2 - Add page to site
3 - Delete page from site
4 - View site info
5 - Exit

Enter your choice: '''

while True:
    selection = (input(menu))
    match selection:
        case '1':
            name = input('Enter your Web Site name: ')
            url = input('Enter url for your site: ')
            site_name = name.strip(' .,!<>?').replace(' ', '_')
            locals()[site_name] = WebSite(name, url)
            print(f'Your site name is "{site_name}"')
        case '2':
            if locals().get(site_name):
                caption = input('Enter your Web Page name: ')
                content = input('Enter content of yor web page: ')
                publication_date = input('Enter publication date for your page: ')
                page_name = caption.strip(' .,!<>?').replace(' ', '_')
                locals()[page_name] = WebPage(caption, content, publication_date)
                locals()[site_name].add_page(locals()[page_name]._caption, locals()[page_name])
            else:
                print('Site not found')
        case '3':
            if locals().get(site_name):
                caption = input('Enter your Web Page name: ')
                locals()[site_name].delete_page(caption)
            else:
                print('Site not found')
        case '4':
            print(locals()[site_name].get_webpage_info())
        case _:
            break
