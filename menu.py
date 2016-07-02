# menu.py
import Tkinter as tk
import tkMessageBox 
import pygubu

import ConfigParser

class MyApplication(pygubu.TkApplication):

    def _create_ui(self):
        #1: Create a builder
        self.builder = builder = pygubu.Builder()

        #2: Load an ui file
        #builder.add_from_file('menu.ui')
        builder.add_from_file('menu_new.ui')

        #3: Create the widget using self.master as parent
        self.mainwindow = builder.get_object('mainwindow', self.master)

        # Set main menu
        self.mainmenu = menu = builder.get_object('mainmenu', self.master)
        self.set_menu(menu)

        # Configure callbacks
        builder.connect_callbacks(self)


    def on_mfile_item_clicked(self, itemid):
        if itemid == 'mfile_open':
            tkMessageBox .showinfo('File', 'You clicked Open menuitem')

        if itemid == 'mfile_quit':
            tkMessageBox .showinfo('File', 'You clicked Quit menuitem. Byby')
            self.quit();


    def on_about_clicked(self):
        tkMessageBox .showinfo('About', 'You clicked About menuitem')


def create_ui():
    
    f = open('menu.ui', 'r')
    f1 = open('menu_new.ui', 'w')
    flag = False
    sec_flag = False

    target_str="        <child>\n"+"          <object class=\"tk.Menuitem.Radiobutton\" id=\"k1\">\n"+"            <property name=\"command_id_arg\">false</property>\n"+"            <property name=\"label\" translatable=\"yes\">k1</property>\n"+"          </object>\n"+"        </child>\n"

    config = ConfigParser.ConfigParser()
    config.optionxform = str
    config.read('Config.ini')
     
    total_section = config.sections()

    for line in f:
        if line.find("<!--Radiobutton_start-->")>=0:
            flag = True;
            sec_flag = True;
        if line.find("<!--Radiobutton_end-->")>=0:
            flag = False;    

        if flag == False and line.find("<!--Radiobutton_end-->")<0:
            #print line
            f1.write(line)
        
        if flag == True and sec_flag == True:
            for sSection in total_section:
                #print "Section = ", sSection
                f1.write('\n')
                #target_str.replace("k1",sSection)
                target_str="        <child>\n"+"          <object class=\"tk.Menuitem.Radiobutton\" id=\""+sSection+"\">\n"+"            <property name=\"command_id_arg\">false</property>\n"+"            <property name=\"label\" translatable=\"yes\">"+sSection+"</property>\n"+"          </object>\n"+"        </child>\n"
                f1.write(target_str)
            sec_flag = False


    f1.close()

if __name__ == '__main__':
    root = tk.Tk()
    create_ui()
    app = MyApplication(root)
    app.run()
