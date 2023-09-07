def shipping_rate(weight):
  if weight <= 2:
    rate_per_pound = 1.5
    shipping_cost = weight * rate_per_pound
  if weight > 2 and weight <=6:
    rate_per_pound = 3.0
    shipping_cost = 2 * 1.5 + (weight - 2)*rate_per_pound
