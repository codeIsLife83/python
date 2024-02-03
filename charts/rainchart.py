import re
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup

# livingston, tx
url = f"https://www.usclimatedata.com/climate/livingston/texas/united-states/ustx0779"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
table = soup.find("table", id="monthly_table_one")
table2 = soup.find("table", id="monthly_table_two")

# Drill down to the specific td cell (e.g., Row 1, Cell 2)
row_index = 3  # 0-based index for rows

rainamount = [] # yaxis

for i in range(0, 6):
    td_cell = table.find_all("tr")[row_index].find_all("td")[i]
    td_cell2 = table2.find_all("tr")[row_index].find_all("td")[i]
    cell_text = float(td_cell.get_text())
    cell_text2 = float(td_cell2.get_text())
    rainamount.append(cell_text)
    rainamount.append(cell_text2)

# Madison, Va
vurl = f"https://www.usclimatedata.com/climate/madison/virginia/united-states/usva1148"
vresponse = requests.get(vurl)
vsoup = BeautifulSoup(vresponse.text, "html.parser")
vtable = vsoup.find("table", id="monthly_table_one")
vtable2 = vsoup.find("table", id="monthly_table_two")

# Drill down to the specific td cell (e.g., Row 1, Cell 2)
vrow_index = 3  # 0-based index for rows

vrainamount = []  # yaxis

for i in range(0, 6):
    vtd_cell = vtable.find_all("tr")[vrow_index].find_all("td")[i]
    vtd_cell2 = vtable2.find_all("tr")[vrow_index].find_all("td")[i]
    vcell_text = float(vtd_cell.get_text())
    vcell_text2 = float(vtd_cell2.get_text())
    vrainamount.append(vcell_text)
    vrainamount.append(vcell_text2)


months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct","Nov","Dec"]

# Create a figure and a set of subplots (one subplot in this case)
fig, ax = plt.subplots()
ax.set_facecolor("black")
fig.set_facecolor("grey")
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
ax.spines['bottom'].set_color('white')
ax.spines['top'].set_color('white')
ax.spines['left'].set_color('white')
ax.spines['right'].set_color('white')
ax.set_xticklabels(months, rotation=45)
ax.set_yticklabels(rainamount, rotation=45)


# Plot the data
ax.plot(months, rainamount, "purple", linewidth=2.0, label="Livinston, Tx")
ax.plot(months, vrainamount, "gold", linewidth=2.0, label="Madison, Va")

# Customize the chart
ax.set_title("Rain for the 2023", color="white")
ax.set_xlabel("Month", color="white")
ax.set_ylabel("Amount in inches", color="white")

# Displaying the legend
plt.legend()

# Show the chart
plt.show()
