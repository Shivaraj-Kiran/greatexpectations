import great_expectations as ge
from great_expectations.core.batch import BatchRequest

# Initialize the Data Context
context = ge.DataContext()

# Define the BatchRequest for the MySQL table
batch_request = BatchRequest(
    datasource_name="my_mysql_datasource",
    data_connector_name="default_inferred_data_connector_name",
    data_asset_name="employees"  # Replace with your actual MySQL table name
)

# Load the Expectation Suite
expectation_suite_name = "my_expectation_suite"
context.add_or_update_expectation_suite(expectation_suite_name)

# Create a Validator for the MySQL data
validator = context.get_validator(
    batch_request=batch_request,
    expectation_suite_name=expectation_suite_name
)

# Define expectations
validator.expect_column_to_exist("salary")
validator.expect_column_values_to_not_be_null("salary")
validator.expect_column_values_to_be_in_set("salary", [70000,85000,60000])
validator.expect_column_values_to_be_between("salary", min_value=50000, max_value=100000)
validator.expect_column_values_to_be_unique("salary")

# Save the updated Expectation Suite
context.save_expectation_suite(validator.get_expectation_suite(), expectation_suite_name)

# Run validation
validation_result = validator.validate()

# Print validation results
print(validation_result)
