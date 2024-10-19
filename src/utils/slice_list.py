def slice_list(elements, size):
    return [
        elements[i:i + size]
        for i in range(0, len(elements), size)
    ]
