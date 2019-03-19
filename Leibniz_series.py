from matplotlib import pyplot
import numpy

# Estimation of pi by means of the Leibneiz formula for pi
# Reference: https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80
# Inspired on the Coding Challenge #140: Pi Approximation with Leibniz Series
# Daniel Shiffman - The Coding Train.

def main():

	pi = 4
	max_iterations = 1000
	to_plot = numpy.linspace(0, max_iterations, max_iterations)
	pi_ = []

	pyplot.figure()

	for i in range(max_iterations):

		if (i%2 == 0):
			pi -= 4/(2*i + 3)
		else:
			pi += 4/(2*i + 3)
		pi_.append(pi)
		
	print(pi)

	pyplot.plot(to_plot, pi_, "-", color = "crimson")
	pyplot.title(r"$\rm{iterations} = %i,  value = %f$"%(max_iterations, pi), fontsize=20)
	pyplot.axhline(numpy.pi, linestyle = "--", color = "k", linewidth = 2.0)
	pyplot.xlabel(r"$\rm{Number \ of \ iterations}$", fontsize = 20)
	pyplot.ylabel(r"$\rm{Approximated \ value \ of} \ \pi$", fontsize = 20)
	pyplot.grid()
	pyplot.savefig("approximation_to_pi.pdf")
	pyplot.close()

if __name__ == '__main__':
	main()


