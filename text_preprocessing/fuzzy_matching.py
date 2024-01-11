from fuzzywuzzy import fuzz

# Sample list of product names
product_list = [
    "iPhone 13 Pro",
    "Samsung Galaxy S21",
    "Google Pixel 6",
    "OnePlus 9",
    "Sony Xperia 1 III",
    "Huawei P40 Pro",
]

# User input with a typo
user_query = "Samsang Glaxy S21"

# Calculate similarity using fuzz.ratio
ratio_similarity = [(product, fuzz.ratio(user_query, product)) for product in product_list]

# Calculate similarity using partial_ratio
partial_similarity = [(product, fuzz.partial_ratio(user_query, product)) for product in product_list]

# Calculate similarity using token_sort_ratio
token_sort_similarity = [(product, fuzz.token_sort_ratio(user_query, product)) for product in product_list]

# Calculate similarity using token_set_ratio
token_set_similarity = [(product, fuzz.token_set_ratio(user_query, product)) for product in product_list]

# Print results
print("User Query:", user_query)
print("\nSimilarity Using fuzz.ratio:")
print(sorted(ratio_similarity, key=lambda x: x[1], reverse=True))

print("\nSimilarity Using partial_ratio:")
print(sorted(partial_similarity, key=lambda x: x[1], reverse=True))

print("\nSimilarity Using token_sort_ratio:")
print(sorted(token_sort_similarity, key=lambda x: x[1], reverse=True))

print("\nSimilarity Using token_set_ratio:")
print(sorted(token_set_similarity, key=lambda x: x[1], reverse=True))
