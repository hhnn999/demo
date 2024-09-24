from nen_xau_module import nen_xau

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        xau = f.readline().strip()

    xau_nen = nen_xau(xau)

    with open("output.txt", "w") as f:
        f.write(xau_nen)