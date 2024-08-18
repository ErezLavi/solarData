import data
import analysis
import pandas as pd
import streamlit as st
import plotly.express as px


# Streamlit app
def main():
    st.title("Energy solar car data analysis")

    # Upload CSV files
    file_1 = st.file_uploader("Upload first CSV file", type="csv")
    file_2 = st.file_uploader("Upload second CSV file", type="csv")

    if file_1 and file_2:
        # Load data
        df_1 = data.load_data_by_5_minutes(file_1)
        df_2 = data.load_data_by_5_minutes(file_2)

        # Extract years from file names
        year_1 = file_1.name.split('.')[0][-4:]
        year_2 = file_2.name.split('.')[0][-4:]

        # Date range selection
        start_date_1 = pd.to_datetime(
            st.date_input(f'Start date for {year_1}', pd.to_datetime(f'{year_1}-09-18'))).tz_localize('UTC')
        end_date_1 = pd.to_datetime(
            st.date_input(f'End date for {year_1}', pd.to_datetime(f'{year_1}-09-20'))).tz_localize('UTC')
        start_date_2 = pd.to_datetime(
            st.date_input(f'Start date for {year_2}', pd.to_datetime(f'{year_2}-09-18'))).tz_localize('UTC')
        end_date_2 = pd.to_datetime(
            st.date_input(f'End date for {year_2}', pd.to_datetime(f'{year_2}-09-20'))).tz_localize('UTC')

        # Validate date range
        if start_date_1 >= end_date_1 or start_date_2 >= end_date_2:
            st.error('Error: End date must be greater than start date.')
            return
        # Validate date within september
        if start_date_1.month != 9 or end_date_1.month != 9 or start_date_2.month != 9 or end_date_2.month != 9:
            st.error('Error: Date must be within September.')
            return

        # Calculate energy metrics
        mean_daily_energy_1 = analysis.calculate_mean_daily_energy(df_1, start_date_1, end_date_1)
        minutes_energy_dates_1 = analysis.calculate_dates_mean_ghi(df_1, start_date_1, end_date_1)

        mean_daily_energy_2 = analysis.calculate_mean_daily_energy(df_2, start_date_2, end_date_2)
        minutes_energy_dates_2 = analysis.calculate_dates_mean_ghi(df_2, start_date_2, end_date_2)

        # Plotting using Plotly
        fig = px.line(x=minutes_energy_dates_1.index, y=minutes_energy_dates_1.values,
                      labels={'x': 'Time', 'y': 'Mean Energy (GHI)'},
                      title=f'Comparison of Mean Energy (GHI) - {year_1} ({mean_daily_energy_1}) vs '
                            f'{year_2} ({mean_daily_energy_2})')

        fig.add_scatter(x=minutes_energy_dates_1.index, y=minutes_energy_dates_1.values,
                        mode='lines', name=f'{year_1} Data')
        fig.add_scatter(x=minutes_energy_dates_2.index, y=minutes_energy_dates_2.values,
                        mode='lines', name=f'{year_2} Data')

        fig.update_xaxes(
            tickformat='%H:%M',
            nticks=12  # Number of ticks on the x-axis
        )

        st.plotly_chart(fig)


if __name__ == "__main__":
    main()
