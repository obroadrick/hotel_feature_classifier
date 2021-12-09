"""
Functions for our initial, naive search that we will use to build an 
understanding of how r2d2 points can be used for our matching problem.
"""

from closeness_computations import closest_vector_handler


def compute_matches_for_image_across_hotels(hid, rid):
    """
    This function is the initial "search" algorithm that we are implementing.
    For the query image, we compute the pairwise-closest r2d2 points for a sample 
    of a images from the same hotel and a sample of images from a different hotel.
    We then save and plot the distribution of cosine-similarity for these two classes.

    hid     hotel id of the query image
    rid     room id of the query image
    """
    # Get the query image features
    query_img_features = r2d2_features.open_and_extract_feature_file(hotel_ids[0], room_ids[0])

    # SAME HOTEL
    # Get a sample of images from the same hotel
    same_hotel_rids = #TODO ask marshall
    same_hotel_feature_lists = []
    for same_rid in same_hotel_rids:
        same_hotel_feature_lists.append(r2d2_features.open_and_extract_feature_file(hid, same_rid))
    
    # Compute the cosine similarities between the query image and sampled images from the same hotel
    for features in same_hotel_feature_lists:
        # We want all pairwise matches, so we choose n an upper bound on the possible total pairwise matches
        n = min(len(query_img_features), len(features)
        closest = closest_vector_handler(query_img_features, features, n)
    # TODO 




    # DIFFERENT HOTEL
    # Get a sample of images from a different hotel
    # TODO 

    # Compute the cosine similarities between the query image and sampled images from a different hotel
    # TODO 

    # Save this data
    # TODO 

    # Plot the distribution of cosine similarities for each class (hotel)
    # TODO 







"""
# NOTES
def closest_vector_handler(h1, h2,n):
Computes and returns the n closest (by cosine distance) r2d2 points between h1 and h2.
"""

