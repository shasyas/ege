# ((x ≡ y) → (¬z ∨ w)) ≡ ¬ ((w → x) ∨ (y → z)).
# ((x==y) <= ((not(z)) or w)) != ((w <= x) or (y <= z))

a = [0, 1]

print('x', 'y', 'z', 'w')

for x in a:

    for y in a:

        for z in a:

            for w in a:

                if ((x == y) <= ((not (z)) or w)) != ((w <= x) or (y <= z)):
                    print(x, y, z, w)