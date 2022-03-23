import arcade
import os
import random

#Importing the assets.py file
import assets

# Constants
SCREEN_WIDTH = 810
SCREEN_HEIGHT = 670
SCREEN_TITLE = "Ice Cream Shoppe Rush"
# Constants used to scale our sprites from their original size
l = []
bin_locations = []
topping_locations = []
bin_x_locations = [40, 115, 190, 265, 340, 415]
bin_y_locations = [265, 190, 115, 40]
topping_x_locations = [770, 690, 610, 530]
customers = [assets.diva, assets.e, assets.candy, assets.chester, assets.todd, assets.boban, assets.smashing, assets.rocco, 
             assets.scribble, assets.ic_man, assets.bearington, assets.cow, assets.karen, assets.sneke,
             assets.mars, assets.tera, assets.strongberry, assets.heather, assets.coda, assets.harvest, assets.milly]
positive_customers = [assets.diva_pos, assets.e_pos, assets.candy_pos, assets.chester_pos, assets.todd_pos, assets.boban_pos, assets.smashing_pos,
                      assets.rocco_pos, assets.scribble_pos, assets.ic_man_pos, assets.bearington_pos, assets.cow_pos, assets.karen_pos,
                      assets.sneke_pos, assets.mars_pos, assets.tera_pos, assets.strongberry_pos, assets.heather_pos, assets.coda_pos, assets.harvest_pos, assets.milly_pos]
negative_customers = [assets.diva_neg, assets.e_neg, assets.candy_neg, assets.chester_neg, assets.todd_neg, assets.boban_neg, assets.smashing_neg,
                      assets.rocco_neg, assets.scribble_neg, assets.ic_man_neg, assets.bearington_neg, assets.cow_neg, assets.karen_neg,
                      assets.sneke_neg, assets.mars_neg, assets.tera_neg, assets.strongberry_neg, assets.heather_neg, assets.coda_neg, assets.harvest_neg, assets.milly_neg]
flavors = [assets.bacon_ic, assets.berry_ic, assets.chocolate_ic, assets.strawberry_ic, assets.vanilla_ic, assets.mint_ic, assets.cake_ic,
           assets.pb_ic, assets.pistachio_ic, assets.rocky_road_ic, assets.licorice_ic, assets.c_and_c_ic, assets.bubblegum_ic,
           assets.peppermint_ic, assets.coffee_ic, assets.tootie_ic, assets.candy_ic, assets.peach_ic, assets.lemon_ic, assets.sour_apple_ic,
           assets.cherry_ic, assets.syrup_ic, assets.cookie_dough_ic, assets.neapolitan_ic]
bins = [assets.bacon_bin, assets.berry_bin, assets.chocolate_bin, assets.strawberry_bin, assets.vanilla_bin, assets.mint_bin, assets.cake_bin,
           assets.pb_bin, assets.pistachio_bin, assets.rocky_road_bin, assets.licorice_bin, assets.c_and_c_bin, assets.bubblegum_bin,
           assets.peppermint_bin, assets.coffee_bin, assets.tootie_bin, assets.candy_bin, assets.peach_bin, assets.lemon_bin, assets.sour_apple_bin,
           assets.cherry_bin, assets.syrup_bin, assets.cookie_dough_bin, assets.neapolitan_bin]
toppings = [assets.chocolate_sprinkles, assets.rainbow_sprinkles, assets.confetti_sprinkles, assets.heart_sprinkles, assets.chocolate_syrup,
            assets.caramel_syrup, assets.strawberry_syrup, assets.raspberry_syrup, assets.nuts, assets.cookie_bits, assets.marshmellows, assets.pbcups,
            assets.banana, assets.coconut, assets.gummy_worms, assets.mochi]
containers = [assets.chocolate_sprinkles_jar, assets.rainbow_sprinkles_jar, assets.confetti_sprinkles_jar, assets.heart_sprinkles_jar, assets.chocolate_syrup_container,
            assets.caramel_syrup_container, assets.strawberry_syrup_container, assets.raspberry_syrup_container, assets.nut_can, assets.cookie_bit_can, assets.marshmellow_can, assets.pbcups_can,
            assets.banana_can, assets.coconut_can, assets.gummy_worm_can, assets.mochi_can]
symbols = [assets.chocolate_sprinkles_symbol, assets.rainbow_sprinkles_symbol, assets.confetti_sprinkles_symbol, assets.heart_sprinkles_symbol, assets.chocolate_syrup_symbol,
            assets.caramel_syrup_symbol, assets.strawberry_syrup_symbol, assets.raspberry_syrup_symbol, assets.nuts_symbol, assets.cookie_bits_symbol, assets.marshmellows_symbol, assets.pbcups_symbol,
            assets.banana_symbol, assets.coconut_symbol, assets.gummy_worm_symbol, assets.mochi_symbol]




class Ice_Cream_Game(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        
        self.mouse_x = 100 # Mouse location x axis
        self.mouse_y = 100 # Mouse location y axis
        self.scene = None # The scene for the game
        self.cone = [] # The cone you make
        self.wanted_cone = [] # The cone the customer wants
        self.scoop = '' # The scoop/topping you click
        self.customer_choice = 0 # The customer that gets selected
        self.ic_layer = 365 # Where the ice cream will go when clicked
        self.score = 0 # Your score 
        self.num = 1 # Count down
        self.display_emotion = 0 # How long a customer displays a positive or negative emotion
        self.symbol_start = 190 # The icon that goes across the screen to show the time's starting location
        self.chosen_symbol = random.choice(flavors) # The icon that moves across the timer bar
        self.time_speed = 0 # How fast the timer is
        self.second = 0 # How long a second is
        self.customers_left = 70 # How many customers are left to serve
        self.tip_prob = 0 # Based on the difficulty, the chance of a tip will become more likley 
        self.timer_active = False # If the timer should be running or not
        self.in_store = False # If a customer is in the store
        self.new_scoop = False # If you picked a new scoop 
        self.screen_hold = False # If the screen needs to pause for a second
        self.time_up = False # Time is up
        self.countdown = False # If the countdown is active or not
        self.game_over = False # If the customers_left is at 0
        self.play_again = False # If you want to play again
        self.how_to_play = False # If you want to see how to play
        self.satisfied_customer = False # If the customer is happy from the order
        self.main_game_active = False
        self.music = '' # The music that plays in the background
        arcade.set_background_color(arcade.csscolor.LIGHT_PINK)

    def setup(self): # This will setup the main menu
        self.scene = arcade.Scene() # Make the scene
        easy_button = arcade.Sprite(assets.easy, 1) # Anytime you see this, it creates a sprite 
        easy_button.position = [SCREEN_WIDTH/2, 500] # Gives that sprite a location
        self.scene.add_sprite("buttons", easy_button)# Puts the sprite on the screen and gives it a list (the quotes)
        hard_button = arcade.Sprite(assets.hard, 1)
        hard_button.position = [SCREEN_WIDTH/2, 350]
        self.scene.add_sprite("buttons", hard_button)
        master_button = arcade.Sprite(assets.master, 1)
        master_button.position = [SCREEN_WIDTH/2, 200]
        self.scene.add_sprite("buttons", master_button)
        htp_button = arcade.Sprite(assets.htp, 1)
        htp_button.position = [SCREEN_WIDTH/2, 50]
        self.scene.add_sprite("buttons", htp_button)
        title = arcade.Sprite(assets.title, 3)
        title.position = [SCREEN_WIDTH - 450, SCREEN_HEIGHT - 150]
        self.scene.add_sprite("buttons", title)
        logo = arcade.Sprite(assets.logo, 4)
        logo.position = [SCREEN_WIDTH - 100, 300]
        self.scene.add_sprite("buttons", logo)
        self.scene.add_sprite_list_after("htp", "buttons", False) # This will layer the sprites
        
        
        
        

    def on_draw(self):
        self.clear()
        self.scene.draw() 
        if self.main_game_active == True:
            score_text = (f"Score: {self.score}")
            arcade.draw_text(score_text, 10, 350, arcade.csscolor.BLACK, 18)  # Draws the score
            score_text = (f"Customers Left: {self.customers_left}")
            arcade.draw_text(score_text, 600, 350, arcade.csscolor.BLACK, 18) # Draws the customers left
    
    def on_mouse_motion(self, x, y, dx, dy): # Finds the mouse location 
        self.mouse_x = x 
        self.mouse_y = y
      
    def on_mouse_press(self, x, y, button, modifiers): # Mouse press 
        if self.main_game_active == False: # main menu


            def main_game():
                self.main_game_active = True
                self.scene = arcade.Scene()
                backdrop = arcade.Sprite(assets.new_backdrop, 1.5)
                backdrop.position = [SCREEN_WIDTH/2, SCREEN_HEIGHT/2]
                print(backdrop.position)
                self.scene.add_sprite("shoppe", backdrop)
                count = 0
                for j in range(len(bin_y_locations)): 
                    for i in range(len(bin_x_locations)):
                        bin = arcade.Sprite(bins[count], 2)
                        bin.position = [bin_x_locations[i], bin_y_locations[j]]
                        self.scene.add_sprite("ice_cream_bin", bin)
                        count += 1
                        bin_locations.append(bin.position)
                count = 0
                for i in range(len(topping_x_locations)):
                    for j in range(len(bin_y_locations)):
                        container = arcade.Sprite(containers[count], 2)
                        container.position = [topping_x_locations[i], bin_y_locations[j]]
                        self.scene.add_sprite("ice_cream_topping", container)
                        count += 1
                        topping_locations.append(container.position)
                counter = arcade.Sprite(assets.new_counter, 1.5)
                counter.position = [SCREEN_WIDTH/2, SCREEN_HEIGHT - 501]
                self.scene.add_sprite_list_before("counter", "ice_cream_bin", False, counter)
                timer = arcade.Sprite(assets.timer, 2)
                timer.position = [SCREEN_WIDTH/7, SCREEN_HEIGHT - 25]
                ic_cone = arcade.Sprite(assets.cone, 3)
                ic_cone.position = [470, 315]
                self.scene.add_sprite_list_after("timer", "shoppe", False, timer)
                self.scene.add_sprite("cone", ic_cone)
                self.scene.add_sprite_list_after("scoops", "cone", False)
                self.scene.add_sprite_list_after("topping", "scoops", False)
                self.scene.add_sprite_list_before("customers", "counter", False)
                self.scene.add_sprite_list_after("bubble", "customers", True)
                self.scene.add_sprite_list_after("wanted", "bubble", True)
                self.scene.add_sprite_list_after("timer_bar", "timer", True)
                self.scene.add_sprite_list_after("numbers", "ice_cream_bin", True)
                audio = arcade.load_sound(self.music, True) # Loads the music
                arcade.play_sound(audio,1.0,-1,True) # Plays the music and loops it
                self.countdown = True # Starts the countdown


            if self.how_to_play == False:

                if SCREEN_WIDTH/2 in range(self.mouse_x - 100, self.mouse_x + 100): # The mouse location will be used to know if a sprite was clicked
                    if 500 in range(self.mouse_y - 50, self.mouse_y + 50):
                        self.time_speed = .4
                        self.tip_prob = 7
                        self.main_game_active = True
                        self.satisfied_customer = True
                        self.music = assets.easy_music
                        main_game() # Calls the function that makes the main game

                if SCREEN_WIDTH/2 in range(self.mouse_x - 100, self.mouse_x + 100):
                    if 350 in range(self.mouse_y - 50, self.mouse_y + 50):
                        self.time_speed = .6
                        self.tip_prob = 5
                        self.main_game_active = True
                        self.satisfied_customer = True
                        self.music = assets.hard_music
                        main_game()

                if SCREEN_WIDTH/2 in range(self.mouse_x - 100, self.mouse_x + 100):
                    if 200 in range(self.mouse_y - 50, self.mouse_y + 50):
                        self.time_speed = .8
                        self.tip_prob = 3
                        self.main_game_active = True
                        self.satisfied_customer = True
                        self.music = assets.intense_music
                        main_game()

                if SCREEN_WIDTH/2 in range(self.mouse_x - 100, self.mouse_x + 100):
                    if 50 in range(self.mouse_y - 50, self.mouse_y + 50):
                        instructions = arcade.Sprite(assets.how_to_play, 1)
                        instructions.position = [SCREEN_WIDTH/2, SCREEN_HEIGHT/2]
                        self.scene.add_sprite("htp", instructions)
                        x = arcade.Sprite(assets.x_button, 1)
                        x.position = [680, 590]
                        self.scene.add_sprite("htp", x)
                        self.how_to_play = True

            if self.how_to_play == True:
                if 680 in range(self.mouse_x - 40, self.mouse_x + 40):
                    if 590 in range(self.mouse_y - 40, self.mouse_y + 40):
                        self.scene.remove_sprite_list_by_name("htp") # This removes a list of sprites
                        self.how_to_play = False
                        
        if self.game_over == True:
            if SCREEN_WIDTH/2 in range(self.mouse_x - 100, self.mouse_x + 100):
                if SCREEN_HEIGHT/2 + 70 in range(self.mouse_y - 50, self.mouse_y + 50):
                    self.score = 0
                    self.countdown = True
                    self.in_store = False
                    self.play_again = True
                    self.scene.add_sprite_list_before("customers", "counter", False)
                    self.scene.add_sprite_list_after("numbers", "cone", False)
                    self.scene.add_sprite_list_after("bubble", "customers", False)
                    self.scene.add_sprite_list_after("wanted", "bubble", False)
                    
                    

        if self.main_game_active == True and self.satisfied_customer == False: 
        # puts ice cream and toppings on the cone    
            for i in range(len(bin_x_locations)):
                if bin_x_locations[i] in range(self.mouse_x - 35, self.mouse_x + 35):
                    for j in range(len(bin_y_locations)):
                        if bin_y_locations[j] in range(self.mouse_y - 35, self.mouse_y + 35):
                            scooped = (flavors[(j * 6) + i])
                            scoop = arcade.Sprite(
                                scooped, 3
                            )
                            scoop.position = [470, self.ic_layer]
                            self.ic_layer += 17
                            l.append(scoop.position)
                            self.scene.add_sprite("scoops", scoop)
                            self.cone.append(flavors[(j * 6) + i])
                            self.new_scoop = True
                            self.scoop = scooped
            for i in range(len(topping_x_locations)):
                if topping_x_locations[i] in range(self.mouse_x - 35, self.mouse_x + 35):
                    for j in range(len(bin_y_locations)):
                        if bin_y_locations[j] in range(self.mouse_y - 35, self.mouse_y + 35):
                            top = toppings[(i * 4) + j]
                            topping = arcade.Sprite(
                                top, 3
                            )
                            topping.position = [470, (365 + 18)]
                            l.append(topping.position)
                            self.scene.add_sprite("topping", topping)
                            self.cone.append(toppings[(i * 4) + j])
                            self.new_scoop = True
                            self.scoop = top

    def on_update(self, delta_time):   

        if self.main_game_active == True:
            
            if self.play_again == True: # Will check if you've run out of customers and will give you the play again menu
                self.scene.remove_sprite_list_by_name("replay")
                self.scene.remove_sprite_list_by_name("game_over")
                self.game_over = False
                self.play_again = False

            if self.countdown == True: # Will do a countdown from three to play again

                countdown_nums = [assets.three, assets.two, assets.one]
                if self.num < 4:

                    self.second += delta_time # Delta time is how much time in between each update. This keeps track of how much time has past
                    if self.second >= 1:
                        self.scene.remove_sprite_list_by_name("numbers")
                        number = arcade.Sprite(countdown_nums[self.num - 1], 4)
                        number.position = [SCREEN_WIDTH/2, SCREEN_HEIGHT/2]
                        self.scene.add_sprite("numbers", number)     
                        self.second = 0
                        self.num += 1
                if self.num >= 4:

                    self.second += delta_time 
                    if self.second >= 1:

                        self.scene.remove_sprite_list_by_name("numbers")
                        self.timer_active = True
                        self.countdown = False
                        self.satisfied_customer = False
                        self.num = 1
            if self.customers_left == 0: # Stops the game from moving

                self.scene.add_sprite_list_before("customers", "counter", False)
                self.scene.add_sprite_list_after("game_over", "cone", False)
                self.scene.add_sprite_list_after("replay", "cone", False)
                self.scene.remove_sprite_list_by_name("customers")
                game_over = arcade.Sprite(assets.game_over, 2)
                game_over.position = [SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 200]
                self.scene.add_sprite("game_over", game_over)
                replay = arcade.Sprite(assets.replay, 2)
                replay.position = [SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 70]
                self.scene.add_sprite("replay", replay)
                self.timer_active = False
                self.in_store = True
                self.game_over = True
                self.satisfied_customer = True
                self.customers_left = 70

            if self.timer_active == True: # Makes the timer go

                self.scene.remove_sprite_list_by_name("timer_bar")
                self.scene.add_sprite_list_after("timer_bar", "timer", True)
                timer_bar = arcade.Sprite(self.chosen_symbol, 3)
                timer_bar.position = [self.symbol_start, SCREEN_HEIGHT - 35]  
                self.scene.add_sprite("timer_bar", timer_bar)
                self.symbol_start -= self.time_speed
                if self.symbol_start < 8:

                    self.new_scoop = True
                    self.time_up = True

            if self.in_store == False: # Checks if a customer is in the shoppe or not

                self.customer_choice = random.randint(0, 20)
                scoop1 = random.randint(0, 23)
                scoop2 = random.randint(0, 23)
                scoop3 = random.randint(0, 23)
                topping = random.randint(0, 15)
                self.wanted_cone.append(flavors[scoop1])
                self.wanted_cone.append(flavors[scoop2])
                self.wanted_cone.append(flavors[scoop3])
                self.wanted_cone.append(toppings[topping])
                ic1 = arcade.Sprite(flavors[scoop1], 2.5)
                ic1.position = [SCREEN_WIDTH/2 + 190, SCREEN_HEIGHT/2 + 250]
                self.scene.add_sprite("wanted", ic1)
                ic2 = arcade.Sprite(flavors[scoop2], 2.5)
                ic2.position = [SCREEN_WIDTH/2 + 250, SCREEN_HEIGHT/2 + 250]
                self.scene.add_sprite("wanted", ic2)
                ic3 = arcade.Sprite(flavors[scoop3], 2.5)
                ic3.position = [SCREEN_WIDTH/2 + 310, SCREEN_HEIGHT/2 + 250]
                self.scene.add_sprite("wanted", ic3)
                t = arcade.Sprite(symbols[topping], 3.5)
                t.position = [SCREEN_WIDTH/2 + 250, SCREEN_HEIGHT/2 + 180]
                self.scene.add_sprite("wanted", t)
                customer = arcade.Sprite(customers[self.customer_choice], 1.6)
                customer.position = [SCREEN_WIDTH/2 + 20, SCREEN_HEIGHT/2 + 50]
                bubble = arcade.Sprite(assets.order_bubble, 2)
                bubble.position = [SCREEN_WIDTH/2 + 250, SCREEN_HEIGHT/2 + 225]
                self.scene.add_sprite("customers", customer)
                self.scene.add_sprite("bubble", bubble)
                self.in_store = True

            if self.new_scoop == True: # Will check if you are adding a new scoop/topping to the cone

                if self.scoop not in self.wanted_cone or self.time_up == True: # Negative customers
                # Either you put the wrong ice cream/topping on the cone or you run out of time
                    self.timer_active = False
                    self.cone = []
                    self.wanted_cone = []
                    self.scene.remove_sprite_list_by_name("customers")
                    self.scene.remove_sprite_list_by_name("bubble")
                    self.scene.remove_sprite_list_by_name("wanted")
                    self.scene.add_sprite_list_before("customers", "counter", False)
                    self.scene.add_sprite_list_after("bubble", "customers", False)
                    self.scene.add_sprite_list_after("wanted", "bubble", False)
                    customer = arcade.Sprite(negative_customers[self.customer_choice], 1.6)
                    customer.position = [SCREEN_WIDTH/2 + 20, SCREEN_HEIGHT/2 + 50]
                    self.scene.add_sprite("customers", customer)             
                    self.display_emotion += delta_time
                    if self.display_emotion >= 2.0:
                        self.scene.remove_sprite_list_by_name("scoops")
                        self.scene.remove_sprite_list_by_name("topping")
                        self.scene.remove_sprite_list_by_name("customers")
                        self.new_scoop = False
                        self.display_emotion = 0
                        self.scene.add_sprite_list_after("scoops", "cone", False)
                        self.scene.add_sprite_list_after("topping", "scoops", False)
                        self.scene.add_sprite_list_before("customers", "counter", False)
                        self.scene.add_sprite_list_after("bubble", "customers", False)
                        self.scene.add_sprite_list_after("wanted", "bubble", False)
                        self.ic_layer = 365
                        self.time_up = False
                        self.symbol_start = 190
                        self.timer_active = True
                        self.in_store = False
                        self.customers_left -= 1

                if self.scoop in self.wanted_cone: # Will pass if wanted ice cream/topping is one the cone
                    good_scoop = self.scoop
                    self.new_scoop = False   
                    self.cone.remove(self.scoop)
                    self.wanted_cone.remove(good_scoop)
                    self.cone.append('yes')
                    self.scoop = ''

            if len(self.cone) >= 4: # This may not look like it but it checks if the cone is right or not

                self.timer_active = False
                self.satisfied_customer = True
                self.scene.remove_sprite_list_by_name("customers")
                self.scene.remove_sprite_list_by_name("bubble")
                self.scene.remove_sprite_list_by_name("wanted")
                self.scene.add_sprite_list_before("customers", "counter", False)
                self.scene.add_sprite_list_after("bubble", "customers", False)
                self.scene.add_sprite_list_after("wanted", "bubble", False)
                customer = arcade.Sprite(positive_customers[self.customer_choice], 1.6)
                customer.position = [SCREEN_WIDTH/2 + 20, SCREEN_HEIGHT/2 + 50]
                self.scene.add_sprite("customers", customer)
                self.display_emotion += delta_time
                if self.display_emotion >= 2.0:

                    tip = 5
                    tip_chance = random.randint(1,self.tip_prob)
                    if tip_chance == 1:

                        tip += round(self.symbol_start / 10)
                    self.score += tip
                    self.cone = []
                    self.wanted_cone = []
                    self.scene.remove_sprite_list_by_name("customers")
                    self.scene.remove_sprite_list_by_name("scoops")
                    self.scene.remove_sprite_list_by_name("topping")
                    self.scene.add_sprite_list_after("scoops", "cone", False)
                    self.scene.add_sprite_list_after("topping", "scoops", False)
                    self.scene.add_sprite_list_before("customers", "counter", False)
                    self.scene.add_sprite_list_after("bubble", "customers", False)
                    self.scene.add_sprite_list_after("wanted", "bubble", False)              
                    self.ic_layer = 365
                    self.timer_active = True
                    self.satisfied_customer = False
                    self.symbol_start = 190
                    self.display_emotion = 0
                    self.in_store = False   
                    self.customers_left -= 1    
        pass


def main():
    """Main function"""
    window = Ice_Cream_Game()
    window.setup()
    arcade.run()
    
        


if __name__ == "__main__":
    main()