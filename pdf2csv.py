import pandas as pd

def text_to_csv(input_path, output_path):
    try:
        # Read the text file into a DataFrame
        df = pd.read_csv(input_path, delimiter=',', header=None)
        
        # Write the DataFrame to a CSV file
        df.to_csv(output_path, index=False, header=False)
        
        print(f"Data successfully written to {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Specify the input and output file paths
    input_file_path = 'PATH.pdf'
    output_file_path = 'PATH.csv'
    
    # Convert text file to CSV
    text_to_csv(input_file_path, output_file_path)

