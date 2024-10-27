import numpy as np
import matplotlib.pyplot as plt

# Define the Type I Half Logistic Rayleigh PDF
def tihlrayleigh_pdf(x, a, k):
    return 4 * k * a * x * np.exp(-a * k * x**2) / (1 + np.exp(-a * k * x**2))**2

# Define the Type I Half Logistic Rayleigh CDF
def tihlrayleigh_cdf(x, a, k):
    return 1 - np.exp(-a * k * x**2) / (1 + np.exp(-a * k * x**2))

# Define the Type I Half Logistic Rayleigh Hazard Rate Function
def tihlrayleigh_hazard(x, a, k):
    pdf = tihlrayleigh_pdf(x, a, k)
    cdf = tihlrayleigh_cdf(x, a, k)
    return pdf / (1 - cdf)

# Function to plot PDF, CDF, and Hazard Rate
def plot_tihlrayleigh(a, k):
    # Generate a range of x values for plotting
    x = np.linspace(0, 5, 1000)
    
    # Compute the PDF, CDF, and Hazard Rate for the TIHLR distribution
    pdf_values = tihlrayleigh_pdf(x, a, k)
    cdf_values = tihlrayleigh_cdf(x, a, k)
    hazard_values = tihlrayleigh_hazard(x, a, k)
    
    # Plot the PDF, CDF, and Hazard Rate
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6))

    # Plot PDF
    ax1.plot(x, pdf_values, label=f'TIHLR PDF (a={a}, k={k})', color='b')
    ax1.set_title('TIHLR PDF')
    ax1.set_xlabel('x')
    ax1.set_ylabel('f(x)')
    ax1.legend()

    # Plot CDF
    ax2.plot(x, cdf_values, label=f'TIHLR CDF (a={a}, k={k})', color='r')
    ax2.set_title('TIHLR CDF')
    ax2.set_xlabel('x')
    ax2.set_ylabel('F(x)')
    ax2.legend()

    # Plot Hazard Rate
    ax3.plot(x, hazard_values, label=f'TIHLR Hazard Rate (a={a}, k={k})', color='g')
    ax3.set_title('TIHLR Hazard Rate')
    ax3.set_xlabel('x')
    ax3.set_ylabel('h(x)')
    ax3.legend()

    plt.tight_layout()
    plt.show()

def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError("The value must be greater than 0.")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid positive number.")

if __name__ == "__main__":
    # Get user input for parameters 'a' and 'k'
    print("Welcome to the TIHLR distribution plotter!")
    print("Please provide the parameters for the distribution.")
    
    a = get_positive_float("Enter the value for parameter 'a' (scale parameter, > 0): ")
    k = get_positive_float("Enter the value for parameter 'k' (shape parameter, > 0): ")
    
    # Plot the distribution with the input parameters
    plot_tihlrayleigh(a, k)
