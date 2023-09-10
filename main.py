# write your code here
def padel_court_cost(court_type):
    if court_type == "indoor":
        return 30
    elif court_type == "outdoor":
        return 20
def rackets_cost(racket_brand):
    if racket_brand == "bullpadel":
        return 100
    elif racket_brand == "nox":
        return 140
    elif racket_brand == "siux":
        return 200
def padel_balls_cost(ball_boxes):
    if ball_boxes == 1:
        return 2
    elif ball_boxes == 2:
        return 3.5
    elif ball_boxes == 3:
        return 5
def padel_game_cost():
    court_type = input("enter court type: ")
    racket_brand = input("enter racket brand: ")
    ball_boxes = int(input("enter number of ball boxes: "))
    total = padel_court_cost(court_type) + rackets_cost(racket_brand) + padel_balls_cost(ball_boxes)
    return total 
print(f"total cost{padel_game_cost()}")