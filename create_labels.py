import numpy as np
from util import open_pckl_file, load_dir

# hotels = np.load('datasets/0.1k/datasets/same_diff_hotel/141527.npy', allow_pickle=True)[0]
# hotels = open_pckl_file('datasets/0.1k/datasets/same_diff_hotel/38889.pckl')
# hotels = open_pckl_file('datasets/0.1k/datasets/same_diff_hotel/38889.pckl')
# # same/diff, query_points, query_point, (distance, descriptor, xys, hid, iid)
hotel_files = load_dir('./datasets/0.1k/datasets/same_diff_hotel')
total_good = 0
total_points = 0
for hotel in hotel_files:
    hotel = open_pckl_file(hotel)
    good_per_hotel = 0
    for i in range(len(hotel[1])):
        if hotel[1][i][0] / hotel[2][i][0] < 1:
            good_per_hotel += 1
    total_good += good_per_hotel
    total_points += len(hotel[1])
    
print("Percent total points that are good  --- " + str(total_good / total_points))