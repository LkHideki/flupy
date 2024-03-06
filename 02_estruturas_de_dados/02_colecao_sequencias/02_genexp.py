def main():
    colors = ['black', 'white']
    sizes = ['S', 'M', 'L']
    for tshirt in (f'{color} {size}' for color in colors for size in sizes):
        print(tshirt)

if __name__ == "__main__":
    main()