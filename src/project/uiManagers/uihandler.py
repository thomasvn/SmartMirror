from news import *
from weather import *
from cursorhandler import *
from calendarBook import *
from src.project.uiManagers.clock import *
from page import *
from returnButton import *


class UIManager:
    def __init__(self):
        self.counter = 0;
        self.zone = None
        self.current_page = Page.main
        self.cursor_handler = CursorHandler();
        self.weather, self.clock, self.news, self.returnButton = None, None, None, None
        self.tk = Tk()
        self.tk2 = Tk()
        self.canvas = Canvas(self.tk2, width=300, height=300, background='black')
        self.circle_coord = (0,0)
        self.circle_diameter = 10       #todo scale the cursor to match screen size
        # todo create a variable class to make these constants into variables
        self.cursor = self.canvas.create_oval(0,0,50,50,fill="blue", outline="#DDD", width=4)
        self.line1 = self.canvas.create_line((150,0), (150,300), fill = "green",)
        self.line2 = self.canvas.create_line((0, 150), (300, 150), fill="green", )
        self.canvas.pack()
        self.tk.configure(background='black')
        self.topFrame = Frame(self.tk, background='black')
        self.bottomFrame = Frame(self.tk, background='black')
        self.topFrame.pack(side=TOP, fill=BOTH, expand=YES)
        self.bottomFrame.pack(side=BOTTOM, fill=BOTH, expand=YES)
        self.state = False
        self.tk.bind("<Return>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.end_fullscreen)

        self.open_main_page()
        # calender - removing for now
        # self.calender = Calendar(self.bottomFrame)
        # self.calender.pack(side = RIGHT, anchor=S, padx=100, pady=60)

    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.tk.attributes("-fullscreen", self.state)
        return "break"

    # ---------------------------------- Starter and Enders ----------------------------------- #

    def open_main_page(self):
        self.start_clock()
        self.start_weather()
        self.start_news()

    def close_main_page(self):
        self.end_news()
        self.end_weather()
        self.end_clock()

    def start_news(self):
        self.news = News(self.bottomFrame)
        self.news.pack(side=LEFT, anchor=S, padx=100, pady=60)

    def end_news(self):
        self.news.destroy()

    def start_weather(self):
        self.weather = Weather(self.topFrame)
        self.weather.pack(side=LEFT, anchor=N, padx=100, pady=60)

    def end_weather(self):
        self.weather.destroy()

    def start_clock(self):
        self.clock = Clock(self.topFrame)
        self.clock.pack(side=RIGHT, anchor=N, padx=100, pady=60)

    def end_clock(self):
        self.clock.destroy()

    def new_return_button(self):
        self.returnButton = ReturnButton(self.topFrame)
        self.returnButton.pack(side=LEFT, anchor=N, padx=100, pady=60)

    def remove_return_button(self):
        self.returnButton.destroy()

        # ---------------------------------- ----------------------------------- #
    def end_fullscreen(self, event=None):
        self.state = False
        self.tk.attributes("-fullscreen", False)
        return "break"

    def update(self, cursor):
        if self.counter == 50:
            self.change_page(2)
        elif self.counter == 150:
            self.change_page(1)
        self.counter += 1
        self.update_zone(cursor)
        # print str(self.counter)
        # print "X Coord: "  + str(cursor[0]) + "  |  Y Coord: " + str(cursor[1])
        diff_x = cursor[0] - self.circle_coord[0]
        diff_y = cursor[1] - self.circle_coord[1]
        #print "diff X = " + str(diff_x) + "  |  diff y = " + str(diff_y)
        self.canvas.move(self.cursor, diff_x, diff_y)
        # self.canvas.move(self.cursor, cursor[0], cursor[1])
        self.circle_coord = cursor
        #self.canvas.update()
        #self.canvas.update_idletasks()
        self.tk.update_idletasks()
        self.tk.update()
        self.tk2.update_idletasks()
        self.tk2.update()

    def update_zone(self, cursor):
        self.zone = self.cursor_handler.update_cursor(cursor, )
        if self.current_page == Page.main:
            if self.zone == 1:
                self.weather.change_color_to_yellow()
                self.news.change_color_to_white()
                self.clock.change_color_to_white()
            elif self.zone == 2:
                self.weather.change_color_to_white()
                self.news.change_color_to_yellow()
                self.clock.change_color_to_white()
            elif self.zone == 3:
                self.weather.change_color_to_white()
                self.news.change_color_to_white()
                self.clock.change_color_to_yellow()
        elif self.current_page == Page.weather:
            x = 0  #todo finish this

    def change_page(self, newpage):
        if newpage == 1: # MAIN PAGE
            self.remove_return_button()
            self.open_main_page()
            self.current_page = Page.main
        elif newpage == 2: # BLANK PAGE
            self.close_main_page()
            self.current_page = Page.weather
            self.new_return_button()