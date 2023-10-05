class CustomList:
    def __init__(self):
        self.items = []

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        item_type = self.get_item_type()
        if not isinstance(value, item_type):
            raise ValueError(f"Item must be of type {item_type}")
        self.items[index] = value

    def get_item_type(self):
        # Extract the item type from the class name inside the square brackets
        class_name = str(self.__class__.__annotations__["item"])
        return eval(class_name)

    def append(self, item):
        item_type = self.get_item_type()
        if not isinstance(item, item_type):
            raise ValueError(f"Item must be of type {item_type}")
        self.items.append(item)

    def __str__(self):
        return str(self.items)

# Usage example
if __name__ == "__main__":
    string_list = CustomList[str]()
    int_list = CustomList[int]()

    try:
        string_list.append("apple")
        string_list.append("banana")
        # Uncommenting the next line would raise a ValueError
        # string_list.append(42)

        int_list.append(42)
        int_list.append(123)
        # Uncommenting the next line would raise a ValueError
        # int_list.append("apple")

        print("String List:", string_list)
        print("Integer List:", int_list)

        # Access elements using square brackets
        print("First element of the string list:", string_list[0])
        print("Second element of the integer list:", int_list[1])
    except ValueError as e:
        print(f"Error: {e}")
