from django.core.management.base import BaseCommand
from django.conf import settings

import os

from api.models import NavigationMenu, NavigationTab

class Command(BaseCommand):
    help = 'Populates the static .md files into the database.'

    def handle(self, *args, **options):
        #Delete all things
        NavigationMenu.objects.all().delete()

        with os.scandir(settings.NAVIGATION_ROOT) as entries:
            for entry in entries:
                menu, created = self.create_menu(entry)
                if created:
                    with os.scandir(entry) as tabs:
                        for tab in tabs:
                            self.create_destination(menu, tab)

    def create_menu(self, entry):
        try:
            #get the icon
            parts = entry.name.split('#')
            icon = parts.pop()

            #split up the position and the title
            parts = parts.pop().split('_')
            position = parts[0]

            #now unshift
            parts = parts[1:]
            name = ' '.join(parts)
            
            #looks like everything went as expected
            menu = NavigationMenu(
                name=name, 
                position=position, 
                icon=icon, 
                is_story=True 
            )

            menu.save()

            print('%s - menu created...' % menu)

            return menu, True

        except Exception as e:
            print('There was an error parsing %s' % entry.name)
            print(e)
    
        return (None, False)

    def create_destination(self, menu, tab):
        try:
            
            name = ' '.join(tab.name.rstrip('.md').split('_')[1:])
            position = tab.name.split('_')[0]
            text = self.read_content(tab).replace('\r\n', '\n')
            

            page = NavigationTab(
                menu=menu,
                position=position,
                name=name,
                text=text
            )

            page.save()

            print('%s - page created...' % page)
            
        except Exception as e:
            print('there was an error parsing %s' % tab.name)
            print(e)

    def read_content(self, file):
        with open(file.path) as f:
            data = f.read()
        
        return data

