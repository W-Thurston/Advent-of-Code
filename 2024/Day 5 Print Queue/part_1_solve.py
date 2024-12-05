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
        # print(pages)
        for page_idx, page in enumerate(pages):
            # print(f"{page_idx}: {page}")
            # Check rules
            for rule in page_ordering_rules:
                if page in rule:
                    if rule[0] == page:
                        if rule[1] in pages:
                            if rule[1] in pages[page_idx:]:
                                # print(f"Rule {rule} satisfied.")
                                pass
                            else:
                                valid_ordering_flag = False
                                # print(f"Rule {rule} failed.")
                                break
                    else:
                        if rule[0] in pages:
                            if rule[0] in pages[:page_idx]:
                                # print(f"Rule {rule} satisfied.")
                                pass
                            else:
                                valid_ordering_flag = False
                                # print(f"Rule {rule} failed.")
                                break
            else:
                # print()
                continue  # only executed if the inner loop did NOT break
            break  # only executed if the inner loop DID break
        # print()
        if valid_ordering_flag:
            total += int(pages[len(pages)//2])

    print(f"Part 1: {total}")

if __name__ == '__main__':
    main()