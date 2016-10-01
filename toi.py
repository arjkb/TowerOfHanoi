# Tower of Hanoi
# toi.py python3 application
# Arjun Krishna Babu
# Fedora 24 Workstation

peg =  {
    'A': [8, 7, 6, 5, 4, 3, 2, 1],
    'B': [],
    'C': []
}

def verify_hanoi_property(peg):
    # raise an exception if a bigger peg is kept on top of a smaller peg

    # if the peg is not reverse-sorted... raise an Exception
    if peg != sorted(peg, reverse=True):
        raise Exception('Bigger peg kept on top of smaller peg!')

def get_spare_peg(peg1, peg2):
    # convert to upper case (sometimes redundantly) to prevent problems later
    peg1 = peg1.upper()
    peg2 = peg2.upper()

    pegs = (peg1 + peg2)

    # lookup table to find out the spare peg
    spare = {
        'AB': 'C',
        'BA': 'C',
        'AC': 'B',
        'CA': 'B',
        'BC': 'A',
        'CB': 'A'
    }

    if pegs in spare:
        return spare[pegs]
    else:
        raise Exception('Invalid peg letters!')

def solve_hanoi(n, from_peg, to_peg):
    # convert to upper case (sometimes redundantly) to prevent problems later
    from_peg = from_peg.upper()
    to_peg = to_peg.upper()

    # move n disks from from_peg to to_peg
    spare = get_spare_peg(from_peg, to_peg)

    # print(from_peg, peg[from_peg])
    # print(to_peg, peg[to_peg])

    if n < 1:
        # to handle cases where somebody decides to call
        # with ridiculous values for n
        return
    elif n == 1:
        peg[to_peg].append(peg[from_peg].pop())
    else:
        solve_hanoi(n-1, from_peg, spare)
        solve_hanoi(1, from_peg, to_peg)
        solve_hanoi(n-1, spare, to_peg)

    # print(from_peg, peg[from_peg])
    # print(to_peg, peg[to_peg])

    verify_hanoi_property(peg['A'])
    verify_hanoi_property(peg['B'])
    verify_hanoi_property(peg['C'])

def main():
    print(" Tower of Hanoi")

    print(" Before Solving: ")
    print(" Peg A: ", peg['A'])
    print(" Peg B: ", peg['B'])
    print(" Peg C: ", peg['C'])
    print("")

    solve_hanoi(8, 'A', 'C')

    print(" After Solving: ")
    print(" Peg A: ", peg['A'])
    print(" Peg B: ", peg['B'])
    print(" Peg C: ", peg['C'])

if __name__ == '__main__':
    main()
