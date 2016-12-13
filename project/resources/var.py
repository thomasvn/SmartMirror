import varLoader
import coordcreator

wall_light_color = True

# -------------------- Coloring ------------------------ #
selected_off = 'white'
selected_on = 'deep pink'
background_color = 'black'
font_style = 'Helvetica'
# -------------------- For Web Parsing -------------------- #

ip = '<IP>'
country_code = 'us'  # todo read this from file
f = open('key.txt', 'r')
weather_api_token = f.read()
print weather_api_token
f.close()

# -------------------- Window Sizing -------------------- #

camera_width = 200
camera_height = 200
tk_cursor_diameter = 25
tk_cursor_outline_thickness = tk_cursor_diameter / 10

# ------------------- Polygon Coordinate ---------------- #

#    0 ----------50-----------100- ... X Axis
#    |
#    |      THIS IS HOW THE
#    |      AXIS WORKS
#    50     NOTE* Y IS UPSIDE DOWN
#    |
#    |
#    |
#    100
#   ...
#    Y Axis

# Four Corners

bottom_left_rectangle = coordcreator.get_polygon_coord(0, camera_height / 2, camera_width / 2, camera_height / 2)

bottom_right_rectangle = coordcreator.get_polygon_coord(camera_width / 2, camera_height / 2, camera_width / 2,
                                                        camera_height / 2)

top_left_rectangle = coordcreator.get_polygon_coord(0, 0, camera_width / 2, camera_height / 2)

top_right_rectangle = coordcreator.get_polygon_coord(camera_width / 2, 0, camera_width / 2, camera_height / 2)

# ------------------- Selection Constants ----------------------#
selection_time = 2.5  # in seconds
update_time = 10  # in minutes

# -------------------- Saved Data -------------------- #

saved_data = {}
varLoader.get_saved_data()

# -------------------- Key ---------------------- #

pref_keys = {
    'mp_stocks' : 'main_page_stocks',
    'mp_news' : 'main_page_news',
    'mp_sunset': 'main_page_sunset',
    'mp_sunrise' : 'main_page_sunrise',
    'mp_humidity' : 'main_page_humidity',
    'mp_hilo' : 'main_page_high_low'
}

# -------------------- Settings ----------------------- #
preferences = {}
varLoader.get_preferences()

# ------------------- Other Data ---------------------- #

other_data = {}
varLoader.get_other()

print other_data

# ---------------------- Images ----------------------- #
color_hex_codes= {
    'yellow' : '#ffff00',
    'deep sky blue' : '#00bfff',
    'deep pink' : '#ff1493'
}