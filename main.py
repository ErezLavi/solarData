import data
import analysis
import plotting
import pandas as pd


def main():
    file_path_1 = 'Data/sep2022.csv'
    file_path_2 = 'Data/sep2020.csv'

    # Load data for September "file_path_1" year
    df_1 = data.load_data_by_5_minutes(file_path_1)
    year_1 = file_path_1.split('.')[0][-4:]
    start_date_1 = pd.to_datetime(f'{year_1}-09-18').tz_localize('UTC')
    end_date_1 = pd.to_datetime(f'{year_1}-09-20').tz_localize('UTC')
    mean_daily_energy_1 = analysis.calculate_mean_daily_energy(df_1, start_date_1, end_date_1)
    mean_hourly_energy_1 = analysis.calculate_hourly_energy(df_1, start_date_1, end_date_1)
    minutes_energy_dates_1 = analysis.calculate_dates_mean_ghi(df_1, start_date_1, end_date_1)

    # Load data for September "file_path_2" year
    df_2 = data.load_data_by_5_minutes(file_path_2)
    year_2 = file_path_2.split('.')[0][-4:]
    start_date_2 = pd.to_datetime(f'{year_2}-09-18').tz_localize('UTC')
    end_date_2 = pd.to_datetime(f'{year_2}-09-20').tz_localize('UTC')
    mean_daily_energy_2 = analysis.calculate_mean_daily_energy(df_2, start_date_2, end_date_2)
    mean_hourly_energy_2 = analysis.calculate_hourly_energy(df_2, start_date_2, end_date_2)
    minutes_energy_dates_2 = analysis.calculate_dates_mean_ghi(df_2, start_date_2, end_date_2)

    # Plotting

    plotting.plot_5_minute_mean(minutes_energy_dates_1, minutes_energy_dates_2,
                                start_date_1, end_date_1,
                                start_date_2, end_date_2)

    plotting.plot_hourly_energy_mean(mean_hourly_energy_1, start_date_1, end_date_1, mean_daily_energy_1)
    plotting.plot_hourly_energy_mean(mean_hourly_energy_2, start_date_2, end_date_2, mean_daily_energy_2)


if __name__ == "__main__":
    main()
