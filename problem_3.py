'''
Includes functions assockiated with problem 3, which reads:
    3. (Comparison to other methods.) You can't solve this
       example with the relaxation method, because you cannot
       track y\rightarrow\infty on a grid. So I will tell you
       that there happens to be an exact analytic solution
       for this problem:

       \[
       V(x,y)=\frac{2V_0}{\pi}\arctan\left(\frac{\sin\left(\frac{\pi x}{L}\right)}{\sinh\left(\frac{\pi y}{L}\right}\right).
       \]

       a. At each point on your grid, compute the fractional
          error of your series approximation to V. Display it as
          a colormap with imshow and a colorbar.

       b. Interpret this physically: where are the biggest
          fractional errors and why?
'''
