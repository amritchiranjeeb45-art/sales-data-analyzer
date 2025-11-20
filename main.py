"""Sales Data Analyzer - simple analytics script

Outputs:
- prints KPI summary to console
- saves monthly_sales.png (line chart)
- creates summary.csv with aggregated monthly totals
"""
import pandas as pd
import matplotlib.pyplot as plt

def load_data(path='sample_data.csv'):
    df = pd.read_csv(path, parse_dates=['order_date'])
    return df

def compute_kpis(df):
    df['sales'] = df['quantity'] * df['unit_price']
    total_sales = df['sales'].sum()
    avg_order_value = df.groupby('order_id')['sales'].sum().mean()
    top_product = df.groupby('product')['sales'].sum().idxmax()
    kpis = {
        'total_sales': round(total_sales, 2),
        'avg_order_value': round(avg_order_value, 2),
        'top_product': top_product
    }
    return kpis

def monthly_aggregation(df):
    df['month'] = df['order_date'].dt.to_period('M').dt.to_timestamp()
    monthly = df.groupby('month')['sales'].sum().reset_index()
    monthly.columns = ['month', 'monthly_sales']
    return monthly

def save_monthly_plot(monthly, out='monthly_sales.png'):
    plt.figure()
    plt.plot(monthly['month'], monthly['monthly_sales'], marker='o')
    plt.title('Monthly Sales')
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.tight_layout()
    plt.savefig(out)
    plt.close()

def export_summary(monthly, out='summary.csv'):
    monthly.to_csv(out, index=False)

def main():
    df = load_data()
    kpis = compute_kpis(df)
    print('--- KPI Summary ---')
    print(f"Total sales: ${kpis['total_sales']}")
    print(f"Average order value: ${kpis['avg_order_value']}")
    print(f"Top product: {kpis['top_product']}")
    monthly = monthly_aggregation(df)
    export_summary(monthly)
    save_monthly_plot(monthly)
    print('\nGenerated files: summary.csv, monthly_sales.png')

if __name__ == '__main__':
    main()
