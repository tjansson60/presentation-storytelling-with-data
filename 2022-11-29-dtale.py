#!/usr/bin/env python

import seaborn as sns
import dtale

if __name__ == '__main__':
    # Load the data
    tips = sns.load_dataset("tips")
    tips['Tip [%]'] = (tips['tip'] / tips['total_bill']) * 100

    # Start the webserver and show the data
    d = dtale.show(tips, subprocess=False)
    d.open_browser()
