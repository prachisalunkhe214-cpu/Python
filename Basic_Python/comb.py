from math import comb

total = 0

# w: wicketkeepers (Limit: 1 to 2)
for w in range(1, 3): 
    # ib: Indian batters (Limit: 1 to 3)
    for ib in range(1, 4): 
        # ob: overseas batters (Limit: 1 to 2)
        for ob in range(1, 3): 
            # ia: Indian all-rounders/bowlers (Limit: 4 to 9)
            for ia in range(4, 10): 
                # oa: overseas all-rounders/bowlers (Limit: 1 to 3)
                for oa in range(1, 4): 
                    
                    # Ensure total team size is exactly 11 players
                    if w + ib + ob + ia + oa == 11:
                        
                        # Ensure enough all-rounders/bowlers (at least 5)
                        if ia + oa >= 5: 
                            
                            # Ensure overseas balance (at most 4)
                            if ob + oa <= 4: 
                                
                                ways = (comb(2, w) * comb(3, ib) * comb(2, ob) * comb(10, ia) * comb(6, oa))
                                total += ways

print(f"Total valid team combinations: {total}")
