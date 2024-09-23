import pandas as pd
import great_expectations as ge

# Create a Pandas DataFrame
data = {
    'id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'status': ['active', 'inactive', 'active', 'inactive', 'pending'],
    'price': [10, 15, 0, 100, None]
}
df = pd.DataFrame(data)

# Convert the DataFrame to a Great Expectations DataFrame (gdf)
gdf = ge.from_pandas(df)

# Apply column-related Great Expectations methods on the 'price' column

# Column existence
gdf.expect_column_to_exist('price')

# Null checks
gdf.expect_column_values_to_not_be_null('price')
gdf.expect_column_values_to_be_null('price')

# Unique checks
gdf.expect_column_values_to_be_unique('price')

# Range checks
gdf.expect_column_values_to_be_between('price', min_value=0, max_value=100)
gdf.expect_column_quantile_values_to_be_between('price', quantile_ranges={
    "quantiles": [0.25, 0.5, 0.75], 
    "value_ranges": [[0, 20], [10, 50], [50, 100]]
})

# Set checks
gdf.expect_column_values_to_be_in_set('price', [0, 10, 15, 100])
gdf.expect_column_values_to_not_be_in_set('price', [1000, 2000])

# Statistical expectations
gdf.expect_column_mean_to_be_between('price', min_value=0, max_value=100)
gdf.expect_column_median_to_be_between('price', min_value=0, max_value=100)
gdf.expect_column_min_to_be_between('price', min_value=0, max_value=100)
gdf.expect_column_max_to_be_between('price', min_value=0, max_value=100)
gdf.expect_column_sum_to_be_between('price', min_value=0, max_value=500)
gdf.expect_column_stdev_to_be_between('price', min_value=0, max_value=100)

# Type checks
gdf.expect_column_values_to_be_of_type('price', 'float')
gdf.expect_column_values_to_be_in_type_list('price', type_list=["INTEGER", "FLOAT"])

# Regular expressions
gdf.expect_column_values_to_match_regex('price', r'^\d+$')
gdf.expect_column_values_to_not_match_regex('price', r'^\d{4}$')

# String length (not applicable here, but demonstrating)
gdf.expect_column_value_lengths_to_be_between('name', min_value=1, max_value=10)

# Order checks
gdf.expect_column_values_to_be_increasing('price')
gdf.expect_column_values_to_be_decreasing('price')

# Distribution checks
gdf.expect_column_kl_divergence_to_be_less_than('price', partition_object=None, threshold=0.1)

# Run validation and print results
validation_results = gdf.validate()

# Print validation results
print(validation_results)
