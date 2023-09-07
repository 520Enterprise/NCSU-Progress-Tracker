def shipping_rate(weight):
  if weight <= 2:
    rate_per_pound = 1.5
    shipping_cost = weight * rate_per_pound
#@#
  if weight > 2 and weight <=6:
    rate_per_pound = 3.0
    shipping_cost = 2 * 1.5 + (weight - 2)*rate_per_pound
#@#
  if weight > 6 and weight <= 10:
    rate_per_pound = 4.0
    shipping_cost = 2 * 1.5 + 4 * 3 + (weight - 6)*rate_per_pound
#@#
  if weight > 10:
    rate_per_pound = 4.75
    shipping_cost = 2 * 1.5 + 4 * 3 + 4 * 4 + (weight - 10)*rate_per_pound
  return shipping_cost
#@#
    weight = 12
    print(shipping_rate(weight))
if __name__ == '__main__':
    main()
#@#