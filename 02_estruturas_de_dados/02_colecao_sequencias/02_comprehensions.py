def main():
    colors = ['black', 'white']
    sizes = ['S', 'M', 'L']

    # realiza o produto cartesiano
    tshirts = [(color, size) for color in colors for size in sizes]

    for pair in tshirts: print(pair)

if __name__ == "__main__":
    main()