# Chronicle Android Raw Data Preprocessing App

An application for preprocessing and plotting Chronicle Android raw data.

Not affiliated with GetMethodic/Chronicle, please visit them here: https://getmethodic.com/

Credits:
- GetMethodic/Chronicle for their app, website, and providing their original preprocessing code: https://github.com/methodic-labs/chronicle-processing
- Anil Kumar Vadathya for writing our original custom preprocessing code: https://github.com/anilrgukt
- Heidi Weeks for writing the original plotting code in R
- Josh Culverhouse for modifying and helping to convert the plotting code to Python, providing the initial app codebook, and helping to test the code significantly

## Preprocessing Features
- Labeling usage differently for filtered apps defined in a file
- Custom definition of the minimum duration in seconds required to include an instance of app usage
- Custom app engagement duration estimation
- Custom hour thresholds for flagging potentially erroneous instances of long-running app usage or data gaps
- Custom timezone removal/conversion
- Custom configuration of which interaction types to stop usage at
- Custom configuration of which interaction types to remove from the final preprocessed output
- Various columns to help with sorting and filtering the final preprocessed output

## Plotting Features
- Including or excluding filtered app usage defined in the preprocessing
- Custom loading of app codebooks to color apps in plots based on their categories
- Marking device shutdown and device startup events
- Marking data time gaps (WIP)
