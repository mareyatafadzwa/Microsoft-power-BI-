# Microsoft-power-BI-
Data Analytics Test  A real world example due to the increase of fuel in the world:
Source: https://www.fueleconomy.gov/feg/download.shtml
#Read data from the vehicles excelfile.
df = pd.read_excel ('C:/Users/T/Desktop/vehicles.xlsx')


#Sample cope of how i Deleted unwanted columns and selecting a data sample for the assignment.
df.drop('modifiedOn', axis=1, inplace=True)
df.drop(rows 29,30,31), axis=0, inplace=True)


#After selecting a record of 29 rows and 5 columns i am now saving my current work
df.to_excel(excel_writer='C:/Users/T/Desktop/vehicles.xlsx', index=False)


#i AM viewing how my graph looks after removing many columns and leaving only 29
df


#Sorting the data so that cars that consume less fuel appear at the top
df.sort_values ("You Save/Spend", ascending=False,)


#Plotting a graph to show the cars that are consuming/saving fuel. 
df.plot.bar(x='Make', y='You Save/Spend');


#Exporting my file as csv to the python assignment folder
df.to_csv(path_or_buf='C:/Users/T/Desktop/Python Assignment/vehiclesupdated.csv', index=False)


# I also expressed the fuel usage as a horizontal bar plot to show cars that are consuming less. 
sns.barplot(x='You Save/Spend', y='Make', data=df);
