# Brief Description of Data
These computed similarities are organized into directories by hotel id number.
Within each hotel directory, you will find many files each with name of
the form num1\_num2.npy and num1\_num2.png. The files are named where num1 refers 
to the hotel id number (matches the directory name), and num2 refers to a specific
image id number. The .npy files contain lists of all cosine similarities that
we have computed, by point, to all other points in a relatively small subset of 
the total Hotels-50K database. The images are of plots that we have saved
of the density of similarities for points in the same hotel and those in a different
hotel. These plots don't show great separation, but we have been able to show that
there are usually a few points at the far right end of the distribution that 
match disproportionately well, and these are the points which we intend to use
for our ultimate search metric.

