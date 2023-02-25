def rectangle(length, width):
    if type(length) != int or type(width) != int:
        return "Enter valid values!"

    def rectangle_area():
        return length * width

    def rectangle_perimeter():
        return (length * 2) + (width * 2)


    return f"Rectangle area: {rectangle_area()}\nRectangle perimeter: {rectangle_perimeter()}"








# print(rectangle(2, 10))
print(rectangle('2', 10))