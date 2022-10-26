"""Notes and examples of tuple and range sequence types."""

# Declaring a type alias that "invents" the Point2D type
Point2D = tuple[float, float]

start_position: Point2D = (5.0, 10.0)
print(start_position)


a_range: range = range(0, 10, 1)
print(a_range[0])
print(a_range[1])
print(len(a_range))
for i in a_range:
    print(i)