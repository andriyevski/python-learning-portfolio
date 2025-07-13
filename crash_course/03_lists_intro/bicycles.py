# S1mple list
bicycles = ['trec','kannondale','redline','specialized']
print(bicycles)

# Find value from element
# bicycles = [   0  ,    1       ,    2    ,     3        ]
#bicycles = ['trec','kannondale','redline','specialized']
print(bicycles[1])
# Print -> 'kannondale'

# Use method title
print(bicycles[0].title())
# Print -> 'Trec'

# f-string use key in list and use method Title()
message = f"My first bicycles was a {bicycles[0].title()}."
print(message)
