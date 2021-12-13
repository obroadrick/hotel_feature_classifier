"""
Now that we have generated all this label data, let's explore it a bit.
Some questions we'd like to answer:
- What is the distribution of c_same?
- What is the distribution of c_diff?
- What is the distribution of their ratio?
- Where do the mean, median, and other quantiles lie for the ratio distribution?
- Are the results consistent with what we would expect, or have we revealed something new?
"""

from util import open_pckl_file, load_dir
import pandas as pd


hotel_files = load_dir(
    '/pless_nfs/home/mdt_/tcam/datasets/0.1k/same_diff_hotels/same_diff_hotel')
total_good = 0
total_points = 0

dataset_points = []
dataset_labels = []
for hotel in hotel_files:
    hotel = open_pckl_file(hotel)
    good_per_hotel = 0
    for i in range(len(hotel[1])):
        if hotel[2][i][0] / hotel[1][i][0] > 1:
            good_per_hotel += 1
            dataset_labels.append(1)
        else:
            dataset_labels.append(0)
        dataset_points.append(hotel[1][i][1])
    total_good += good_per_hotel
    total_points += len(hotel[1])

print('total points- {}'.format(total_points))
print("Percent total points that are good  --- " + str(total_good / total_points))


df = pd.DataFrame(dataset_points)
df['label'] = dataset_labels
df.to_pickle(
    '/pless_nfs/home/mdt_/tcam/datasets/0.1k/BinClassDatasets/dataset_4_hotel.pckl')
