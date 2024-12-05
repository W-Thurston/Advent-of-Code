def main():
    with open('input_text.txt') as file:
        safety_manual_updates = file.readlines()

    # Remove trailing newline
    safety_manual_updates = [x.strip() for x in safety_manual_updates]

    # Split input data on the index of ''
    page_ordering_rules = safety_manual_updates[:safety_manual_updates.index('')]
    pages_to_produce    = safety_manual_updates[safety_manual_updates.index('')+1:]
    
    # Change data to list of tuples
    page_ordering_rules    = [(x[:2], x[-2:]) for x in page_ordering_rules]
    pages_to_produce       = [x.split(',') for x in pages_to_produce]

    total = 0
    for pages in pages_to_produce:
        valid_ordering_flag = True
        failed_flag = False
        #print(pages)
        for page_idx, page in enumerate(pages):
            #print(f"{page_idx}: {page}")
            # Check rules
            for rule in page_ordering_rules:
                if page in rule:
                    if rule[0] == page:
                        if rule[1] in pages:
                            if rule[1] in pages[page_idx:]:
                                #print(f"Rule {rule} satisfied.")
                                pass
                            else:
                                valid_ordering_flag = False
                                failed_flag = True
                                #print(f"Rule {rule} failed.")
                                break
                    else:
                        if rule[0] in pages:
                            if rule[0] in pages[:page_idx]:
                                #print(f"Rule {rule} satisfied.")
                                pass
                            else:
                                valid_ordering_flag = False
                                failed_flag = True
                                #print(f"Rule {rule} failed.")
                                break
            else:
                #print()
                continue  # only executed if the inner loop did NOT break
            break  # only executed if the inner loop DID break
        #print()
        while not valid_ordering_flag:
            #print(pages)
            for page_idx in range(len(pages)):
                page = pages[page_idx]
                #print(f"{page_idx}: {page}")
                # Check rules
                for rule in page_ordering_rules:
                    if page in rule:
                        if rule[0] == page:
                            if rule[1] in pages:
                                if rule[1] in pages[page_idx:]:
                                    #print(f"Rule {rule} satisfied.")
                                    valid_ordering_flag = True
                                else:
                                    valid_ordering_flag = False
                                    #print(f"Rule {rule} failed.")
                                    a, b = page_idx, pages.index(rule[1])
                                    pages[b], pages[a] = pages[a], pages[b]
                                    #print(f"New pages: {pages}")
                                    break
                        else:
                            if rule[0] in pages:
                                if rule[0] in pages[:page_idx]:
                                    #print(f"Rule {rule} satisfied.")
                                    valid_ordering_flag = True
                                else:
                                    valid_ordering_flag = False
                                    #print(f"Rule {rule} failed.")
                                    a, b = page_idx, pages.index(rule[0])
                                    pages[b], pages[a] = pages[a], pages[b]
                                    #print(f"New pages: {pages}")
                                    break
                else:
                    #print()
                    continue  # only executed if the inner loop did NOT break
                break  # only executed if the inner loop DID break
            #print()
        if failed_flag:
            total += int(pages[len(pages)//2])
        

    print(f"Part 2: {total}")

if __name__ == '__main__':
    main()