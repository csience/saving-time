import time
import sys

VERSION = 2

def generator_for_wp(new_card, uid):
    global VERSION
    global DECIMAL_PLACE

    wp = "W"
    # Year - Version - Card Type (replacement or new) - Database (W for Wordpress lol) - 5 decimal ID
    formatted_year = time.strftime("%y", time.gmtime()) # 'YY'
    version_num = "V%s" % VERSION # V2
    if new_card:    # if it is a new card for the purchaser
        card = "N"  # set their card to R for replacement eligbility
        #TODO: setting user's card status in database
    else:
        card = "R"

    preformat_id = len(str(uid))
    formatted_id = "00000"
    # if an id is greater than 5 decimal places, quit
    if preformat_id > 5 or uid <= 0:
        sys.exit()
    else:
       """ # this is pure overkill. stop.
        # for each decimal place of 0's one through 5
        for x in range(1,DECIMAL_PLACE):
            # decimal places leftover
            if preformat_id % x is 0:
                formatted_id = "0" * (5-x) + str(uid)
        """
        # fully loaded
        if preformat_id % 5 is 0:
            formatted_id = str(uid)
        # 4 decimal places
        elif preformat_id is not 2 and preformat_id % 4 is 0:
            formatted_id = "0" + str(uid)
        elif preformat_id % 3 is 0:
            formatted_id = "00" + str(uid)


    sku = formatted_year + version_num + card + wp