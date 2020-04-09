"""
1) Given a matrix of n*n. Each cell contain 0, 1, -1.
0 denotes there is no diamond but there is a path.
1 denotes there is diamond at that location with a path
-1 denotes that the path is blocked.
Now you have start from 0,0 and reach to last cell & then return back to 0,0 collecting maximum no of diamonds.
While going to last cell you can move only right and down.
While returning back you can move only left and up.
"""

