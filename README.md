

# Sales Data Visualization

This Python project allows you to visualize sales data from an Excel file using different types of plots such as line graphs, bar charts, pie charts, scatter plots, and histograms. It gives users an interactive menu to choose various types of visualizations related to sales data.

## Features
- **Line Chart**: Shows the trend of sales over time.
- **Bar Chart**: Visualizes total sales for each month.
- **Pie Chart**: Shows the distribution of sales based on product categories.
- **Scatter Plot**: Demonstrates the relationship between product prices and sales volume.
- **Histogram**: Visualizes the distribution of product prices.
- **Monthly Sales Visualization**: Shows the monthly sales trend over time.
- **Price Category Bar Chart**: Displays total sales for each product price category.

## Prerequisites

Before running the project, ensure you have the following dependencies installed in your Python environment:

- **pandas**: For handling Excel files and data manipulation.
- **matplotlib**: For plotting the data.
- **numpy**: For numeric operations and fitting a trendline in scatter plots.
- **openpyxl**: (Optional) Required if your Excel file format is `.xlsx`.

### Installation

You can install the required dependencies using the following commands:

```bash
pip install pandas matplotlib numpy openpyxl
```

## How to Run the Project

1. **Prepare an Excel file**: Ensure you have an Excel file with the following columns:
   - `Tarih` (Date) for the time of the sale.
   - `Satış` (Sales) for the quantity of products sold.
   - `Fiyat (TL)` (Price in Turkish Lira) for the price of each product.
   - `Kategori` (Category) for the product category.

2. **Run the Script**:
   - Launch the program by running the Python script in your terminal:
   ```bash
   python ders_1.py
   ```

3. **Input the Excel File**:
   - When prompted, enter the name of the Excel file (without the `.xlsx` extension). The script will load the file and offer you various graph options.

4. **Choose Visualization**:
   - The program will show you a menu with different options for visualizing the data:
     1. Line chart of sales over time.
     2. Bar chart of monthly total sales.
     3. Pie chart showing sales distribution by category.
     4. Scatter plot showing the relationship between price and sales.
     5. Histogram showing the distribution of product prices.
     6. Line chart of monthly sales amounts.
     7. Bar chart of sales distribution by price category.
   - Enter the number corresponding to the visualization you want to see.

5. **Exit**:
   - Select `0` to exit the program.

## Code Structure

### Main Components:

1. **Data Loading**:
   - The script loads an Excel file with sales data and processes it using `pandas`. It also converts the `Tarih` (Date) column into a `datetime` object and sets it as the index.

2. **Menu System**:
   - The user is presented with a simple text-based menu to choose between different types of visualizations.

3. **Visualization Functions**:
   - Each menu option corresponds to a specific type of plot, created using `matplotlib`. Depending on the user's choice, the appropriate plot is displayed.

### Menu Options:
- `1`: Line graph of sales changes over time.
- `2`: Bar chart of total monthly sales.
- `3`: Pie chart showing sales distribution by category.
- `4`: Scatter plot with a trendline, showing the relationship between product prices and sales volumes.
- `5`: Histogram displaying the price distribution.
- `6`: Monthly sales amounts (Line chart).
- `7`: Total sales by price category (Bar chart).

## Example

When the program is run, it will prompt for the Excel file name:

```bash
Lütfen Excel dosyasının adını giriniz (uzantı olmadan): my_sales_data
```

After entering the file name (without the `.xlsx` extension), you will be presented with the following menu:

```
Grafik Seçenekleri
1- Satışların zaman içerisindeki değişimi (Çizgi grafiği)
2. Aylık toplam satışlar (bar grafiği)
3. Kategorilere göre satış dağılımı (pasta grafiği)
4. Fiyat ve satış ilişkisi (scatter plot)
5. Fiyat dağılımı (Histogram)
6. Aylık satış miktarları (çizgi grafiği)
7. Fiyat kategörisine göre toplam satışlar (bar grafiği)
0. Çıkış
Seçim yapınız: 
```

Select the number corresponding to the visualization you want to see.

