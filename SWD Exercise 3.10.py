# SWD EXERCISE 3.10 - REMOVE THE UNESSENTIAL

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

# GET THE DATA
exercise_data = pd.read_excel("C:/Users/marce/Documents/Python/Data/swdexercise3.10 DATA.xlsx", sheet_name="Data")

# VARIABLE TO HOLD NUMBER OF ROWS
num_rows = len(exercise_data)

# SET X VALUES BASED ON YEARS
x_values = ['2020', '2021', '2022', '2023']

# SET COLORS FOR GRAPHS
colors_used = ['bisque', 'cornflowerblue', 'firebrick', 'paleturquoise']

# CREATE SUBPLOT FRAME
fig, ax = plt.subplots(figsize=(16, 4))

for r in range(0, num_rows):
    # CREATE FIGURE IN APPROPRIATE CELL IN THE FRAME
    fig = plt.subplot(1, 4, r+1)
    
    # GET TITLE FROM TYPE COLUMN
    title = exercise_data.iloc[r, 0]
    
    # GET VALUES TO GRAPH
    values = (exercise_data.iloc[r, 1:]/100).tolist()
    
    # GRAPH VERTICAL BAR CHART
    vbc = plt.bar(x_values, values, color=colors_used[r], width=0.9)
    
    plt.title(title)  # ADD TITLE
    plt.tick_params(axis='both', length=0)  # TURN OFF ALL TICK MARKS
    
    plt.gca().yaxis.set_major_formatter(PercentFormatter(1))  # FORMAT Y-AXIS AS PERCENTAGE
    plt.ylim((0, 1))  # SET Y-AXIS RANGE TO BE CONSISTENT ACROSS SUBPLOTS
    plt.yticks(ticks=(0, 0.25, 0.50, 0.75, 1))  # ADD Y-AXIS TICK MARKS
    plt.box(on=None)  # REMOVE FRAME AROUND EACH SUBPLOT

    # ADD VALUE LABELS TO BARS
    fig.bar_label(fig.containers[0], label_type='edge', fmt='{:.1%}', color='gray', fontsize=8, padding=4)

    # REMOVE Y-AXIS TICK MARKS ON ALL BUT THE LEFT-MOST SUBPLOT
    if r > 0:
        plt.tick_params(labelleft=False, left=False)

# PLOT THE GRAPHS
ax.set_frame_on(False)  # REMOVE FRAME FROM THE FIGURE
ax.axis('off')  # REMOVE AXES FROM THE FIGURE

plt.show()
