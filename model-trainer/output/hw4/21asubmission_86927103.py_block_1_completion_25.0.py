def shipping_rate(weight):
  if weight <= 2:
    rate_per_pound = 1.5
    shipping_cost = weight * rate_per_pound
