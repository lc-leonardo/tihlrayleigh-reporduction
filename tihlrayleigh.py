import numpy as np
import pandas as pd
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

# Function to plot all curves on a single plot for multiple (a, k) pairs
def plot_multiple(df):
    x_values = np.linspace(0, 5, 1000)

    # Set up plots
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6))

    # Iterate over each row in the dataset to plot each (a, k) line
    for idx, row in df.iterrows():
        a, k = row['a'], row['k']
        
        # Calculate PDF, CDF, and Hazard Rate
        pdf_values = tihlrayleigh_pdf(x_values, a, k)
        cdf_values = tihlrayleigh_cdf(x_values, a, k)
        hazard_values = tihlrayleigh_hazard(x_values, a, k)

        # Plot on each respective axis
        ax1.plot(x_values, pdf_values, label=f'a={a}, k={k}')
        ax2.plot(x_values, cdf_values, label=f'a={a}, k={k}')
        ax3.plot(x_values, hazard_values, label=f'a={a}, k={k}')

    # Set titles and labels for each subplot
    ax1.set_title('TIHLR PDF')
    ax1.set_xlabel('x')
    ax1.set_ylabel('f(x)')
    
    ax2.set_title('TIHLR CDF')
    ax2.set_xlabel('x')
    ax2.set_ylabel('F(x)')
    
    ax3.set_title('TIHLR Hazard Rate')
    ax3.set_xlabel('x')
    ax3.set_ylabel('h(x)')

    # Add legends to each subplot
    ax1.legend()
    ax2.legend()
    ax3.legend()

    plt.tight_layout()
    plt.show()

# Function to process a dataset and output results to CSV
def process_dataset(filename):
    try:
        df = pd.read_csv(filename)
        if 'a' not in df.columns or 'k' not in df.columns:
            raise ValueError("The dataset must contain 'a' and 'k' columns.")
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return

    # Plot all values in a single set of plots
    plot_multiple(df)

    # Save results for all (a, k) values to output_results.csv
    x_values = np.linspace(0, 5, 1000)
    output_data = []
    for idx, row in df.iterrows():
        a, k = row['a'], row['k']
        pdf_values = tihlrayleigh_pdf(x_values, a, k)
        cdf_values = tihlrayleigh_cdf(x_values, a, k)
        hazard_values = tihlrayleigh_hazard(x_values, a, k)

        for x, pdf, cdf, hazard in zip(x_values, pdf_values, cdf_values, hazard_values):
            output_data.append({"a": a, "k": k, "x": x, "PDF": pdf, "CDF": cdf, "Hazard Rate": hazard})

    output_df = pd.DataFrame(output_data)
    output_df.to_csv("output_results.csv", index=False)
    print("Results saved to 'output_results.csv'.")

# Function to get user input for 'a' and 'k'
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
    # Prompt user to choose input method
    print("Choose an option to proceed:")
    print("1. Input parameters manually")
    print("2. Load parameters from a dataset (CSV format)")
    
    choice = input("Enter 1 or 2: ").strip()
    
    if choice == '1':
        # Manual input mode
        print("\nYou chose manual input.")
        a = get_positive_float("Enter the value for parameter 'a' (scale parameter, > 0): ")
        k = get_positive_float("Enter the value for parameter 'k' (shape parameter, > 0): ")
        
        # Plot single input values
        x_values = np.linspace(0, 5, 1000)
        pdf_values = tihlrayleigh_pdf(x_values, a, k)
        cdf_values = tihlrayleigh_cdf(x_values, a, k)
        hazard_values = tihlrayleigh_hazard(x_values, a, k)
        
        # Set up plots
        fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6))

        ax1.plot(x_values, pdf_values, label=f'a={a}, k={k}')
        ax1.set_title('TIHLR PDF')
        ax1.set_xlabel('x')
        ax1.set_ylabel('f(x)')
        ax1.legend()

        ax2.plot(x_values, cdf_values, label=f'a={a}, k={k}')
        ax2.set_title('TIHLR CDF')
        ax2.set_xlabel('x')
        ax2.set_ylabel('F(x)')
        ax2.legend()

        ax3.plot(x_values, hazard_values, label=f'a={a}, k={k}')
        ax3.set_title('TIHLR Hazard Rate')
        ax3.set_xlabel('x')
        ax3.set_ylabel('h(x)')
        ax3.legend()

        plt.tight_layout()
        plt.show()
    
    elif choice == '2':
        # Dataset input mode
        print("\nYou chose to load parameters from a dataset.")
        dataset_filename = input("Enter the filename of the dataset (CSV format): ")
        process_dataset(dataset_filename)
    
    else:
        print("Invalid choice. Please restart and enter 1 or 2.")
