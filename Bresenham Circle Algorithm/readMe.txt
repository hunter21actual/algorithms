#  Circle Drawing using Bresenham's Algorithm and Mid point Circle Algorithm

Basic concept cited from wikipedia

"This algorithm draws all eight octants simultaneously, starting from each cardinal direction (0°, 90°, 180°, 270°) and extends both ways to reach the nearest multiple of 45° (45°, 135°, 225°, 315°). 
This algorithm draws all eight octants simultaneously, starting from each cardinal direction (0°, 90°, 180°, 270°) and extends both ways to reach the nearest multiple of 45° (45°, 135°, 225°, 315°). 
It can determine where to stop because when y = x, it has reached 45°. 
The reason for using these angles is: As y increases, it does not skip nor repeat any y value until reaching 45°. 
So during the while loop, y increments by 1 each iteration, and x decrements by 1 on occasion, never exceeding 1 in one iteration. This changes at 45° because that is the point where the tangent is rise=run. Whereas rise > run before and rise < run after.

The second part of the problem, the determinant, is far trickier. This determines when to decrement x. 
It usually comes after drawing the pixels in each iteration, because it never goes below the radius on the first pixel. 
Because in a continuous function, the function for a sphere is the function for a circle with the radius dependent on z (or whatever the third variable is), it stands to reason that the algorithm for a discrete(voxel) sphere would also rely on this Midpoint circle algorithm. But when looking at a sphere, the integer radius of some adjacent circles is the same, but it is not expected to have the same exact circle adjacent to itself in the same hemisphere. 
Instead, a circle of the same radius needs a different determinant, to allow the curve to come in slightly closer to the center or extend out farther."


Further reading:

https://en.wikipedia.org/wiki/Midpoint_circle_algorithm
